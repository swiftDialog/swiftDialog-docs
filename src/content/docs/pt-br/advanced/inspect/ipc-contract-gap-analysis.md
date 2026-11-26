---
title: Análise de lacunas nos contratos do ICP
description: Uma análise comparativa do contrato IPC entre swiftDialog e ignitecli, que identifica as lacunas observadas, os riscos envolvidos e as cláusulas contratuais propostas para garantir uma comunicação eficiente e robusta entre os dois componentes.
translationSynced: 2026-11-25T11:43:22+00:00
---

**Status:** Rascunho para revisão. **Data:** 17 de junho de 2026. **Escopo:** Comunicação entre processos (IPC) em tempo de execução entre `swiftDialog` (Modo de Inspeção, predefinições 1–6) e `ignitecli`, que é responsável por iniciá-lo e controlá-lo. **Repositórios:**
- swiftDialog — `/Users/henry/Projects/GitHub/swiftDialog`
- ignitecli — `/Users/henry/Projects/GitHub/ignitecli-swift-private`

Este documento descreve o contrato do IPC como ele existe atualmente e, em seguida, lista as áreas em que as duas partes concordam apenas por coincidência ou onde uma garantia é assumida, mas não aplicada. Cada afirmação está fundamentada em uma referência específica `file:line` para que possa ser verificada novamente.

---

## 1. Visão geral do transporte

Três sistemas de transporte estão em operação. O contrato engloba todos os três; uma implementação eficaz não deve presumir que nenhum deles seja confiável individualmente.

| Transporte | Direção | Canal / Caminho | Carga útil | Confiabilidade |
|---|---|---|---|---|
| Notificação (comando) distribuída. | ignitecli → diálogo | `com.swiftdialog.command` **e** `com.ignitecli.command` | `userInfo` dicionário, convertido em string | Tentativa de envio, sem garantia de ordem, **perda de dados se enviados antes do registro do observador** |
| Notificação distribuída (evento). | dialog → ignitecli | `com.swiftdialog.event` | `userInfo` dicionário, incluindo `event` e `pid` | Máximo esforço |
| Notificação distribuída (confirmação). | dialog → ignitecli | `com.swiftdialog.ack` | `userInfo` Dicionário, incluindo `command`, `stepId`, `status`, `pid` | Esforço máximo, **raramente utilizado** |
| Arquivo de gatilho / arquivo de comando | ignitecli → diálogo | `--status-log-file` / por processo (PID). `.command` | Delimitado por novas linhas, com campos separados por dois pontos | Durável, com rastreamento por deslocamento de bytes |
| Arquivo de prontidão | dialog → ignitecli | `<trigger>.ready` ou configuração `readinessFile` | JSON | Durável, com ausência de chifres |
| Arquivo de evento | dialog → ignitecli | configuração `eventFile` ou derivada `.events` | JSONL | Durável, sem cauda |
| Arquivo de resultados | dialog → ignitecli | configuração `resultFile` / por processo (PID) `.result.json` | JSON | Durável |
| Diretório de sessões publicadas | diálogo → *(ninguém)* | `--published-sessions-dir` (padrão `/private/tmp/swiftdialog/sessions/<pid>.json`) | JSON | Durável, **não consumível** — veja a lacuna 1 |
| Estado da comunicação entre processos (IPC) do ignitecli | ignitecli → ignitecli | `/private/tmp/.ignitecli-ipc-<pid>.json` | JSON | Durável |

Pontos de referência
- Canais: `dialog/Views/Inspect/Core Framework/DistributedNotifications.swift:36`;
  ignitecli `Sources/Dialog/ActionDispatcher.swift:9`.
- Publicação em ambos os canais: utilize o comando `ignitecli` `Sources/Commands/IpcCommand.swift:414`.
- Roteamento de arquivos de comando: `dialog/Views/Inspect/Core Framework/CommandRouter.swift:76`.
- Diretório das sessões publicadas: `dialog/Command Line/CommandLineArguments.swift:167`,
  `dialog/Views/Inspect/Core Framework/PresetCommonHelpers.swift:1134`.
- ignitecli: estado: `Sources/Dialog/IpcState.swift:11`.

---

## 2. Vocabulário do evento (o contrato de fornecimento).

