---
title: Mode d'inspection
description: "Guide d'introduction au mode d'inspection de swiftDialog : surveillance des installations et conformité du système"
translationSynced: 2026-11-23T03:32:02+00:00
---


# Mode d'inspection de swiftDialog

Le mode d'inspection de swiftDialog est une nouvelle fonctionnalité intégrée qui permet un suivi en temps réel au sein du système de fichiers macOS. Il surveille l'état du système de fichiers (en utilisant l'API FSEvents d'Apple) tout en surveillant les installations d'applications et en examinant les dossiers de cache, les fichiers et le contenu des fichiers plist, afin de visualiser les contrôles de conformité. Cette fonctionnalité est spécialement conçue pour être utilisée lors de l'inscription des appareils, du déploiement des logiciels et des audits de conformité, offrant aux utilisateurs finaux une visibilité claire sur leur statut de conformité.

## Aperçu

Le mode d'inspection surveille en permanence les chemins de fichiers et les répertoires de cache spécifiés afin de suivre l'état des applications ou des composants système. Il fournit une rétroaction visuelle grâce à différents modèles prédéfinis, chacun étant conçu pour des cas d'utilisation spécifiques.


### Caractéristiques principales
- Surveillance en temps réel du système de fichiers
- Détection de l'avancement du téléchargement par surveillance du cache
- Plusieurs préréglages visuels pour différents scénarios
- Validation simple basée sur un fichier plist (`bool`, `string`, `exists`).
- Personnalisation des thèmes et de l'identité visuelle (avec certaines limitations).
- Activer automatiquement les boutons une fois la tâche terminée

## Premiers pas

### Utilisation de base

1. Créez un fichier de configuration au format JSON :
```json
{
  "title": "Application Installation",
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}

```
:::tip[ordre des éléments]
Important : l'attribut guiIndex doit être unique et détermine l'ordre des éléments dans l'interface graphique. Les nombres les plus faibles sont affichés en premier.
:::

2. Lancer swiftDialog avec l'option d'inspection :
```bash
/usr/local/bin/dialog --inspect-mode --inspect-config /path/to/config.json
```

3. Facultativement, vous pouvez définir la variable d'environnement qui spécifie le chemin d'accès au fichier de configuration :
```bash
export DIALOG_INSPECT_CONFIG="/path/to/config.json"
/usr/local/bin/dialog --inspect-mode
```

## Référence de configuration JSON

### Options de dialogue générales

Le mode d'inspection prend désormais en charge un nouvel objet `options` dans la configuration JSON, permettant de contrôler le comportement général de la boîte de dialogue. Cela vous permet de définir directement les propriétés de la fenêtre dans la configuration de l'inspection, sans avoir besoin de passer d'arguments en ligne de commande.

```json
{
  "options": {
    "moveable": true,
    "ontop": true,
    "resizable": true,
    "windowbuttons": "min,max,close"
  }
}
```

**Options disponibles :**
- `moveable` (booléen) - Permettre de déplacer la fenêtre en la faisant glisser
- `ontop` (booléen) - Garder la fenêtre au-dessus de toutes les autres fenêtres
- `resizable` (booléen) - Autoriser le redimensionnement de la fenêtre (implique `moveable`).
- `windowbuttons` (chaîne de caractères) - Activer les boutons de la fenêtre : `close`, `min`, `max` (séparés par des virgules).

**Priorité :** Les options passées en ligne de commande ont priorité sur les options définies dans le fichier JSON.

**Options non prises en charge :** Toute option qui ne figure pas dans la liste autorisée est ignorée, et un message d'erreur est enregistré.

**Exemple :**
```json
{
  "title": "Application Installation",
  "options": {
    "moveable": true,
    "ontop": true
  },
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}
```

### Clés de niveau racine

