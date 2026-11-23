---
title: Elementlisten
description: Erstellen dynamischer, sortierter Listen mit Statusanzeigen und Icons
translationSynced: 2026-11-23T08:35:52+00:00
---

Listen können verwendet werden, um eine angemessene Anzahl von Elementen in einer geordneten Liste anzuzeigen. Wenn die Liste den sichtbaren Bereich überschreitet, wird sie scrollbar.

Listen können in Dialogen angezeigt werden, wobei alle bestehenden Anpassungsoptionen verfügbar sind, mit Ausnahme von Bildern, die den gesamten Anzeigebereich belegen.

<hr />
Es gibt drei Möglichkeiten, eine Elementliste zu erstellen:

### 1) Befehlszeile

Geben Sie einen oder mehrere `--listitem <text>` Einträge als Befehlszeilenargument an. Die Liste wird in der angegebenen Reihenfolge erstellt.

Icons für Listenelemente können über Befehlszeilenargumente eingestellt werden `--listitem "<text>,icon=<image>"`, jedoch müssen Sie für erweiterte Optionen JSON verwenden.

### 2) JSON

Wenn JSON als Konfigurationsquelle verwendet wird, geben Sie die Elemente als ein eindimensionales Array an.

#### Grundlegend

Die grundlegende Methode ist eine einfache Möglichkeit, eine Liste von Elementen zu erstellen, denen noch kein Status zugewiesen wurde.

```json
{
  "listitem" : ["Item 1", "Item 2", "Item 3"]
}
```

#### Fortgeschritten

"Erweitert" ermöglicht es Ihnen, eine Liste zu initialisieren und optional ein Icon, einen Status und einen Status-Text festzulegen

```json
{
  "listitem" : [
    {"title" : "Item One", "icon" : "/path/to/image", "status" : "pending", "statustext" : "Pending"},
    {"title" : "Item Two", "icon" : "/path/to/SomeApp.app", "status" : "wait", "statustext" : "Waiting"},
    {"title" : "Item Three", "icon" : "https://some.url/image", "status" : "success", "statustext" : "Winning"}
  ]
}
```

##### Statusoptionen

Der Status der Listenelemente kann einer der folgenden Werte sein: `wait`, `success`, `fail`, `error`, `pending` oder `progress`, und es wird ein entsprechendes Icon im Statusbereich angezeigt.

Wenn `progress` als Status verwendet wird, wird ein kreisförmiger Fortschrittsbalken als Status-Icon angezeigt. Durch Anhängen einer Zahl, z. B. `progress: 20`, wird der Fortschrittsbalken animiert, um die entsprechende Position anzuzeigen, die den zu füllenden Prozentsatz repräsentiert. Der Fortschrittsbalken akzeptiert beliebige Werte zwischen `0` und `100`

<img width="599" alt="image" src="https://user-images.githubusercontent.com/3598965/182604151-3eabe9b5-3f77-4949-9b88-c522676e3314.png">

#### JSON-Konfiguration pro Argument

Ab Version 3.1.1 können Listenelemente auch als JSON-Objekte über `--listitem` definiert werden (anstatt die gesamte Konfiguration als JSON zu verwenden). Dies ermöglicht eine direktere Steuerung und ist besonders nützlich für komplexe Konfigurationen mit verschachtelten Icon-Objekten.

**Syntax:**
```bash
dialog --listitem '{"title":"Download","status":"wait","statustext":"Working…"}'
```

**Eigenschaften:**
- `title` - Der Text der Beschriftung für den Listeneintrag
- `status` - Statusanzeige: `wait`, `success`, `fail`, `error`, `pending`, `progress` oder `progress:<value>` (0-100)
- `statustext` - Statusmeldung, die neben dem Statusanzeiger angezeigt wird
- `icon` - Pfad zum Icon, URL oder **verschachteltes JSON-Objekt für das Icon**

**Verschachtelte Icons:**

Das `icon`-Feld akzeptiert JSON-Objekte für Icons, um erweiterte Icon-Einstellungen vorzunehmen:

```bash
# Basic list item with SF Symbol
dialog --listitem '{"title":"Processing","status":"wait","icon":{"sf":"gear","colour":"blue"}}'

# List item with animated icon
dialog --listitem '{"title":"Downloading","status":"progress:50","icon":{"sf":"arrow.triangle.turn","colour":"green","animation":"variable"}}'

# List item with gradient icon
dialog --listitem '{"title":"Installing","status":"wait","icon":{"sf":"arrow.down.circle","colour":"pink","colour2":"purple"}}'

# List item with application icon
dialog --listitem '{"title":"App Installation","status":"success","icon":{"path":"/Applications/MyApp.app"}}'
```

