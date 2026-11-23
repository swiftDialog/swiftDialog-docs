---
title: Options de ligne de commande
description: Référence complète de toutes les options et arguments de ligne de commande de swiftDialog
translationSynced: 2026-11-23T03:56:57+00:00
---

swiftDialog peut être configuré via des options de ligne de commande. Toutes les options peuvent également être spécifiées à l'aide d'un [fichier de configuration JSON](/fr/advanced/json-configuration).

```sh
dialog --title "Hello" --message "World"
```

Utilisez `--help <option>` pour obtenir des informations détaillées sur un argument spécifique.

---

## Contenu

| Argument | Court | Description |
|---|---|---|
| `--title <text>` | `-t` | Définissez le titre de la boîte de dialogue. Utilisez `none` pour la masquer. |
| `--subtitle <text>` | | Une ligne de texte secondaire est affichée sous le titre. Elle est également utilisée comme texte de sous-titre pour les [notifications](/fr/advanced/notifications). |
| `--message <text>` | `-m` | Définissez le message de dialogue. Prend en charge [Markdown](/fr/basic-use/markdown). |
| `--messagealignment [left\|centre\|right]` | | Alignement horizontal du message |
| `--messageposition [top\|centre\|bottom]` | | Position verticale du bloc de contenu du message |
| `--titlefont <params\|json>` | | Modifiez la police du titre. Accepte des paires séparées par des virgules ou un objet JSON : `key=value`, `colour`, `size`, `weight`, `name`, `alignment`, `offset`, `shadow` |
| `--messagefont <params\|json>` | | Modifier la police de caractères du message. Accepte des paires de valeurs séparées par des virgules `key=value` ou un objet JSON |

Consultez [Titre](/fr/basic-use/title) et [Message](/fr/basic-use/message) pour plus de détails.

---

## Icône

| Argument | Court | Description |
|---|---|---|
| `--icon <file\|url\|json>` | `-i` | Définissez l'icône de dialogue. Accepte un chemin de fichier, une URL, un symbole SF (`SF=name`), des éléments intégrés ou un objet JSON |
| `--iconsize <num>` | | Taille de l'icône en points (par défaut : 150). |
| `--iconalpha <num>` | | Opacité des icônes, de 0,0 (transparent) à 1,0 (opaque). |
| `--iconalttext <text>` | | Étiquette d'accessibilité pour l'icône |
| `--overlayicon <file\|url\|json>` | `-y` | Image superposée affichée en bas à droite de l'icône. Elle accepte les mêmes formats que `--icon` |
| `--hideicon` | `-h` | Masquer l'icône pour agrandir la zone de message |
| `--centreicon` / `--centericon` | | Déplacer l'icône pour la centrer entre le titre et le message |