| Clé | Type | Obligatoire | Par défaut | Description |
|-----|------|----------|---------|-------------|
| `preset` | Chaîne | Non | "preset1" | Disposition visuelle prédéfinie (preset1 à preset7). |
| `title` | Chaîne | Non | "Inspection du système" | Titre de la fenêtre |
| `message` | Chaîne | Non | - | Texte principal du message |
| `icon` | Chaîne | Non | - | Chemin d'accès à l'icône ou symbole SF (par exemple, "sf=shield.fill"). |
| `size` | Chaîne | Non | "standard" | Dimensions de la fenêtre : "compact", "standard", "large" |
| `width` | Entier | Non | - | Largeur de fenêtre personnalisée (remplace la taille définie). |
| `height` | Entier | Non | - | Hauteur de fenêtre personnalisée (remplace les dimensions prédéfinies). |
| `cachePaths` | Tableau | Non | - | Répertoires à surveiller pour les téléchargements |
| `scanInterval` | Entier | Non | 2 | Interval de numération du système de fichiers en secondes |
| `button1text` | Chaîne | Non | "OK" | Texte du bouton principal |
| `button1disabled` | Booléen | Non | false | Désactiver le bouton principal initialement |
| `button2text` | Chaîne | Non | "Cancel" | Texte du bouton secondaire |
| `button2visible` | Booléen | Non | true | Afficher le bouton secondaire |
| `autoEnableButton` | Booléen | Non | true | Bouton d'activation automatique une fois la tâche terminée |
| `autoEnableButtonText` | Chaîne | Non | "OK" | Texte du bouton lorsque l'activation automatique est activée |
| `items` | Tableau | Oui | - | Liste des éléments à vérifier |

### Clés de personnalisation visuelle

