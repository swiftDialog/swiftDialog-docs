---
title: Mitteilungen
description: Das Senden von Systemmitteilungen mit swiftDialog anstelle der Anzeige von Dialogfenstern
translationSynced: 2026-11-23T08:35:52+00:00
---

## Benachrichtigungen

swiftDialog ermöglicht es Ihnen, Benachrichtigungen zu versenden, indem Sie das Argument `--notification` verwenden. Dies gibt an, dass swiftDialog stattdessen eine Benachrichtigung senden soll, anstatt ein Dialogfenster anzuzeigen.

Benachrichtigungen verwenden die gleichen `--title`, `--message` und `--icon`-Parameter, um Text und Medien darzustellen. Alle anderen Parameter, die auf dieser Seite nicht aufgeführt sind, werden ignoriert.

Es gibt ein zusätzliches Argument `--subtitle`, das eine Untertitelzeile zur Benachrichtigung hinzufügt.

### Benachrichtigungsstile (Version 3.1 und höher).

Ab Version 3.1 leitet swiftDialog Benachrichtigungen über spezielle Hilfsprogramme weiter, die in `Dialog.app` integriert sind. Verwenden Sie das Argument `--style`, um den Benachrichtigungstyp auszuwählen:

| `--style` Wert | Verhalten | Verwendeter Helfer |
|---|---|---|
| `banner` | Systemmeldung, die kurz angezeigt wird und sich dann automatisch schließt | `Dialog Banner` |
| `alert` | Systemmeldung, die angezeigt wird, bis der Benutzer sie manuell entfernt | `Dialog Alert` |
| `pseudo` | Pseudo-Benachrichtigungsbanner (gleich wie `pseudo-banner`). | Hauptanwendung |
| `pseudo-banner` | Eine Pseudo-Benachrichtigung, die sich nach Ablauf einer Zeitspanne automatisch schließt | Hauptanwendung |
| `pseudo-alert` | Eine Pseudo-Benachrichtigung, die angezeigt wird, bis der Benutzer damit interagiert | Hauptanwendung |

Das Standardverhalten, wenn `--style` weggelassen wird, hängt von den für die App konfigurierten Systemeinstellungen ab.

> #### Legacy-Pfad (veraltet ab Version 3.1)
>
> Das Anrufen `--notification` **ohne** `--style` funktioniert weiterhin aus Gründen der Abwärtskompatibilität, wird aber über das Haupt-`Dialog.app`-Paket geleitet. Dieser Pfad ist veraltet und erzeugt eine Warnmeldung, die an die Standardfehlerausgabe (stderr) gesendet wird:
> In einer zukünftigen Version wird das Senden einer Benachrichtigung ohne `--style` standardmäßig zu `--style banner` führen.

Um sicherzustellen, dass die Formatierungsoptionen für Systembenachrichtigungen korrekt eingestellt sind, installieren Sie eine MobileConfig-Datei, die Benachrichtigungen für die entsprechenden Hilfsprogramme (`au.csiro.dialog.notifier.banner` und `au.csiro.dialog.notifier.alert`) mit der gewünschten Formatierung vorab genehmigt.

### Verwenden Sie

Das Senden einer einfachen Banner-Benachrichtigung:

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message"
```

Das Senden einer dauerhaften Benachrichtigung:

```bash
dialog --notification --style alert --title "Test Notification" --message "A test notification message"
```

![image](https://user-images.githubusercontent.com/3598965/201508706-be8fd3c5-5f06-434c-b97b-b773f6b96bdb.png)

Wenn die Nachricht länger ist als der Platz, den die Benachrichtigung bietet, wird die Nachricht gekürzt und es werden Auslassungspunkte `...` angezeigt, um dies zu kennzeichnen. Außerdem sollte ein Pfeil in der oberen rechten Ecke der Benachrichtigung erscheinen, wenn der Benutzer mit der Maus über die Benachrichtigung fährt, sodass der Benutzer den Inhalt erweitern kann

![Screenshot 2022-11-13 at 5:26 PM](https://user-images.githubusercontent.com/3598965/201508943-f382a961-9a8e-4bc6-98a3-67925d367005.png)

![Screenshot 2022-11-13 at 5:26 PM](https://user-images.githubusercontent.com/3598965/201509015-cc6591cc-5e66-4f9f-94bb-d9c0688460e9.png)

Eine Untertitel hinzufügen:

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message" --subtitle "Test Subtitle"
```