Consultez [l'icône](/fr/basic-use/icon) pour plus de détails.

---

## Bannière et arrière-plan

| Argument | Court | Description |
|---|---|---|
| `--bannerimage <file\|url>` | `-n` | Affichez une image de bannière en haut de la fenêtre de dialogue |
| `--bannertitle <text>` | | Afficher le texte du titre superposé à la bannière |
| `--bannertext <text>` | | Équivalent à la définition de `--bannertitle` et `--title` |
| `--bannerheight <num>` | | Définir la hauteur de la bannière |
| `--background <file>` | `-bg` | Définir une image de fond/un filigrane |
| `--bgalpha <num>` | `-ba` | Opacité de l'image de fond (par défaut : 0.5). |
| `--bgposition <position>` | `-bp` | Position de l'image de fond (par exemple, `center`, `topleft`). |
| `--bgfill [fill\|fit]` | `-bf` | Mode de remplissage de l'image de fond |
| `--bgscale [fill\|fit]` | `-bs` | Mode d'échelle de l'image de fond |
| `--screenbackground <file\|url>` | | Afficher une image en plein écran, derrière la fenêtre de dialogue |

Consultez les [images de bannière](/fr/advanced/banner-images) et les [images de fond](/fr/advanced/background-images) pour plus de détails.

---

## Boutons

| Argument | Court | Description |
|---|---|---|
| `--button1text <text>` | | Étiquette pour le bouton 1 (lié à la touche `Return` ↵, valeur par défaut : `OK`). |
| `--button1action <url>` | | URL à ouvrir lorsque le bouton 1 est cliqué |
| `--button1shellaction <cmd>` | | Commande shell à exécuter lorsque le bouton 1 est cliqué |
| `--button1symbol <sf symbol\|json>` | | Symbole SF ou objet JSON pour le bouton 1 |
| `--button1disabled` | | Démarrage avec le bouton 1 désactivé |
| `--button2` | `-2` | Afficher le bouton 2 |
| `--button2text <text>` | | Étiquette pour le bouton 2 (lié à la touche `Esc` ⎋, valeur par défaut : `Cancel`). |
| `--button2symbol <sf symbol\|json>` | | Symbole SF ou objet JSON pour le bouton 2 |
| `--button2disabled` | | Démarrer en désactivant le bouton 2 |
| `--infobutton` | `-3` | Afficher le bouton d'informations |
| `--infobuttontext <text>` | | Étiquette pour le bouton d'information |
| `--infobuttonaction <url>` | | URL à ouvrir lorsque le bouton d'information est cliqué |
| `--infobuttonsymbol <sf symbol\|json>` | | Symbole SF ou objet JSON pour le bouton d'information |
| `--buttonstyle [center\|stack]` | | Style de disposition des boutons |
| `--buttonsize [mini\|small\|regular\|large]` | | Taille du bouton |
| `--buttontextsize <num>` | | Taille de la police des étiquettes de boutons |
| `--quitoninfo` | | Quitter la boîte de dialogue lorsque le bouton d'information est sélectionné |

Voir [Boutons](/fr/basic-use/buttons) pour plus de détails.

---

## Flux de travail

| Argument | Court | Description |
|---|---|---|
| `--nextbuttontext <text>` | | Étiquette du bouton "Suivant" dans le flux de travail (par défaut : `Next`). |
| `--previousbuttontext <text>` | | Étiquette pour le bouton "Précédent" du flux de travail (par défaut : `Previous`). |
| `--onadvance <command>` | | Commande shell à exécuter lors de la transition entre les pages du flux de travail <br> (les entrées sont fournies via l'entrée standard ; un code de sortie non nul bloque la progression). |

Consultez [le flux de travail](/fr/advanced/workflows) pour plus de détails.

---

## Message d'aide

| Argument | Court | Description |
|---|---|---|
| `--helpmessage <text>` | | Afficher un bouton d'aide avec un contenu contextuel affiché au survol. Prend en charge le format Markdown. |
| `--helpimage <file\|url>` | | Ajouter une image à la fenêtre d'aide contextuelle |
| `--helpsheetbuttontext <text>` | | Étiquette du bouton de fermeture de la feuille d'aide (par défaut : `OK`). |
| `--helpalignment [left\|centre\|right]` | | Alignement du contenu des messages d'aide |

Consultez [le message d'aide](/fr/operation/help-message) pour plus de détails.

---

## Images, vidéos et contenus web

| Argument | Court | Description |
|---|---|---|
| `--image <file\|url>` | `-g` | Afficher une image. Plusieurs instances créent une galerie de diapositives. |
| `--imagecaption <text>` | | Légende affichée sous l'image |
| `--video <file\|url>` | | Afficher une vidéo. Prend en charge les raccourcis `youtube=<id>` et `vimeo=<id>`. |
| `--videocaption <text>` | | Légende affichée sous la vidéo |
| `--autoplay` | | Lecture automatique de la vidéo au démarrage |
| `--webcontent <url>` | | Afficher une page web dans la zone de message |

Consultez les [Images](/fr/basic-use/images), la [Vidéo](/fr/basic-use/video) et le [Contenu Web](/fr/basic-use/web-content) pour plus de détails.

---

## Zone d'informations

| Argument | Court | Description |
|---|---|---|
| `--infotext <text>` | | Remplacez le bouton d'information par un texte statique |
| `--infobox <text>` | | Afficher le texte (format Markdown pris en charge) sous l'icône |
| `--infoboxwidth <num>` | | Définissez la largeur de la zone d'informations indépendamment de la taille de l'icône |

Consultez [la boîte d'informations](/fr/advanced/info-box) pour plus de détails.

---

## Saisie utilisateur

| Argument | Court | Description |
|---|---|---|
| `--textfield <text\|json>[,options]` | | Ajouter un champ de saisie de texte. Prend en charge `required`, `secure`, `prompt`, `regex`, `fileselect`, `date`, `time`, `mindate`, `maxdate` et d'autres formats. Peut également être spécifié sous forme d'objet JSON |
| `--textfieldlivevalidation` | | Afficher une validation en temps réel des expressions régulières directement dans les champs de texte |
| `--checkbox <text\|json>` | | Ajouter une case à cocher avec le libellé spécifié. Cela peut également être spécifié sous forme d'objet JSON |
| `--checkboxstyle [checkbox\|switch][,size]` | | Modifier l'apparence de la case à cocher |
| `--selecttitle <text>[,options]` | | Ajoutez une liste déroulante avec le nom spécifié |
| `--selectvalues <csv>` | | Valeurs séparées par des virgules pour la liste de sélection |
| `--selectdefault <text>` | | Valeur par défaut sélectionnée pour la liste déroulante |
| `--selectstyle` | | Style pour la liste déroulante |
| `--selectitem <json>` | | Définir un élément de liste sélectionnable en utilisant la syntaxe d'objet JSON |

Consultez [Champs de texte](/fr/advanced/textfields), [Cases à cocher](/fr/advanced/checkboxes) et [Listes de sélection](/fr/advanced/select-lists) pour plus de détails.

### Configuration JSON par argument

De nombreux arguments qui acceptent des valeurs séparées par des virgules peuvent également être spécifiés sous forme d'objets JSON. Cela offre un contrôle plus direct et est particulièrement utile pour les configurations complexes.

**Détection :** Si une valeur peut être interprétée comme un objet JSON, le constructeur JSON est utilisé ; sinon, l'analyse CSV est appliquée.

**Arguments pris en charge :**
- `--textfield` - Configuration complète du champ, avec tous les modificateurs
- `--checkbox` - Case à cocher avec icône et activation du bouton
- `--listitem` - Élément de liste avec des objets icônes imbriqués
- `--selecttitle` - Traité de la même manière que `--selectitem`
- `--selectitem` - Éléments de liste de sélection définis par JSON
- `--titlefont` / `--messagefont` - Configuration de la police : couleur, taille, épaisseur, effet d'ombre
- `--icon` / `--overlayicon` - Objets icones avec symboles, couleurs, palettes et animations
- `--button1symbol` / `--button2symbol` / `--infobuttonsymbol` - Symboles de boutons avec indication de positionnement

Consultez les pages de documentation individuelles pour connaître les schémas JSON détaillés et les exemples.

---

## Listes d'éléments

| Argument | Court | Description |
|---|---|---|
| `--listitem <text\|json>` | | Ajouter un élément de liste. Prend en charge les icônes de statut et les actions de clic. Peut également être spécifié sous forme d'objet JSON avec prise en charge des icônes imbriquées |
| `--liststyle [expanded\|compact]` | | Espacement vertical entre les lignes de la liste |
| `--enablelistselect` | | Permettre la sélection des éléments de la liste ; la sélection effectuée est renvoyée à la sortie |

Voir les [listes d'éléments](/fr/advanced/item-lists) pour plus de détails.

---

## Minuteur et progression

| Argument | Court | Description |
|---|---|---|
| `--timer [<seconds>]` | | Afficher un compte à rebours (par défaut : 10 secondes). La sortie se fera avec le code 4 en cas de dépassement du délai. |
| `--hidetimerbar` | | Masquer la barre de chronomètre tout en continuant le compte à rebours |
| `--hidetimer` | | Masquer complètement le minuteur |
| `--progress [<int>]` | | Afficher une barre de progression avec le nombre d'étapes spécifié |
| `--progresstext <text>` | | Texte initial affiché sous la barre de progression |

Consultez [Minuteur et progression](/fr/advanced/timer-progress)] pour plus de détails.

---

## Dimensions et position de la fenêtre

| Argument | Court | Description |
|---|---|---|
| `--width <num>` | | Largeur de la boîte de dialogue en points |
| `--height <num>` | | Hauteur de la boîte de dialogue, en points |
| `--small` | `-s` | Réduire la taille par défaut de la fenêtre de 25 % |
| `--big` | `-b` | Augmenter la taille par défaut de la fenêtre de 25 % |
| `--position <position>` | | Position de la fenêtre (par exemple, `center`, `topright` ou `x,y`). |
| `--positionoffset <int>` | | Décalage des bords lors de l'utilisation de `--position` (valeur par défaut : 16). |
| `--moveable` | `-o` | Permettre de déplacer la fenêtre en la faisant glisser |
| `--resizable` | | Permettre de redimensionner la fenêtre (implique `--moveable`). |
| `--ontop` | `-p` | Assurez-vous que cette fenêtre reste toujours au-dessus des autres fenêtres |
| `--windowbuttons [close,min,max]` | | Activer les boutons de fermeture, de minimisation et de maximisation de la fenêtre |
| `--showonallscreens` | | Afficher la fenêtre sur tous les écrans connectés |
| `--appearance [dark\|light]` | | Modifier l'apparence de la fenêtre |

Consultez les sections "Taille de la fenêtre" et "Mise en page" pour plus de détails. ](/fr/advanced/window-size) ](/fr/advanced/layout)

---

## Préconfigurations de styles de fenêtres

| Argument | Court | Description |
|---|---|---|
| `--style <preset>` | | Appliquer un style prédéfini : `presentation`, `mini`, `centered`, `alert`, `caution`, `warning` |
| `--mini` | | Fenêtre compacte affichant le titre, l'icône et un message en deux lignes |
| `--fullscreen` | `-f` | Mode plein écran (sans boutons ; les événements liés au clavier restent actifs). |
| `--presentation` | | Mode de présentation avec barre de progression et mise en page structurée |
| `--eula` | | Afficher en mode d'acceptation des conditions d'utilisation |
| `--blurscreen` | | Estomper tout le contenu de l'écran qui se trouve derrière la fenêtre de dialogue |
| `--hideotherapps` | | Masquer toutes les autres applications au démarrage |

Consultez [Écran plein](/fr/advanced/full-screen) et [Présentation](/fr/advanced/presentation)] pour plus de détails.

---

## Notifications

| Argument | Court | Description |
|---|---|---|
| `--notification` | | Envoyer une notification système macOS |
| `--identifier <text>` | `-id` | Identifiant unique pour la notification |
| `--remove` | | Supprimer la notification correspondant à l'élément `--identifier` |
| `--enablenotificationsounds` | | Activer les sons de notification |

Consultez [les notifications](/fr/advanced/notifications)] pour plus de détails.

