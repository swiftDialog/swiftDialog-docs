---
title: Análisis de las deficiencias en los contratos de ICP
description: Un análisis comparativo del contrato de integración entre swiftDialog e ignitecli, que identifica las deficiencias existentes, los riesgos potenciales y las cláusulas contractuales propuestas para garantizar una comunicación robusta entre los dos componentes.
translationSynced: 2026-11-24T22:56:37+00:00
---

**Estado:** Borrador para revisión. **Fecha:** 17 de junio de 2026. **Alcance:** Comunicación entre procesos en tiempo de ejecución entre `swiftDialog` (Modo de inspección, preajustes 1–6) y `ignitecli`, que se encarga de iniciar y controlar este proceso. **Repositorios:**
- swiftDialog — `/Users/henry/Projects/GitHub/swiftDialog`
- ignitecli — `/Users/henry/Projects/GitHub/ignitecli-swift-private`

Este documento define el contrato del IPC tal como existe actualmente, y luego enumera las áreas en las que ambas partes coinciden solo por casualidad, o donde se asume una garantía pero no se hace cumplir. Cada afirmación está respaldada por una referencia `file:line` para que pueda ser verificada nuevamente.

---

## 1. Resumen del transporte

Existen tres sistemas de transporte en funcionamiento. El contrato es la integración de los tres; una implementación sólida no debe asumir que ninguno de ellos sea fiable.

| Transporte | Dirección | Canal / Vía | Carga útil | Fiabilidad |
|---|---|---|---|---|
| Notificación (comando) distribuida. | ignitecli → diálogo | `com.swiftdialog.command` **y** `com.ignitecli.command` | `userInfo` diccionario, convertido a cadena de texto | Envío sin garantía de orden, **se perderá si se publica antes de que el observador se registre** |
| Notificación distribuida (evento). | dialog → ignitecli | `com.swiftdialog.event` | `userInfo` Diccionario, incluyendo `event` y `pid` | Esfuerzo máximo |
| Notificación distribuida (confirmación). | dialog → ignitecli | `com.swiftdialog.ack` | `userInfo` Diccionario que incluye: `command`, `stepId`, `status`, `pid` | Esfuerzo máximo, **consumo muy poco frecuente** |
| Archivo de activación / archivo de comandos | ignitecli → diálogo | `--status-log-file` / por proceso (o ID de proceso) `.command` | Delimitado por saltos de línea, con campos separados por dos puntos | Duradero, con seguimiento del desplazamiento de bytes |
| Carpeta de preparación | dialog → ignitecli | `<trigger>.ready` o configuración `readinessFile` | JSON | Resistente, con características que favorecen la ausencia de cuernos |
| Archivo de evento | dialog → ignitecli | configuración `eventFile` o derivada `.events` | JSONL | Resistente, sin cola |
| Archivo de resultados | dialog → ignitecli | configuración `resultFile` / por proceso (PID) `.result.json` | JSON | Duradero |
| Directorio de sesiones publicadas | diálogo → *(nadie)* | `--published-sessions-dir` (por defecto `/private/tmp/swiftdialog/sessions/<pid>.json`) | JSON | Duradero, **no consumible** — ver la laguna 1 |
| estado de la comunicación entre procesos (IPC) de ignitecli | ignitecli → ignitecli | `/private/tmp/.ignitecli-ipc-<pid>.json` | JSON | Duradero |

**Anclajes de referencia**
- Canales: `dialog/Views/Inspect/Core Framework/DistributedNotifications.swift:36`;
  ignitecli `Sources/Dialog/ActionDispatcher.swift:9`.
- Publicación en ambos canales: `ignitecli` `Sources/Commands/IpcCommand.swift:414`.
- Enrutamiento de archivos de comandos: `dialog/Views/Inspect/Core Framework/CommandRouter.swift:76`.
- Directorio de sesiones publicadas: `dialog/Command Line/CommandLineArguments.swift:167`
  `dialog/Views/Inspect/Core Framework/PresetCommonHelpers.swift:1134`.
- ignitecli: estado: `Sources/Dialog/IpcState.swift:11`.

---

## 2. Vocabulario relacionado con el evento (el contrato de suministro).

swiftDialog emite estos tipos de eventos (`DistributedNotifications.swift:36`, valores sin procesar bloqueados):

