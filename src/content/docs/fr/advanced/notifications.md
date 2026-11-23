---
title: Notifications
description: Envoyer des notifications système avec swiftDialog au lieu d'afficher des fenêtres de dialogue
translationSynced: 2026-11-23T04:05:16+00:00
---

## Notifications

swiftDialog vous permet d'envoyer des notifications en utilisant l'argument `--notification`. Cela indique à swiftDialog d'envoyer une notification au lieu d'afficher une boîte de dialogue.

Les notifications utilisent les mêmes arguments `--title`, `--message` et `--icon` pour afficher le texte et les éléments multimédias. Tous les autres arguments qui ne sont pas répertoriés sur cette page sont ignorés.

Il existe un argument supplémentaire `--subtitle` qui permet d'ajouter un sous-titre à la notification.

### Styles de notification (version 3.1 et suivantes).

À partir de la version 3.1, swiftDialog transmet les notifications via des applications auxiliaires spécifiques intégrées à `Dialog.app`. Utilisez l'argument `--style` pour sélectionner le type de notification :

| `--style` valeur | Comportement | Application auxiliaire |
|---|---|---|
| `banner` | Notification système qui apparaît brièvement, puis disparaît automatiquement | `Dialog Banner` |
| `alert` | Notification système qui reste affichée jusqu'à ce que l'utilisateur la ferme | `Dialog Alert` |
| `pseudo` | Bannière de notification simulée (identique à `pseudo-banner`). | Application principale |
| `pseudo-banner` | Notification temporaire qui disparaît automatiquement après un certain délai | Application principale |
| `pseudo-alert` | Notification temporaire qui reste affichée jusqu'à ce que l'utilisateur interagisse avec elle | Application principale |

Le comportement par défaut lorsque `--style` est omis dépend des paramètres de notification du système configurés pour l'application.

> #### Chemin d'accès obsolète (déprécié dans la version 3.1)
>
> Appeler `--notification` **sans** `--style` fonctionne toujours pour assurer la compatibilité ascendante, mais le trafic est acheminé via le groupe principal `Dialog.app`. Ce chemin est obsolète et générera un avertissement sur la sortie d'erreur standard :
> Dans une prochaine version, l'envoi d'une notification sans [`--style`] se fera par défaut par [`--style banner`].

Pour garantir que les types de style soient correctement configurés pour les notifications système, déployez un fichier de configuration mobile (mobileconfig) qui pré-approuve les notifications pour les applications auxiliaires concernées (`au.csiro.dialog.notifier.banner` et `au.csiro.dialog.notifier.alert`) et qui définit le style de notification souhaité.

### Utiliser

Envoyer une notification de bannière simple :

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message"
```

Envoyer une notification d'alerte persistante :

```bash
dialog --notification --style alert --title "Test Notification" --message "A test notification message"
```

![image](https://user-images.githubusercontent.com/3598965/201508706-be8fd3c5-5f06-434c-b97b-b773f6b96bdb.png)

Si le message est plus long que ce que la notification peut afficher, le message sera tronqué et des points de suspension `...` seront ajoutés pour indiquer cela. De plus, une petite flèche doit apparaître en haut à droite de la notification lorsque l'utilisateur passe le curseur de la souris sur celle-ci, ce qui permet à l'utilisateur d'afficher le contenu complet

![Screenshot 2022-11-13 at 5 26 10 pm](https://user-images.githubusercontent.com/3598965/201508943-f382a961-9a8e-4bc6-98a3-67925d367005.png)

![Capture d'écran du 13 novembre 2022 à 17h26](https://user-images.githubusercontent.com/3598965/201509015-cc6591cc-5e66-4f9f-94bb-d9c0688460e9.png)

Ajouter un sous-titre :

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message" --subtitle "Test Subtitle"
```

