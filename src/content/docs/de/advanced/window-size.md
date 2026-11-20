---
title: Fenstergröße und -verhalten
description: Steuerung der Positionierung, Größe und des visuellen Erscheinungsbilds von Dialogfenstern
translationSynced: 2026-11-20T10:42:50+00:00
---

Das Standardverhalten des Dialogfensters ist, sich in der Mitte des Bildschirms zu positionieren und nicht verschiebbar zu sein. Andere Fenster können darüber platziert werden. Dieses Verhalten kann mit den folgenden Befehlszeilenoptionen geändert werden.

Beide Optionen können unabhängig voneinander genutzt werden.

## Fensteransicht

`-p` oder `--ontop`

Verwenden Sie diese Option, um sicherzustellen, dass das Dialogfenster immer im Vordergrund bleibt.

## Fensterposition

`-o` oder `--moveable`

Verwenden Sie diese Option, um zu ermöglichen, dass das Fenster über den Bildschirm verschoben werden kann.

`--position [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]`

Platziert das Dialogfenster an der im System definierten Position auf dem Bildschirm

`--positionoffset <num>`

Legt den Randabstand für das Fenster fest (der Abstand zwischen den Bildschirmrändern und dem Fenster).

`--position <x>,<y>`

Positioniert das Dialogfenster an den angegebenen x- und y-Koordinaten, beispielsweise `--position 100,200`

**Hinweise:**
 - Die Position 0,0 befindet sich in der oberen linken Ecke des sichtbaren Bildschirmbereichs
 - Der sichtbare Bildschirmbereich schließt den Bereich aus, der von der Leiste oder der Menüleiste belegt wird. Wenn beispielsweise die Leiste auf der linken Seite des Bildschirms positioniert ist, wird der Ursprungspunkt entsprechend verschoben.


## Fenstergröße

Sie können die Größe anpassen, um sie größer oder kleiner als die Standardgröße zu machen, je nachdem, ob Sie mehr oder weniger Informationen in Ihrer Nachricht vermitteln möchten oder ob Sie unterschiedliche Größen auf Bildschirmen unterschiedlicher Größe anzeigen wollen. Bilder werden entsprechend skaliert. Die Schriftgröße bleibt dabei gleich.

`-b` oder `--big`

Dadurch wirkt das Fenster etwa 25 % größer als normal, was die sichtbare Fläche für die Icons vergrößert

