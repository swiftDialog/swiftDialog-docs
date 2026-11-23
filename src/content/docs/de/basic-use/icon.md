---
title: Anpassen des Icons
description: Erfahren Sie, wie Sie Icons, Bilder und Überlagerungen in swiftDialog einrichten und anpassen können.
translationSynced: 2026-11-23T08:35:52+00:00
---

##### Inhaltsverzeichnis
 - [Grundlegende Verwendung](#grundlegende-nutzung)
 - [Etwas fortgeschrittenere Anwendung](#etwas-fortgeschrittene-anwendung)
 - [Integrierte Icons](#integrierte-icons)
 - [Verwendung von SF Symbols](#die-verwendung-von-sf-symbols)
 - [Icon-Überlagerungen](#icon-überlagerungen)
 - [Icon-Größe](#icon-größe)
 - [Das Icon ausblenden](#das-icon-ausblenden)
 - [Einrichten von hellen oder dunklen Icons, je nachdem, ob sich die UI im Dunkelmodus oder Hellmodus befindet](#anpassung-der-icons-an-das-farbschema-der-benutzeroberfläche-entweder-dunkle-icons-bei-aktiviertem-dark-mode-oder-helle-icons-bei-aktiviertem-light-mode)

***


Verwenden Sie die Kommandozeilenoption `-i` oder `--icon`, um anzugeben, welches Icon oder Bild Sie im Bereich der Icon-Beschriftung anzeigen möchten.

### Anwendung:

`--icon <file | url | text= >`


## Grundlegende Nutzung

swiftDialog akzeptiert Bilder in den Formaten `png` und `jpg` und zeigt das angegebene Bild im Bereich für die Icon-Anzeige.

Die Bilder werden so skaliert, dass sie in den dafür vorgesehenen Anzeigebereich passen, der eine Breite von 170 Punkt und eine Höhe von 260 Punkt hat.

`png` wird bevorzugt, jedoch werden `jpg` die Bilder mit leicht abgerundeten Ecken dargestellt, um einen weicheren Eindruck zu erzielen.

<img src="https://user-images.githubusercontent.com/3598965/111853793-912e3880-8970-11eb-852f-3d5f7e5d2119.png" width=450>

## Etwas fortgeschrittene Anwendung
swiftDialog akzeptiert einen Pfad zu einer Anwendung und verwendet das Anwendungs-Icon als Bild.

e.g. `--icon /Applications/Safari.app`

<img src="https://user-images.githubusercontent.com/3598965/111853901-e36f5980-8970-11eb-80e2-c3fca298627d.png" width=450>

swiftDialog akzeptiert auch eine URL, die auf eine Bilddatei verweist.

e.g. `--icon "https://user-images.githubusercontent.com/3598965/111854068-84f6ab00-8971-11eb-935b-487f1a15b91f.png"`

<img src="https://user-images.githubusercontent.com/3598965/111854089-a5bf0080-8971-11eb-95fe-a720206bb10a.png" width=450>

## Transparenz der Icons einstellen

Verwenden Sie `--iconalpha`, um einen Transparenzwert festzulegen.

Der Wertebereich reicht von `0.0` (vollständig transparent) bis `1.0` (vollständig undurchsichtig).

## Alternatives Icon (Dunkelmodus)

Verwenden Sie `:dark=` und geben Sie ein alternatives Icon oder einen alternativen Pfad an, der verwendet werden soll, wenn der Benutzer den Dunkelmodus aktiviert hat.

e.g. `--icon /path/to/light.png:dark=/path/to/dark.png`

## Integrierte Icons

swiftDialog verfügt über mehrere integrierte Icons, die mit der Option `--icon` verwendet werden können.

`--icon info`

![Info-Icon](https://user-images.githubusercontent.com/3598965/111854259-5e853f80-8972-11eb-9476-e2c5ceed3da9.png)

`--icon caution`

![Warnsymbol](https://user-images.githubusercontent.com/3598965/111854239-46adbb80-8972-11eb-9708-e864a71e3e0a.png)

`--icon warning`

![Warnsymbol](https://user-images.githubusercontent.com/3598965/111854248-52997d80-8972-11eb-9f11-52a0b8a8d650.png)

`--icon computer`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/2ee4c788-bc9a-4328-ac1b-1537bf30dcb7">

## Mit `text=`

Sie können das Präfix `text=` auch verwenden, um Text im Bereich des Icons anzuzeigen. Dies ist nützlich, um ein einzelnes Zeichen oder ein Emoji darzustellen.

e.g. `--icon text=👍`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/931fa9f5-0f96-4b32-bf6e-cffa28c26e31">


## Die Verwendung von SF Symbols

swiftDialog kann auch beliebige Symbole aus der SF Symbol-Bibliothek anzeigen. https://developer.apple.com/sf-symbols/

### SF-Symbol-Syntax (im CSV-Format)

Bei der Angabe von SF-Symbolen für Icons oder Overlay-Icons stehen zusätzliche Parameter für Farbe und Strichstärke zur Verfügung.

  `"SF=sf.symbol.name,colour=<text><hex>,weight=<text>"`

  `color,colour=<text><hex>` Angegeben im Hexadezimalformat, z. B. #00A4C7. Akzeptiert auch alle Standard-Farben von Apple `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Wenn die Option ungültig ist, wird die Systemfarbe `primary` als Standard verwendet.

Besondere Farbe `"auto"`.

Bei einem mehrfarbigen SF-Symbol wird das Standard-Farbschema des Symbols angewendet. Wenn es jedoch mit einem einfarbigen SF-Symbol verwendet wird, wird standardmäßig Schwarz verwendet, und der dunkle Modus wird nicht berücksichtigt.

e.g. `dialog -s -i SF=airplane.circle.fill,colour=auto`

![image](https://user-images.githubusercontent.com/3598965/126090330-8dc612a9-40f9-99e2-caf41d07903e.png)

Farbverläufe können durch Hinzufügen des zusätzlichen Arguments `colour2` oder `color2` eingestellt werden, beispielsweise `SF=applelogo,colour=pink,colour2=purple`.

![image](https://user-images.githubusercontent.com/3598965/170815055-e943c2a4-e846-44d5-b323-bb8be1333438.png)

Mehrfarbige SF-Symbole können mit dem Argument `palette` eingefärbt werden, beispielsweise `SF=person.3.sequence.fill,palette=red,green,blue`.

![image](https://user-images.githubusercontent.com/3598965/171398294-0a74dcad-b5b2-4dd0-b5b2-4dd0-b320-c65d5d5e8d22.png)

Die Schriftstärke des SF-Symbols kann mit dem Argument `weight` festgelegt werden.

   `weight=<text>` kann einen der folgenden Werte annehmen:
    * dünn (Standardeinstellung)
    * Licht.
    * regelmäßig
    * mittelgroß
    * schwer
    * fettgedruckt

### Animierte SF-Symbole

Die Unterstützung für animierte SF-Symbole ist ab macOS 14 oder neuer verfügbar.

Beispielhafte Verwendung:

`--icon sf=rainbow,colour=auto,animation=variable`

Derzeit wird nur eingeschränkte Unterstützung für die folgenden Animationstypen angeboten:
 - "Variable":
 - "variable.umkehrbar"
 - "variabel.iterativ"
 - "variabel.iterativ.umkehrbar"
 - "variabel.kumulativ"
 - "Puls"
 - "pulse.bylayer"

### JSON-Icon-Objekte

Icons können auch als JSON-Objekte definiert werden, um eine präzisere Steuerung zu ermöglichen. Dies ist besonders nützlich für komplexe Icon-Konfigurationen mit mehreren Eigenschaften.

**Syntax:**
```bash
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'
```

**Unterstützte Schlüssel:**
- `sf` / `name` / `symbol` - Name des SF-Symbols.
- `path` / `icon` / `value` - Dateipfad zu einem Bild oder einer Anwendung.
- `weight` - Symbolstärke (dünn, leicht, normal, mittel, schwer, fett)
- `colour` / `color` - Primärfarbe (als Hex-Code oder als Name).
- `colour2` / `color2` - Sekundäre Farbe für Farbverläufe.
- `palette` - Farbpalette für mehrfarbige Symbole.
- `animation` - Animationstyp für animierte Symbole (macOS 14 oder neuer).
- `bgcolour` / `bgcolor` - Hintergrundfarbe für Overlay-Icons.
- `auto` - Spezieller Wert für automatische Farbauswahl.
- `light` / `dark` - Varianten für hellen/dunklen Modus (verschachteltes Icon-Objekt).

**Beispiele:**

```bash
# Basic symbol with colour and weight
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'

# Gradient
dialog --icon '{"sf":"applelogo","colour":"pink","colour2":"purple"}'

# Multicolor palette
dialog --icon '{"sf":"person.3.sequence.fill","palette":["red","green","blue"]}'

# Application icon
dialog --icon '{"path":"/Applications/Chess.app"}'

# Light/dark variants
dialog --icon '{"light":{"sf":"sun.max"},"dark":{"sf":"moon"}}'

# Animated symbol (macOS 14+)
dialog --icon '{"sf":"rainbow","colour":"auto","animation":"variable"}'

# Overlay icon with background
dialog --overlayicon '{"sf":"exclamationmark","colour":"yellow","bgcolour":"none"}'
```

Funktioniert in: `--icon`, `--overlayicon`, `--listitem` (Icon-Feld), `--checkbox` (Icon-Feld).

**Hinweis:** Wenn das Icon-Feld in `--listitem` oder `--checkbox` verwendet wird, akzeptiert es verschachtelte JSON-Objekte:

```bash
dialog --listitem '{"title":"Download","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}'
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}'
```



## Icon-Überlagerungen

Verwenden Sie die Kommandozeilenoption `-y` oder `--overlayicon `, um anzugeben, welches Icon oder Bild Sie als Überlagerung für das Haupt-Icon wünschen.

Die Overlays werden mit halber Auflösung angezeigt und in der unteren rechten Ecke des Hauptbereichs für Icon-Darstellungen platziert. Mit dieser Option können Sie Bilder kombinieren, um eine Anzeige zu erstellen.

Overlay-Icons verwenden die gleichen Bildtypen und Positionen wie der Parameter `--icon`, einschließlich der vordefinierten Optionen und der SF-Symbole.


Beispiel:

`--icon caution --overlayicon /Applications/Safari.app`

`-i caution -y /Applications/Safari.app`

![Warn-Icon mit Safari-Overlay-Icon](https://user-images.githubusercontent.com/3598965/111854381-16b2e800-8973-11eb-9cf9-c2b1d8d8b6b7.png)

Beispiel 2:

`--icon /Applications/Google\ Chrome.app --overlayicon warning`

`-i /Applications/Google\ Chrome.app -y warning`

![Chrome-Icon mit Warnhinweis-Overlay](https://user-images.githubusercontent.com/3598965/111888622-2e9d7100-8a32-11eb-9693-e53bb2f42692.png)

### Hintergrund überlagern bei Verwendung von SF-Symbolen

Bei der Verwendung von SF Symbols wird ein leicht transparentes, eckiges Element hinzugefügt, um das Symbol hervorzuheben und es von dem Haupt-Icon abzugrenzen. Dies ist notwendig, da viele Symbole Elemente enthalten, die sich nicht gut als Überlagerung eignen.

![image](https://user-images.githubusercontent.com/3598965/173157681-0dd05429-35db-4872-89a1-8a8e42bf44a4.png)

Das Erscheinungsbild des Hintergrunds kann mit einem `bgcolor=`-Modifikator angepasst werden und verwendet dieselbe Syntax, überall dort, wo `color` gesetzt werden kann. Sie können auch die spezielle Farbe `bgcolor=none` angeben, wenn der Overlay-Hintergrund nicht gewünscht wird.

![image](https://user-images.githubusercontent.com/3598965/173157715-46fda24b-2cfb-417b-835a-ed452888546d.png)

## Icon-Größe

`--iconsize <float>` Die Icon-Größe wird auf die angegebene Breite angepasst. Die Standardbreite ist `170`.

Beispiel 1:

`--icon caution --overlayicon /Applications/Safari.app --iconsize 300`

![image](https://user-images.githubusercontent.com/3598965/137573508-a2eb2dfc-cf46-4009-8783-66d8e2040724.png)


Beispiel 2:

`--icon /Applications/Firefox.app --iconsize 100 -s`

![image](https://user-images.githubusercontent.com/3598965/137573587-0e11823b-dc12-4756-ab4c-8442c4d5f050.png)

## Icon-Position

`--centreicon` oder `--centericon`

Ändert die Position des Icons, sodass es zentriert wird.

![image](https://user-images.githubusercontent.com/3598965/159693524-551b863d-33db-4af0-b971-a9a08161d525.png)

Kann auch während der Ausführung von swiftDialog über eine Konfigurationsdatei geändert werden.

`echo "icon: centre" >> /var/tmp/dialog.log`

## Das Icon ausblenden

Das Icon kann vollständig entfernt werden, indem einer der folgenden Befehle verwendet wird:

`--hideicon`

oder

`--icon none`

## Anpassung der Icons an das Farbschema der Benutzeroberfläche, entweder dunkle Icons bei aktiviertem Dark Mode oder helle Icons bei aktiviertem Light Mode

Mit Ausnahme einiger SF-Symbole bietet swiftDialog keine integrierte Funktionalität zum Umschalten zwischen Icons für den Dunkel- und Hellmodus.

Das Setzen des Icons kann basierend auf den UI-Einstellungen im aufrufenden Skript erfolgen:

**zsh / bash** (Vielen Dank an [mm2270](https://github.com/mm2270)).

```bash
#!/bin/zsh

icon_path_dark="/path/to/icondark.png"
icon_path_lite="/path/to/iconlite.png"

logged_in_user=$(/usr/sbin/scutil <<< "show State:/Users/ConsoleUser" | /usr/bin/awk '/Name :/ && ! /loginwindow/ {print $3}')

os_color_mode=$(/usr/bin/defaults read /Users/$logged_in_user/Library/Preferences/.GlobalPreferences.plist AppleInterfaceStyle)

if [ "$os_color_mode" = "Dark" ]; then
	icon_path=$icon_path_dark
else
	icon_path=$icon_path_lite
fi
```

oder in Python (dank [joncrain](https://github.com/joncrain)]).

```python
from Foundation import NSBundle

def is_dark_mode():
    appearanceBundle = NSBundle.bundleWithPath_(
        "/System/Library/PreferencePanes/Appearance.prefPane"
    )
    appearanceShared = appearanceBundle.classNamed_("AppearanceShared")
    app = appearanceShared.sharedAppearanceAccess()
    if app.theme() == 1:
        return False
    else:
        return True

if is_dark_mode():
    content["icon"] = "dark_icon.png"
else:
    content["icon"] = "light_icon.png"
```