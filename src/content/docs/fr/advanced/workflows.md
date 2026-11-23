---
title: Workflow de swiftDialog
description: Flux de dialogue multi-étapes dans swiftDialog
translationSynced: 2026-11-23T08:35:52+00:00
---

> **NOTE :** La fonctionnalité "Workflow" a été introduite dans la version 3.1 de swiftDialog.

# Documentation des fonctionnalités de flux de travail de swiftDialog

## Aperçu

La fonctionnalité **Workflow** permet de créer des flux de dialogue en plusieurs étapes dans swiftDialog, vous offrant la possibilité de concevoir des interfaces utilisateur de type assistant qui guident les utilisateurs à travers plusieurs écrans de saisie et d'informations. Chaque carte représente un écran distinct, avec sa propre configuration, et les utilisateurs peuvent naviguer vers l'avant et vers l'arrière dans le flux de travail.

Les flux de travail sont définis à l'aide de fichiers de configuration JSON, ce qui permet de créer facilement des dialogues complexes et comportant plusieurs étapes, sans avoir à écrire de code.

## Principales caractéristiques

- **Flux de travail en plusieurs étapes :** Divisez les dialogues complexes en étapes gérables
- **Commandes de navigation :** Boutons "Suivant", "Précédent" et "Terminer" automatiques
- **Ramification conditionnelle :** Permet de diriger vers différentes cartes de flux de travail en fonction de la sélection dans une liste déroulante ou de l'état d'une case à cocher, sans nécessiter de script de rappel
- **Persistance des données :** Les informations saisies par l'utilisateur sont conservées lors de la navigation entre les différentes étapes du processus
- **Paramètres globaux :** Définissez des paramètres communs une seule fois, puis modifiez-les individuellement pour chaque carte
- **Substitution de variables :** Utilisation de la syntaxe `{fieldname}` pour référencer les valeurs provenant des étapes précédentes du flux de travail
- **Validation :** Vérification obligatoire des champs avant de passer à l'étape suivante
- **Configuration dynamique :** Chaque carte peut présenter des éléments d'interface utilisateur et des paramètres uniques
- **Appels de fonction (Callbacks) :** Exécutez des scripts shell lorsque vous passez d'une étape à une autre dans le flux de travail

## Concepts de base

### Structure du flux de travail

Un dialogue basé sur un flux de travail est défini dans un fichier de configuration JSON, qui possède la structure suivante :

```json
{
  "workflow": [
    { "title": "Step 1", "message": "First screen..." },
    { "title": "Step 2", "message": "Second screen..." },
    { "title": "Step 3", "message": "Final screen..." }
  ]
}
```

### Configuration globale

Les propriétés définies au niveau racine (en dehors du tableau `workflow`) servent de valeurs par défaut pour toutes les cartes de flux de travail. Les cartes de flux de travail individuelles peuvent remplacer ces valeurs par défaut :

```json
{
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertNoteIcon.icns",
  "button1text": "Continue",
  "workflow": [
    { "title": "Step 1", "message": "Uses default icon" },
    { "title": "Step 2", "icon": "SF=checkmark.circle", "message": "Custom icon" }
  ]
}
```

### Identification par carte

Les cartes sont automatiquement ordonnées en fonction de leur position dans le tableau. Vous pouvez, si vous le souhaitez, spécifier un critère de tri personnalisé pour définir un ordre spécifique : `id`.

```json
{
  "workflow": [
    { "id": 0, "title": "First" },
    { "id": 10, "title": "Second" },
    { "id": 5, "title": "Third (will be displayed second)" }
  ]
}
```

## Navigation

### Comportement du bouton

En mode de flux de travail, le comportement du bouton change automatiquement :

- **Bouton 1** (côté droit) :
  - Affiche le bouton "Suivant" sur les cartes de flux de travail numérotées de 1 à n-1
  - Affiche le mot "Fin" sur la dernière carte (ou un texte personnalisé via `button1text`).
  - Valide les champs obligatoires avant de passer à l'étape suivante
  
- **Bouton 2** (côté gauche) :
  - Caché sur la première carte
  - Affiche le bouton "Précédent" sur les cartes de flux de travail, de la carte numéro 2 à la carte numéro n
  - Aucune validation lors de la navigation en arrière

### Personnalisation du texte des boutons