O swiftDialog emite os seguintes tipos de eventos (`DistributedNotifications.swift:36`, valores brutos bloqueados):

| Tipo de evento | Valor bruto | Emitido quando | Campos principais |
|---|---|---|---|
| `ready` | `ready` | Interface pronta para receber comandos | `triggerFile`, `preset?`, `itemCount?`, `items?`, `ackChannel` |
| `exit` | `exit` | Prestes a ser encerrado | `triggerFile`, `exitCode?`, `completedCount?`, `failedCount?`, `resultFile?` |
| `deferred` | `defer` | Usuário suspenso | `duration`, `seconds`, `exitCode`, `resultFile` |
| `button` | `button` | Clique no botão | `stepId`, `button`, `action` |
| `step` | `step` | Transição de degrau | `stepId`, `action` (e.g. `completed`, `all_complete`) |
| `selection` | `selection` | Commit de seleção/grade | `key`, `values` |

O modo predefinido 6 foi confirmado como emissor de `step`, `button`, `selection` (`Preset6.swift:1251`, `:1116`, `:1638`).

Comandos aceitos (ignitecli → diálogo), roteados em: `CommandRouter.swift:76–163`, `success`, `failure`, `warning`, `complete`, `navigate`/`goto`, `next`/`prev`/`back`, `reset`, `progress`, `update_guidance`, `update_message`, `batch_update`, `display_data`, `recheck`, `set`, `item`, `listitem`, `select`. As teclas de atalho `userInfo` expandem-se para esses comandos (`DistributedNotifications.swift:177`).

---

## 3. Lacunas

Classificados por gravidade. Cada item descreve a **realidade observada**, o **risco** e uma **cláusula contratual proposta** (linguagem normativa para uma futura especificação compartilhada).

### Problema 1 – O diretório de sessões publicado possui permissão de escrita apenas; o ignitecli nunca o lê. · **ALTO**

**Observed.** swiftDialog writes a per-PID discovery file to `/private/tmp/swiftdialog/sessions/<pid>.json` (`PresetCommonHelpers.swift:1134`, CLI `CommandLineArguments.swift:167`). A grep of all of ignitecli `Sources/` finds **no reader** for that directory. ignitecli discovers sessions solely via its own `/private/tmp/.ignitecli-ipc-<pid>.json` (`IpcState.swift:11`), which it wrote at launch.

Dois registros paralelos descrevem o mesmo fato (qual diálogo está ativo em qual arquivo de gatilho) e nunca são sincronizados.

| Registro | swiftDialog escreve | ignitecli lê |
|---|---|---|
| `…/swiftdialog/sessions/<pid>.json` | ✅ | ❌ |
| `…/.ignitecli-ipc-<pid>.json` | ❌ | ✅ |

**Risco:** O utilitário `ignitecli` só pode se conectar a uma janela de diálogo que ele próprio iniciou. Se o arquivo de estado do `ignitecli` for perdido (devido a uma falha, reinicialização ou execução separada), a janela de diálogo em execução não poderá ser recuperada, mesmo que o `swiftDialog` a esteja anunciando. A função de descoberta, recentemente lançada, não oferece nenhum benefício para o único componente que a utiliza.

**Cláusula proposta.**
> A swiftDialog publicará um registro de descoberta para cada sessão ativa. A ignitecli deverá...
> Considere o diretório das sessões publicadas como a fonte de informações mais confiável e DEVE:
> ser possível adotar uma sessão encontrada ali (leia `triggerFile`, `resultFile`,
> `readinessFile`, `ackChannel`, `pid`) sem que ela tenha sido lançada. O utilitário ignitecli
> O arquivo de estado privado pode permanecer como um cache durante a inicialização, mas NÃO deve ser a única fonte de dados
> fonte de informação confiável.

**Decisão aberta (responsável: ignitecli).** O diretório de sessões é destinado à recuperação do ignitecli, ou para ferramentas *externas* (monitoramento/MDM)? Essa escolha determina se o ignitecli desenvolverá um caminho de "descoberta e adoção" ou se essa funcionalidade permanecerá intencionalmente separada.

### Lacuna 2 – Caminho do arquivo de evento derivado por duas regras diferentes. **NÍVEL MÉDIO.**