![image](https://user-images.githubusercontent.com/3598965/184131775-9ec40570-8e70-47ba-aecd-5561f6b6f54d.png)

`-s` oder `--small`

Dadurch erscheint das Fenster etwa 25 % kleiner als üblich

![image](https://user-images.githubusercontent.com/3598965/184131853-94255fc7-b040-4b64-812b-bbe7e9bf412b.png)

## Fensteransicht

Sie können entweder den Dunkelmodus oder den Hellmodus erzwingen, und das System verwendet dann diese Einstellung, unabhängig von den aktuellen Präferenzen des Benutzers

`--appearance dark` oder `--appearance light`

## Mini-Modus

Der "Mini"-Modus wird durch Übergabe des entsprechenden Arguments aktiviert. `--mini`

Der Mini-Modus öffnet ein kleines Fenster mit einer angepassten Anordnung und begrenzten Optionen zur Anzeige von Inhalten. `--title` ist kleiner und wird oben mittig im Fenster angezeigt, oder kann mit `--title none` deaktiviert werden. `--message` kann bis zu vier Textzeilen enthalten (längere Texte werden abgeschnitten). `--icon` nimmt, wenn sichtbar, den linken Bereich des Fensters ein, und alle anderen Inhalte werden rechts davon angezeigt. `--hideicon` und `--icon none` werden berücksichtigt. `--button1text` und `--button2text` sind verfügbar, aber die Info-Schaltfläche nicht.

![image](https://user-images.githubusercontent.com/3598965/184130942-8e0461e3-744d-4e69-89bc-6754cbd92abf.png)

Wenn das Argument `--progress` verwendet wird, wird der Bereich für die Schaltflächen entfernt und durch einen Fortschrittsbalken sowie eine einzelne Zeile mit Fortschrittstext ersetzt. Um das Dialogfenster zu schließen, muss der Befehl `quit:` an die Befehlsdatei übergeben werden.

![image](https://user-images.githubusercontent.com/3598965/184131293-efe2e2a3-2a33-42cf-b397-941d053b2693.png)

## `--style` - Konfigurieren Sie einen vordefinierten Fensterstil

Ändert die Standardwerte, um die Anzeige eines Dialogfensters zu verändern.

Andere Stile als `--mini` haben keine besonderen Eigenschaften, und das visuelle Erscheinungsbild kann durch die Verwendung verschiedener Parameter zur Einstellung von Fenstereigenschaften erreicht werden.

`centered`, `alert` und `caution` verwenden den Wert aus `--title` und fügen ihn als Überschrift zum Nachrichtenbereich hinzu, deaktivieren dann aber die Überschrift. Dadurch wird die Überschrift unter dem angezeigten zentralen Symbol platziert.

    "mini" ist funktional äquivalent zu "--mini". "centered" legt alle Optionen für zentrierte Inhalte fest. "alert" öffnet ein vordefiniertes Dialogfenster mit den Maßen 300x300 und zentriertem Inhalt. "caution" und "warning" funktionieren wie "alert", verwenden aber ein entsprechendes Symbol

Beispiel: `dialog --style alert`

<img width="412" alt="image" src="https://github.com/bartreardon/swiftDialog/assets/3598965/53add8af-3407-4152-b374-486db664b8e9">

Dies entspricht dem Eingeben von:

```bash
dialog --title none --iconsize 80 --message "### An Important Message  \n\nThis contains important message content\n\nPlease read" --messagealignment centre --buttonstyle centre --centreicon --width 300 --height 300
```

## Maßgefertigte Fenstergrößen

Der Dialog kann jede beliebige Größe haben, anstatt der Standardoptionen `--small` oder `--big`.

`--width` und `--height` können verwendet werden, um die gewünschte Dialoggröße festzulegen. Der Inhalt wird automatisch angepasst, um in den verfügbaren Platz zu passen.

swiftDialog unterstützt die Verwendung von `%` als Funktion der aktuellen Bildschirmgröße, beispielsweise wird `--width 50%` die Breite des Dialogfensters auf 50 % der aktuellen Bildschirmauflösung setzen.

![image](https://user-images.githubusercontent.com/3598965/129476080-a708fe71-c566-4caf-8323-899e5dbdcc2b.png)

## `--blurscreen`

`--blurscreen` Blendet alle Bildschirme mit einem unscharfen Hintergrund ein und platziert das Dialogfenster oberhalb aller anderen Fenster. Dies ermöglicht entweder eine fokussiertere Darstellung oder Arbeitsabläufe, bei denen Sie nicht möchten, dass ein Benutzer mit anderen Anwendungen oder dem Desktop interagiert (z. B. während der Einführung).


<img src="https://user-images.githubusercontent.com/8291873/229149297-ab060e52-120a-42bc-8a4c-1150b7d80ca2.png" width="500">


### Verhalten von `--ontop` in Verbindung mit `--blurscreen` und bestehenden Dialogfenstern

Wenn ein bestehender Dialog mit `--blurscreen` aktiv ist, führt die Verwendung von `--ontop` dazu, dass nachfolgende Dialoge über der Hintergrundunschärfe (Blur-Ebene) angezeigt werden. Dies ermöglicht es, einen Hintergrunddialog auszuführen und zusätzliche Dialoge zu öffnen, die dann sichtbar sind. Es ist wichtig zu beachten, dass Sie, wenn Sie planen, mit diesen Dialogen programmatisch zu interagieren, sicherstellen sollten, dass Sie für jeden Dialog eindeutige Konfigurationsdateien verwenden.

## `--showonallscreens`

Wenn die Funktion verwendet wird, erscheint das Dialogfenster auf allen virtuellen Desktops

Wenn mehrere Bildschirme verwendet werden, erscheint das Dialogfenster auf allen virtuellen Desktops, die mit dem Bildschirm verbunden sind, auf dem es gestartet wurde.