Par défaut, les boutons de navigation affichent les libellés suivants : "Suivant", "Précédent" et "Terminer". Vous pouvez les modifier comme suit :

- `--nextbuttontext "<text>"` — Texte du bouton "Suivant" (par défaut `Next`).
- `--previousbuttontext "<text>"` — Texte pour le bouton "Précédent" (par défaut `Previous`).
- `button1text` (niveau supérieur ou par carte) — texte pour le bouton **Terminer**

```bash
dialog --jsonfile config.json --nextbuttontext "Continue" --previousbuttontext "Back"
```

### Flux de navigation

<img width="650" alt="image" src="/images/navigation-flow.png" />


## Navigation hiérarchique

Par défaut, les cartes de flux de travail sont consultées dans l'ordre de leur arrangement. Vous pouvez modifier ce comportement en utilisant trois propriétés facultatives, configurables pour chaque carte individuellement :

| Propriété | Type | Objectif |
|---|---|---|
| `branch` | objet | Choisissez la carte suivante en fonction d'une valeur spécifique présente sur la carte actuelle |
| `nextpage` | entier | Surcharge statique — accédez à cette carte `id` après "Suivant" |
| `finalpage` | booléen | Cette carte interrompt le flux de travail ; l'étape suivante devient "Terminer" |

Lorsque l'utilisateur clique sur "Suivant", swiftDialog détermine la destination selon l'ordre suivant :