---

## Son

| Argument | Court | Description |
|---|---|---|
| `--sound <file\|url>` | | Lire un fichier audio au démarrage |
| `--showsoundcontrols` | | Afficher les commandes de lecture (lecture/pause, mise en sourdine, barre de progression). |

---

## Icône de la barre des applications

| Argument | Court | Description |
|---|---|---|
| `--showdockicon` | | Afficher l'icône swiftDialog dans la barre des applications de macOS |
| `--dockicon <file\|url>` | | Afficher une image personnalisée comme icône de la barre des applications (implique `--showdockicon`). |
| `--dockiconbadge <text>` | | Afficher un badge sur l'icône de la barre des applications |

---

## Fichier de commandes

| Argument | Court | Description |
|---|---|---|
| `--commandfile [<file>]` | | Chemin d'accès au fichier de commandes pour les mises à jour en direct des boîtes de dialogue (par défaut : `/var/tmp/dialog.log`). |
| `--displaylog <file>` | | Afficher le contenu d'un fichier tel qu'il est écrit |
| `--loghistory [<int>]` | | Remplir automatiquement `--displaylog` avec les N dernières lignes (par défaut : 100). |

Voir le [fichier de commandes](/fr/advanced/command-file)] pour plus de détails.

---

## Entrées et sorties au format JSON