| Tipo de evento | Valor sin procesar | Se emite cuando... | Campos clave |
|---|---|---|---|
| `ready` | `ready` | La interfaz de usuario está lista para recibir comandos | `triggerFile`, `preset?`, `itemCount?`, `items?`, `ackChannel` |
| `exit` | `exit` | A punto de finalizar | `triggerFile`, `exitCode?`, `completedCount?`, `failedCount?`, `resultFile?` |
| `deferred` | `defer` | Usuario en espera | `duration`, `seconds`, `exitCode`, `resultFile` |
| `button` | `button` | Clic del botón | `stepId`, `button`, `action` |
| `step` | `step` | Transición de pasos | `stepId`, `action` (e.g. `completed`, `all_complete`) |
| `selection` | `selection` | Compromiso de selección/organización | `key`, `values` |

El preset 6 ha sido verificado para emitir `step`, `button`, `selection` (`Preset6.swift:1251`, `:1116`, `:1638`).

Comandos aceptados (de ignitecli a diálogo), enrutados en: `CommandRouter.swift:76–163`, `success`, `failure`, `warning`, `complete`, `navigate`/`goto`, `next`/`prev`/`back`, `reset`, `progress`, `update_guidance`, `update_message`, `batch_update`, `display_data`, `recheck`, `set`, `item`, `listitem`, `select`. Las abreviaturas `userInfo` se expanden a estos comandos (`DistributedNotifications.swift:177`).

---

## 3. Vacíos

Clasificados por gravedad. Cada sección describe la **realidad observada**, el **riesgo** y una **cláusula contractual propuesta** (lenguaje normativo para una futura especificación conjunta).

### Directorio de sesiones publicado (Gap 1): solo permite escritura; la herramienta ignitecli nunca lo lee. **ALTO**

**Observed.** swiftDialog writes a per-PID discovery file to `/private/tmp/swiftdialog/sessions/<pid>.json` (`PresetCommonHelpers.swift:1134`, CLI `CommandLineArguments.swift:167`). A grep of all of ignitecli `Sources/` finds **no reader** for that directory. ignitecli discovers sessions solely via its own `/private/tmp/.ignitecli-ipc-<pid>.json` (`IpcState.swift:11`), which it wrote at launch.

Dos registros paralelos describen el mismo hecho (qué diálogo está activo en función de qué archivo de activación), pero nunca se sincronizan.

| Registro | swiftDialog escribe | ignitecli lee... |
|---|---|---|
| `…/swiftdialog/sessions/<pid>.json` | ✅ | ❌ |
| `…/.ignitecli-ipc-<pid>.json` | ❌ | ✅ |

**Riesgo.** `ignitecli` solo puede conectarse a un diálogo que haya iniciado directamente. Si `ignitecli` pierde su propio archivo de estado (por un fallo, reinicio o ejecución separada), el diálogo en ejecución no se puede recuperar, incluso si `swiftDialog` lo está anunciando. La función de descubrimiento, recientemente lanzada, no aporta ningún valor a su único usuario interno.

**Cláusula propuesta.**
> swiftDialog publicará un registro de cada sesión en vivo. ignitecli también...
> Considere el directorio de sesiones publicadas como la fuente de información autorizada y DEBE...
> poder adoptar una sesión encontrada allí (leer `triggerFile`, `resultFile`,
> `readinessFile`, `ackChannel`, `pid`) sin haberla iniciado. La herramienta ignitecli
> El archivo de estado privado puede seguir funcionando como una caché al inicio, pero NO debe ser la única opción
> fuente de información confiable.

**Decisión abierta (propietario: ignitecli).** ¿Está el directorio de sesiones destinado a la recuperación de ignitecli, o a herramientas *externas* (monitorización/MDM)? Esa elección determina si ignitecli desarrolla una funcionalidad de "descubrimiento e implementación" o si, intencionalmente, se mantiene separada de ella.

### Brecha 2: La ruta del archivo de eventos se deriva mediante dos reglas diferentes. **GRAVEDAD: MEDIA**

