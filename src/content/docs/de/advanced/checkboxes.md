---
title: Kontrollkästchen
description: Erstellen von interaktiven Kontrollkästchen und Schaltern in swiftDialog
translationSynced: 2026-11-20T10:51:35+00:00
---

Kontrollkästchen können verwendet werden, um eine Reihe von Optionen anzubieten, die ausgewählt oder nicht ausgewählt werden können und anschließend verarbeitet werden.

## Grundlegende Nutzung

Geben Sie einen oder mehrere `--checkbox <text>` Parameter an, und das Dialogfenster zeigt ein Kontrollkästchen an, wobei `<text>` als Beschriftung verwendet wird.

### Stil

Kontrollkästchen können alternativ als Schalter und nicht als Kontrollkästchen dargestellt werden.

Standardmäßig wird dies als ein Kontrollkästchen neben der Beschriftung angezeigt:

![image](https://user-images.githubusercontent.com/3598965/235893894-1d4c26ba-1afc-4e9f-a58d-16a36c27787f.png)

Verwenden Sie die Option `--checkboxstyle switch`, um das Design des Schalters zu ändern:

![image](https://user-images.githubusercontent.com/3598965/235894156-c8cf82e7-d627-43a4-b11e-3acfc296a3e2.png)

Wenn Sie einen größeren Schalter bevorzugen, können Sie dies als Eigenschaft für den Schalterstil angeben:

Die Optionen sind `mini`, `small`, `regular` oder `large`

`--checkboxstyle switch,large`

![image](https://user-images.githubusercontent.com/3598965/235894351-71200445-5871-4e27-b792-2a983a34514c.png)
## Fortgeschrittene Nutzung

Wenn [JSON-Konfigurationen](/de/advanced/json-configuration) verwendet werden, um Dialogoptionen festzulegen, werden optionale Kontrollkästchenparameter verfügbar.

Die JSON-Datei hat folgendes Format:

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

`"checked" : [true|false]` - Initialisiert das Kontrollkästchen im angekreuzten Zustand, wenn dieser Wert auf `true` gesetzt ist. Standardmäßig ist das Kontrollkästchen nicht angekreuzt.

`"disabled" : [true|false]` - Deaktiviert das Kontrollkästchen, wenn es auf `true` eingestellt ist, unabhängig vom aktuellen Zustand (aktiviert oder deaktiviert)

`"icon" : "<file|url>"` ist als JSON-Parameter verfügbar, wenn `checkboxstyle` auf `switch` eingestellt ist; andernfalls wird es ignoriert

<img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-16aa041aeeca8ffc.png" width=400>

### JSON-Konfiguration pro Argument

Ab Version 3.1.1 können Kontrollkästchen auch als JSON-Objekte über `--checkbox` definiert werden (anstatt die gesamte Konfigurationsdatei im JSON-Format zu verwenden). Dies ermöglicht eine direktere Steuerung und ist besonders nützlich für komplexe Konfigurationen.

**Syntax:**
```bash
dialog --checkbox '{"label":"Enable telemetry","checked":true,"enableButton1":true}'
```

**Eigenschaften:**
- `label` - Der Text der Beschriftung für das Kontrollkästchen
- `checked` - Anfangszustand (wahr/falsch, Standardwert: falsch)
- `disabled` - Ob das Kontrollkästchen deaktiviert ist (wahr/falsch, Standardwert: falsch).
- `enableButton1` - Aktivieren Sie Schaltfläche 1, wenn dieses Kontrollkästchen aktiviert ist (wahr/falsch).
- `icon` - Pfad zum Symbol oder JSON-Objekt für das Symbol (nur bei Verwendung des `switch`-Stils).

**Beispiele:**

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

**Hinweis:** Wenn Sie `enableButton1` verwenden, sollten Sie auch `--button1disabled` aktivieren, um zu verhindern, dass der Benutzer auf die Schaltfläche klickt, bevor das Kontrollkästchen aktiviert wurde.

### Gesamte Konfigurationsdatei im JSON-Format

Die vollständige JSON-Konfigurationsform wird weiterhin unterstützt:

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

### Beispiel

Die folgenden JSON-Daten und der resultierende Screenshot des Dialogfensters veranschaulichen, wie diese Einstellungen funktionieren.

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

## Die Verwendung einer Kontrollkästchen zur Steuerung des Zustands von Schaltfläche 1

Sie können ein Kontrollkästchen verwenden, um den Zustand des Standardbuttons zu steuern. Dies ist nützlich, wenn Sie sicherstellen möchten, dass der Benutzer eine erforderliche Option ausgewählt hat, bevor er fortfährt.

Beispiel:

`dialog --checkbox "I Agree",enableButton1 --button1disabled`

<img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/5a4d2ce4-ea37-447d-86d1-a12ca9d4807e"> <img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/ec12eb71-b6f9-466e-ad32-cb8812bc759c">

Dies kann auch mithilfe von JSON konfiguriert werden:

```json
{
  "checkbox" : [
    {"label" : "I Agree", "enableButton1" : true }
  ],
  "button1disabled" : true
}
```

 > Es ist wichtig, die Schaltfläche "button1" anfänglich zu deaktivieren, da der Benutzer sonst die Schaltfläche anklicken könnte, bevor das Kontrollkästchen aktiviert wurde. Dies ist standardmäßig nicht der Fall. Es sollte außerdem erwähnt werden, dass das Setzen der Eigenschaften `disabled` und `enablebutton1` bei einem Kontrollkästchen nicht empfehlenswert ist, da dies das Kontrollkästchen unzugänglich macht

## Ausgabe

Die Ergebnisse werden an die Standardausgabe gesendet und haben standardmäßig folgendes Format:
```
Option 1 : true
Option 2 : true
Option 3 : false
Option 4 : true
Option 5 : false
Option 6 : false
```

Optional können Sie den Parameter `--json` angeben und die Ergebnisse im JSON-Format erhalten:

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