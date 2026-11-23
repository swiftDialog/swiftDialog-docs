---
title: Personnalisation de l'icône
description: Apprenez comment configurer et personnaliser les icônes, les images et les superpositions dans swiftDialog
translationSynced: 2026-11-23T02:44:34+00:00
---

##### Table des matières
 - [Utilisation de base](#utilisation-de-base)
 - [Utilisation légèrement plus avancée ](#utilisation-légèrement-plus-avancée)
 - [Icônes intégrées](#icônes-intégrées)
 - [Utilisation des symboles SF](#utilisation-des-symboles-sf)
 - [Superpositions d'icônes](#superpositions-dicônes)
 - [Taille de l'icône](#taille-de-l-icône)
 - [Masquer l'icône](#masquer-licône)
 - [Définir les icônes en mode sombre ou en mode clair en fonction de si l'interface utilisateur est en mode sombre ou en mode clair](#définir-les-icônes-en-mode-sombre-ou-en-mode-clair-en-fonction-de-si-linterface-utilisateur-est-en-mode-sombre-ou-en-mode-clair)

***


Utilisez l'option de ligne de commande `-i` ou `--icon` pour spécifier quelle icône ou image vous souhaitez afficher dans la zone du titre de l'icône.

### Utilisation :

`--icon <file | url | text= >`


## Utilisation de base

swiftDialog accepte les images aux formats `png` et `jpg` et affiche l'image spécifiée dans la zone d'affichage des icônes.

Les images seront redimensionnées pour s'adapter à la zone d'affichage, qui mesure 170 points de largeur par 260 points de hauteur.

`png` est préférable, mais si `jpg` est spécifié, les images seront présentées avec des coins légèrement arrondis pour un rendu moins agressif.

<img src="https://user-images.githubusercontent.com/3598965/111853793-912e3880-8970-11eb-852f-3d5f7e5d2119.png" width=450>

## Utilisation légèrement plus avancée
swiftDialog acceptera le chemin d'accès à une application et utilisera l'icône de cette application comme image.

e.g. `--icon /Applications/Safari.app`

<img src="https://user-images.githubusercontent.com/3598965/111853901-e36f5980-8970-11eb-80e2-c3fca298627d.png" width=450>

swiftDialog acceptera également une URL pointant vers une ressource image.

e.g. `--icon "https://user-images.githubusercontent.com/3598965/111854068-84f6ab00-8971-11eb-935b-487f1a15b91f.png"`

<img src="https://user-images.githubusercontent.com/3598965/111854089-a5bf0080-8971-11eb-95fe-a720206bb10a.png" width=450>

## Définir la transparence de l'icône

Utilisez `--iconalpha` pour définir une valeur de transparence.

La plage de valeurs s'étend de `0.0` (totalement transparent) à `1.0` (totalement opaque).

## Icône alternative (mode sombre)

Utilisez `:dark=` et spécifiez une icône alternative ou un chemin d'accès à utiliser si l'apparence de l'utilisateur est configurée en mode sombre

e.g. `--icon /path/to/light.png:dark=/path/to/dark.png`

## Icônes intégrées

swiftDialog possède plusieurs icônes intégrées qui peuvent être utilisées avec l'option `--icon`

`--icon info`

![Icône d'information](https://user-images.githubusercontent.com/3598965/111854259-5e853f80-8972-11eb-9476-e2c5ceed3da9.png)

`--icon caution`

![Icône d'attention](https://user-images.githubusercontent.com/3598965/111854239-46adbb80-8972-11eb-9708-e864a71e3e0a.png)

`--icon warning`

![Icône d'avertissement](https://user-images.githubusercontent.com/3598965/111854248-52997d80-8972-11eb-9f11-52a0b8a8d650.png)

`--icon computer`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/2ee4c788-bc9a-4328-ac1b-1537bf30dcb7">

## Utilisation de `text=`

Vous pouvez également utiliser le préfixe `text=` pour afficher du texte dans la zone de l'icône. Ceci est utile pour afficher un seul caractère ou un emoji.

e.g. `--icon text=👍`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/931fa9f5-0f96-4b32-bf6e-cffa28c26e31">


## Utilisation des symboles SF

swiftDialog peut également afficher n'importe quelle icône de la bibliothèque SF Symbols. https://developer.apple.com/sf-symbols/

### Syntaxe des symboles SF (format CSV).

Lors de la spécification des symboles SF pour une icône ou une icône de superposition, des paramètres supplémentaires pour la couleur et l'épaisseur sont disponibles.

  `"SF=sf.symbol.name,colour=<text><hex>,weight=<text>"`

  `color,colour=<text><hex>` Spécifié au format hexadécimal, par exemple : #00A4C7. Accepte également toutes les couleurs standard d'Apple, `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Si l'option est invalide, la couleur par défaut est la couleur système `primary`

Couleur spéciale `"auto"`.

Lorsqu'il est utilisé avec un symbole SF multicolore, le schéma de couleurs par défaut du symbole sera appliqué. S'il est utilisé avec un symbole SF monochrome, il affichera par défaut la couleur noire et ne prendra pas en compte le mode sombre.

e.g. `dialog -s -i SF=airplane.circle.fill,colour=auto`

![image](https://user-images.githubusercontent.com/3598965/126090330-8dc612a9-40f9-99e2-caf41d07903e.png)

Les dégradés de couleurs peuvent être définis en ajoutant l'argument supplémentaire `colour2` ou `color2`, par exemple : `SF=applelogo,colour=pink,colour2=purple`

![image](https://user-images.githubusercontent.com/3598965/170815055-e943c2a4-e846-44d5-b323-bb8be1333438.png)

Les symboles SF multicolores peuvent être colorés en utilisant l'argument `palette`, par exemple : `SF=person.3.sequence.fill,palette=red,green,blue`

![image](https://user-images.githubusercontent.com/3598965/171398294-0a74dcad-b5b2-4dd0-b5b2-4dd0-b320-c65d5d5e8d22.png)

La taille des symboles SF peut être définie à l'aide de l'argument `weight`

   `weight=<text>` peut prendre l'une des valeurs suivantes :
    * thin (par défaut)
    * light
    * regular
    * medium
    * heavy
    * bold

### Symboles SF animés

La prise en charge des symboles SF animés est disponible sur macOS 14 et versions ultérieures.

Exemple d'utilisation :

`--icon sf=rainbow,colour=auto,animation=variable`

Le support pour les types d'animation suivants est limité pour le moment :
 - "variable" :
 - "variable.reversing"
 - "variable.iterative"
 - "variable.iterative.reversing"
 - "variable.cumulative"
 - "pulse"
 - "pulse.bylayer"

### Objets iconiques au format JSON

Les icônes peuvent également être spécifiées sous forme d'objets JSON pour un contrôle plus précis. Cela est particulièrement utile pour les configurations d'icônes complexes qui comportent plusieurs propriétés.

**Syntaxe :**
```bash
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'
```

**Touches prises en charge :**
- `sf` / `name` / `symbol` - Nom du symbole SF
- `path` / `icon` / `value` - Chemin d'accès au fichier image ou à l'application
- `weight` - Épaisseur du symbole (thin, light, regular, medium, heavy, bold).
- `colour` / `color` - Couleur primaire (code hexadécimal ou nom).
- `colour2` / `color2` - Couleur secondaire pour les dégradés
- `palette` - Palette de couleurs pour les symboles multicolores
- `animation` - Type d'animation pour les symboles animés (macOS 14 et versions ultérieures).
- `bgcolour` / `bgcolor` - Couleur de fond pour les icônes superposées
- `auto` - Valeur spéciale pour le schéma de couleurs automatique
- `light` / `dark` - Versions claires/sombre (objet d'icône imbriqué).

**Exemples :**

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

Fonctionne dans : `--icon`, `--overlayicon`, `--listitem` (champ d'icône), `--checkbox` (champ d'icône)

**Note :** Lorsqu'il est utilisé dans `--listitem` ou `--checkbox`, le champ "icône" accepte des objets JSON imbriqués.

```bash
dialog --listitem '{"title":"Download","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}'
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}'
```



## Superpositions d'icônes

Utilisez l'option de ligne de commande `-y` ou `--overlayicon ` pour spécifier quelle icône ou image vous souhaitez utiliser comme superposition à l'icône principale.

Les superpositions sont affichées avec une résolution réduite de moitié et sont positionnées en bas à droite de la zone principale d'affichage des icônes. En utilisant cette option, vous pouvez combiner des images pour créer une visualisation

Les icônes superposées utilisent les mêmes types d'images et les mêmes emplacements que le paramètre `--icon`, y compris les éléments intégrés et les symboles SF


Exemple :

`--icon caution --overlayicon /Applications/Safari.app`

`-i caution -y /Applications/Safari.app`

![icône d'avertissement avec superposition de l'icône Safari](https://user-images.githubusercontent.com/3598965/111854381-16b2e800-8973-11eb-9cf9-c2b1d8d8b6b7.png)

Exemple 2 :

`--icon /Applications/Google\ Chrome.app --overlayicon warning`

`-i /Applications/Google\ Chrome.app -y warning`

![Icône Chrome avec une superposition d'avertissement](https://user-images.githubusercontent.com/3598965/111888622-2e9d7100-8a32-11eb-9693-e53bb2f42692.png)

### Superposer un arrière-plan lors de l'utilisation des symboles SF

Lors de l'utilisation des symboles SF, un cercle légèrement transparent est ajouté pour faire ressortir le symbole par rapport à l'icône principale, car de nombreux symboles contiennent des éléments qui ne fonctionnent pas bien en superposition.

![image](https://user-images.githubusercontent.com/3598965/173157681-0dd05429-35db-4872-89a1-8a8e42bf44a4.png)

L'apparence de l'arrière-plan peut être ajustée à l'aide d'un modificateur `bgcolor=`, et la même syntaxe est utilisée partout où `color` peut être défini. Vous pouvez également spécifier une couleur spéciale `bgcolor=none` si vous ne souhaitez pas utiliser l'arrière-plan par défaut.

![image](https://user-images.githubusercontent.com/3598965/173157715-46fda24b-2cfb-417b-835a-ed452888546d.png)

## Taille de l'icône

`--iconsize <float>` Redimensionnera l'icône à la largeur spécifiée. La largeur par défaut est `170`

Exemple 1 :

`--icon caution --overlayicon /Applications/Safari.app --iconsize 300`

![image](https://user-images.githubusercontent.com/3598965/137573508-a2eb2dfc-cf46-4009-8783-66d8e2040724.png)


Exemple 2 :

`--icon /Applications/Firefox.app --iconsize 100 -s`

![image](https://user-images.githubusercontent.com/3598965/137573587-0e11823b-dc12-4756-ab4c-8442c4d5f050.png)

## Position de l'icône

`--centreicon` ou `--centericon`

Modifie la position de l'icône pour la centrer

![image](https://user-images.githubusercontent.com/3598965/159693524-551b863d-33db-4af0-b971-a9a08161d525.png)

Il est également possible de modifier ces paramètres à l'aide d'un fichier de commandes pendant l'exécution de swiftDialog

`echo "icon: centre" >> /var/tmp/dialog.log`

## Masquer l'icône

L'icône peut être supprimée complètement en utilisant l'une des commandes suivantes :

`--hideicon`

ou

`--icon none`

## Définir les icônes en mode sombre ou en mode clair en fonction de si l'interface utilisateur est en mode sombre ou en mode clair

À l'exception de certains symboles SF, swiftDialog ne dispose d'aucune fonctionnalité intégrée pour basculer entre les icônes du mode sombre et du mode clair.

L'icône de configuration peut être définie en fonction des paramètres de l'interface utilisateur, bien que cela puisse être réalisé dans le script appelant.

**zsh / bash** (merci à [mm2270](https://github.com/mm2270)).

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

ou en Python (merci à [joncrain](https://github.com/joncrain)).

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