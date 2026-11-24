---
title: Casillas de verificación
description: Creación de casillas de verificación y botones de alternancia interactivos en swiftDialog
translationSynced: 2026-11-24T22:26:54+00:00
---

Las casillas de verificación se pueden utilizar para ofrecer una serie de opciones que pueden seleccionarse o no, y que luego se procesarán.

## Uso básico

Especifique uno o más parámetros `--checkbox <text>` y el diálogo mostrará una casilla de verificación con `<text>` como etiqueta.

### Estilo

Las casillas de verificación también pueden mostrarse como un interruptor en lugar de una casilla.

La opción predeterminada es mostrarlo como una casilla de verificación junto a la etiqueta:

![image](https://user-images.githubusercontent.com/3598965/235893894-1d4c26ba-1afc-4e9f-a58d-16a36c27787f.png)

Utilice la opción `--checkboxstyle switch` para cambiar el estilo del interruptor:

![image](https://user-images.githubusercontent.com/3598965/235894156-c8cf82e7-d627-43a4-b11e-3acfc296a3e2.png)

Si prefiere un estilo de interruptor más grande, puede especificarlo como una propiedad del estilo del interruptor:

Las opciones son `mini`, `small`, `regular` o `large`

`--checkboxstyle switch,large`

![image](https://user-images.githubusercontent.com/3598965/235894351-71200445-5871-4e27-b792-2a983a34514c.png)
## Uso avanzado

Al utilizar la configuración [JSON](/es/advanced/json-configuration) para establecer las opciones del diálogo, se habilitan parámetros de casilla de verificación opcionales.

El formato del archivo JSON es el siguiente:

```json
{
  "checkbox" : [
	  {"label" : "<label>", "checked" : false, "disabled" : false, "icon" : "<file|url>" }
	],
 "checkboxstyle" : {
    "style" : "switch",
    "size"  : "regular"
	}
}
```

`"checked" : [true|false]` - Inicializará la casilla de verificación en estado marcado si se establece en `true`. El valor predeterminado es "desmarcada".

`"disabled" : [true|false]` - Deshabilitará la casilla de verificación si está configurada en `true`, independientemente de si está marcada o no

`"icon" : "<file|url>"` - Está disponible como parámetro JSON cuando `checkboxstyle` se establece en `switch`; de lo contrario, se ignorará

<img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-16aa041aeeca8ffc.png" width=400>

### Configuración JSON para argumentos individuales

A partir de la versión 3.1.1, las casillas de verificación también pueden especificarse como objetos JSON a través de `--checkbox` (en lugar de utilizar el archivo JSON de configuración completo). Esto proporciona un control más directo y es especialmente útil para configuraciones complejas.

**Sintaxis:**
```bash
dialog --checkbox '{"label":"Enable telemetry","checked":true,"enableButton1":true}'
```

**Características:**
- `label` - El texto de la etiqueta de la casilla de verificación
- `checked` - Estado inicial (verdadero/falso, valor predeterminado: falso).
- `disabled` - Indica si la casilla de verificación está desactivada (verdadero/falso, valor predeterminado: falso).
- `enableButton1` - Activar el botón 1 cuando esta casilla de verificación esté marcada (verdadero/falso).
- `icon` - Ruta al icono o objeto de icono en formato JSON (solo se utiliza con el estilo `switch`).

**Ejemplos:**

```bash
# Basic checkbox
dialog --checkbox '{"label":"I agree to terms"}'

# Checked by default
dialog --checkbox '{"label":"Enable notifications","checked":true}'

# Checkbox that enables Button 1
dialog --checkbox '{"label":"I understand","enableButton1":true}' --button1disabled

# Checkbox with icon (switch style)
dialog --checkbox '{"label":"Enable feature","checked":true,"icon":"/System/Library/CoreServices/Software Update.app"}' --checkboxstyle switch

# Checkbox with JSON icon object
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}' --checkboxstyle switch
```

**Nota:** Cuando se utiliza `enableButton1`, también se debe establecer `--button1disabled` para evitar que el usuario haga clic en el botón antes de marcar la casilla.

### JSON de configuración completa

El formato JSON de configuración completa sigue estando disponible.

```json
{
  "checkbox" : [
    {"label" : "Option 1", "checked" : true, "disabled" : true },
    {"label" : "Option 2", "checked" : true, "disabled" : false },
    {"label" : "Option 3", "checked" : false }
  ],
  "checkboxstyle" : {
    "style" : "switch",
    "size" : "large"
  }
}
```

### ejemplo

El siguiente código JSON y la captura de pantalla del diálogo resultante ilustran cómo se comportan estas configuraciones.

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true, "disabled" : false },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5" },
	  {"label" : "Option 6", "disabled" : true }
	]
}
```

![image](https://user-images.githubusercontent.com/3598965/150663608-6ee03207-0558-4769-a016-44fe5822fccb.png)

## Usar una casilla de verificación para controlar el estado del botón1

Puede utilizar una casilla de verificación para controlar el estado del botón predeterminado. Esto es útil si desea asegurarse de que el usuario haya seleccionado una opción obligatoria antes de continuar.

Aquí hay un ejemplo:

`dialog --checkbox "I Agree",enableButton1 --button1disabled`

<img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/5a4d2ce4-ea37-447d-86d1-a12ca9d4807e"> <img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/ec12eb71-b6f9-466e-ad32-cb8812bc759c">

Esto también se puede configurar utilizando JSON:

```json
{
  "checkbox" : [
    {"label" : "I Agree", "enableButton1" : true }
  ],
  "button1disabled" : true
}
```

 > Es importante deshabilitar inicialmente el botón1, de lo contrario, el usuario podría hacer clic en el botón antes de que la casilla de verificación esté marcada. Esto no está configurado por defecto. También es importante señalar que establecer la propiedad `disabled` así como `enablebutton1` en una casilla de verificación no es recomendable, ya que esto hará que la casilla de verificación no sea accesible

## Salida

Los resultados se envían a la salida estándar (stdout) y, por defecto, tienen el siguiente formato:
```
Option 1 : true
Option 2 : true
Option 3 : false
Option 4 : true
Option 5 : false
Option 6 : false
```

Opcionalmente, puede especificar el parámetro `--json` y obtener los resultados en formato JSON:

```json
{
  "Option 2" : true,
  "Option 4" : true,
  "Option 5" : false,
  "Option 6" : true,
  "Option 1" : true,
  "Option 3" : false
}
```