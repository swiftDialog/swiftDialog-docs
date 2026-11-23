---
title: Vollbild
description: Erstellung von Vollbild-Dialogen für Präsentationen und Kiosk-Modi
translationSynced: 2026-11-23T08:35:52+00:00
---

Der Vollbildmodus wird durch die Kommandozeilenoptionen `--fullscreen` oder `-f` unterstützt.

In dieser Ansicht sind nur Banner, Titel, Icon und Nachricht sichtbar. Andere Optionen können zwar weiterhin festgelegt werden, werden aber nicht angezeigt. Das Dialogfenster reagiert jedoch weiterhin auf Tastatureingaben (Eingabetaste und Esc-Taste) und wird mit dem entsprechenden Exit-Code beendet.

Der Anzeigebereich wird sich an verschiedene Auflösungen anpassen, von 1024x640 bis zu 5k. (Spenden von XDR-Displays für Tests mit 6k-Auflösungen werden gerne angenommen.)

Die Optionen verhalten sich im Vollbildmodus leicht anders als im normalen Modus:

### `--bannerimage` `-n`

Bannerbilder werden zentriert am oberen Bildschirmrand angezeigt und nehmen dabei maximal 95 % der Bildschirmbreite und maximal 10 % der Bildschirmhöhe ein. Dies ermöglicht die Darstellung von länglichen, schmalen Bannerbildern, falls erforderlich.

Die Anzeige eines Bannermotivs erzeugt auch eine horizontale Linie darunter, die ebenfalls 95 % der Breite des Anzeigebereichs einnimmt.

### `--title` `-t`

Der Titel wird oben im Anzeigebereich oder direkt unter einem Banner platziert und erstreckt sich über die volle Breite des Anzeigebereichs.

### `--icon` `-i`

Icon-Bilder werden zentriert unterhalb des Titels angezeigt. Standardmäßige Bildquellen werden akzeptiert, jedoch unterstützt diese Anzeige keine Option für ein Overlay-Icon.

### `--message` `-m`

Der Nachrichtenbereich nimmt den verbleibenden Bildschirmbereich unterhalb der Überschrift, des Banners und der Icons ein. Er ist sowohl vertikal als auch horizontal zentriert und erstreckt sich über die gesamte Breite des Bildschirms.

Wenn Banner, Titel und Icon alle verwendet werden, nimmt der Nachrichtenbereich den unteren Bereich des Bildschirms zu 40-50 % ein (auf größeren Bildschirmen steht mehr Fläche zur Verfügung). Wenn Icon und Banner weggelassen werden, wird der untere Bereich des Bildschirms zu 60-75 % genutzt.

Jede Textzeile im Nachrichtenbereich wird mit doppeltem Zeilenabstand formatiert, wobei die maximale Anzahl der Zeilen 12 beträgt.

## Beispiele

Diese Beispiele zeigen, wie der Vollbildmodus auf einem Standard-13-Zoll-Display aussieht, wobei die Inhaltsbereiche hervorgehoben sind.

### Einfache Ansicht mit Titel und Nachricht

<img width="1000" alt="Screenshot1" src="https://user-images.githubusercontent.com/3598965/114690586-306d0280-9d5a-11eb-9504-1e2d25f93711.png">


### Alle Optionen mit Bannerbild und Icon

<img width="1000" alt="Screenshot2" src="https://user-images.githubusercontent.com/3598965/114690604-3531b680-9d5a-11eb-94c5-242693f6d335.png">