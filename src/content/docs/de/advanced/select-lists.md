---
title: Auswahllisten und Optionsfelder
description: Erstellen von Auswahllisten und Optionsgruppen zur Auswahl durch den Benutzer
translationSynced: 2026-11-20T10:50:16+00:00
---

Dialog bietet die Möglichkeit, eine Liste von Werten entgegenzunehmen und diese als Dropdown-Menü anzuzeigen, wobei optional eine Standardauswahl möglich ist.

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)

## Wie man es benutzt


### Titel der Auswahlliste

`--selecttitle <text>(,radio|required|searchable|multiselect|name="<text>")`

Die Beschriftung kann über die Kommandozeilenoption `--selecttitle` für die Liste festgelegt werden. Zum Beispiel: `--selecttitle "Select an Option"`

![image](https://user-images.githubusercontent.com/3598965/122635336-9ee98a80-d126-11eb-8839-f859eb19688e.png)


Dieser Name wird in der Ausgabe von swiftDialog auf der Standardausgabe (STDOUT) angezeigt, zusammen mit dem Wert des ausgewählten Elements. Für eine einfache Auswahlliste ist das Standardausgabeformat wie folgt:
```
    "SelectedOption" : "<value>"
    "SelectedIndex" : <index>
    "<name>" : "<value>"
    "<name>" index : "<index>"
```

Mehrere `--selecttitle` Argumente können angegeben werden. Verwandte `--selectvalues` und `--selectdefault` Argumente können ebenfalls angegeben werden und werden in der Reihenfolge ihrer Angabe einer Auswahlliste zugeordnet

Wenn mehrere Auswahlmöglichkeiten gleichzeitig verwendet werden, werden die Attribute "SelectedOption" und "SelectedIndex" nicht berücksichtigt.

Die Anzeige ausgewählter Elemente erfolgt nur, wenn der Exit-Code von swiftDialog den Wert 0 hat

### Wählen Sie Werte aus der Liste

`--selectvalues <text><csv>`

Die Werte werden im CSV-Format angegeben und über die Befehlszeilenoption `--selectvalues` übergeben, z. B. `--selectvalues "Option 1,Option 2,Option 3,Option 4, Option 5"`

![image](https://user-images.githubusercontent.com/3598965/122635303-6053d000-d126-11eb-94f1-6950f0e3d43e.png)

### Auswahlliste – Standardeinstellung

`--selectdefault <text>`

Die Standardeinstellung kann mithilfe der `--selectdefault` Befehlszeilenoption festgelegt werden, z. B. `--selectdefault "Option 4"`

![image](https://user-images.githubusercontent.com/3598965/122635358-c2143a00-d126-11eb-80b2-475a62b6ed9a.png)

Wenn kein Standardwert angegeben ist und der Benutzer keinen Eintrag aus der Liste auswählt, wird keine Ausgabe erzeugt.


Beispielausgabe:
```
    SelectedOption: Option 1
    SelectedIndex: 0
```

Die Anzeige bestimmter Elemente erfolgt nur, wenn der Exit-Code von Dialog 0 ist

### JSON-Konfiguration pro Argument

Auswahllisten können auch mithilfe von JSON-Objekten über `--selectitem` (oder `--selecttitle` mit einem JSON-Wert) definiert werden. Dies ermöglicht eine direktere Kontrolle über die Eigenschaften jedes einzelnen Elements.

**Syntax:**
```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU","required":true}'
```

**Eigenschaften:**
- `title` - Die Beschriftung für die Auswahlliste
- `values` - Array von Optionswerten
- `default` - Der standardmäßig ausgewählte Wert
- `required` - Gibt an, ob das Feld ausgefüllt werden muss (wird bei Radiobuttons ignoriert).
- `style` - Anzeigeformat: `list`, `radio`, `searchable` oder `multiselect`
- `name` - Alternativer Name für den Ausgabeschlüssel

**Beispiele:**

```bash
# Basic JSON item
dialog --selectitem '{"title":"Size","values":["S","M","L"],"default":"M"}'

# Searchable with required field
dialog --selectitem '{"title":"Region","values":["AU","US","UK"],"required":true,"style":"searchable"}'

# Radio button group
dialog --selectitem '{"title":"Priority","values":["Low","Medium","High"],"style":"radio"}'

# Mix JSON with positional arguments
dialog --selectitem '{"title":"Color","values":["red","green","blue"]}' --selectdefault "red"
```

JSON-Elemente sind unabhängig von positionellen `--selectvalues/--selecttitle/--selectdefault` Argumenten. Bei der Verwendung von JSON werden die Werte aus der Liste der positionellen Bezeichnungen gefiltert, um Duplikate zu vermeiden.

## JSON-Schema

Auswahlmöglichkeiten können mithilfe von JSON definiert werden, um eine direktere Steuerung zu ermöglichen.

### Gesamte Konfigurationsdatei im JSON-Format (JSON-Konfigurationsdatei).

```json
{
  "selectitems" : [
    {
      "title" : "Select Item",
      "name" : "altname",
      "values" : ["red","green","blue"],
      "default" : "red",
      "required" : false,
      "style" : "default | radio | searchable | multiselect"
    }
  ]
}
```

### JSON-Format pro Argument

Einzelne Elemente können auch mit `--selectitem` oder `--selecttitle` und einem JSON-Objekt definiert werden:

```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU"}'
dialog --selecttitle '{"title":"Size","values":["S","M","L"],"required":true}'
```

**Hinweis:** `--selecttitle` behandelt JSON-Objekte genauso wie `--selectitem`.

### Beispiele:

```json
"selectitems" : [
  {"title" : "Select 1", "values" : ["one","two","three"]},
  {"title" : "Select 2", "values" : ["red","green","blue"], "default" : "red"}
]
```

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)


```json
"selectitems" : [
  {"title" : "Pick One", "values" : ["One","Two","Three"], "style" : "radio"}
]
```

![image](https://github.com/bartreardon/swiftDialog/assets/3598965/1d2659c6-9048-440b-9246-2756ec097a24)


## Modifikatoren

### Name:

Verursacht, dass die Ausgabe mit dem angegebenen `name` aufgezeichnet wird, anstatt den Titel zu verwenden

```bash
% dialog --selecttitle "Alternate Name",name=alt --selectvalues "Option One, Option Two, Option Three"

"SelectedOption" : "Option One"
"SelectedIndex" : 0
"alt" : "Option One"
"alt" index : "0"
```

### Durchsuchbar

Der `searchable`-Modifikator fügt der Liste ein Suchfeld hinzu. Durch Eingabe von Text in das Textfeld wird die Liste gefiltert.

<img width="550" alt="image" src="/images/select_1.png" />

<img width="550" alt="image" src="/images/select_2.png" />

### Radio

Der Modifikator `radio` ändert die Auswahlliste so, dass eine Gruppe mit Radiobuttons angezeigt wird. Wenn `radio` ohne Angabe eines Standardeintrags verwendet wird, wird der erste Eintrag in der Liste zum standardmäßig ausgewählten Eintrag. Daher führt die Verwendung von Radiobuttons *immer* dazu, dass einer der Werte ausgewählt wird, und Modifikatoren wie `required` werden ignoriert.

`--selecttitle "Radio buttons",radio --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235897669-c08fdd79-aa14-4fec-8c6d-a930861a122f.png)

### Erforderlich

Der `required`-Modifikator bewirkt, dass diese bestimmte Liste zu einem Pflichtfeld wird, das einen Wert enthalten muss, bevor das Dialogfenster geschlossen wird

`--selecttitle "Required item",required --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235898090-5f7e9fac-2913-413f-ae85-c850ae86ee6b.png)

![image](https://user-images.githubusercontent.com/3598965/235898473-6fb9749f-3406-4f8d-b112-b214e95dccd4.png)

### Mehrfachauswahl

Der `multiselect`-Modifikator ermöglicht die Auswahl mehrerer Optionen aus der Liste. Die ausgewählten Elemente werden als entfernungsfähige Tags angezeigt, und die Ausgabe ist eine durch Kommas getrennte Liste der ausgewählten Werte.

`--selecttitle "Choose options",multiselect --selectvalues "Option One, Option Two, Option Three, Option Four"`

Wenn `multiselect` verwendet wird, werden die ausgewählten Werte als eine einzelne, durch Kommas getrennte Zeichenkette zurückgegeben:

```
"Choose options" : "Option One, Option Three"
```

Oder im JSON-Format:
```json
{
  "Choose options" : "Option One, Option Three"
}
```

## Globaler Stil

`--selectstyle [list | radio | searchable | multiselect]`

Legt den Anzeigestil für **alle** ausgewählten Listenelemente im Dialog fest. Dies entspricht einer globalen Einstellung, die die Stilmodifikatoren für jedes Element `--selecttitle` einzeln festlegt. Stilmodifikatoren, die für einzelne Listen `--selecttitle` definiert sind, haben Vorrang vor dieser globalen Einstellung.

| Wert | Beschreibung |
|---|---|
| `list` | Standard-Auswahlliste (Standardeinstellung). |
| `radio` | Optionsgruppe (mit Radiobuttons) |
| `searchable` | Ein Dropdown-Menü mit einem Filtertextfeld |
| `multiselect` | Ein Suchfeld, das mehrere Auswahlen ermöglicht |

## Abschnitte zur Liste hinzufügen

Fügen Sie in Ihrer Liste drei oder mehr Bindestriche `---` ein, wo immer Sie eine Trennung in der Liste benötigen

`--selectvalues "Option One, Option Two, ---, Option Three, Option Four, ---, Option Five"`

![image](https://user-images.githubusercontent.com/3598965/235900591-96ace495-5205-459c-9b2e-4bcd3ede00ee.png)

**HINWEIS: Jeder `---` wird im Index berücksichtigt, auch wenn der Trenner selbst nicht auswählbar ist. Im obigen Beispiel enthält das Array der Liste 7 Elemente, obwohl im Menü nur 5 angezeigt werden. Bitte berücksichtigen Sie dies bei der Erstellung Ihrer Auswahllisten.**

## Ausgabe

Dialog gibt den vom Benutzer ausgewählten Wert (oder den Standardwert, falls dieser angegeben wurde und der Benutzer keinen Wert auswählt) beim Beenden auf `stdout` aus. Diese Ausgabe kann von einem Skript analysiert und entsprechend verarbeitet werden.

Die Ausgabe enthält zwei Zeilen.
* Die erste Zeile enthält den Text des Listenelements und wird wie folgt ausgegeben: `SelectedOption: <text of item>`
* Die zweite Zeile gibt den Index des ausgewählten Elements an und hat das Format `SelectedIndex: <index of item>`

Der Index beginnt bei `0`, sodass, wenn das dritte Element in der Liste ausgewählt wird, die Ausgabe von `SelectedIndex` `SelectedIndex: 2` sein wird

## Beispielhafte Ausgabedaten

Angesichts der folgenden Ausgabe:
```
 SelectedOption: Option 4
 SelectedIndex: 3
```

Verwenden Sie die Programme `grep` und `awk`, um den gewünschten Wert zu extrahieren, den Sie weiterverarbeiten möchten

` | grep "SelectedOption" | awk -F ": " '{print $NF}'`

oder

` | grep "SelectedIndex" | awk -F ": " '{print $NF}'`

## Das Hinzufügen von Mehrfachauswahlfeldern

Um mehrere Auswahllisten hinzuzufügen, geben Sie einfach mehrere Instanzen von `--selectvalues`, `--selecttitle` und `--selectdefault` an. Der Titel und der Standardwert werden in der Reihenfolge zugewiesen, in der sie angegeben sind.


### Mehrfachauswahl-Ausgabe

Wenn mehrere Auswahllisten verwendet werden, wird die Ausgabe so angepasst, dass die verschiedenen benannten Listen verarbeitet werden können. Zum Beispiel: Wenn das oben genannte JSON-Format verwendet und die Optionen "zwei" und "rot" ausgewählt werden, ergibt dies die folgende Ausgabe:

```
Select 1 : two
Select 1 index : 1
Select 2 : red
Select 2 index : 0
```

Wenn die Ausgabe im JSON-Format erfolgt, würde dies zu folgendem Ergebnis führen:

```json
{
  "Select 1" : {
    "selectedIndex" : 1,
    "selectedValue" : "two"
  },
  "Select 2" : {
    "selectedIndex" : 0,
    "selectedValue" : "red"
  }
}
```