1. `branch` (si cette option est activée et qu'une règle correspondante est trouvée).
2. `nextpage` (si cette option est activée).
3. La carte suivante dans la séquence
4. Fin du flux de travail (si aucune carte suivante n'existe, ou si `finalpage` est vrai).

Le bouton "Précédent" tient compte de l'historique : il renvoie à la carte à partir de laquelle l'utilisateur est réellement venu, et non à la position "index actuel - 1". Cela fonctionne correctement, même en cas de navigation entre différentes sections.

> swiftDialog ne vérifie ni les boucles ni les étapes qui ne peuvent être atteintes. Si votre flux de travail peut revenir sur lui-même, l'utilisateur reviendra simplement à ces étapes. Si ce n'est pas le comportement souhaité, il faut corriger la logique du flux de travail.

### Déclenchement à partir d'une liste déroulante

La valeur `branch.field` correspond à la `name` (préférée) du champ, ou à sa `title`/`label`. Pour une liste déroulante, la valeur sélectionnée est comparée aux clés présentes dans `branch.map` :

```json
{
  "workflow": [
    {
      "id": 1,
      "title": "Choose your path",
      "message": "Pick an option to control which card appears next.",
      "selectitems": [
        {
          "name": "userType",
          "title": "Account type",
          "values": ["Admin", "Standard", "Guest"],
          "default": "Standard"
        }
      ],
      "branch": {
        "field": "userType",
        "map": {
          "Admin":    10,
          "Standard": 20,
          "Guest":    30
        },
        "default": 99
      }
    },
    { "id": 10, "title": "Admin setup", "nextpage": 99 },
    { "id": 20, "title": "Standard setup", "nextpage": 99 },
    { "id": 30, "title": "Guest setup", "nextpage": 99 },
    { "id": 99, "title": "Summary", "finalpage": true }
  ]
}
```

`branch.default` est facultatif. S'il est défini et que la valeur sélectionnée ne figure pas dans `map`, le flux de travail passe à la carte de secours correspondante.

### Départ à partir d'une case à cocher

Pour un champ booléen unique, utilisez la notation abrégée `ifTrue` / `ifFalse` au lieu de `map` :

```json
{
  "id": 5,
  "checkbox": [
    { "name": "wantsExtras", "label": "Show advanced options" }
  ],
  "branch": {
    "field": "wantsExtras",
    "ifTrue":  6,
    "ifFalse": 99
  }
}
```

Vous pouvez également utiliser `map` avec les clés `"true"` et `"false"` si vous le préférez, mais `ifTrue`/`ifFalse` est plus lisible.

### Remplacement statique de `nextpage`

Si vous n'avez pas besoin d'un routage dynamique, mais que vous souhaitez que la carte avance plus rapidement, réglez `nextpage` :

```json
{ "id": 3, "title": "Optional details", "nextpage": 10 }
```

### Interrompre le flux de travail de manière anticipée

Pour arrêter le flux de travail à une étape spécifique, vous pouvez marquer une carte comme étant "définitive".

```json
{ "id": 99, "title": "Summary", "finalpage": true }
```

Sur la dernière carte, le bouton 1 affiche "Terminer" et ferme la boîte de dialogue lorsqu'on clique dessus, quel que soit le nombre de cartes de flux de travail restantes dans le tableau.

## Exemples d'utilisation

### Exemple 1 : Assistant simple en trois étapes

```json
{
  "title": "Setup Wizard",
  "icon": "SF=gearshape.2",
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to the setup wizard. Click Continue to begin."
    },
    {
      "title": "Enter Information",
      "message": "Please provide your details:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email Address", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Setup is complete! Click Finish to close this wizard.",
      "button1text": "Finish"
    }
  ]
}
```

Exécutez-le
```bash
dialog --jsonfile /path/to/config.json
```

### Exemple 2 : Utilisation de la substitution de variables

La substitution de variables vous permet de faire référence à des valeurs provenant de cartes de flux de travail précédentes en utilisant la syntaxe `{fieldname}` :

```json
{
  "title": "User Registration",
  "workflow": [
    {
      "title": "Personal Information",
      "message": "Step 1: Enter your details",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true }
      ]
    },
    {
      "title": "Confirmation",
      "message": "Hello {First Name} {Last Name}! Please confirm your information is correct.",
      "infobox": "**Name:** {First Name} {Last Name}"
    }
  ]
}
```

Les espaces réservés `{First Name}` et `{Last Name}` dans la carte 2 seront remplacés par les valeurs saisies dans la carte 1.

### Exemple 3 : Paramètres globaux avec possibilité de les modifier

```json
{
  "icon": "SF=info.circle",
  "width": 600,
  "height": 400,
  "workflow": [
    {
      "title": "Introduction",
      "message": "This card uses the default icon and size."
    },
    {
      "title": "Custom Layout",
      "icon": "SF=wrench.and.screwdriver",
      "width": 800,
      "height": 500,
      "message": "This card has a custom icon and larger size."
    },
    {
      "title": "Back to Normal",
      "message": "This card reverts to default icon and size."
    }
  ]
}
```

### Exemple 4 : Collecte de données à plusieurs étapes

```json
{
  "title": "System Configuration",
  "icon": "/System/Library/PreferencePanes/Appearance.prefPane/Contents/Resources/AppIcon.icns",
  "workflow": [
    {
      "title": "Network Settings",
      "message": "Configure network preferences:",
      "selectitems": [
        {
          "title": "Network Type",
          "values": ["WiFi", "Ethernet", "VPN"],
          "default": "WiFi"
        }
      ]
    },
    {
      "title": "User Preferences",
      "message": "Set user preferences:",
      "checkbox": [
        { "label": "Enable notifications", "checked": true },
        { "label": "Auto-update", "checked": true },
        { "label": "Send analytics", "checked": false }
      ]
    },
    {
      "title": "Summary",
      "message": "Review your settings:",
      "infobox": "**Network:** {Network Type}\\n\\n**Notifications:** {Enable notifications}\\n**Auto-update:** {Auto-update}\\n**Analytics:** {Send analytics}"
    }
  ]
}
```

### Exemple 5 : Indicateur de progression avec des cartes

```json
{
  "title": "Installation Wizard",
  "workflow": [
    {
      "title": "Preparing (1 of 3)",
      "message": "Preparing installation...",
      "progress": 100,
      "progresstext": "Checking system requirements"
    },
    {
      "title": "Installing (2 of 3)",
      "message": "Installing software...",
      "progress": 100,
      "progresstext": "Copying files"
    },
    {
      "title": "Complete (3 of 3)",
      "message": "Installation complete!",
      "icon": "SF=checkmark.circle.fill",
      "progress": 100,
      "progresstext": "Finished"
    }
  ]
}
```

### Exemple 6 : Validation des champs obligatoires

```json
{
  "title": "Registration Form",
  "workflow": [
    {
      "title": "Account Details",
      "message": "All fields marked with * are required",
      "textfield": [
        { "title": "Username", "required": true, "prompt": "Enter username" },
        { "title": "Password", "required": true, "secure": true },
        { "title": "Confirm Password", "required": true, "secure": true }
      ]
    },
    {
      "title": "Contact Information",
      "message": "Please provide at least one contact method",
      "textfield": [
        { "title": "Email", "required": true },
        { "title": "Phone", "required": false }
      ]
    }
  ]
}
```

Si les utilisateurs tentent de cliquer sur "Suivant" sans avoir rempli les champs obligatoires, une fenêtre de message d'erreur s'affichera.

## Fonctionnalités avancées

### Propriétés spécifiques au flux de travail

Toute propriété standard de swiftDialog peut être utilisée dans un flux de travail. Les propriétés les plus courantes comprennent :

- **Mise en page** : `width`, `height`, `position`
- **Contenu :** `title`, `message`, `icon`, `iconsize`
- **Saisie :** `textfield`, `selectitems`, `checkbox`, `radio`
- Affichage : `image`, `video`, `webcontent`, `listitem`
- **Avancement :** `progress`, `progresstext`
- **Informations :** `infobox`, `helpmessage`
- **Style** : `messagefont`, `alignment`, `bannerimage`
- **Navigation** : `branch`, `nextpage`, `finalpage` (voir la [navigation hiérarchique](#navigation-hiérarchique)]).

### Nommage des champs de saisie

Pour que le remplacement de variables fonctionne correctement, les champs de saisie doivent avoir une nomenclature cohérente :

```json
{
  "textfield": [
    { "title": "First Name" }  // Referenced as {First Name}
  ],
  "selectitems": [
    { "title": "Department", "values": ["IT", "HR", "Sales"] }  // Referenced as {Department}
  ]
}
```

Si un champ ne possède pas de valeur explicite `title`, vous pouvez utiliser une propriété `name` :

```json
{
  "textfield": [
    { "title": "Your Name", "name": "username" }  // Referenced as {username}
  ]
}
```

### Persistance des données

Les données saisies par l'utilisateur sont automatiquement enregistrées lorsque :
- Cliquez sur « Suivant » pour passer à la carte suivante
- Cliquez sur "Précédent" pour revenir en arrière

Lorsque les utilisateurs reviennent à une carte précédente, leurs données saisies sont rétablies.

### Accès aux données de la carte

Lorsque l'utilisateur clique sur le bouton "Terminer" sur la dernière carte, toutes les données collectées sont affichées sur la sortie standard (stdout) au format JSON :

```json
{
  "First Name": "John",
  "Last Name": "Doe",
  "Email Address": "john.doe@example.com",
  "Department": "IT",
  "Enable notifications": true
}
```

### Rappels (callbacks) à l'avancement

Utilisez l'option `--onadvance` pour exécuter une commande shell lorsque vous passez d'une carte à l'autre dans le flux de travail :

```bash
dialog --jsonfile config.json --onadvance "/path/to/script.sh"
```

Le script reçoit :
- Index de carte (à base zéro).
- Numéro de carte (si applicable).
- Lecture des informations de la carte au format JSON via l'entrée standard

Le script doit se terminer avec :
- **Code de sortie 0 :** Autorise la progression
- **Code de sortie non nul :** Interrompre l'exécution et afficher un message d'erreur

Exemple de script de rappel :
```bash
#!/bin/bash
# script.sh - Validate email format before advancing

input=$(cat)
email=$(echo "$input" | jq -r '.["Email Address"]')

if [[ ! "$email" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$ ]]; then
    echo "Invalid email address format"
    exit 1
fi

exit 0
```

## Meilleures pratiques

### 1. Maintenez la concentration des flux de travail
Chaque carte doit avoir un objectif unique et clair. Évitez de surcharger les utilisateurs en incluant trop de champs sur une seule carte.

### 2. Utilisez des titres descriptifs
Les titres des cartes doivent indiquer clairement à quelle étape du processus l'utilisateur se trouve.
```json
{ "title": "Step 1: Personal Information" }
{ "title": "Step 2: Contact Details" }
{ "title": "Step 3: Review & Confirm" }
```

### 3. Fournir un contexte
Utilisez le champ de message pour expliquer ce que l'utilisateur doit faire :
```json
{
  "title": "Account Setup",
  "message": "Create your account by choosing a username and password. Your username must be at least 6 characters."
}
```

### 4. Utilisez la validation des champs obligatoires
Veuillez indiquer les champs obligatoires pour garantir la complétude des données.
```json
{ "title": "Email", "required": true }
```

### 5. Fournir des fiches de résumé
Inclure une fiche de récapitulatif finale présentant toutes les informations recueillies :
```json
{
  "title": "Review Your Information",
  "message": "Please verify everything is correct before proceeding.",
  "infobox": "**Name:** {Full Name}\\n**Email:** {Email}\\n**Department:** {Department}"
}
```

### 6. Tenez compte du flux de navigation
- Ne faites pas en sorte que la première étape nécessite une saisie complexe ; facilitez l'expérience pour les utilisateurs
- Placez la collecte des données les plus importantes au début
- Enregistrer la confirmation/la révision pour la carte finale

### 7. Adoptez une mise en forme cohérente
Définir les paramètres par défaut globaux pour assurer une présentation uniforme :
```json
{
  "icon": "SF=person.crop.circle",
  "width": 700,
  "height": 450,
  "messagefont": "size=13",
  "workflow": [ /* ... */ ]
}
```

## Limitations et remarques

1. **Mises à jour des fichiers de commandes :** Lors de l'utilisation du mode workflow avec un fichier de commandes, certaines mises à jour dynamiques peuvent ne pas fonctionner comme prévu. Le mode workflow est conçu pour la collecte de données plutôt que pour les mises à jour dynamiques de l'état.

2. **Personnalisation des boutons :** Le comportement des boutons 1 et 2 est contrôlé par le mode de flux de travail et ne peut pas être entièrement personnalisé lorsque ce mode est activé.

3. **Codes de sortie :** En mode workflow, la boîte de dialogue se ferme uniquement lorsque :
   - L'utilisateur clique sur le bouton "Terminer" sur la dernière carte (code de sortie : 0).
   - L'utilisateur a annulé l'opération (le code de sortie varie).
   - La validation échoue et l'utilisateur choisit d'annuler l'opération

4. **Portée des variables :** Les variables provenant des étapes précédentes du flux de travail ne sont disponibles que dans les étapes suivantes, et non dans les étapes antérieures. La substitution des variables est unidirectionnelle.

5. **Nommage des champs :** Pour une substitution de variables correcte, utilisez des caractères alphanumériques et des espaces dans les titres des champs. L'utilisation de caractères spéciaux peut entraîner des problèmes.

## Dépannage

### Les cartes ne s'affichent pas
- Vérifiez la syntaxe du fichier JSON à l'aide de `jsonlint` ou d'un outil similaire
- Assurez-vous que le tableau `workflow` se trouve au niveau supérieur
- Vérifiez qu'au moins une carte est définie

### Variables non substituées
- Vérifiez que les noms de champs correspondent exactement (respecter la casse).
- Vérifiez que les références aux variables utilisent des accolades : `{fieldname}`
- Vérifiez que le champ référencé se trouvait sur une carte précédente, et non sur la carte actuelle ou une carte future

### La validation ne fonctionne pas
- Vérifiez que les champs `"required": true` sont correctement configurés
- Vérifiez que ce champ possède une propriété de type `title` ou `name`
- Consulter les journaux de débogage avec l'indicateur `--debug`

### Bouton "Précédent" non affiché
- Vérifiez que vous ne vous trouvez pas sur la première carte du flux de travail (l'élément précédent est masqué sur la première carte).
- Vérifiez que le mode de flux de travail est bien activé (que le tableau de flux de travail existe).

### La branche a été affectée à la mauvaise carte
- Confirmer que la valeur `branch.field` correspond au champ `name` (ou à son `title`/`label` si aucun nom n'est défini).
- Pour les listes déroulantes, les clés utilisées pour la comparaison sont comparées directement à la valeur sélectionnée par l'utilisateur, en tenant compte de la casse et des espaces
- Pour les cases à cocher, privilégiez les clés de mappage `ifTrue`/`ifFalse` plutôt que `"true"`/`"false"`
- Vérifiez le journal de swiftDialog : les cibles [`nextpage` / `branch`] invalides sont signalées au moment du chargement

## Exemple complet : Assistant d'intégration des nouveaux employés

```json
{
  "title": "Employee Onboarding",
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/UserIcon.icns",
  "width": 750,
  "height": 500,
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome to the Company!",
      "message": "## Welcome Aboard!\\n\\nThis wizard will guide you through the onboarding process.\\n\\nClick Continue to get started.",
      "icon": "SF=hands.clap.fill",
      "iconsize": 120
    },
    {
      "title": "Personal Information",
      "message": "Please provide your personal details (all fields required):",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true },
        { "title": "Employee ID", "required": true },
        { "title": "Work Email", "required": true, "prompt": "name@company.com" }
      ]
    },
    {
      "title": "Department Assignment",
      "message": "Select your department and role:",
      "selectitems": [
        {
          "title": "Department",
          "values": ["Engineering", "Marketing", "Sales", "HR", "Finance"],
          "default": "Engineering"
        },
        {
          "title": "Role",
          "values": ["Manager", "Senior", "Mid-level", "Junior"],
          "default": "Mid-level"
        }
      ]
    },
    {
      "title": "System Preferences",
      "message": "Configure your system preferences:",
      "checkbox": [
        { "label": "Enable email notifications", "checked": true },
        { "label": "Join company Slack", "checked": true },
        { "label": "Subscribe to company newsletter", "checked": true },
        { "label": "Opt-in to mentorship program", "checked": false }
      ]
    },
    {
      "title": "Review & Confirm",
      "message": "Please review your information before completing the onboarding process:",
      "icon": "SF=checkmark.circle",
      "infobox": "**Name:** {First Name} {Last Name}\\n**Employee ID:** {Employee ID}\\n**Email:** {Work Email}\\n\\n**Department:** {Department}\\n**Role:** {Role}\\n\\n**Email Notifications:** {Enable email notifications}\\n**Slack:** {Join company Slack}\\n**Newsletter:** {Subscribe to company newsletter}\\n**Mentorship:** {Opt-in to mentorship program}",
      "button1text": "Complete Onboarding"
    }
  ]
}
```

Enregistrez ceci sous le nom `onboarding.json` et exécutez-le :
```bash
dialog --jsonfile onboarding.json
```

## Exemple d'intégration : Script Shell

Voici un exemple complet de script shell qui utilise le mode de flux de travail et traite les résultats :

```bash
#!/bin/bash

# onboarding.sh - Employee onboarding with swiftDialog workflow

DIALOG="/usr/local/bin/dialog"
CONFIG="/tmp/onboarding_config.json"

# Create the JSON configuration
cat > "$CONFIG" << 'EOF'
{
  "title": "Employee Onboarding",
  "icon": "SF=person.crop.circle.badge.checkmark",
  "width": 700,
  "height": 450,
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to Company XYZ! This wizard will set up your account."
    },
    {
      "title": "Enter Details",
      "message": "Please provide your information:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Onboarding complete for {Full Name}!",
      "infobox": "We'll send a confirmation to {Email}"
    }
  ]
}
EOF

# Run dialog and capture output
if output=$("$DIALOG" --jsonfile "$CONFIG" 2>&1); then
    echo "Onboarding completed successfully!"
    echo "Collected data:"
    echo "$output" | jq .
    
    # Extract specific fields
    full_name=$(echo "$output" | jq -r '.["Full Name"]')
    email=$(echo "$output" | jq -r '.Email')
    
    echo "Processing onboarding for $full_name ($email)..."
    
    # Add your custom logic here
    # - Create user account
    # - Send welcome email
    # - Configure systems
    
else
    echo "Onboarding was cancelled or failed"
    exit 1
fi

# Cleanup
rm -f "$CONFIG"
```

## Résumé

La fonctionnalité Workflow dans swiftDialog offre un moyen puissant de créer des interfaces multi-étapes, de type assistant, grâce à une configuration simple basée sur JSON. Parmi les principaux avantages, on trouve :

- **Simplification des processus complexes** : Décomposez les processus complexes en étapes gérables
- **Navigation intégrée** - Boutons "Suivant", "Précédent" et "Fin" automatiques
- **Collecte de données** : Collectez et validez facilement les informations saisies par les utilisateurs, quel que soit le nombre d'écrans utilisés
- **Configuration flexible** : Utilisez les paramètres par défaut globaux et les modifications spécifiques à chaque flux de travail
- **Substitution de variables** : Permettre de référencer les valeurs des étapes précédentes du flux de travail dans les étapes suivantes
- **Aucune compétence en programmation requise** – Définissez tout dans un fichier JSON

Pour plus d'informations sur les différentes options et paramètres de swiftDialog, veuillez consulter la documentation principale de swiftDialog ou utiliser `dialog --help`.