| Argument | Court | Description |
|---|---|---|
| `--jsonfile <file>` | | Charger la configuration de la boîte de dialogue à partir d'un fichier JSON |
| `--jsonstring <text>` | | Charger la configuration de la boîte de dialogue à partir d'une chaîne de caractères au format JSON |
| `--json` | `-j` | Les résultats sont présentés au format JSON |

Consultez [la configuration JSON](/fr/advanced/json-configuration)] pour plus de détails.

---

## Clavier et interaction

| Argument | Court | Description |
|---|---|---|
| `--quitkey <char>` | | Touches de raccourci personnalisées (utilisée comme `⌘ + <key>`, par défaut : `q`). |
| `--hidedefaultkeyboardaction` | | Exiger `⌘ + ⇧` pour déclencher les actions clavier Return/Esc |
| `--alwaysreturninput` | | Retournez toujours les données saisies par l'utilisateur lors de la sortie, quel que soit le code de sortie |
| `--ignorednd` | `-d` | Afficher la boîte de dialogue même lorsque le mode "Ne pas déranger" est activé |
| `--vieworder <csv>` | | Modifier l'ordre d'affichage des types d'éléments de saisie |

---

## Autorisation

| Argument | Court | Description |
|---|---|---|
| `--key <string>` | `-k` | Clé d'authentification requise pour lancer la boîte de dialogue |
| `--checksum <string>` | | Générer une empreinte SHA256 (à utiliser avec `--key`). |