**Observado.** O swiftDialog resolve o caminho do evento como `config.eventFile ?? readinessFile(.ready → .events)` (`Preset5.swift:4834`, idêntico em `Preset1.swift:460`, `Preset2.swift:533` e no Preset 6). Os modelos do ignitecli **sempre definem `eventFile` explicitamente** (`Sources/Resources/templates/*/config.json` → `/tmp/__WORKFLOW_NAME__.events`). Eles convergem apenas porque a configuração sempre define a chave.

**Risk.** A config that sets a custom `readinessFile` and omits `eventFile` makes swiftDialog derive a path ignitecli's `wait-step` is not watching. `wait-step` (`IpcCommand.swift` WaitStep, 2 s poll) then hangs to its timeout with no diagnostic naming the path mismatch.

**Cláusula proposta.**
> O caminho do arquivo de evento DEVE ser derivado por exatamente uma regra, compartilhada por ambas as partes.
> Se ambas as extremidades derivam (em vez de exigirem uma especificação `eventFile`), então...
> O algoritmo de derivação DEVE ser especificado aqui, integralmente, e deverá ser objeto de um teste
> cada lado. Um `wait-step` tempo limite (timeout) DEVE incluir o caminho do arquivo de evento resolvido
> Seu erro.

### Lacuna 3 – Garçons que fazem a diferença não verificam a continuidade do processo. · **MÉDIA**

**Observado.** `wait-exit` verifica `kill(pid, 0)` (`IpcState.swift:58`) e detecta uma comunicação interrompida. `wait-ready` e `wait-step` aguardam uma notificação ou alteração em um arquivo; `wait-step` só detecta um processo (PID) inativo se a verificação inicial for acionada, caso contrário, ele espera o tempo limite completo (`IpcCommand.swift` WaitStep, `:376`).

**Risco.** Uma falha durante a execução de uma etapa específica pode resultar em um erro generalizado de tempo limite (de 2 a 600 segundos), sem indicar a causa real da falha.

**Cláusula proposta.**
> Todo garçom (`wait-ready`, `wait-step`, `wait-exit`) deverá responder a uma pesquisa sobre `kill(pid,0)`
> o mesmo intervalo de tempo que a verificação de arquivos/notificações e DEVE apresentar falha rapidamente ao...
> `dialog PID <n> exited before <condition>` em vez de um tempo limite genérico.

### Lacuna 4 — O canal de confirmação (ACK) existe em ambas as extremidades, mas não está sendo utilizado como uma barreira. **NÍVEL MÉDIO**

**Observado.** O swiftDialog envia mensagens para `com.swiftdialog.ack` após cada comando roteado (`CommandRouter.swift:351`). O ignitecli possui `waitAck()` (`Sources/Dialog/DialogOrchestrator.swift:151`), mas a maioria dos fluxos de trabalho nunca o utiliza; o modo de entrega padrão é "enviar e esquecer", utilizando um transporte com melhor esforço.

**Risco.** Uma notificação `navigate` que falha e impede a execução de um lote subsequente pré-carregado pode causar uma interrupção silenciosa em todo o processo. Interfaces de usuário que suportam operações repetidas (idempotentes) toleram essa perda; comandos críticos para a ordem de execução não.