**Mehrere Artikel:**

```bash
dialog --listitem '{"title":"Step 1","status":"success","statustext":"Complete"}' \
       --listitem '{"title":"Step 2","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}' \
       --listitem '{"title":"Step 3","status":"pending"}'
```

**Hinweis:** Bei der Verwendung von JSON-Dateien, die Parameter einzeln definieren, ist jeder `--listitem` unabhängig. Das Format mit einer einzigen JSON-Datei zur Konfiguration wird weiterhin für die Batch-Initialisierung unterstützt.


### 3) Als ein Befehl, der an die Befehlsdatei gesendet wird

Senden Sie die Elemente als kommagetrennte Werte

`echo "list: Item 1, Item 2, Item 3" >> /var/tmp/dialog.log`


## Aktualisierung einer bestehenden Liste

Einträge in einer bereits angezeigten Liste können durch das Senden von Befehlen an eine Befehlsdatei mit einem Status aktualisiert werden.


#### Grundlegend

Die erforderliche grundlegende Syntax ist:

`echo listitem: <list item title>: <status text> >> /var/tmp/dialog.log`

 - `<list item title>` muss mit dem Namen/der Überschrift des Listenelements übereinstimmen und ist Groß- und Kleinschreibungsempfindlich
 - `<status text>` kann jede beliebige Unicode-Textzeichenkette sein
   - Wenn einer der unterstützten Status-Schlüsselwörter gesendet wird, wird stattdessen ein passender Indikator angezeigt, anstatt eines Textes

#### Fortgeschritten

Die erweiterte Syntax ermöglicht es Ihnen, den Status-Text und den Status-Indikator zu aktualisieren sowie das Listenelement anhand seines Index zu referenzieren. Schlüsselwörter werden in einer durch Kommas getrennten Liste angegeben (was bedeutet, dass die Einträge `title` und `statustext` keinen Text enthalten dürfen, der ein Komma enthält).

`listitem: [title: <title>|index: <index>], status: <status>, statustext: <text>`

`<index>` beginnt bei 0

z. B.

`listitem: index: 0, status: complete, statustext: Item 1 on the list has completed`

Neue Elemente können mit dem Befehl `add:` am Ende einer bestehenden Liste hinzugefügt werden, und Elemente können mit dem Befehl `delete:` entfernt werden. Beim Hinzufügen einer Zeile sind "Status" und "Statustext" optional.

Beispiele:

`echo "listitem: add, title: <title>, statustext: <text>, status: <status>" >> /var/tmp/dialog.log`

Löschen nach Index: `echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log`

Löschen anhand des Titels. `echo "listitem: title: Some Row Title, delete:" >> /var/tmp/dialog.log`

Es ist möglich, Elemente zu einer Liste hinzuzufügen oder daraus zu entfernen, auch wenn die Liste im Moment nicht sichtbar ist.

## Anzeigen oder Ausblenden einer Liste

Die Liste kann ausgeblendet oder angezeigt werden, ohne dass sich der Inhalt der Liste ändert.

zeigen `echo "list: show`

verbergen `echo "list: hide`

## Eine Liste löschen

Eine bestehende Liste kann gelöscht werden, indem der Befehl `list: clear` an die Befehlsdatei gesendet wird.

Das Löschen einer Liste entfernt alle darin enthaltenen Einträge und zugehörigen Statusinformationen.

## Beispiele


`echo "list: Test item 1, Test item 2, Test item 3" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151488006-ba027af7-0736-47b2-abdd-ba847491f086.png)

Anschließend aktualisieren die folgenden Befehle den Status der Liste

`echo "listitem: Test item 1: Complete ✅" >> /var/tmp/dialog.log`

`echo "listitem: Test item 2: There was an error processing this item ❌" >> /var/tmp/dialog.log`

`echo "listitem: Test item 3: wait" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151486051-967e760e-f164-467f-8bd6-dcccba3c7504.png)

#### Erweitertes JSON-Format

![image](https://user-images.githubusercontent.com/3598965/163742836-22fd32e8-8010-467f-a518-b4d348619698.png)