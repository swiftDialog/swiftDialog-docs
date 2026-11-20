---
title: Hintergrundbilder
description: Das Hinzufügen von Hintergrundbildern und Wasserzeichen zu Dialogfenstern
translationSynced: 2026-11-20T10:42:15+00:00
---

## Hintergrundbilder

Bilder können im Hintergrund angezeigt werden, als Teil des Hauptdialogfensters, wodurch ein Wasserzeichen oder ein anderes Bild hinter dem eigentlichen Dialoginhalt platziert werden kann.

![image](https://user-images.githubusercontent.com/3598965/171406081-8e9e5363-56fc-46f9-baa8-ff881a4a4af3.png)

Hintergründe können mit den folgenden Bedienelementen gesteuert werden:

### `--background`

```
-bg, --background <file | url | colour= >
```

Zeigt die ausgewählte Datei als Hintergrundbild an. Wenn das Bild größer ist als die Standardgröße des Dialogfensters (820x380) und keine Optionen für die Fenstergröße angegeben sind (insbesondere die Fensterhöhe), wird die Höhe des Dialogfensters angepasst, sodass das Bild die gesamte Fensterbreite ausfüllt, standardmäßig 820 Pixel oder, falls angegeben, mit dem Wert von `--width`

Alternativ kann eine einfarbige Füllung durch Verwendung des `colour=`-Präfixes angegeben werden. Die Farbe kann als Hexadezimalwert oder als benannter Farbname definiert werden.

z.B. `--background colour=red` oder `--background colour=#ff0000`

Standardmäßig wird eine dezente Farbverlaufüberlagerung auf einfarbige Flächen angewendet. Fügen Sie `,nogradient` hinzu, um dies zu deaktivieren:

`--background colour=red,nogradient`

Ein linearer Farbverlauf kann mit dem Präfix `gradient=` definiert werden. Geben Sie zwei oder mehr Farben an, getrennt durch Kommas, und optional können Sie die Richtung mit `:angle=<degrees>` festlegen:

```sh
--background "gradient=red,blue"
--background "gradient=red,orange,yellow:angle=135"
```

Winkelkonventionen: `0` = von unten nach oben, `90` = von links nach rechts (Standard), `180` = von oben nach unten, `270` = von rechts nach links.

Wenn nur eine Farbe an `gradient=` angelegt wird, ist das Ergebnis identisch mit dem von `colour=`.


### `--bgalpha`

```
-ba, --bgalpha <number>
```

Legt den Alphawert oder die Transparenz der Hintergrundebene fest. Dieser Wert kann jede Zahl zwischen `0` (vollständig transparent) und `1` (vollständig opak) sein. Der Standardwert ist `0.5`


### --bgposition

```
-bp, --bgposition [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]
```

Platziert das Hintergrundbild im Fenster. Funktioniert am besten, wenn die Bildabmessungen kleiner sind als die des Hauptdialogfensters, beispielsweise bei einem Firmenlogo. Die Standardposition ist `centre`


### --bgfill

```
-bf, --bgfill [fill | fit]
```

Gibt dem Dialog an, wie das Bild innerhalb des Fensterrahmens angezeigt werden soll

`fill` Ändert die Größe des Bildes, sodass es das gesamte Fenster ausfüllt. Das Bild wird gegebenenfalls beschnitten. `fit` Ändert die Größe des Bildes, um es an das Fenster anzupassen, schneidet es aber nicht zu. Dies kann dazu führen, dass nicht-transparente Bereiche am oberen und unteren Rand "schwarz" erscheinen (bei Verwendung einer PNG-Bildquelle).

Die Standardeinstellung ist `none`, wodurch das Bild in der tatsächlichen Bildauflösung angezeigt wird

## Bildschirmhintergrund - `--screenbackground`

```
--screenbackground <file | url>
```

Zeigt das angegebene Bild **im Vollbildmodus, hinter dem Dialogfenster** – im Gegensatz zu `--background`, das *innerhalb* des Dialogfensters angezeigt wird. Alle anderen Dialogfunktionen bleiben verfügbar, aber der Benutzer kann nicht mit anderen Anwendungen interagieren, bis swiftDialog geschlossen wird (ähnlich wie `--blurscreen`, jedoch mit einem Bild anstelle eines Unschärfeeffekts).

```sh
dialog --screenbackground /path/to/wallpaper.jpg
dialog --screenbackground https://example.com/background.png
```