| Clé | Type | Par défaut | Description |
|-----|------|---------|-------------|
| `banner` | Chaîne | - | Chemin de l'image d'en-tête (remplace l'icône). |
| `bannerHeight` | Entier | 100 | Hauteur de la bannière en pixels |
| `bannerTitle` | Chaîne | - | Superposition du titre sur la bannière |
| `highlightColor` | Chaîne | "#808080" | Couleur d'accentuation (code hexadécimal). |
| `backgroundColor` | Chaîne | - | Couleur de fond (code hexadécimal). |
| `backgroundImage` | Chaîne | - | Chemin d'accès de l'image de fond |
| `backgroundOpacity` | Double | 1.0 | Opacité de fond (0 à 1). |
| `textOverlayColor` | Chaîne | - | Couleur de la superposition de texte pour les arrière-plans |
| `gradientColors` | Tableau | - | Tableau de codes hexadécimaux pour le dégradé |
| `iconBasePath` | Chaîne | - | Chemin de base pour les chemins relatifs des icônes |
| `appearance` | Chaîne | "auto" | Forcer l'affichage de la fenêtre d'inspection : `"dark"`, `"light"`, ou `"auto"` (en fonction du système d'exploitation). Cette option remplace le paramètre du système d'exploitation, dans les deux sens. |

### Configuration des éléments

Chaque élément du tableau `items` requiert :

| Clé | Type | Obligatoire | Description |
|-----|------|----------|-------------|
| `id` | Chaîne | Oui | Identifiant unique |
| `displayName` | Chaîne | Oui | Nom affiché dans l'interface utilisateur |
| `guiIndex` | Entier | Oui | Ordre de tri (à partir de 0). |
| `paths` | Tableau | Oui | Chemins d'accès aux fichiers à vérifier pour s'assurer de leur existence |
| `icon` | Chaîne | Non | Icône spécifique à l'élément |
| `plistKey` | Chaîne | Non | Clé PLIST pour la validation |
| `expectedValue` | Chaîne | Non | Valeur attendue dans le fichier plist |
| `evaluation` | Chaîne | Non | Type d'évaluation : "equals", "boolean", "exists", "contains", "range" |
| `description` | Chaîne | Non | Description facultative, affichée sous le titre de l'article (rendue par les paramètres 1, 2, 3, 5 et 6). |
<!-- | `subtitle` | String | No | Subtitle text (preset6) | --> <!-- | `category` | Chaîne de caractères | Non | Regroupement par catégorie (paramètre prédéfini 5) |
| `categoryIcon` | Chaîne | Non | Icône de catégorie (paramètre prédéfini 5). | -->


## Fonctionnalités avancées

### Surveillance du cache

Surveiller les répertoires de téléchargement pour détecter les installations en cours.

```json
{
  "cachePaths": [
    "/Library/Managed Installs/Cache",
    "/Library/Application Support/Installomator/Downloads",
    "/Library/Application Support/JAMF/Downloads", 
    "/Library/Application Support/AirWatch/Data/Munki/Managed Installs/Cache"
  ],
  "scanInterval": 5,
  "cacheExtensions": ["download", "pkg", "dmg", "aria2"]
}
```

Par défaut, les fichiers se terminant par `.pkg`, `.dmg` et `.download`, situés dans `cachePaths`, sont marqués comme étant en cours de *téléchargement*. Vous pouvez modifier cette liste en définissant `cacheExtensions` ; par exemple, vous pouvez ajouter `aria2` pour que les fichiers partiels de `<name>.aria2` (utilisés par aria2c) soient détectés (problème n° 617). Le point initial est facultatif.

### Validation de la conformité aux listes (Plist)

Valider la configuration du système à l'aide de vérifications basées sur les fichiers plist.

```json
{
  "preset": "preset5",
  "items": [{
    "id": "findmymac",
    "displayName": "Find My Mac Status",
    "guiIndex": 0,
    "paths": ["/Library/Preferences/com.apple.FindMyMac.plist"],
    "plistKey": "FMMEnabled",
    "expectedValue": "true",
    "evaluation": "boolean"
  }]
}
```

### Seuils de couleur personnalisés

Définir les niveaux de conformité personnalisés et les couleurs correspondantes.

```json
{
  "colorThresholds": {
    "excellent": 0.95,
    "good": 0.80,
    "warning": 0.60,
    "excellentColor": "#00C853",
    "goodColor": "#2196F3",
    "warningColor": "#FF9800",
    "criticalColor": "#F44336"
  }
}
```


### Tableaux de bord de conformité

Pour la génération de rapports de conformité basés sur des fichiers plist, ajoutez un tableau de niveau supérieur `plistSources`. swiftDialog regroupe les fichiers plist référencés en catégories, avec le nombre de succès et le nombre total, puis calcule un score global, avant de les afficher via les blocs de contenu `compliance-summary` et `findings-list` (et toutes les cellules "bento"), en les actualisant à intervalles réguliers.

```json
{
  "plistSources": [
    {
      "path": "/Library/Preferences/com.company.compliance.plist",
      "type": "compliance",
      "healthyLabel": "Compliant",
      "attentionLabel": "Action Required"
    }
  ],
  "guidance": [
    { "type": "compliance-summary" },
    { "type": "findings-list" }
  ]
}
```

**`plistSources[]` Propriétés :**

| Clé | Type | Par défaut | Description |
|-----|------|---------|-------------|
| `path` | Chaîne | - | Chemin vers le fichier plist |
| `type` | Chaîne | - | Type de source : `compliance`, `health`, `licenses`, `preferences` ou `custom` |
| `healthyLabel` | Chaîne | "Healthy" | Étiquette pour une vérification réussie <br> (apparaît dans les fiches récapitulatives, les lignes de résultats et les sous-titres des tableaux). |
| `attentionLabel` | Chaîne | "Needs Attention" | Étiquette indiquant un contrôle échoué |
| `successValues` | Tableau | - | Valeurs qui témoignent du succès |
| `expectedValue` | Chaîne | - | Valeur attendue en matière de conformité |
| `findingKey` | Chaîne | "finding" | Clé secondaire pour lire les détails du résultat |
| `timestampKey` | Chaîne | auto | Clé indiquant la date et l'heure de la dernière vérification (tentatives automatiques `lastComplianceCheck`, `LastUpdateCheck`, `lastCheck`, `timestamp`). |
| `includePattern` | Chaîne | - | Expression régulière des clés à inclure dans la découverte automatique |
| `excludeKeys` | Tableau | - | Clés à exclure de la découverte automatique |
| `keyMappings` | Tableau | - | Comment interpréter les clés spécifiques des fichiers plist |
| `maxCheckDetails` | Entier | 15 | Nombre maximal d'éléments affichés par catégorie |
| `icon` | Chaîne | - | Symbole SF pour la catégorie |

**Blocs de contenu qui affichent les données agrégées :**

- `compliance-summary` — une bannière affichant l'état général, ainsi que des tableaux de statistiques par catégorie.
- `findings-list` — Une liste de contrôles individuels, classés par catégorie, et dont le contenu est accessible.

Les cellules Bento se lient également automatiquement aux mêmes données : le sous-titre et la couleur de l'icône d'une cellule sont mis à jour en temps réel, sans nécessiter de champs de schéma supplémentaires. <br>

## Exemples complets

### Programme d'installation de base

```json
{
  "title": "Installing Office Suite",
  "message": "Please wait while we install your applications",
  "preset": "preset1",
  "icon": "sf=apps.iphone.badge.plus",
  "iconBasePath":"/Users/Shared/icons/",
  "cachePaths": ["/Users/Shared/Downloads"],
  "button1text": "Please Wait...",
  "button1disabled": true,
  "autoEnableButton": true,
  "autoEnableButtonText": "Continue",
  "items": [
    {
      "id": "microsoft_word",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"],
      "icon": "Microsoft Word.png"
    },
    {
      "id": "microsoft_excel",
      "displayName": "Microsoft Excel",
      "guiIndex": 1,
      "paths": ["/Applications/Microsoft Excel.app"],
      "icon": "Microsoft Excel.png"
    },
    {
      "id": "microsoft_powerpoint",
      "displayName": "Microsoft PowerPoint",
      "guiIndex": 2,
      "paths": ["/Applications/Microsoft PowerPoint.app"],
      "icon": "Microsoft PowerPoint.png"
    }
  ]
}
```
:::tip[chemin de base des icônes]
Définissez un chemin de base pour les icônes des éléments afin de simplifier la configuration. Les noms des images sont chargés à partir de `iconBasePath` lorsque cela est possible. Sinon, spécifiez le chemin complet pour un élément.
:::


## Dépannage

### Configuration non chargée
- Vérifiez la syntaxe du fichier JSON à l'aide de `jq` ou de validateurs en ligne
- Vérifiez les permissions du fichier (il doit être accessible en lecture).
- Assurez-vous que la variable d'environnement est correctement exportée

### Éléments non détectés
- Vérifiez les chemins d'accès exacts des fichiers (en respectant la casse).
- Vérifiez si les chemins d'accès nécessitent des privilèges d'administrateur
- Utilisez `cachePaths` pour la détection de téléchargement
- Augmentez la valeur `scanInterval` pour les systèmes moins performants

### Mode de débogage
Activer la sortie de débogage :
```bash
/usr/local/bin/dialog --inspect-mode --debug
```

```bash
export DIALOG_DEBUG=1
/usr/local/bin/dialog --inspect-mode
```

### Variables d'environnement courantes
- `DIALOG_INSPECT_CONFIG` : Chemin vers le fichier de configuration JSON
- `DIALOG_DEBUG`: Activer la journalisation de débogage
- `DIALOG_COMMAND_FILE` : Chemin d'accès au fichier de commandes personnalisé

## Meilleures pratiques

1. **Commencez simplement :** Utilisez `preset1` et une configuration minimale
2. **Chemins de test :** Vérifier que tous les chemins de fichiers existent ou seront créés
3. **Utilisez la surveillance du cache :** Ajoutez `cachePaths` pour la détection des téléchargements
4. **Gestion des icônes** : Stockez les icônes dans un emplacement centralisé avec `iconBasePath`
5. **États des boutons :** Utilisez `autoEnableButton` pour une meilleure expérience utilisateur
6. **Préréglages adaptés :** Sélectionnez les préréglages en fonction de l'utilisation prévue.
   - Suivi de l'installation : preset1, preset2 ou preset3
   - Affichage de la conformité : preset4


