---
title: Scripts de démonstration
description: Script complet de démonstration pour la sélection et l'installation d'applications
translationSynced: 2026-11-23T05:32:20+00:00
---

Une suite de démonstrations complète est disponible à l'adresse suivante : https://github.com/swiftDialog/demo

## Suite de démonstrations complète de swiftDialog

Une collection de scripts zsh qui illustrent toutes les fonctionnalités principales de [swiftDialog](https://github.com/swiftDialog/swiftDialog), grâce à une visite guidée interactive et autonome.

## Exigences

- macOS 15 ou version ultérieure
- [**swiftDialog version 3 ou supérieure**](https://github.com/swiftDialog/swiftDialog/releases)

## Démarrage rapide

```zsh
# clone this repo
git clone https://github.com/swiftDialog/demo.git swiftDialog-demo

# or download the zip
curl -sL "https://github.com/swiftDialog/demo/archive/refs/heads/main.zip" -o swiftDialog-demo.zip && unzip swiftDialog-demo.zip -d swiftDialog-demo

cd swiftDialog-demo
./run_demos.zsh
```

Le contrôleur principal utilise directement swiftDialog. Choisissez les démonstrations avec des cases à cocher, puis parcourez-les une par une.

## Compétences en intelligence artificielle pour la création de dialogues avec swiftDialog

**Vous découvrez swiftDialog ?** Commencez par la page officielle [swiftDialog Builder](https://swiftdialog.app/builder/builder/) pour vous familiariser avec l'outil et réaliser des prototypes visuels, puis utilisez l'un des ensembles de compétences intégrés au dépôt pour transformer cette compréhension en scripts shell de type dépôt. L'outil Builder est utile, mais il n'est pas exhaustif et ne remplace pas les décisions finales concernant la taille, la mise en forme et le flux de travail.

### Compétences disponibles

**[`codex-swiftdialog-builder`](skills/codex-swiftdialog-builder/)** — Pour GitHub Copilot / OpenAI Codex

- [`SKILL.md`](skills/codex-swiftdialog-builder/SKILL.md) — Flux de travail de Codex et sélection du niveau de service
- [`references/`](skills/codex-swiftdialog-builder/references/) — Conseils pour la création de maquettes et la conception de contenu.]
- [`assets/templates/`](skills/codex-swiftdialog-builder/assets/templates/) — Scripts de démarrage (pour l'environnement shell)
- Comprend un script Jamf/root-run `/var/tmp` ainsi qu'un mécanisme de transfert de propriété pour les flux de travail basés sur des fichiers de commandes, lancés en tant que `root`

**[`claude-swiftdialog-builder`](skills/claude-swiftdialog-builder/)** — Pour Claude Sonnet

- [`CLAUDE.md`](skills/claude-swiftdialog-builder/CLAUDE.md) — Flux de travail et choix du niveau de service de Claude
- [`references/`](skills/claude-swiftdialog-builder/references/) — Conseils pour la création de maquettes et la conception de contenu.]
- [`templates/`](skills/claude-swiftdialog-builder/templates/) — Scripts de démarrage (pour l'environnement shell)
- Comprend un script Jamf/root-run `/var/tmp` ainsi qu'un mécanisme de transfert de propriété pour les flux de travail basés sur des fichiers de commandes, lancés en tant que `root`

Les deux compétences suivent les mêmes conventions de référentiel et produisent une sortie de script identique. Choisissez celle qui correspond à votre plateforme d'intelligence artificielle. Consultez [`skills/README.md`](skills/README.md) pour des instructions d'utilisation détaillées.

Ce sont des ensembles de compétences pour les assistants IA, et non des démonstrations fonctionnelles intégrées à la suite.

## Plateforme de développement assistée par l'intelligence artificielle

Après avoir exploré la version de démonstration et compris les fonctionnalités de swiftDialog, utilisez le répertoire [`playground/`](playground/)] pour créer vos propres scripts personnalisés avec l'aide de l'intelligence artificielle. L'environnement de développement inclut un guide détaillé, étape par étape, qui vous explique comment :

- Utilisez les assistants d'IA (Claude, Copilot) grâce aux fonctionnalités intégrées
- Choisissez le niveau de fonctionnalité adapté à votre flux de travail (dialogues de base → formulaires → mises à jour de progression → mode d'inspection).
- Suivez des scénarios concrets et détaillés, avec des instructions précises et des exemples des interactions attendues avec l'IA
- Créez des scripts prêts à être utilisés en production pour les tâches d'administration Mac (intégration, conformité, déploiement, surveillance, confirmation des actions destructrices).

**Commencez ici :** [`playground/README.md`](playground/README.md) — Votre espace de travail pour le développement rapide de scripts swiftDialog assisté par l'IA.

## Index des démonstrations

- `01_basic_styles.zsh` — `--style` (alerte, précaution, avertissement, centré), remplacements de style
- `02_title_message.zsh` — `--title`, `--titlefont`, `--message`, `--messagefont`, `--messagealignment`, `--messageposition`, `--bannertitle`, titre "aucun"
- `03_icons.zsh` — `--icon` (Symboles SF, applications, fonctionnalités intégrées, QR, palette, couleurs automatiques, épaisseur), `--iconsize`, `--iconalpha`, `--centreicon`, `--overlayicon`, `--hideicon`
- `04_buttons.zsh` — `--button1text`, `--button1symbol`, `--button1disabled`, `--button2text`, `--button2symbol`, `--infobuttontext`, `--infobuttonsymbol`, `--infobuttonaction`, `--buttonstyle` (centre, empilement), `--buttonsize`, `--buttontextsize`, `--hidedefaultkeyboardaction`
- `05_images_banners.zsh` — `--image`, `--imagecaption`, `--bannerimage`, `--bannertitle`, `--bannertext`, `--background`, `--bgalpha`, `--bgposition`, `--bgfill`
- `06_progress_timer.zsh` — `--progress` (absolu, incrément, remise à zéro, terminé), `--progresstext`, `--progresstextalignment`, `--timer`, `--hidetimerbar`, mises à jour de l'état d'avancement des fichiers de commandes
- `07_text_fields.zsh` — `--textfield` (obligatoire, sécurisé, rapide, valeur, expression régulière, erreur d'expression régulière, confirmation, sélection de fichiers, type de fichier, chemin, nom), `--textfieldlivevalidation`
- `08_dropdowns.zsh` — `--selecttitle`, `--selectvalues`, `--selectdefault`, modificateurs (obligatoires, radio, recherchables, multi-sélection, nom), séparateurs
- `09_checkboxes.zsh` — `--checkbox` (modificateur de nom), `--checkboxstyle` (case à cocher, interrupteur, tailles)
- `10_list_items.zsh` — `--listitem` (état, description de l'état, symboles SF personnalisés), `--liststyle`, `--enablelistselect`, fichier de commandes (list:, listitem:, ajouter, supprimer, index).
- `11_window_options.zsh` — `--width`, `--height`, `--big`, `--small`, `--position`, `--positionoffset`, `--moveable`, `--ontop`, `--resizable`, `--windowbuttons`, `--appearance`, `--showdockicon`, `--dockiconbadge`
- `12_command_file.zsh` — Fichier de commandes complet : titre : , police de caractères du titre : , message : (+ajout), alignement : , icône : , icône de superposition : , transparence de l'icône : , texte du bouton 1 : , bouton 1 : , texte d'information : , zone d'information : , icône : centre/gauche
- `13_notifications.zsh` — `--notification`, `--subtitle`, `--identifier`, `--remove`
- `14_mini_presentation.zsh` — `--mini` (avec barre de progression), `--presentation` (avec liste à puces, tableau d'informations, barre de progression).
- `15_web_video.zsh` — `--webcontent`, `--video` (raccourci YouTube), `--videocaption`, `--autoplay`
- `16_json_input.zsh` — `--jsonstring`, `--jsonfile`, tableaux JSON pour les cases à cocher, les éléments de sélection, les champs de texte et les images
- `17_fullscreen_blur.zsh` — `--fullscreen`, `--blurscreen`, `--hideotherapps`
- `18_misc_features.zsh` — `--helpmessage`, `--infotext`, `--infobox`, `--vieworder`, `--quitkey`, `--sound`, `--showsoundcontrols`, `--displaylog`, `--loghistory`, `--debug`, `--eula`, `--alwaysreturninput`, explication de la clé d'authentification/de la somme de contrôle
- `19_inspect_mode.zsh` — `--inspect-mode`, `--inspect-config`, `--published-sessions-dir`, `stepType: "cadence"`, `cadenceStyle: "carousel"`, fréquence d'images (images par seconde) (IPC) (`cadence:satisfy`, `cadence:advance`, `cadence:goto`), refonte de la configuration prédéfinie 3, logo du pied de page, option forcée `appearance`, `cacheExtensions` avec `aria2`
- `20_branched_workflows.zsh` — tableau de niveau supérieur, `workflow`, `branch.map`, `branch.default`, `branch.ifTrue`, `branch.ifFalse`, `nextpage`, `finalpage`, tenant compte de l'historique. Précédent

## Exécution de démonstrations individuelles

Chaque script de démonstration est autonome.

```zsh
./demos/06_progress_timer.zsh
./demos/12_command_file.zsh
```

## Remarques

- Les démonstrations qui utilisent `--blurscreen` ou `--fullscreen` occuperont brièvement l'écran
- Les démonstrations de notifications nécessitent les autorisations de notification pour le fonctionnement de swiftDialog
- Certaines démonstrations d'images utilisent des images de fond d'écran du système, qui peuvent varier en fonction de la version de macOS
- La version de démonstration 19 met désormais l'accent sur les améliorations de la version 3.1.0b4, notamment le système de navigation "cadence carousel", la refonte compacte du préréglage 3, la publication des sessions, et un exemple de fichier JSON pour la gestion des préférences.
- Les versions 19 et 20 nécessitent **swiftDialog version 3.1.0b4 ou une version ultérieure** pour la prise en charge des fonctionnalités de synchronisation et des flux de travail structurés.
- Consultez les notes de version de [swiftDialog v3.1.0b4](https://github.com/swiftDialog/swiftDialog/releases/tag/v3.1.0b4)] pour connaître la liste précise des fonctionnalités abordées ici.