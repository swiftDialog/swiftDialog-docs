---
title: Textfelder
description: Das Erstellen von Textfeldern mit verschiedenen Eigenschaften und Validierungsfunktionen
translationSynced: 2026-11-23T08:35:52+00:00
---

Die `--textfield` Option ermöglicht es, einen Bereich festzulegen, in den der Benutzer Text eingeben kann, bevor das Dialogfenster geschlossen wird

Es nimmt einen Parameter als Text entgegen und verwendet diesen Parameter sowohl als Beschriftung für das Textfeld in der Dialogoberfläche als auch in den Ausgabedaten für Berichte

Die Ergebnisse werden im folgenden Format an die Standardausgabe (stdout) gesendet, wenn das Programm beendet wird:

`<textfield text> : <user input>`

oder falls die Option `--json` zur Aktivierung der JSON-Ausgabe verwendet wird:

```json
{
"<textfield text>" : "<user input>"
}
```

## Beispiele

Wenn Sie den folgenden Dialog verwenden:

`dialog --textfield "Textfield 1"`

Zeigt den folgenden Dialog an:

![image](https://user-images.githubusercontent.com/3598965/235908715-5f24a167-5ad1-4f81-aa7e-30faf5590b1c.png)

Der Benutzer gibt eine Antwort ein:

![image](https://user-images.githubusercontent.com/3598965/235908865-40b37eac-874b-4ceb-a4e7-e8701ebdf790.png)

was zu folgendem Ergebnis führen wird:

`Textfield 1 : This is what the user entered`

oder wenn Sie `--json` verwenden

```json
{
"Textfield 1" : "This is what the user entered"
}
```

## Zusätzliche Textfelder

Mehrere Textfelder können angegeben werden, indem zusätzliche `--textfield` Optionen beim Aufruf des Dialogfensters hinzugefügt werden

e.g. `dialog --textfield "Textfield 1" --textfield "Textfield 2"`

![image](https://user-images.githubusercontent.com/3598965/235909015-2c4f187b-a86d-4281-84ff-09afa6b87857.png)

Sie können so viele Textfelder angeben, wie Sie benötigen. Jedes Textfeld wird als ein separates Feld in der Ausgabe dargestellt.

Möglicherweise müssen Sie die `--height` Ihres Dialogfensters anpassen, wenn Sie mehrere Textfelder hinzufügen, damit diese Platz finden

Beispiel:

`dialog --textfield "First Name" --textfield "Surname" --textfield "Age" --textfield "Favourite Colour"`

Dies führt zu folgendem Ergebnis:

```
First Name : Joe
Surname : Bloggs
Age : 32
Favourite Colour : Red
```

`--json`
```json
{
"First Name" : "Joe",
"Surname" : "Bloggs",
"Age" : "32",
"Favourite Colour" : "Red"
}
```

## Textfeld-Modifikatoren

Modifikatoren werden als kommagetrennte Werte an das Label des Textfelds angefügt.

```sh
--textfield "<label>,<modifier>,<modifier>=<value>"
```

| Modifikator | Beschreibung |
|---|---|
| `name=<text>` | Verwenden Sie diesen Wert als Ausgabeschlüssel anstelle des Labels |
| `required` | Das Feld muss ausgefüllt sein, bevor swiftDialog geschlossen wird |
| `secure` | Passwortfeld: Eingabe während der Eingabe verbergen. |
| `passwordfill` | Aktivieren Sie die automatische Passworteingabe von macOS für ein `secure` Feld |
| `prompt="<text>"` | Platzhaltertext, der innerhalb des Feldes angezeigt wird (wird nicht in der Ausgabe zurückgegeben). |
| `value="<text>"` | Füllen Sie das Feld mit einem Standardwert vor, der jedoch bearbeitbar ist. |
| `regex=<pattern>` | Stellen Sie sicher, dass der Inhalt eines Feldes mit einem regulären Ausdruck übereinstimmt |
| `regexerror=<text>` | Eine benutzerdefinierte Fehlermeldung wird angezeigt, wenn der reguläre Ausdruck nicht erfüllt ist |
| `editor` | Ein mehrzeiliger Texteditor anstelle eines einzelnen Textfelds |
| `isdate` | Ersetzen Sie das Textfeld durch einen Datums-Auswahlkalender. Die Ausgabe wird als kurzer Datumsstring formatiert. |
| `fileselect` | Fügen Sie eine Schaltfläche mit der Beschriftung "Auswählen" hinzu, die einen Dateiauswahl-Dialog öffnet |
| `filetype=<types>` | Beschränken Sie den Dateiauswahl-Dialog auf die angegebenen Dateitypen (durch Leerzeichen getrennt). Verwenden Sie Dateiendungen (z. B. `png jpg`) oder die Typ-Schlüsselwörter `folder`, `image`, `movie`, `video`, `audio`. |
| `path=<path>` | Legen Sie das Startverzeichnis für den Dateiauswahl-Dialog fest |
| `confirm` | Fügen Sie ein Bestätigungsfeld hinzu, dessen Inhalt mit dem Inhalt des Hauptfelds übereinstimmen muss |

### Name

`name=<text>` Ersetzt das Label als Schlüssel in der Ausgabe. Nützlich, wenn Sie eine benutzerfreundliche Bezeichnung wünschen, aber einen präziseren Schlüsselnamen in der Ausgabe benötigen.

### Sicher

`secure` Verbirgt die eingegebenen Zeichen während der Eingabe und zeigt ein Schloss-Icon an. Der Inhalt wird weiterhin als Klartext auf der Standardausgabe ausgegeben.

```sh
--textfield "Password,secure"
```

![image](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

### Passwort-Ausfüllfunktion

`passwordfill` Aktiviert die Funktion zur automatischen Eingabe von Passwörtern unter macOS. Muss in Kombination mit `secure` verwendet werden.

```sh
--textfield "Password,secure,passwordfill"
```

### Erforderlich

`required` Verhindert, dass sich das Dialogfenster "swiftDialog" schließt, bevor ein Wert in das Feld eingegeben wurde. Pflichtfelder sind mit einem `*` gekennzeichnet und werden hervorgehoben, wenn der Benutzer versucht, das Fenster zu schließen, ohne sie auszufüllen.

```sh
--textfield "Full Name,required"
```

![image](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)

### Schnell

`prompt="<text>"` zeigt Text als Platzhalter innerhalb des Feldes. Dieser Text verschwindet, sobald der Benutzer mit der Eingabe beginnt, und wird nicht in der Ausgabe berücksichtigt. Nicht unterstützt bei Feldern vom Typ `secure`.

```sh
--textfield "Name,prompt="Enter your full name""
```

![image](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

### Wert

`value="<text>"` Das Feld wird vorab mit einem Standardwert gefüllt, den der Benutzer bearbeiten kann.

```sh
--textfield "Default Value Test",value="Some default value"
```

![image](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

### Reguläre Ausdrücke und Fehler bei regulären Ausdrücken

`regex=<pattern>` Verlangt, dass der Inhalt des Feldes mit dem regulären Ausdruck übereinstimmt, bevor swiftDialog beendet wird. `regexerror=<text>` Legt die Meldung fest, die angezeigt wird, wenn das Muster nicht übereinstimmt.

Es sei denn, das Muster erlaubt es ausdrücklich, ein `regex`-Feld darf nicht leer sein.

```sh
--textfield "Product Code",prompt="Enter 5 digit code",regex="\d{5}",regexerror="Must be a five digit number"
```

![image](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

Verwenden Sie `--textfieldlivevalidation`, um eine grüne/rote Überlagerung auf dem Feld anzuzeigen, während der Benutzer tippt, um sofortiges Feedback darüber zu geben, ob der reguläre Ausdruck erfüllt ist.

### Texteditor

`editor` zeigt einen größeren, mehrzeiligen Textbereich anstelle eines einzelnen Feldes.
```sh
--textfield "Notes,editor"
```

![image](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

### Datums-Auswahlfeld

Verwenden Sie den Modifikator `date` oder `time`, um das Textfeld durch einen macOS-Datums-/Zeit-Auswahlfeld zu ersetzen. Der ausgewählte Wert wird als formatierter String zurückgegeben.

```sh
--textfield "Start Date,date"
--textfield "Start Time,time"
--textfield "Start Date and Time,date,time"
```

**Hinweis:** Der Modifikator `isdate` wurde zugunsten von `date` und `time` als veraltet markiert.

#### Datumsbereich

Verwenden Sie `mindate=` und `maxdate=`, um den auswählbaren Datumsbereich einzuschränken:

```sh
--textfield "Pick a day,date,mindate=20260901,maxdate=20260930"
--textfield "No earlier than today,date,mindate=20260928"
--textfield "Before end of year,date,maxdate=20261231"
```

**Format:** Die Datumsangaben müssen im Format `YYYYMMDD` vorliegen (regionsunabhängig). Trennzeichen werden akzeptiert und entfernt (z.B. `2026-09-30` → `20260930`). Ungültige Datumsangaben werden ignoriert, und die maximale Anzahl wird nicht angewendet.

#### Datumsformat

Verwenden Sie `format=`, um das Ausgabeformat mithilfe der strftime-Syntax anzugeben:

```sh
--textfield "Select date,date,format=+%Y-%m-%d"
--textfield "Get epoch,date,value=20260901,format=+%s"
```

Häufig verwendete Formatierungszeichenketten:
- `+%Y-%m-%d` - ISO 8601-Format (z. B. `2026-09-29`).
- `+%s` - Unix-Zeitstempel (Sekunden seit dem Epochenbeginn).
- `+%x` - Die Datendarstellung von Locale
- `+%D` - US-Format (z. B. `09/29/26`).

#### Initialisierung des Datums-Auswahlfelds

Verwenden Sie `value=`, um das Startdatum festzulegen. Der Datums-Auswahlmechanismus akzeptiert verschiedene Formate:

```sh
--textfield "Start date,date,value=2026-09-30"
--textfield "Start date,date,value=September 30, 2026"
--textfield "Start date,date,value=1759132800"
```

Unterstützte Formate: ISO 8601, länderspezifische Formate, 12/24-Stunden-Format, Zeitstempel seit der Epoche und natürliche Sprache.

### Datei auswählen

`fileselect` Fügt eine **Auswählen**-Schaltfläche hinzu, der einen Standard-Datei-Auswahl-Dialog öffnet. Der ausgewählte Pfad wird in das Feld eingefügt und in der Ausgabe zurückgegeben.

```sh
--textfield "Config File,fileselect"
```

Verwenden Sie `filetype`, um die Auswahlmöglichkeiten einzuschränken. Die Werte sind durch Leerzeichen getrennt und können Dateiendungen oder Typbezeichnungen sein:

| Wert | Auswahl |
|---|---|
| `folder` | Nur Verzeichnisse |
| `image` | Jeder Bildtyp |
| `movie` / `video` | Jeder Video-Typ |
| `audio` | Jeder Audio-Typ |
| `<extension>` | Dateien, die diese Erweiterung haben (z. B. `png`, `pdf`). |

```sh
--textfield "Select an image,fileselect,filetype=png jpg"
--textfield "Select a folder,fileselect,filetype=folder"
```

Verwenden Sie `path=<path>`, um das Verzeichnis festzulegen, in dem sich der Dateiauswahl-Dialog öffnet:

```sh
--textfield "Log File,fileselect,path=/var/log"
```

![image](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

### Bestätigen

`confirm` fügt ein zweites Feld unterhalb des ersten Felds hinzu. Beide Felder müssen den gleichen Wert enthalten, bevor swiftDialog die Eingabe akzeptiert. Dies ist nützlich für die Bestätigung von Passwörtern.

```sh
--textfield "Password,secure,required,confirm"
```

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### Kombination von Modifikatoren

Modifikatoren können frei miteinander kombiniert werden (sofern sie kompatibel sind).

```sh
--textfield "<label>,secure,required,prompt="<prompt_text>""
--textfield "<label>,required,regex="\d{5}",regexerror="Five digits required",prompt="00000""
--textfield "<label>,fileselect,filetype="jpeg jpg png",path=/Users/Shared"
```

### JSON-Format

Textfelder können auf zwei Arten als JSON definiert werden:

#### Gesamte Konfigurationsdatei im JSON-Format

Bei der Verwendung einer JSON-Konfigurationsdatei oder einer `--jsonstring`/`--jsonfile`-Datei sollten Textfelder als Array angegeben werden:

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "date" : true, "mindate" : "20260901", "maxdate" : "20260930", "format" : "+%Y-%m-%d"},
    {"title" : "<label>", "time" : true, "value" : "14:30"},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

#### JSON-Konfiguration pro Argument

Ab Version 3.1.1 können Textfelder auch als JSON-Objekte über `--textfield` definiert werden (anstatt durch kommagetrennte Modifikatoren). Dies bietet eine direktere Kontrolle und ist besonders nützlich für komplexe Konfigurationen.

**Syntax:**
```bash
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'
```

**Eigenschaften:**
- `title` - Der Text des Feldbezeichners
- `name` - Alternativer Name für den Ausgabeschlüssel
- `required` - Das Feld muss ausgefüllt werden (wahr/falsch).
- `secure` - Eingabe während der Eingabe verbergen (Passwortfeld).
- `passwordfill` - Passwort-Autovervollständigung für macOS aktivieren (erfordert `secure`).
- `prompt` - Platzhaltertext, der innerhalb des Feldes angezeigt wird
- `value` - Das Feld mit einem Standardwert vorbelegen
- `regex` - Es muss sichergestellt werden, dass der Inhalt eines Feldes mit einem regulären Ausdruck übereinstimmt
- `regexerror` - Eine benutzerdefinierte Fehlermeldung wird angezeigt, wenn der reguläre Ausdruck nicht erfüllt ist
- `editor` - Mehrzeiliger Texteditor anstelle eines einfachen Textfelds
- `date` - Feld durch eine Datums-Auswahlfunktion ersetzen (wahr).
- `time` - Feld durch eine Zeitwähler-Komponente ersetzen (wahr).
- `mindate` - Frühestes auswählbares Datum (im Format YYYYMMDD).
- `maxdate` - Maximal auswählbares Datum (im Format YYYYMMDD).
- `format` - Rückgabeformat unter Verwendung der strftime-Syntax (z. B. `+%Y-%m-%d`, `+%s`).
- `fileselect` - Füge eine "Auswählen"-Schaltfläche hinzu, die einen Dateiauswahldialog öffnet
- `filetype` - Beschränken Sie den Dateiauswahldialog auf bestimmte Dateitypen (durch Leerzeichen getrennte Erweiterungen oder Schlüsselwörter).
- `path` - Anfangsverzeichnis für den Dateiauswahl-Dialog
- `confirm` - Ein Bestätigungsfeld hinzufügen, das mit dem Hauptfeld übereinstimmen muss

**Beispiele:**

```bash
# Basic required field with prompt
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'

# Secure field with password fill
dialog --textfield '{"title":"Password","secure":true,"passwordfill":true,"prompt":"Enter password"}'

# Date picker with bounds
dialog --textfield '{"title":"Select Date","date":true,"mindate":"20260901","maxdate":"20260930","format":"+%Y-%m-%d"}'

# Time picker with default value
dialog --textfield '{"title":"Select Time","time":true,"value":"14:30"}'

# File picker with restrictions
dialog --textfield '{"title":"Select Config","fileselect":true,"filetype":"json plist","path":"/Library/Preferences"}'

# Multi-line editor
dialog --textfield '{"title":"Notes","editor":true}'

# Regex validation
dialog --textfield '{"title":"Product Code","prompt":"Enter 5 digit code","regex":"\\d{5}","regexerror":"Must be a five digit number"}'

# Confirmation field
dialog --textfield '{"title":"Password","secure":true,"required":true,"confirm":true}'
```

**Felder zur Datenauswahl:**
- Verwenden Sie `"date": true` oder `"time": true` (oder beide), um eine Auswahlmöglichkeit zu erstellen
- `"mindate"` und `"maxdate"` akzeptieren Datumsangaben im Format `YYYYMMDD` (Trennzeichen werden entfernt).
- `"format"` legt das Ausgabeformat mithilfe der strftime-Syntax fest
- `"value"` Legt das ursprüngliche Datum/die ursprüngliche Uhrzeit in verschiedenen Formaten fest (ISO, lokale Einstellungen, Epoche, natürliche Sprache).

**Alle Modifikatoren werden unterstützt:** Jeder Modifikator, der in CSV-Form verfügbar ist, kann auch als JSON-Schlüssel verwendet werden.

**Mehrere Textfelder:**

```bash
dialog --textfield '{"title":"First Name","required":true}' \
       --textfield '{"title":"Last Name","required":true}' \
       --textfield '{"title":"Email","regex":".+@.+\\..+","prompt":"user@example.com"}'
```

**Hinweis:** Bei der Verwendung von JSON-Daten pro Parameter ist jeder `--textfield` unabhängig. Die gesamte JSON-Konfigurationsform wird weiterhin für die Batch-Initialisierung unterstützt.

## Tastaturverhalten

Das Drücken der **Eingabetaste** (Return) in jedem Textfeld mit einer einzelnen Zeile löst die Aktion von Schaltfläche 1 aus, was dem Klicken auf die Standardschaltfläche entspricht. Dies gilt nicht für `editor` Felder.