![image](https://user-images.githubusercontent.com/3598965/201508719-5f13f9fd-9507-4d6d-81c5-854d6ad4a79b.png)

Ein Benachrichtigungstext kann, einschließlich Titel und Untertitel, bis zu 5 Zeilen enthalten. Ein `\n`-Zeichen innerhalb des Textkörpers erzeugt einen Zeilenumbruch in der Benachrichtigung.

Ein Bild kann mit `--icon` hinzugefügt werden und unterstützt alle gängigen Bildformate und -quellen.

![image](https://user-images.githubusercontent.com/3598965/201508767-b091140f-d040-4c86-b16b-d25bcfac8606.png)

Beim Anzeigen eines Bildes kann der Benutzer den Inhalt der Benachrichtigung erweitern

![image](https://user-images.githubusercontent.com/3598965/201508803-29a1a02a-450f-4952-8991-9348dd754b38.png)

_Hinweis: Sie können das Standard-Icon, das mit der Benachrichtigung angezeigt wird, __nicht__ ersetzen. Bilder, die mit `--icon` hinzugefügt werden, werden innerhalb der Benachrichtigung angezeigt._

## Eine Aktion einrichten

Sie können eine Aktion festlegen, die ausgeführt wird, wenn der Benutzer auf die Benachrichtigung klickt. Dies kann eine URL oder ein Befehl für die Kommandozeile sein.

_HINWEIS: Benachrichtigungen werden vom Benutzer initiiert, und die daraufhin ausgeführten Aktionen erfolgen im Benutzerkontext._

Der grundlegende Verwendungszweck dieser Funktion ist:

```bash
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "open -a Safari.app"
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "https://swiftdialog.app/"
```

Sie können eine zusätzliche Aktion festlegen und die Beschriftungen der Schaltflächen definieren:

```bash
dialog --notification --style banner --title "<text>" --message "<text>" \
    --button1text "Do Something" --button1action "/do/something" \
    --button2text "Do Something Else" --button2action "/do/something/else/"
```

`--button1action` ist die Standardaktion, die ausgeführt wird, wenn entweder der Benachrichtigungstext oder Schaltfläche 1 angeklickt wird. `--button2action` wird nur ausgelöst, wenn Schaltfläche 2 angeklickt wird.

## Benachrichtigungs-Identifikatoren und deren Entfernung

Sie können einer Benachrichtigung mithilfe von `--identifier` einen persistenten Identifikator zuweisen. Dies ermöglicht es Ihnen, eine bestimmte Benachrichtigung später zu entfernen:

```bash
# Send a notification with an identifier
dialog --notification --style banner --title "Update Available" --message "Version 2.0 is ready" --identifier "update-available"

# Remove it later
dialog --notification --style banner --remove --identifier "update-available"
```

Das Aufrufen von `--remove` ohne `--identifier` löscht alle ausstehenden Benachrichtigungen von diesem Hilfsdienst.

Identifikatoren funktionieren auch mit Pseudo-Benachrichtigungen (siehe unten).

## Benachrichtigungstöne aktivieren

Verwenden Sie `--enablenotificationsounds`, um den Standard-Benachrichtigungston abzuspielen, wenn die Benachrichtigung empfangen wird:

```bash
dialog --notification --style alert --title "Alert" --message "Action required" --enablenotificationsounds
```

## Pseudo-Benachrichtigungen

"Pseudo-Benachrichtigungen" sind benutzerdefinierte Fenster im Stil von Benachrichtigungen, die von swiftDialog selbst erstellt werden und keine Systembenachrichtigungen von macOS sind. Sie erscheinen von der rechten Bildschirmkante und ahmen das Aussehen der nativen Benachrichtigungen mit einem transparenten Hintergrund nach.

### Warum sollte man Pseudo-Benachrichtigungen verwenden?

- **Unterstützung für benutzerdefinierte Icons** – Das Icon, das in der Benachrichtigung angezeigt wird, lässt sich vollständig anpassen, und zwar mithilfe von `--icon`, einschließlich SF Symbols, URLs, Dateipfaden und App-Bundles. Im Gegensatz zu Systembenachrichtigungen ist dafür nicht erforderlich, das Icon des Dialog.app-Bundles festzulegen und den NotificationCenter neu zu starten.
- **Kein MDM-Profil erforderlich** – Die simulierten Benachrichtigungen werden nicht über das macOS-Benachrichtigungszentrum angezeigt, daher sind weder eine MobileConfig-Datei noch spezielle Berechtigungen für Benachrichtigungen erforderlich.
- **Eingebettete Bilder** — Verwenden Sie `--image`, um ein Bild innerhalb des Benachrichtigungstexts anzuzeigen.
- **Inline-Formatierung mit Markdown** — Der `--message` Inhalt unterstützt die Inline-Formatierung mit Markdown.

### Was sind keine Pseudo-Benachrichtigungen?

"Pseudobenachrichtigungen" sind keine Systembenachrichtigungen. Sie bleiben nicht erhalten, nachdem sie geschlossen wurden, und folgen nicht den Standardregeln für macOS-Systembenachrichtigungen. Außerdem werden sie nicht übereinander gestapelt. Es können mehrere Pseudobenachrichtigungen gesendet werden, aber sie erscheinen übereinander, bis sie geschlossen werden. Wenn dies für Sie wichtig ist, verwenden Sie stattdessen reguläre Systembenachrichtigungen.



### Pseudonachricht-Designs

| `--style` Wert | Verhalten |
|---|---|
| `pseudo` | Wie `pseudo-banner` |
| `pseudo-banner` | Automatische Schließung nach 6 Sekunden (oder dem Wert von `--timer`). |
| `pseudo-alert` | Bleibt auf dem Bildschirm, bis der Benutzer darauf klickt oder es schließt |

### Grundlegende Nutzung

<img width="400" alt="image" src="/images/update-available.png" />

```bash
# Banner-style pseudo notification (auto-dismisses)
dialog --notification --style pseudo --title "Update Available" --message "Version 2.0 is ready to install"

# Alert-style pseudo notification (persistent)
dialog --notification --style pseudo-alert --title "Restart Required" --message "Please save your work and restart"
```

### Benutzerdefiniertes Icon und benutzerdefiniertes Bild

<img width="400" alt="image" src="/images/deployment-install-complete.png" />

```bash
dialog --notification --style pseudo --title "Deployment" --message "Software install complete" \
    --icon /System/Applications/App\ Store.app  \
    --image "/Applications/Keynote.app"
```

### Aktionsschaltflächen

Wenn `--button2text` oder `--button2action` angegeben ist, erscheint eine Aktionsleiste am unteren Rand der Benachrichtigung mit zwei Schaltflächen:

<img width="400" alt="image" src="/images/update-available-buttons.png" />

```bash
dialog --notification --style pseudo-alert --title "Update Available" \
    --message "macOS 26.4 is ready to install" \
    --button1text "Later" \
    --button2text "Install Now" --button2action "open 'x-apple.systempreferences:com.apple.Software-Update-Settings.extension'"
```

- Das Anklicken des Benachrichtigungsinhalts oder von **Schaltfläche 1** führt `--button1action` aus.
- Das Anklicken von **Schaltfläche 2** führt `--button2action` aus.
- Wenn weder `--button2text` noch `--button2action` angegeben sind, wird die Aktionsleiste ausgeblendet, und ein Klick an beliebiger Stelle auf der Benachrichtigung löst `--button1action` aus.

### Automatische Timer-Funktion zum automatischen Schließen

Für den Stil `pseudo-banner` wird die Benachrichtigung standardmäßig nach 6 Sekunden automatisch geschlossen. Verwenden Sie `--timer`, um eine benutzerdefinierte Dauer in Sekunden festzulegen:

```bash
# Auto-dismiss after 15 seconds
dialog --notification --style pseudo-banner --title "Reminder" --message "Meeting in 5 minutes" --timer 15
```

### Schließen-Schaltfläche

<img width="400" alt="image" src="/images/restart-hover-button.png" />

Wenn der Benutzer mit dem Mauszeiger über eine Pseudo-Benachrichtigung fährt, erscheint eine Schließen-Schaltfläche (×) in der oberen linken Ecke. Ein Klick darauf schließt die Benachrichtigung mit dem gleichen Verhalten wie bei einem Timeout (sie verschwindet, wird mit dem Code 0 beendet, es werden keine Aktionen ausgeführt).

### Echtzeit-Zeitstempel

Pseudo-Benachrichtigungen zeigen einen Zeitstempel mit der Angabe "jetzt" neben dem Titel an. Nach 60 Sekunden ändert sich dies zu "vor 1 Minute" und wird alle 60 Sekunden aktualisiert, solange die Benachrichtigung sichtbar bleibt.

### Kennzeichnungen und Entfernung

Pseudo-Benachrichtigungen unterstützen `--identifier` für gezielte Entfernung:

```bash
# Send a pseudo notification with an identifier
dialog --notification --style pseudo-alert --title "Updating" --message "Please wait..." --identifier "update-progress"

# Remove it when done
dialog --notification --style pseudo --remove --identifier "update-progress"

# Remove ALL visible pseudo notifications
dialog --notification --style pseudo --remove
```

Wenn eine neue Pseudo-Benachrichtigung mit derselben Kennung wie eine bereits vorhandene gesendet wird, wird die alte Benachrichtigung automatisch gelöscht, bevor die neue angezeigt wird.

### Benachrichtigungstöne

Verwenden Sie `--enablenotificationsounds`, um den Systemalarmton abzuspielen, wenn die Pseudo-Benachrichtigung erscheint:

```bash
dialog --notification --style pseudo --title "Alert" --message "Something happened" --enablenotificationsounds
```

## Genehmigung und Konfiguration des Benachrichtigungstyps über MDM

Beim ersten Mal, wenn Sie Benachrichtigungen verwenden, erhalten Sie möglicherweise keine Rückmeldung oder werden nicht aufgefordert, die Anzeige von Benachrichtigungen zu erlauben.

Um Benachrichtigungen manuell zu aktivieren, müssen Sie zu den Systemeinstellungen -> Benachrichtigungen gehen und die Benachrichtigungen für die jeweilige(n) Anwendung(en) aktivieren. Sie können auch zwischen den Optionen "Keine", "Banner" oder "Alarm" wählen.

Bei der Bereitstellung von swiftDialog über ein Mobile Device Management (MDM)-System wird empfohlen, eine Mobileconfig-Datei zu verwenden, die Benachrichtigungen im Voraus genehmigt und den Benachrichtigungstyp festlegt.

### Bundle-Kennungen

| Version | Bundle-Kennung | Anmerkungen |
|---|---|---|
| Version 2.2.1 und frühere Versionen | `au.bartreardon.dialog` | Erbe |
| v2.3 – v3.0 | `au.csiro.dialog` | Haupt-App-Paket |
| Version 3.1 oder höher (mit Banner-Design). | `au.csiro.dialog.notifier.banner` | `Dialog Banner` Helfer |
| Version 3.1 oder höher (mit Warnungsstil). | `au.csiro.dialog.notifier.alert` | `Dialog Alert` Helfer |

> Um die genauen Bundle-IDs einer installierten Version zu überprüfen, führen Sie folgenden Befehl aus:
> ```bash
> defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Banner.app/Contents/Info.plist" CFBundleIdentifier
> defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Alert.app/Contents/Info.plist" CFBundleIdentifier
> ```

Wenn Sie eine gemischte Installation haben, können Sie mehrere Bundle-Einträge in demselben Profil zusammenfassen. Ein Beispiel für eine Payload für Benachrichtigungen im Banner-Stil könnte wie folgt aussehen:

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

Bitte beachten Sie, dass der Schlüssel `AlertType` das Benachrichtigungsdesign unabhängig von `--style` steuert:
- `1` = Banner (wird automatisch geschlossen).
- `2` = Warnmeldung (bleibt aktiv, bis sie manuell geschlossen wird).

Bei der Bereitstellung mit `--style alert`, setzen Sie `AlertType` auf `2` im Eintrag `au.csiro.dialog.notifier.alert`, und umgekehrt für Banner.

 > #### Hinweise zu Fehlermeldungen bezüglich Benachrichtigungen
 >
 > Wenn Sie Folgendes erhalten:
 >
 > ```
 > Benachrichtigungen sind derzeit nicht verfügbar: Es konnte keine Verbindung zu einer Hilfesanwendung hergestellt werden
 > ```
 >
 > Überprüfen Sie, ob die entsprechende Dialog-Anwendung in den Systemeinstellungen Benachrichtigungen aktiviert hat, entweder durch die Anwendung einer der oben genannten .mobileconfig-Dateien über ein Mobile Device Management (MDM)-System oder manuell in den Systemeinstellungen.

## Aktualisierung des Standardsymbols für Benachrichtigungen

Benachrichtigungen verwenden standardmäßig das SwiftDialog-Icon. Wenn Sie das Erscheinungsbild ändern und ein anderes Icon verwenden möchten, beispielsweise ein unternehmensspezifisches Logo, können Sie die folgenden Schritte ausführen, um das App-Icon durch ein für Ihre Zwecke geeigneteres Icon zu ersetzen.

> #### Unterstützung ab macOS 26.4
>
> In macOS 26.4 funktioniert das Aktualisieren des App-Bundle-Icons und damit auch des Icons für Benachrichtigungen nicht mehr korrekt. Wenn die Markenidentität wichtig ist, verwenden Sie die neue, pseudo-Benachrichtigungsfunktion. Diese bietet eine ähnliche Benutzeroberfläche wie Systembenachrichtigungen, verwendet aber nicht das macOS-System für Benachrichtigungen und ist daher möglicherweise nicht für alle Situationen geeignet.

### Voraussetzungen

 - Neueste Version des swiftDialog-Pakets
 - Ein geeignetes Ersatzbild mit einer Auflösung von mindestens 512x512 Pixeln (bevorzugt 1024x1024 Pixel).

 <img src="https://user-images.githubusercontent.com/3598965/201548460-042b057f-3174-407e-ae42-0916c0a57cee.png" width="500" />

 - #### Ein Bild erzeugen

   Sie können ein Bild aus der Self-Service-Anwendung Ihrer MDM-Anbieter mit dem Befehl `sips` generieren. Zum Beispiel:

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

### Schritte

  1. Kopieren Sie das Bild Ihres neuen Icons in den Ordner `/Library/Application Support/Dialog/Dialog.png` (Achtung: Groß- und Kleinschreibung ist wichtig).
  2. Installieren Sie swiftDialog mit dem `.pkg` Installationsprogramm.

Nachdem die Ersetzung `Dialog.png` durchgeführt wurde, ersetzt das Installationsprogramm das standardmäßige Icon durch das angegebene Bild. Benachrichtigungen verwenden dann dieses benutzerdefinierte Bild als Icon.

 ![Screenshot 2022-11-14 at 9:55 am](https://user-images.githubusercontent.com/3598965/201548926-669bc9e0-8257-4bb1-ac1f-0e23ff82f378.png)