**Observado.** swiftDialog resuelve la ruta del evento como `config.eventFile ?? readinessFile(.ready → .events)` (`Preset5.swift:4834`, idéntico en `Preset1.swift:460`, `Preset2.swift:533` y en la configuración predefinida 6). Las plantillas de ignitecli **siempre establecen `eventFile` de forma explícita** (`Sources/Resources/templates/*/config.json` → `/tmp/__WORKFLOW_NAME__.events`). Convergen solo porque la configuración siempre define la clave.

**Riesgo.** Una configuración que establece una ruta personalizada y omite la especificación de otra ruta hace que swiftDialog derive una ruta que ignitecli no está monitorizando. `readinessFile` Esto provoca que `eventFile` no se detecte. `wait-step`. `wait-step` (EsperaStep, sondeo de 2 segundos) y luego se bloquea debido a su tiempo de espera, sin proporcionar información diagnóstica que indique la falta de coincidencia en la ruta. `IpcCommand.swift`.

**Cláusula propuesta.**
> La ruta del archivo de eventos DEBE derivarse mediante una única regla, compartida por ambas partes.
> Si ambos extremos se derivan (en lugar de requerir una especificación explícita `eventFile`), entonces...
> El algoritmo de derivación se especificará textualmente aquí y estará sujeto a una prueba
> cada lado. Un `wait-step` tiempo de espera DEBE incluir la ruta del archivo de eventos resuelto en
> su error.

### Brecha 3: Los camareros que realmente importan no verifican el estado del proceso. · **DE RIESGO MODERADO**

**Observado.** `wait-exit` verifica `kill(pid, 0)` (`IpcState.swift:58`) y detecta un diálogo inactivo. `wait-ready` y `wait-step` esperan una notificación o una modificación de archivo; `wait-step` solo detecta un PID inactivo si la verificación inicial se activa, de lo contrario, se consume todo el tiempo de espera (`IpcCommand.swift` WaitStep, `:376`).

**Riesgo.** Un diálogo que se interrumpe inesperadamente puede transformar una falla rápida y evidente en un tiempo de espera genérico de 2 a 600 segundos, sin indicar la causa del problema.

**Cláusula propuesta.**
> Cada camarero (`wait-ready`, `wait-step`, `wait-exit`) DEBE participar en una encuesta sobre `kill(pid,0)`
> debe realizar la misma verificación que el proceso de comprobación de archivos/notificaciones y, en caso de fallo, debe generar una alerta de manera rápida
> `dialog PID <n> exited before <condition>` en lugar de un tiempo de espera genérico.

### Espacio 4: Existe un canal de confirmación en ambos extremos, pero no se utiliza como una barrera. **NIVEL MEDIO**

**Observado.** swiftDialog publica mensajes en `com.swiftdialog.ack` después de cada comando ejecutado (`CommandRouter.swift:351`). ignitecli tiene `waitAck()` (`Sources/Dialog/DialogOrchestrator.swift:151`), pero la mayoría de los flujos de trabajo nunca lo utilizan; el modo de entrega predeterminado es "envía y olvida" a través de un transporte que ofrece el mejor rendimiento posible.

**Riesgo.** Una notificación omitida `navigate` que impide la ejecución de un lote predefinido provoca una desincronización silenciosa de todo el proceso. La interfaz de usuario, que puede tolerar repeticiones, no lo hace con las operaciones críticas que dependen del orden.

