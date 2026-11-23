---
title: Fenêtre de connexion
description: Exécution des boîtes de dialogue swiftDialog dans le contexte de la fenêtre de connexion macOS
translationSynced: 2026-11-23T05:27:00+00:00
---

## Prise en charge de la fenêtre de connexion (à partir de la version 2.5.0).

`--loginwindow`

Dans swiftDialog 2.5, vous pouvez afficher des boîtes de dialogue dans la fenêtre de connexion.

Les dialogues standards sont pris en charge, avec ou sans `--blurscreen`

## Exigences

Pour fonctionner dans le contexte de la fenêtre de connexion, vous devrez configurer les éléments suivants :

 - Un script qui lance swiftDialog avec la configuration que vous souhaitez
   - Inclure l'argument `--loginwindow`
 - Un agent de lancement

### Configuration des agents de lancement

#### Configuration manuelle

Voici un exemple de LaunchAgent de base :

```xml
<plist version="1.0">
<dict>
	<key>OnDemand</key>
	<false/>
	<key>LaunchOnlyOnce</key>
	<true/>
	<key>ProgramArguments</key>
	<array>
		<string>/path/to/script.sh</string>
	</array>
	<key>LimitLoadToSessionType</key>
	<string>LoginWindow</string>
	<key>Label</key>
	<string>com.swiftDialog.example-login-window</string>
</dict>
</plist>
```

Nommez ce fichier de manière appropriée, par exemple `com.swiftDialog.example-login-window.plist`, et installez-le dans `/Library/LaunchAgents/`

#### Utilisation de Outset

L'outil open source Macadmins [Outset](https://github.com/macadmins/outset/) offre des fonctionnalités permettant d'exécuter des éléments à l'ouverture de session.

En plus de simplifier le processus, vous avez également accès à des paramètres qui empêchent un utilisateur de désactiver les éléments de connexion. Consultez le [wiki d'Outset](https://github.com/macadmins/outset/wiki/Deployment#login-items-management)] pour plus de détails.

Placez votre script dans le répertoire `/usr/local/outset/login-window/`, en définissant les permissions à `root:root` `0755` (`-rwxr-xr-x`). L'outil outset gérera le lancement du script lorsque la fenêtre de connexion apparaît.

### Considérations

Vous devrez tenir compte de ce qui se passe après l'exécution du script. Si vous ne souhaitez pas que ce script s'exécute à chaque fois que la fenêtre de connexion s'affiche, vous devrez inclure des conditions dans votre script pour qu'il n'effectue aucune action, ou qu'il se désinstalle lorsqu'il n'est plus nécessaire.

### Exemple de cas d'utilisation

#### Politique d'utilisation acceptable

Voici un exemple de dialogue de politique d'utilisation acceptable qui nécessite la validation d'une case à cocher et qui inclut du contenu provenant d'un fichier Markdown (exemple : [AcceptableUsePolicy.md](https://github.com/user-attachments/files/15521093/AcceptableUsePolicy.md)) et qui est affiché en `--eula` mode. Il serait affiché à chaque fois que la fenêtre de connexion est présentée.

```bash
dialog --message "/path/to/AcceptableUsePolicy.md" --height 50% --width 35% --style centred --icon sf=rectangle.and.pencil.and.ellipsis,colour=accent --title "{COMPANY-NAME} Acceptable Use" --button1disabled --checkbox "I Agree",enableButton1 --quitkey A --eula --blurscreen --loginwindow
```
<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/4139ae63-f420-439f-8aaa-152f8fcc91b9" width=500px>