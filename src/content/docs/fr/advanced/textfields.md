---
title: Champs de texte
description: Création de champs de saisie de texte avec différentes propriétés et mécanismes de validation
translationSynced: 2026-11-23T03:46:08+00:00
---

L'option `--textfield` vous permet de spécifier une zone où l'utilisateur peut saisir du texte avant de fermer la boîte de dialogue

Elle prend un paramètre en entrée, sous forme de texte, et utilise ce paramètre comme étiquette pour le champ de texte, à la fois dans l'interface de dialogue et dans les rapports

Les résultats sont envoyés vers la sortie standard (stdout) lorsque le programme swiftDialog se termine, et ils sont présentés dans le format suivant :

`<textfield text> : <user input>`

ou, si vous utilisez l'option `--json` pour activer la sortie au format JSON :

```json
{
"<textfield text>" : "<user input>"
}
```

## Exemples

Si vous utilisez le dialogue suivant :

`dialog --textfield "Textfield 1"`

Affichera la boîte de dialogue suivante :

![image](https://user-images.githubusercontent.com/3598965/235908715-5f24a167-5ad1-4f81-aa7e-30faf5590b1c.png)

L'utilisateur saisit une réponse :

![image](https://user-images.githubusercontent.com/3598965/235908865-40b37eac-874b-4ceb-a4e7-e8701ebdf790.png)

ce qui donnera le résultat suivant :

`Textfield 1 : This is what the user entered`

ou lors de l'utilisation de `--json`

```json
{
"Textfield 1" : "This is what the user entered"
}
```

## Champs de texte supplémentaires

Il est possible de spécifier plusieurs champs de texte en ajoutant des options `--textfield` supplémentaires lors de l'appel de swiftDialog

e.g. `dialog --textfield "Textfield 1" --textfield "Textfield 2"`

![image](https://user-images.githubusercontent.com/3598965/235909015-2c4f187b-a86d-4281-84ff-09afa6b87857.png)

Vous pouvez spécifier autant de champs de texte que nécessaire. Chaque champ de texte sera affiché comme un champ distinct dans le résultat.

Vous devrez peut-être ajuster la taille `--height` de votre boîte de dialogue si vous ajoutez plusieurs champs de texte, afin qu'ils tiennent correctement

Exemple :

`dialog --textfield "First Name" --textfield "Surname" --textfield "Age" --textfield "Favourite Colour"`

Cela produit le résultat suivant :

```
First Name : Joe
Surname : Bloggs
Age : 32
Favourite Colour : Red
```

`--json`
```json
{
"First Name" : "Joe",
"Surname" : "Bloggs",
"Age" : "32",
"Favourite Colour" : "Red"
}
```

## Modificateurs de champ de texte

Les modificateurs sont ajoutés à l'étiquette du champ de texte sous forme de valeurs séparées par des virgules :

```sh
--textfield "<label>,<modifier>,<modifier>=<value>"
```

| Modifier | Description |
|---|---|
| `name=<text>` | Utilisez cette valeur comme clé de sortie au lieu de l'étiquette |
| `required` | Le champ doit être rempli avant que la fenêtre swiftDialog ne se ferme |
| `secure` | Masquer la saisie au fur et à mesure qu'elle est effectuée (champ de mot de passe). |
| `passwordfill` | Activer la fonction de saisie automatique des mots de passe macOS pour un champ `secure` |
| `prompt="<text>"` | Texte d'exemple affiché à l'intérieur du champ (ce texte ne sera pas inclus dans la sortie). |
| `value="<text>"` | Remplir le champ avec une valeur par défaut (modificable). |
| `regex=<pattern>` | Exiger que le contenu du champ corresponde à l'expression régulière |
| `regexerror=<text>` | Message d'erreur personnalisé affiché lorsque l'expression régulière n'est pas satisfaite |
| `editor` | Éditeur de texte multi-lignes au lieu d'un simple champ de saisie |
| `isdate` | Remplacez le champ de texte par un sélecteur de date. La sortie est formatée sous forme de chaîne de date courte. |
| `fileselect` | Ajoutez un bouton "Sélectionner" qui ouvre une fenêtre de sélection de fichier |
| `filetype=<types>` | Restreindre la sélection de fichiers aux types spécifiés (séparés par des espaces). Utiliser les extensions de fichier (par exemple, `png jpg`) ou les mots-clés de type `folder`, `image`, `movie`, `video`, `audio`. |
| `path=<path>` | Définir le répertoire initial pour la fenêtre de sélection de fichiers |
| `confirm` | Ajoutez un champ de confirmation dont le contenu doit correspondre au champ principal |

### Nom

`name=<text>` remplace l'étiquette par la clé dans la sortie. Cela est utile lorsque vous souhaitez utiliser une étiquette conviviale, mais que vous préférez un nom de clé plus clair dans la sortie.

### Sécurisé

`secure` Masque la saisie au fur et à mesure qu'elle est effectuée, et affiche une icône de cadenas. Le contenu est toujours renvoyé sous forme de texte brut vers la sortie standard.

```sh
--textfield "Password,secure"
```

![image](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

### Remplissage automatique des mots de passe

`passwordfill` Permet l'activation de la fonction de remplissage automatique des mots de passe sur macOS. Doit être utilisé en combinaison avec `secure`.

```sh
--textfield "Password,secure,passwordfill"
```

### Obligatoire

`required` Cela empêche la fenêtre swiftDialog de se fermer tant que le champ ne contient pas de valeur. Les champs obligatoires sont marqués d'un `*` et sont mis en évidence lorsque l'utilisateur tente de fermer la fenêtre sans les avoir remplis.

```sh
--textfield "Full Name,required"
```

![image](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)

### Invite

`prompt="<text>"` affiche un texte d'exemple à l'intérieur du champ. Ce texte disparaît dès que l'utilisateur commence à taper et n'est pas inclus dans le résultat. Cette fonctionnalité n'est pas prise en charge pour les champs `secure`.

```sh
--textfield "Name,prompt="Enter your full name""
```

![image](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

### Valeur

`value="<text>"` Ce champ est pré-rempli avec une valeur par défaut que l'utilisateur peut modifier.

```sh
--textfield "Default Value Test",value="Some default value"
```

![image](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

### Expressions régulières et erreurs liées aux expressions régulières

`regex=<pattern>` Exige que le contenu du champ corresponde à l'expression régulière avant que la boîte de dialogue ne se ferme. `regexerror=<text>` Définit le message qui s'affiche lorsque le modèle ne correspond pas.

À moins que le modèle ne le permette explicitement, un champ `regex` ne peut pas être vide.

```sh
--textfield "Product Code",prompt="Enter 5 digit code",regex="\d{5}",regexerror="Must be a five digit number"
```

![image](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

Utilisez `--textfieldlivevalidation` pour afficher un affichage superposé en vert ou en rouge sur le champ, au fur et à mesure que l'utilisateur tape, afin de fournir un retour immédiat sur le fait que l'expression régulière est respectée ou non.

### Éditeur

`editor` affiche une zone de texte plus grande, qui s'étend sur plusieurs lignes, au lieu d'un simple champ à une seule ligne.

```sh
--textfield "Notes,editor"
```

![image](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

### Sélecteur de date

Utilisez le modificateur `date` ou `time` pour remplacer le champ de texte par un sélecteur de date et d'heure macOS. La valeur sélectionnée est renvoyée sous forme de chaîne de caractères formatée.

```sh
--textfield "Start Date,date"
--textfield "Start Time,time"
--textfield "Start Date and Time,date,time"
```

Note : Le modificateur `isdate` a été déprécié au profit de `date` et `time`.

#### Période de validité

Utilisez `mindate=` et `maxdate=` pour limiter la plage de dates sélectionnable :

```sh
--textfield "Pick a day,date,mindate=20260901,maxdate=20260930"
--textfield "No earlier than today,date,mindate=20260928"
--textfield "Before end of year,date,maxdate=20261231"
```

**Format :** Les dates doivent être au format `YYYYMMDD` (format indépendant de la région). Les séparateurs sont acceptés et supprimés (par exemple, `2026-09-30` → `20260930`). Les dates invalides sont ignorées et la contrainte n'est pas appliquée.

#### Format de date

Utilisez `format=` pour spécifier le format de la réponse en utilisant la syntaxe de `strftime` :

```sh
--textfield "Select date,date,format=+%Y-%m-%d"
--textfield "Get epoch,date,value=20260901,format=+%s"
```

Formats de chaînes de caractères courants :
- `+%Y-%m-%d` - Format ISO 8601 (par exemple : `2026-09-29`).
- `+%s` - Timestamp Unix (secondes depuis l'époque).
- `+%x` - Représentation de la date dans Locale
- `+%D` - Format américain (par exemple, `09/29/26`).

#### Initialisation du sélecteur de date

Utilisez `value=` pour définir la date de début. Le sélecteur accepte plusieurs formats :

```sh
--textfield "Start date,date,value=2026-09-30"
--textfield "Start date,date,value=September 30, 2026"
--textfield "Start date,date,value=1759132800"
```

Formats pris en charge : ISO 8601, formats spécifiques à la locale, formats 12/24 heures, horodatages depuis l'époque (epoch), et langage naturel.

### Sélection de fichier

`fileselect` ajoute un bouton **Sélectionner** qui ouvre une fenêtre de sélection de fichier standard. Le chemin sélectionné est placé dans le champ et renvoyé dans la sortie.

```sh
--textfield "Config File,fileselect"
```

Utilisez `filetype` pour limiter les options de sélection. Les valeurs sont séparées par des espaces et peuvent être des extensions de fichiers ou des mots-clés indiquant le type :

| Valeur | Sélections |
|---|---|
| `folder` | Uniquement des répertoires |
| `image` | Tout type d'image |
| `movie` / `video` | Tout type de vidéo |
| `audio` | Tout type de fichier audio |
| `<extension>` | Fichiers correspondant à cette extension (par exemple, `png`, `pdf`). |

```sh
--textfield "Select an image,fileselect,filetype=png jpg"
--textfield "Select a folder,fileselect,filetype=folder"
```

Utilisez `path=<path>` pour définir le répertoire qui s'ouvre lorsque la boîte de dialogue de sélection de fichier est affichée :

```sh
--textfield "Log File,fileselect,path=/var/log"
```

![image](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

### Confirmation

`confirm` ajoute un deuxième champ en dessous du champ principal. Les deux champs doivent contenir la même valeur avant que swiftDialog n'accepte la saisie. Ceci est utile pour la confirmation de mot de passe.

```sh
--textfield "Password,secure,required,confirm"
```

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### Combiner les modificateurs

Les modificateurs peuvent être combinés librement (lorsqu'ils sont compatibles) :

```sh
--textfield "<label>,secure,required,prompt="<prompt_text>""
--textfield "<label>,required,regex="\d{5}",regexerror="Five digits required",prompt="00000""
--textfield "<label>,fileselect,filetype="jpeg jpg png",path=/Users/Shared"
```

### Format JSON

Les champs de texte peuvent être définis au format JSON de deux manières :

#### Configuration JSON complète

Lorsqu'on utilise un fichier de configuration JSON ou `--jsonstring`/`--jsonfile`, il faut spécifier les champs de texte sous forme de tableau :

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "date" : true, "mindate" : "20260901", "maxdate" : "20260930", "format" : "+%Y-%m-%d"},
    {"title" : "<label>", "time" : true, "value" : "14:30"},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

#### Configuration JSON par argument

À partir de la version 3.1.1, les champs de texte peuvent également être spécifiés sous forme d'objets JSON via `--textfield` (au lieu d'utiliser des modificateurs séparés par des virgules). Cela offre un contrôle plus direct et est particulièrement utile pour les configurations complexes.

**Syntaxe :**
```bash
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'
```

**Caractéristiques :**
- `title` - Le texte de l'étiquette du champ
- `name` - Nom alternatif de la clé de sortie
- `required` - Ce champ doit être rempli (true/false).
- `secure` - Masquer la saisie au fur et à mesure qu'elle est effectuée (champ de mot de passe).
- `passwordfill` - Activer la fonction de remplissage automatique des mots de passe macOS (nécessite `secure`).
- `prompt` - Texte d'exemple affiché à l'intérieur du champ
- `value` - Remplir automatiquement le champ avec une valeur par défaut
- `regex` - Exiger que le contenu du champ corresponde à l'expression régulière
- `regexerror` - Message d'erreur personnalisé affiché lorsque l'expression régulière n'est pas satisfaite
- `editor` - Éditeur de texte multi-lignes au lieu d'un simple champ de saisie
- `date` - Remplacer le champ par un sélecteur de date (true).
- `time` - Remplacer le champ par un sélecteur de date et d'heure (true).
- `mindate` - Date de début minimale sélectionnable (format YYYYMMDD).
- `maxdate` - Date maximale sélectionnable (format YYYYMMDD).
- `format` - Format de sortie utilisant la syntaxe strftime (par exemple, `+%Y-%m-%d`, `+%s`).
- `fileselect` - Ajoutez un bouton "Sélectionner" qui ouvre une fenêtre de sélection de fichier
- `filetype` - Limiter la sélection de fichiers à des types spécifiques (extensions ou mots-clés séparés par des espaces).
- `path` - Répertoire initial pour la sélection de fichiers
- `confirm` - Ajoutez un champ de confirmation qui doit correspondre au champ principal

**Exemples :**

```bash
# Basic required field with prompt
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'

# Secure field with password fill
dialog --textfield '{"title":"Password","secure":true,"passwordfill":true,"prompt":"Enter password"}'

# Date picker with bounds
dialog --textfield '{"title":"Select Date","date":true,"mindate":"20260901","maxdate":"20260930","format":"+%Y-%m-%d"}'

# Time picker with default value
dialog --textfield '{"title":"Select Time","time":true,"value":"14:30"}'

# File picker with restrictions
dialog --textfield '{"title":"Select Config","fileselect":true,"filetype":"json plist","path":"/Library/Preferences"}'

# Multi-line editor
dialog --textfield '{"title":"Notes","editor":true}'

# Regex validation
dialog --textfield '{"title":"Product Code","prompt":"Enter 5 digit code","regex":"\\d{5}","regexerror":"Must be a five digit number"}'

# Confirmation field
dialog --textfield '{"title":"Password","secure":true,"required":true,"confirm":true}'
```

**Champs de sélection de date :**
- Utilisez `"date": true` ou `"time": true` (ou les deux) pour créer un sélecteur
- `"mindate"` et `"maxdate"` acceptent les dates au format `YYYYMMDD` (les séparateurs sont supprimés).
- `"format"` définit le format de sortie en utilisant la syntaxe de `strftime`
- `"value"` Permet de définir la date et l'heure de départ dans plusieurs formats (ISO, format local, époque, langage naturel).

**Tous les modificateurs sont pris en charge :** Chaque modificateur disponible au format CSV est également accessible sous forme de clé JSON.

**Plusieurs champs de texte :**

```bash
dialog --textfield '{"title":"First Name","required":true}' \
       --textfield '{"title":"Last Name","required":true}' \
       --textfield '{"title":"Email","regex":".+@.+\\..+","prompt":"user@example.com"}'
```

**Note :** Lorsque vous utilisez le format JSON par argument, chaque `--textfield` est indépendant. Le format JSON de configuration globale est toujours pris en charge pour l'initialisation par lots.

## Comportement du clavier

Appuyer sur la touche **Return** dans n'importe quel champ de texte à une seule ligne déclenche l'action du bouton 1, ce qui équivaut à cliquer sur le bouton par défaut. Cela ne s'applique pas aux `editor` champs.