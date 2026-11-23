---
title: Erfassung der Dialogausgabe
description: Methoden zur Erfassung von Benutzereingaben und zur Verarbeitung von Dialogergebnissen
translationSynced: 2026-11-23T08:35:52+00:00
---

Es gibt verschiedene Möglichkeiten, Informationen aus einem Dialog zu erhalten oder herauszufinden, welche Aktion ein Benutzer ausgeführt hat oder welche Daten eingegeben wurden.

## Rückgabecodes

Der einfachste Dialog hat immer mindestens eine Schaltfläche. Wird sie angeklickt, endet der Dialog mit dem Rückgabecode `0`.

Die optionalen Schaltflächen, die über `--button2`, `--infobutton` (oder Derivate davon) aktiviert werden, geben beim Anklicken den Rückgabecode `2` oder `3` zurück, je nachdem, welche Schaltfläche angeklickt wurde.

Die folgenden Rückgabecodes werden nach jeder Aktion gesendet. Diese können ignoriert oder in einem aufrufenden Skript für weitere Aktionen verwendet werden

| Aktion      | Optional | Tastenkombination | Rückgabecode |
| ----------- | -------- | ------ | ----------- |
| `button1`   | Nein       | Enter  | 0           |
| `button2`   | Ja      | Esc    | 2           |
| `infobutton` | Ja      |        | 3           |
| \<timer\>   | Ja      |        | 4           |
| Befehlsdatei `quit:` | Ja |    | 5           |
| `--quitkey` | Ja      | `cmd+q`  | 10          |
| Authentifizierung fehlgeschlagen | Ja  |        | 30          |
| Bildressource nicht gefunden | |    | 201         |
| Datei nicht gefunden |       |        | 202         |


Um den Rückgabecode zu verarbeiten, erfassen Sie das Ergebnis von `$?` in Bash oder über Ihre gewählte Skriptsprache.

Beispiel: Verarbeitung von Rückgabecodes in `zsh`:

```zsh
#!/bin/zsh
dialog ...<options_here>
case $? in
  0)
  echo "Pressed OK"
  # Button 1 processing here
  ;;
  2)
  echo "Pressed Cancel Button (button 2)"
  # Button 2 processing here
  ;;
  3)
  echo "Pressed Info Button (button 3)"
  # Button 3 processing here
  ;;
  4)
  echo "Timer Expired"
  # Timer ran out code here
  ;;
  5)
  echo "quit: command used"
  # post quit: command code here
  ;;
  10)
  echo "User quit with cmd+q"
  # User quit code here
  ;;
  30)
  echo "Key Authorisation Failed"
  # Key auth failure code here
  ;;
  201)
  echo "Image resource not found"
  ;;
  202)
  echo "Image for icon not found"
  ;;
  *)
  echo "Something else happened"
  ;;
esac
```


## Standardausgabe

Zusätzlich zu den Rückgabecodes wird die Ausgabe an `sdtout` gesendet, wenn ein oder mehrere `--textfield` oder `--selectvalues` angegeben werden. Die Standardausgabe ist nicht formatiert, außer dass Label und Ausgabe durch ein `:`-Zeichen getrennt werden.

Angesichts des folgenden Dialogs und der Benutzereingabe:

`dialog --textfield "text 1" --textfield "text 2" --selecttitle "make selection" --selectvalues "one,two,three,four"`

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/127793083-b07b4b46-8da6-46ee-a4ce-fcca84949a31.png">

Das Ergebnis würde wie folgt aussehen:

```
 SelectedOption : three
 SelectedIndex : 2
text 1 : one
text 2 : two
```

`SelectedOption` ist der Text der ausgewählten Option in der Auswahlliste. `SelectedIndex` ist der Index der ausgewählten Option (die Indizes beginnen bei 0, sodass Index 2 bedeutet, dass die dritte Option in der Liste ausgewählt wurde).

Textfelder werden mit dem im Dialogfenster übergebenen Label als Beschriftung angezeigt. Für das obige Beispiel gilt also:

`text 1` zeigt den Text an, den der Benutzer in das Textfeld mit der Bezeichnung "text 1" eingegeben hat, und das Gleiche gilt für `text 2`

Um diese Informationen aufzuteilen, könnten Sie `awk` verwenden, um jede Zeile der Ausgabe zu verarbeiten, an der Sie interessiert sind, z. B.
```bash
/usr/local/bin/dialog <...> | grep "SelectedOption" | awk -F " : " '{print $NF}'
```

Für eine komplexere Verarbeitung können Sie den Parameter `--json` übergeben, der dann die Ausgabe im JSON-Format bereitstellt, sodass sie mit einem JSON-Parser verarbeitet werden kann (z. B. in Python).

Die JSON-Ausgabe für das obige Beispiel würde wie folgt aussehen:
```json
{
"SelectedOption" : "three",
"SelectedIndex" : 2,
"text 1" : "one",
"text 2" : "two"
}
```

## Zusätzliche Beispiele

Die Ausgabe und den Rückgabecode mithilfe von Python erfassen:
```python
import subprocess

result = subprocess.Popen("/usr/local/bin/dialog <...>")
text = result.communicate()[0]   # contents of stdout
return_code = result.returncode  # return code
```