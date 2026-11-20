---
title: Anzeigen von Bildern
description: Erfahren Sie, wie Sie Bilder, Bildunterschriften und Bilderslider in swiftDialog anzeigen können.
---

## Anzeigen von Bildern

Bilder können angezeigt werden und ersetzen standardmäßig den Nachrichtenbereich.

`--imagecaption` steht für eine kurze, einzeilige Beschreibung jedes Bildes. Wenn zusätzlich ein `--message` vorhanden ist, wird dieser unterhalb der Bilder und Bildunterschriften angezeigt.

```
-g, --image  <file> | <url>
  Display an image instead of a message.
  Images will be resized to fit the available display area

    --imagecaption <text>
    Text that will appear underneath the displayed image.
```

Jedes unterstützte Bildformat kann entweder als `<file>` oder `<url>` übergeben werden.

Beispiel:

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/129476046-5b0cdef0-346b-4af6-a0eb-e8e72c72715d.png">

### Bilder im Base64-Format

Wo immer ein Bild verwendet werden kann, können sie jetzt im Base64-Format mit dem Präfix `base64=` angegeben werden, z. B. `--icon base64=<base64_text>`.

### Mehrere Bilder

Wenn mehr als ein `--image` angegeben wird, werden die Bilder in einer Karussell-Ansicht mit Pfeilen zur Navigation (weiter/zurück) angezeigt, wobei auch angegeben wird, welches Bild der Sequenz gerade dargestellt wird.

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/148642555-96247bff-8d95-414d-bf96-1fe28e27ed9c.png">

Zusätzlich zur statischen Anzeige der Bilder können Sie `--autoplay <sec>` verwenden, um das nächste Bild nach einer bestimmten Anzahl von Sekunden anzuzeigen (Standardwert ist 10 Sekunden). Ein Fortschrittsbalken wird unterhalb der Bildanzeige angezeigt, um anzuzeigen, wann die nächste Übergang erfolgen wird. Nachdem das letzte Bild angezeigt wurde, wird die Anzeige zurückgesetzt und von dem ersten Bild aus gestartet.

Verwenden Sie `--hidetimer`, um den Countdown-Anzeiger auszublenden, der während der automatischen Übergänge angezeigt wird.