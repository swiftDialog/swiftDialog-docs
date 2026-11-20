---
title: Bannerbilder
description: Anzeige von Bildern am oberen Rand von Dialogfenstern, optional mit Titeltext
translationSynced: 2026-11-20T10:42:25+00:00
---

Verwenden Sie die Befehlszeilenoption `-n` oder `--bannerimage`, um ein Bild anzugeben, das oben im Dialogfenster angezeigt werden soll.

Anwendung:

`--bannerimage <file | url | colour= >`

Die Verwendung eines Bannerbilds deaktiviert die Anzeige des Bereichs für das Symbolbild. Dies entspricht der Verwendung der `--hideicon`-Option

## Grundlegende Nutzung

Dialog akzeptiert Bilder in den Formaten PNG und JPG und zeigt das angegebene Bild im Bannerbereich an. Das Bannerbild ist maximal 150 Punkt hoch und erstreckt sich über die Breite des Dialogfensters. In Kombination mit der Option `-s` oder `--small` ist die Höhe des Bannerbildes auf 100 Punkt begrenzt

Jedes Bildformat kann verwendet werden. Der Anzeigebereich des Bildes passt sich der Größe des verwendeten Bannerbildes an, wobei die maximale Höhe bei 150 Punkten liegt.

<img width="727" alt="Banner Image Small" src="https://user-images.githubusercontent.com/3598965/112744135-fcb77c00-8fe8-11eb-8fac-437c86872eae.png">

Eine bestimmte Höhe kann mit der Option `--bannerheight` festgelegt werden. Dies überschreibt die Standardhöhe.

Zusätzlich kann eine reine Farbe mit dem Präfix `colour=` angegeben werden. Die Farbe kann entweder als Hexadezimalwert oder als Farbname definiert werden.

Beispiel:

`--bannerimage colour=red` oder `--bannerimage colour=#ff0000`

Standardmäßig wird eine dezente Farbverlaufsumwandlung von Weiß zu einer Farbe und dann zu Schwarz auf einfarbige Flächen angewendet. Fügen Sie `,nogradient` hinzu, um dies zu deaktivieren:

`--bannerimage colour=red,nogradient`

### Farbverlaufsbanner

Ein linearer Farbverlauf kann mit dem Präfix `gradient=` angegeben werden. Geben Sie zwei oder mehr Farben an, getrennt durch Kommas, und optional können Sie die Richtung mit `:angle=<degrees>` festlegen:

```sh
--bannerimage "gradient=red,blue"
--bannerimage "gradient=red,orange,yellow:angle=135"
```

Winkelkonventionen: `0` = von unten nach oben, `90` = von links nach rechts (Standard), `180` = von oben nach unten, `270` = von rechts nach links.

Wenn nur eine Farbe an `gradient=` übergeben wird, ist das Ergebnis identisch mit `colour=` (eine Überlagerung von Weiß zu Farbe zu Schwarz).

## Text im Bannerbereich

`--bannertitle`

Mit diesem Befehl können Sie optional Titeltext innerhalb des Banners anzeigen. Dadurch wird die Textfarbe standardmäßig auf Weiß gesetzt, was jedoch mit [Anpassungsmöglichkeiten für die Schriftart des Titels](/basic-use/customizing-title#customising-title-font-properties) geändert werden kann.

Sie können es als Option für `--title` verwenden, oder Sie können eine Zeichenkette übergeben, die als Titel angezeigt werden soll. Wenn sowohl `--title` als auch `--bannertitle` Zeichenketten als Argumente erhalten, hat `--bannertitle` Vorrang.

Alle `--titlefont` Modifikatoren gelten für den Text des Banner-Titels, einschließlich `shadow`, `colour`, `size`, `weight`, `alignment` und `offset`.

`--titlefont shadow=1` Fügt einen Schlagschatten unterhalb des Textes ein.

Wenn `--subtitle` ebenfalls aktiviert ist, wird der Untertitel unterhalb des Titels innerhalb des Bannerbereichs angezeigt und übernimmt dabei die gleiche Schriftart, jedoch in einer kleineren Größe.

![image](https://user-images.githubusercontent.com/3598965/216027666-5e4433d5-9e1e-4590-b34d-8d7943cbe5a5.png)