Consultez [l'autorisation](/fr/operation/authorization)] pour plus de détails.

---

## Fenêtre de connexion

| Argument | Court | Description |
|---|---|---|
| `--loginwindow` | | Afficher la fenêtre de dialogue lors de la connexion (nécessite un agent de lancement approprié). |

Consultez [la fenêtre de connexion](/fr/operation/login-window)] pour plus de détails.

---

## Mode d'inspection

| Argument | Court | Description |
|---|---|---|
| `--inspect-mode` | | Démarrer en mode inspection |
| `--inspect-config <file>` | | Spécifiez la configuration pour le mode d'inspection |
| `--inspect-schema <file>` | | Spécifier le schéma pour le mode d'inspection |
| `--schema-validate <file>` | | Valider une configuration par rapport à un schéma |

Consultez [le mode d'inspection](/fr/advanced/inspect-mode)] pour plus de détails.

---

## Utilitaires et débogage

| Argument | Court | Description |
|---|---|---|
| `--version` | `-v` | Imprimez la chaîne de version |
| `--help [<argument>]` | | Afficher l'aide, ou afficher une aide détaillée pour un argument spécifique |
| `--licence` | `-l` | Imprimer la licence |
| `--debug [<colour>]` | | Activez le mode débogage avec, optionnellement, des indications visuelles pour délimiter les contenus |
| `--verbose` | `-vvv` | Activer la sortie détaillée des journaux |
| `--listfonts` | | Afficher les noms des polices disponibles |
| `--demo` | | Démarrer en mode de démonstration |
| `--builder` | | Lancer l'interface du kit de développement |
| `--jh` | `-jh` | Activer le mode de compatibilité pour jamfHelper |

Consultez [Builder](/fr/reference/builder)] pour plus de détails.
