---
title: Timer und Fortschrittsbalken
description: Das Erstellen von Dialogen mit Countdown-Timern und interaktiven Fortschrittsbalken
translationSynced: 2026-11-20T10:36:45+00:00
---

Ein Dialog kann gestartet werden, wobei ein Timer aktiv ist, der abläuft, sobald die angegebene Anzahl von Sekunden verstrichen ist

`--timer (<seconds>)`


Ersetzt die Standard-Schaltfläche durch einen Timer, der einen Countdown startet. Nach Ablauf des Timers schließt sich das Dialogfenster mit dem Exit-Code `4`. Der Standardwert für den Timer beträgt `10` Sekunden. Ein optionaler Wert `<seconds>` kann angegeben werden, um den gewünschten Wert festzulegen. Wenn `<seconds>` größer als 60 ist, wird der Countdown im Format `HH:MM:SS` angezeigt. Zum Beispiel wird 280 Sekunden anfänglich als `4:40` dargestellt.
Wenn es in Verbindung mit `--button1text` verwendet wird, wird die Standard-Schaltfläche angezeigt, ist aber für die ersten 3 Sekunden des Timers deaktiviert. Danach wird sie aktiviert und kann verwendet werden, um das Dialogfenster mit der Standard-Schaltfläche zu schließen, wobei der Exit-Code 0 ist

<img width="727" alt="image" src="https://user-images.githubusercontent.com/3598965/129475759-9ba50127-8366-46a3-8288-780298142f09.png">


`--hidetimerbar` blendet den Fortschrittsbalken und den Countdown aus.

Dadurch wird sichergestellt, dass die Standard-Schaltfläche sichtbar ist, um Dialogfenster zu vermeiden, die nicht geschlossen werden können und die keine Information darüber geben, wann der Timer abläuft.
---

## Fortschrittsbalken

Dialog kann einen interaktiven Fortschrittsbalken darstellen, der dynamisch über die [Befehlsdatei](/de/advanced/command-file) aktualisiert werden kann.

`--progress [<int>]`

Zeigt einen Fortschrittsbalken mit der angegebenen Anzahl von Schritten an. Wenn kein Wert angegeben wird, ist die Standardeinstellung 10 Schritte.

Um den Fortschrittsbalken zu aktualisieren, senden Sie einen Befehl an die Befehlsdatei des Dialogfensters:

```sh
echo "progress: <int>" >> /var/tmp/dialog.log
```

`--progresstext <text>`

Legt den anfänglichen Text fest, der unterhalb des Fortschrittsbalkens angezeigt wird. Dieser Text kann jederzeit aktualisiert werden:

```sh
echo "progresstext: Installing software..." >> /var/tmp/dialog.log
```

### Textausrichtung unterhalb des Fortschrittsbalkens

`--progresstextalignment [left | right]`

Legt die horizontale Ausrichtung des Fortschrittstexts fest, der unterhalb des Fortschrittsbalkens angezeigt wird. Der Standardwert ist zentriert.