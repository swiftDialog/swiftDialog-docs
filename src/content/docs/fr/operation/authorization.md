---
title: Autorisation
description: Configurer les clés d'autorisation pour contrôler l'accès à swiftDialog
translationSynced: 2026-11-23T05:25:01+00:00
---

## Autorisation 🔐

Dans la version 2.3 et suivantes, swiftDialog peut rechercher une clé d'autorisation, et si elle est présente, elle sera nécessaire pour exécuter le programme

La clé d'autorisation est un moyen de prévenir l'utilisation non autorisée de swiftDialog. La chaîne de caractères sera hachée à l'aide de l'algorithme SHA256 et comparée à la valeur stockée

****

### 🚨 Avertissement

 > L'utilisation de la clé d'autorisation et la manière dont elle est sécurisée ne relèvent pas de la responsabilité de swiftDialog. Il est important de prendre en compte le flux de travail et le moment et l'endroit où la clé d'autorisation est utilisée, car elle risque d'apparaître en texte clair à un moment donné, et un attaquant déterminé pourrait la découvrir
 >
 >_Cette fonctionnalité est nouvelle dans la version 2.3 et est conçue pour dissuader les utilisations abusives de swiftDialog, et non comme une solution préventive complète._

****

### Comment ça fonctionne

swiftDialog vérifiera le `au.csiro.dialog` domaine pour le nom de la clé `AuthorisationKey`. La valeur de la clé doit être un hachage SHA256 d'une phrase secrète. Si cette valeur est présente, elle doit correspondre à la valeur attendue, sinon swiftDialog ne démarrera pas.

Par exemple, si la phrase secrète à utiliser est `password`, alors enregistrez le hachage SHA256 de cette phrase dans le domaine `au.csiro.dialog` :

      "AuthorisationKey" = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

Ouvrir la fenêtre de dialogue et spécifier la phrase secrète :

      dialogue --clé "mot de passe"

Alternativement, vous pouvez définir une variable d'environnement `DIALOG_AUTH_KEY` dans votre environnement ou au début de votre script, puis la supprimer une fois que vous avez terminé, plutôt que de passer la valeur comme argument à chaque fois.

    export DIALOG_AUTH_KEY="password"

    ... traitement automatisé ici...

    Supprimer la variable DIALOG_AUTH_KEY

Si la clé correcte n'est pas spécifiée, la boîte de dialogue se fermera avec le code de sortie `30`

Lorsque l'autorisation est accordée avec succès, swiftDialog s'exécutera et une petite icône de cadenas apparaîtra en haut à droite, indiquant une session de dialogue autorisée.

<img src="https://github.com/bartreardon/swiftDialog/assets/3598965/4026888f-0183-4c5e-be8c-9fb137b0faf2" width="500">


L'argument `--checksum <YourSecretString>` est un moyen pratique de générer le hachage requis pour une chaîne de caractères spécifique. Vous pouvez obtenir le même résultat avec :

    echo -n "Mon mot de passe secret" | shasum -a 256

Assurez-vous d'utiliser `echo -n` si vous utilisez cette méthode. L'utilisation de `echo` inclura un saut de ligne dans la sortie, et la somme de contrôle sera différente de ce que vous attendez

Il existe plusieurs façons de ranger une clé pour pouvoir l'utiliser facilement. Un bon point de départ pourrait être https://scriptingosx.com/2021/04/get-password-from-keychain-in-shell-scripts/

## Exemple d'utilisation

Il existe plusieurs façons de garantir la sécurité de vos scripts. Voici un exemple :

Générer un code secret aléatoire et une somme de contrôle
```bash
secret=$(uuidgen); checksum=$(echo -n "$secret" | shasum -a 256 | awk '{print $1}'); echo "secret = ${secret}"  && echo "checksum = ${checksum}"
```

La sortie doit ressembler à ceci...

```bash
secret = 85F1C8B0-406E-4F8C-8B76-0C9C4AC6A42D
checksum = 557fce8c82dcf62cf04b233a2534912c083900b7ba84364b5991ff6111181cb8
```

Vérifier la somme de contrôle par rapport à swiftdialog

```bash
if [[ "${checksum}" == "$(dialog --checksum ${secret})" ]]; then echo "Success"; else echo "checksum failed"; fi
```

Ceci permet de vérifier que la somme de contrôle générée sera validée par swiftDialog. Si tout se passe bien, créez un profil de configuration pour `au.csiro.dialog` avec `AuthorisationKey = ${checksum}`, puis déployez-le.

Pour la logique de votre script, créez une variable à partir d'un argument transmis (grâce à [Installomator](https://github.com/Installomator/Installomator/blob/471f8b44170ef32699c6bffe587a29b89c5f7e8c/fragments/main.sh#L9)]).

```bash
# read script arguments:
while [[ -n $1 ]]; do
    if [[ $1 =~ ".*\=.*" ]]; then
        # if an argument contains an = character, send it to eval
        eval $1
    fi
    # shift to next argument
    shift 1
done
```

Lors de l'appel du script, créez la variable d'environnement en tant qu'argument plutôt que de stocker la valeur en texte clair directement dans le script

```bash
dialog_script.sh DIALOG_AUTH_KEY="<secret-here>"
```

Vous pouvez ensuite appeler la fonction `swiftDialog` autant de fois que nécessaire dans votre script, et elle effectuera les validations correspondantes `DIALOG_AUTH_KEY`