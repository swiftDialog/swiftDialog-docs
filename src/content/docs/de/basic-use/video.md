---
title: Anzeigen von Videos.
description: Erfahren Sie, wie Sie Videos und Videoinhalte in swiftDialog anzeigen können, einschließlich der Unterstützung für YouTube und Vimeo.
---

## Anzeigen von Videos.

Videos können anstelle einer Nachricht angezeigt werden. Wenn angegeben, wird die Standardgröße des Dialogfensters auf 900x600 geändert, um ein Video im 16:9-Format darzustellen. Benutzerdefinierte Größen können mithilfe der Modifikatoren `--width` und `--height` festgelegt werden.

```
--video  <file> | <url>
  Display a video instead of a message.
  Videos will be resized to fit the available display area (depending on video resolution, some letterboxing may occur)

    --videocaption <text>
    Text that will appear underneath the displayed video.

    --autoplay
    Video will start playing automatically on launch without requiring the user to press play
```

Alle Videoformate, die von QuickTime unterstützt werden, sollten wiedergegeben werden können. Wenn eine URL verwendet wird, muss der vollständige Pfad zur Video-Ressource angegeben werden.

Beispiel: `--title "Video Demo" --video /Users/Shared/Videos/day4session3.mp4`

![image](https://user-images.githubusercontent.com/3598965/138063195-19011cc7-840f-4701-9209-8405ffabcbeb.png)

### YouTube- und Vimeo-Unterstützung (erfordert swiftDialog Version 2.0 oder höher).

Um ein YouTube- oder Vimeo-Video einzubetten, können Sie die Video-ID als Parameter an den `--video`-Befehl übergeben, wobei Sie das Präfix `youtubeid=` oder `vimeoid=` verwenden können.

Die ID lässt sich in der Regel in der URL auf YouTube oder Vimeo finden.

YouTube-Beispiel:

`dialog --video youtubeid=XXXXXXXXXX`

Vimeo-Beispiel:

`dialog --video vimeoid=XXXXXXXXXX`

_Hinweis: Bei IDs privater Vimeo-Videos müssen Sie möglicherweise auch die zusätzlichen Informationen in der Embed-URL erfassen. Diese werden als zusätzliche `h=YYYYYYYY` dargestellt – der vollständige Embed-Befehl für swiftDialog lautet daher `dialog --video "vimeoid=XXXXXXXXXX?h=YYYYYYYY"`. _


## Aktualisierung eines laufenden Dialogs mit neuen Inhalten aus dem Web oder Videos.

Senden Sie die folgenden Befehle, um einen Dialog mit neuen Web- oder Videoinhalten zu aktualisieren.

```bash
echo "webcontent: https://some.website.com" >> /var/tmp/dialog.log
echo "video: https://some.website.com/video.mov" >> /var/tmp/dialog.log
echo "video: /path/to/file.mov" >> /var/tmp/dialog.log
```

Es gibt jedoch einige Einschränkungen: Derzeit können Web- oder Videoinhalte nicht direkt aktualisiert werden. Um zu einer anderen Website zu wechseln, müssen Sie den aktuellen Inhalt löschen und dann den neuen Inhalt hochladen.

```bash
echo "webcontent: none" >> /var/tmp/dialog.log
echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log
```

Sie können diese Elemente jedoch miteinander verknüpfen, sodass auch diese Lösung `echo "webcontent: none" >> /var/tmp/dialog.log && echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log` funktioniert.