**Cláusula propuesta.**
> Comandos cuyo efecto controla la ejecución de comandos posteriores (`navigate`, `goto`, `reset`,
> `batch_update` El mensaje que precede a una solicitud de navegación DEBE enviarse con la opción "espera de confirmación" habilitada.
> `ignitecli` volverá a intentar la operación o mostrará un error si no recibe una confirmación para dicha orden
> Dentro del tiempo de espera de la confirmación (ACK). La función "disparar y olvidar" sigue estando permitida para las operaciones de pintura idempotentes
> (`progress`, `update_message`, `display_data`).

### Gap 5: Se corrigió dos veces un problema relacionado con la repetición de archivos, y la responsabilidad de la corrección no se asignó a ningún equipo. **GRAVEDAD: BAJA-MEDIA.**

**Observed.** ignitecli deletes IPC files pre-launch (`DialogLauncher.swift:199`) to stop swiftDialog replaying stale `success:` lines (the preset-5 flash-through). swiftDialog independently records the initial byte offset to skip pre-existing content (`CommandRouter.swift:79`). Two independent fixes guard one hazard.

**Riesgo.** Si cualquiera de estos componentes vuelve a su estado anterior (ya sea que swiftDialog comience a leer desde el desplazamiento 0 nuevamente, o que ignitecli omita la limpieza en una nueva ruta), el error se manifestará de forma silenciosa.

**Cláusula propuesta.**
> swiftDialog ignorará cualquier contenido del archivo de activación que pueda existir antes de su publicación `ready`.
> Esta garantía será propiedad y será probada por el equipo de swiftDialog; la herramienta ignitecli...
> La limpieza previa al lanzamiento es una medida de seguridad adicional, no la garantía principal.

### Brecha 6: No hay autenticación en ningún tipo de conexión (aceptado, pero no especificado). · **BAJA**

**Observado.** No se realiza ninguna validación del remitente en las notificaciones distribuidas (la API no ofrece ninguna funcionalidad para ello); el archivo de comandos/desencadenamiento es accesible para escritura por cualquier usuario; el directorio de sesiones es legible y enumerable por cualquier usuario. Cualquier proceso local puede controlar o falsificar la interacción y puede listar los procesos activos (PIDs) y las rutas de activación. El nuevo directorio de sesiones *amplía* esta superficie de exposición de información.

**Riesgo.** Aceptable en un modelo de confianza local con un solo usuario; peligroso si esa suposición se ve comprometida (servidor compartido, inquilino con privilegios reducidos).

**Cláusula propuesta.**
> El límite de confianza de IPC es "mismo usuario, mismo host, local". Todos los mecanismos de transporte asumen un...
> Un remitente local que colabora. Esta es una suposición deliberada y documentada; no...
> El transporte proporciona autenticación o integridad. Cualquier implementación fuera de ese contexto...
> El límite especificado está fuera del alcance y no es compatible.

---

## 4. Resumen de la gravedad y ordenación

| # | Gap | Gravedad | Corregir la ubicación |
|---|---|---|---|
| 1 | Sesiones de escritura exclusiva | ALTO | ignitecli (lector) |
| 2 | Dos reglas de trayectoria de eventos | MEDIO | ambos (gobierno compartido). |
| 3 | Los camareros evitan el contacto directo con los clientes | MEDIO | ignitecli |
| 4 | "Ack" no se utiliza como barrera | MEDIO | ignitecli (política) |
| 5 | La función de repetición se ha solucionado dos veces | BAJO-MEDIO | swiftDialog (usted tiene la garantía). |
| 6 | Sin autenticación, información no especificada | BAJO | Solo documento |

**Orden de implementación recomendado.** Primero, implemente este contrato (los puntos 5 y 6 son específicos de la documentación y se deben implementar de inmediato). Luego, implemente **el punto 1 y el punto 2 juntos**: haga que la herramienta ignitecli utilice el directorio de sesiones publicado como la fuente de información principal y simplifique la derivación de la ruta de los eventos a una única regla. Esto convierte los cambios recientes en la comunicación entre procesos (IPC) de swiftDialog en algo que ignitecli realmente utiliza. Los puntos 3 y 4 son mejoras independientes en la robustez de ignitecli que se pueden implementar posteriormente.

---

## 5. Registro de verificación

Las afirmaciones contenidas en este documento fueron verificadas con la fuente original el 17 de junio de 2026.

- Las directivas de la sesión no son leídas por la herramienta ignitecli — se busca `Sources/`
  `swiftdialog/sessions` / `publishedSessions`: sin consumidor.
- El preset 6 emite señales de paso, botón o selección — `Preset6.swift:1116,1152,1251,1638`.
- Derivación dual de la trayectoria del evento — `Preset1.swift:460`, `Preset2.swift:533`
  `Preset5.swift:4834`; comando `ignitecli` utilizado explícitamente `eventFile` en `Sources/Resources/templates/*/config.json`.
- Confirmación enviada, pero es opcional. `CommandRouter.swift:351`
  ignitecli `DialogOrchestrator.swift:151`.
- Vitalidad presente únicamente en `wait-exit` y `IpcState.swift:58`.
- Limpieza previa al lanzamiento frente a la omisión por desplazamiento de bytes — `DialogLauncher.swift:199`,
  `CommandRouter.swift:79`.
