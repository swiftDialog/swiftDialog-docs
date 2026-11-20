---
title: Hilfenachrichten
description: Das Hinzufügen von Hilfenachrichten im Kontext von Dialogen
translationSynced: 2026-11-20T10:02:14+00:00
---

## Hilfenachrichten

Hilfenachrichten können eine Möglichkeit sein, zusätzliche Informationen bereitzustellen, wenn dies erforderlich ist, ohne dabei zusätzlichen Platz im Dialogfenster zu beanspruchen

`--helpmessage <text>`

`<text>` akzeptiert Markdown zur Formatierung von Nachrichten

Wenn verfügbar, erscheint eine zusätzliche Hilfe-Schaltfläche neben der Standard-Schaltfläche.


![image](https://user-images.githubusercontent.com/3598965/216032093-2aede3aa-4cda-402c-9cd7-fa4edb506cfc.png)

Ein Klick darauf öffnet eine Hilfenachricht in einem Popup-Fenster

![image](https://user-images.githubusercontent.com/3598965/216032203-35960f72-24f5-491e-8d75-b6b43e4a123c.png)

Die Höhe des angezeigten Bereichs passt sich automatisch an die Größe der Nachricht an.

### `--helpimage`

Fügen Sie ein Bild hinzu `--helpimage /path/to/image.png`.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/d4c4504f-2e6f-4e83-882f-be0e799c9ffc" />

Unterstützt Standardargumente für Icons, einschließlich QR-Codes:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/1c4c99bc-8548-4547-b16b-0dd02cc2c02d" />

### `--helpalignment`

`--helpalignment [left | centre | center | right]`

Legt die Textausrichtung des Inhalts der Hilfeseiten-Nachricht fest. Die Standardausrichtung entspricht der aktuell eingestellten Ausrichtung für Nachrichten.

### `--helpsheetbuttontext`

`--helpsheetbuttontext <text>`

Legt die Beschriftung für die Schaltfläche fest, die verwendet wird, um das Hilfefenster zu schließen. Der Standardwert ist `OK`.