![image](https://user-images.githubusercontent.com/3598965/201508719-5f13f9fd-9507-4d6d-81c5-854d6ad4a79b.png)

Un message, y compris le titre et le sous-titre, peut contenir jusqu'à 5 lignes de texte. Un caractère `\n` placé dans le corps du message crée un saut de ligne dans la notification.

Une image peut être ajoutée en utilisant `--icon`, et elle accepte tous les formats et sources d'images existants.

![image](https://user-images.githubusercontent.com/3598965/201508767-b091140f-d040-4c86-b16b-d25bcfac8606.png)

Lors de l'affichage d'une image, le contenu de la notification peut être développé par l'utilisateur

![image](https://user-images.githubusercontent.com/3598965/201508803-29a1a02a-450f-4952-8991-9348dd754b38.png)

_Remarque : Vous __ne pouvez pas__ remplacer l'icône par défaut qui s'affiche avec la notification. Les images ajoutées en utilisant `--icon` apparaîtront dans la notification._

## Définir une action

Vous pouvez définir une action à exécuter lorsque l'utilisateur clique sur la notification. Cette action peut être une URL ou une commande système.

_NOTE : Les notifications sont déclenchées par l'utilisateur, et par conséquent, les actions effectuées par la notification sont exécutées dans le contexte de l'utilisateur._

L'utilisation de base de cette fonctionnalité est la suivante :

```bash
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "open -a Safari.app"
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "https://swiftdialog.app/"
```

Vous pouvez spécifier une action supplémentaire et définir les libellés des boutons :

```bash
dialog --notification --style banner --title "<text>" --message "<text>" \
    --button1text "Do Something" --button1action "/do/something" \
    --button2text "Do Something Else" --button2action "/do/something/else/"
```

`--button1action` est l'action par défaut qui s'exécute lorsqu'on clique sur le corps de la notification ou sur le bouton 1. `--button2action` ne s'active que lorsque l'on clique sur le bouton 2.

## Identifiants des notifications et suppression

Vous pouvez attribuer un identifiant permanent à une notification en utilisant `--identifier`. Cela vous permet de supprimer une notification spécifique ultérieurement :

```bash
# Send a notification with an identifier
dialog --notification --style banner --title "Update Available" --message "Version 2.0 is ready" --identifier "update-available"

# Remove it later
dialog --notification --style banner --remove --identifier "update-available"
```

Appeler `--remove` sans `--identifier` supprime toutes les notifications en attente de cet assistant.

Les identifiants fonctionnent également avec les notifications simulées (voir ci-dessous).

## Activer les sons de notification

Utilisez `--enablenotificationsounds` pour activer le son de notification par défaut lorsque la notification est reçue :

```bash
dialog --notification --style alert --title "Alert" --message "Action required" --enablenotificationsounds
```

## Notifications simulées

Les notifications simulées sont des fenêtres de type notification créées directement par swiftDialog, et non par le système macOS. Elles apparaissent en glissant depuis le bord droit de l'écran et imitent l'apparence des notifications natives, avec un fond translucide.

### Pourquoi utiliser des notifications simulées ?

- **Prise en charge des icônes personnalisées** — L'icône affichée dans la notification est entièrement personnalisable grâce à `--icon`, incluant les symboles SF, les URL, les chemins de fichiers et les bundles d'applications. Contrairement aux notifications système, cela ne nécessite pas de définir l'icône du bundle Dialog.app et de redémarrer NotificationCenter.
- **Aucun profil MDM requis** — Les notifications simulées ne passent pas par le centre de notifications de macOS, ce qui signifie qu'aucun fichier de configuration mobile (mobileconfig) ni aucune autorisation de notification n'est nécessaire.
- **Images intégrées** — Utilisez `--image` pour afficher une image dans le corps de la notification.
- **Markdown intégré** — Le `--message` contenu prend en charge la mise en forme Markdown intégrée.

### Qu'est-ce qu'une notification simulée n'est pas ?

Les notifications simulées ne sont pas des notifications système. Elles disparaissent une fois qu'elles sont masquées et ne suivent pas les règles standard des notifications système de macOS. De plus, elles ne s'empilent pas. Plusieurs notifications "pseudo" peuvent être envoyées, mais elles s'afficheront les unes au-dessus des autres jusqu'à ce qu'elles soient masquées. Si cela est important pour vous, utilisez les notifications système classiques.



### Styles de notifications simulées

| `--style` valeur | Comportement |
|---|---|
| `pseudo` | Identique à `pseudo-banner` |
| `pseudo-banner` | Se ferme automatiquement après 6 secondes (ou la valeur de `--timer`). |
| `pseudo-alert` | Elle reste affichée à l'écran jusqu'à ce que l'utilisateur clique dessus ou la ferme |

### Utilisation de base

<img width="400" alt="image" src="/images/update-available.png" />

```bash
# Banner-style pseudo notification (auto-dismisses)
dialog --notification --style pseudo --title "Update Available" --message "Version 2.0 is ready to install"

# Alert-style pseudo notification (persistent)
dialog --notification --style pseudo-alert --title "Restart Required" --message "Please save your work and restart"
```

### Icône et image personnalisées

<img width="400" alt="image" src="/images/deployment-install-complete.png" />

```bash
dialog --notification --style pseudo --title "Deployment" --message "Software install complete" \
    --icon /System/Applications/App\ Store.app  \
    --image "/Applications/Keynote.app"
```

### Boutons d'action

Lorsque `--button2text` ou `--button2action` est spécifié, une barre d'actions apparaît en bas de la notification, avec deux boutons :

<img width="400" alt="image" src="/images/update-available-buttons.png" />

```bash
dialog --notification --style pseudo-alert --title "Update Available" \
    --message "macOS 26.4 is ready to install" \
    --button1text "Later" \
    --button2text "Install Now" --button2action "open 'x-apple.systempreferences:com.apple.Software-Update-Settings.extension'"
```

- Cliquer sur le corps de la notification ou sur le **bouton 1** exécute `--button1action`.
- Cliquer sur le **bouton 2** exécute `--button2action`.
- Si ni `--button2text` ni `--button2action` ne sont spécifiés, la barre d'actions est masquée, et cliquer n'importe où sur la notification déclenche `--button1action`.

### Minuteur de désactivation automatique

Pour le style `pseudo-banner`, la notification disparaît automatiquement après 6 secondes par défaut. Utilisez `--timer` pour définir une durée personnalisée en secondes :

```bash
# Auto-dismiss after 15 seconds
dialog --notification --style pseudo-banner --title "Reminder" --message "Meeting in 5 minutes" --timer 15
```

### Bouton de fermeture

<img width="400" alt="image" src="/images/restart-hover-button.png" />

Lorsqu'un utilisateur survole une notification simulée, un bouton de fermeture (×) apparaît dans le coin supérieur gauche. En cliquant sur ce bouton, la notification disparaît de la même manière qu'en cas de dépassement de délai : elle se fait glisser vers le bas, se ferme avec le code 0, et aucune action de bouton n'est exécutée.

### Horodatage en direct

Les notifications simulées affichent un horodatage indiquant "maintenant" à côté du titre. Après 60 secondes, ce texte change pour indiquer "il y a 1 minute" et se met à jour toutes les 60 secondes tant que la notification reste visible.

### Identifiants et suppression

Les notifications simulées permettent de cibler précisément les éléments à supprimer `--identifier`.

```bash
# Send a pseudo notification with an identifier
dialog --notification --style pseudo-alert --title "Updating" --message "Please wait..." --identifier "update-progress"

# Remove it when done
dialog --notification --style pseudo --remove --identifier "update-progress"

# Remove ALL visible pseudo notifications
dialog --notification --style pseudo --remove
```

Lorsqu'une nouvelle notification avec le même identifiant qu'une notification existante est envoyée, l'ancienne notification est automatiquement supprimée avant que la nouvelle n'apparaisse.

### Sons de notification

Utilisez `--enablenotificationsounds` pour déclencher le son d'alerte du système lorsque la notification apparaît :

```bash
dialog --notification --style pseudo --title "Alert" --message "Something happened" --enablenotificationsounds
```

## Approbation et configuration du type de notification via MDM

Lors de votre première utilisation des notifications, il se peut que vous ne receviez aucun message et que vous ne soyez pas invité à autoriser les notifications.

Pour autoriser manuellement les notifications, vous devez accéder aux paramètres du système, puis à la section "Notifications", et activer les notifications pour l'application ou les applications concernées. Vous pouvez également choisir entre les options "Aucune", "Bannière" ou "Alerte" pour le type de notification.

Lors du déploiement de swiftDialog via une solution de gestion des appareils mobiles (MDM), il est préférable de déployer un fichier de configuration mobile (.mobileconfig) qui pré-approuve les notifications et définit le type de notification.

### Identifiants de paquets

| Version | Identifiant du paquet | Notes : |
|---|---|---|
| Versions 2.2.1 et antérieures | `au.bartreardon.dialog` | Héritage |
| v2.3 – v3.0 | `au.csiro.dialog` | Paquet d'application principal |
| Version 3.1 et suivantes (style de bannière). | `au.csiro.dialog.notifier.banner` | `Dialog Banner` assistant |
| Version 3.1 et suivantes (style d'alerte). | `au.csiro.dialog.notifier.alert` | `Dialog Alert` assistant |

> Pour vérifier les identifiants de paquet exacts d'une version installée, exécutez la commande suivante :
> ```bash
> defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Banner.app/Contents/Info.plist" CFBundleIdentifier
> defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Alert.app/Contents/Info.plist" CFBundleIdentifier
> ```

Si vous avez une installation combinée, vous pouvez inclure plusieurs entrées de groupe dans le même profil. Un exemple de charge utile pour les notifications de type bannière pourrait ressembler à ceci :

```xml
<key>PayloadContent</key>
<array>
    <dict>
        <key>PayloadDisplayName</key>
        <string>Notifications Payload</string>
        <key>PayloadIdentifier</key>
        <string>449B1259-E631-4051-ADCE-9532B813ADDC</string>
        <key>PayloadOrganization</key>
        <string>Org Name</string>
        <key>PayloadType</key>
        <string>com.apple.notificationsettings</string>
        <key>PayloadUUID</key>
        <string>12EA8FDA-B204-4AD0-802C-C980615F0BA5</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>NotificationSettings</key>
        <array>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.bartreardon.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.banner</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>2</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.alert</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
        </array>
    </dict>
</array>
```

Notez que la clé `AlertType` contrôle le style de notification indépendamment de la clé `--style` :
- `1` = Bannière (se ferme automatiquement).
- `2` = Alerte (reste affichée jusqu'à ce qu'elle soit supprimée).

Lors du déploiement avec `--style alert`, définissez `AlertType` sur `2` dans l'entrée `au.csiro.dialog.notifier.alert`, et inversement pour les bannières.

 > #### Une remarque concernant les erreurs de notification
 >
 > Si vous recevez ce qui suit :
 >
 > ```
 > Les notifications ne sont pas disponibles : impossible de communiquer avec une application auxiliaire
 > ```
 >
 > Vérifiez que l'application swiftDialog concernée a les notifications activées dans les paramètres du système, soit en appliquant l'un des fichiers de configuration mobile mentionnés ci-dessus via un système de gestion des appareils mobiles (MDM), soit manuellement dans les paramètres du système.

## Mettre à jour l'icône de notification par défaut

Les notifications utiliseront l'icône par défaut de swiftDialog. Si vous souhaitez personnaliser l'application en utilisant une icône différente, par exemple une icône correspondant à l'identité visuelle de votre entreprise, vous pouvez suivre les étapes suivantes pour modifier l'icône du paquet de l'application et la remplacer par une icône plus appropriée.

> #### Compatibilité avec macOS à partir de la version 26.4
>
> Dans macOS 26.4, la mise à jour de l'icône du paquet d'application, et donc de l'icône de notification, ne fonctionne plus correctement. Si l'identité visuelle est importante, utilisez la nouvelle fonctionnalité de notification "pseudo", qui présente une interface utilisateur similaire aux notifications système, mais qui n'utilise pas le système de notifications de macOS. Par conséquent, elle peut ne pas être appropriée dans toutes les situations.

### Prérequis

 - Dernière version du paquet swiftDialog
 - Une image de remplacement appropriée, d'une résolution minimale de 512x512 (1024x1024 de préférence).

 <img src="https://user-images.githubusercontent.com/3598965/201548460-042b057f-3174-407e-ae42-0916c0a57cee.png" width="500" />

 - #### Générer une image

   Vous pouvez générer une image à partir de l'application d'auto-service de vos fournisseurs de solutions de gestion des appareils mobiles (MDM) en utilisant la commande `sips`. Par exemple :

    ##### Kandji

    ```bash
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sips -s format png /Applications/Kandji\ Self\ Service.app/Contents/Resources/AppIcon.icns --out /Library/Application\ Support/Dialog/Dialog.png
    ```

    ##### Jamf

    ```bash
    temp_file=$(/usr/bin/mktemp)
    /usr/bin/xxd -p -s 260 "$(defaults read /Library/Preferences/com.jamfsoftware.jamf self_service_app_path)"/Icon$'\r'/..namedfork/rsrc | /usr/bin/xxd -r -p > "$temp_file"
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sudo /usr/bin/sips -s format png "$temp_file" --out /Library/Application\ Support/Dialog/Dialog.png
    ```

### Étapes

  1. Copiez l'image de l'icône de remplacement dans le dossier `/Library/Application Support/Dialog/Dialog.png` (respectez la casse).
  2. Installez swiftDialog à partir du programme d'installation .pkg.

Une fois le fichier de remplacement `Dialog.png` mis en place, le programme d'installation remplacera l'icône intégrée par l'image spécifiée. Les notifications utiliseront alors cette image personnalisée comme icône.

 ![Screenshot 2022-11-14 at 9 55 20 am](https://user-images.githubusercontent.com/3598965/201548926-669bc9e0-8257-4bb1-ac1f-0e23ff82f378.png)