**Cláusula proposta.**
> Comandos que impedem a execução de comandos subsequentes (`navigate`, `goto`, `reset`,
> `batch_update` Aquela mensagem que precede a solicitação de navegação DEVE ser enviada com a opção "aguardar confirmação" habilitada.
> O `ignitecli` tentará novamente ou exibirá um erro caso não receba uma confirmação (ACK) para um determinado comando
> Dentro do período de tempo limite de confirmação (ACK). A funcionalidade "disparar e esquecer" continua permitida para operações de pintura idempotentes
> (`progress`, `update_message`, `display_data`).

### Problema 5 — Correção de um problema relacionado à repetição de arquivos de gatilho, que ocorreu duas vezes e não foi atribuído a nenhum responsável. **BAIXO a MÉDIO.**

**Observed.** ignitecli deletes IPC files pre-launch (`DialogLauncher.swift:199`) to stop swiftDialog replaying stale `success:` lines (the preset-5 flash-through). swiftDialog independently records the initial byte offset to skip pre-existing content (`CommandRouter.swift:79`). Two independent fixes guard one hazard.

**Risco.** Se qualquer uma dessas situações ocorrer — o swiftDialog lê novamente a partir do deslocamento 0, ou o ignitecli ignora a limpeza em um novo caminho — o erro se manifesta de forma silenciosa.

**Cláusula proposta.**
> O swiftDialog ignorará qualquer conteúdo do arquivo de gatilho que esteja presente antes de ser exibido. `ready`
> Esta garantia será de responsabilidade e será testada pela equipe da swiftDialog; a ferramenta ignitecli
> A limpeza realizada antes do lançamento é uma medida de segurança adicional, e não a garantia principal.

### Gap 6 – Ausência de autenticação em qualquer tipo de conexão (aceitável, mas não especificado). **BAIXO**

**Observado:** Não há validação do remetente nas notificações distribuídas (a API não oferece essa funcionalidade); o arquivo de comando/gatilho é acessível a todos; o diretório de sessões é legível e listável por qualquer usuário. Qualquer processo local pode controlar ou falsificar a interação e pode listar os processos (PIDs) em execução, bem como os caminhos dos gatilhos. O novo diretório de sessões *amplia* essa superfície de exposição de informações.

**Risco.** Aceitável em um modelo de confiança local com um único usuário; perigoso se essa premissa for violada (servidor compartilhado, usuário com privilégios reduzidos).

**Cláusula proposta.**
> A fronteira de confiança do IPC (Inter-Process Communication) é definida como "mesmo usuário, mesmo host, local". Todos os mecanismos de transporte assumem uma...
> cooperando com o remetente local. Esta é uma premissa intencional e documentada; não há...
> O transporte oferece autenticação ou integridade. Qualquer implementação fora desse contexto...
> A funcionalidade "boundary" está fora do escopo e não é suportada.

---

## 4. Resumo e classificação da gravidade

| # | Gap | Gravidade | Localizar/Encontrar a posição |
|---|---|---|---|
| 1 | Diretório de sessões, somente para escrita | ALTO | ignitecli (leitor) |
| 2 | Duas regras de percurso de eventos | MÉDIO | ambos (governo compartilhado) |
| 3 | Garçons evitam o contato direto com os clientes | MÉDIO | ignitecli |
| 4 | "Ack" não foi utilizado como barreira | MÉDIO | ignitecli (política) |
| 5 | A função de repetição foi corrigida duas vezes | BAIXO – MÉDIO | swiftDialog (tenha a garantia) |
| 6 | Sem autorização, não especificado | BAIXO | Apenas documento |

**Ordem recomendada.** Comece implementando este contrato (os itens 5 e 6 são específicos para a documentação e devem ser implementados imediatamente). Em seguida, implemente **o item 1 e o item 2 juntos** — configure o `ignitecli` para usar o diretório de sessões publicado como a fonte de descoberta principal e simplifique a derivação do caminho do evento para uma única regra. Isso transformará as recentes alterações no sistema de comunicação entre processos (IPC) do `swiftDialog` em algo que o `ignitecli` realmente utiliza. Os itens 3 e 4 são melhorias independentes na robustez do `ignitecli` que podem ser implementadas posteriormente.

---

## 5. Registro de verificação

As informações contidas neste documento foram verificadas em relação à fonte em 17 de junho de 2026:

- O diretório "sessions" não é lido pelo utilitário ignitecli — busca por `Sources/`
  `swiftdialog/sessions` / `publishedSessions`: não para o consumidor.
- A predefinição 6 emite sinais de passo/botão/seleção — `Preset6.swift:1116,1152,1251,1638`.
- Derivação dual de eventos — `Preset1.swift:460`, `Preset2.swift:533`,
  `Preset5.swift:4834`; Comando "ignitecli" usado explicitamente `eventFile` em `Sources/Resources/templates/*/config.json`.
- Confirmação enviada, mas é opcional — `CommandRouter.swift:351`
  ignitecli `DialogOrchestrator.swift:151`.
- Disponível apenas em `wait-exit` — `IpcState.swift:58`.
- Limpeza antes do lançamento versus pulo de deslocamento de bytes — `DialogLauncher.swift:199`,
  `CommandRouter.swift:79`.
