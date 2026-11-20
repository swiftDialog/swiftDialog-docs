---
title: Autorisierung
description: Einrichten von Autorisierungsschlüsseln zur Steuerung des Zugriffs auf swiftDialog
translationSynced: 2026-11-20T09:52:49+00:00
---

## Autorisierung 🔐

In Version 2.3 und neuer kann swiftDialog nach einem Autorisierungsschlüssel suchen. Ist ein solcher Schlüssel vorhanden, muss swiftDialog ihn verwenden, um starten zu können.

Der Autorisierungsschlüssel dient dazu, eine unbefugte Nutzung von swiftDialog zu verhindern. Der Zeichenkettenwert wird mit SHA256 gehasht und mit dem gespeicherten Wert verglichen

****

### 🚨 Haftungsausschluss

 > Die Verwendung des Autorisierungsschlüssels und dessen Sicherheit sind nicht die Verantwortung von swiftDialog. Es sollte berücksichtigt werden, wie der Arbeitsablauf gestaltet ist und wann und wo der Autorisierungsschlüssel verwendet wird, da er wahrscheinlich irgendwann in Klartext vorliegen wird und ein entschlossener Angreifer ihn möglicherweise entdecken könnte
 >
 >_Diese Funktion ist in Version 2.3 neu eingeführt und dient dazu, einen Missbrauch von swiftDialog zu verhindern, und zwar nicht als umfassende Schutzlösung._

****

### Wie es funktioniert

swiftDialog überprüft die `au.csiro.dialog`-Domäne auf den Schlüsselnamen `AuthorisationKey`. Der Wert des Schlüssels sollte ein SHA256-Hash einer geheimen Schlüsselphrase sein. Wenn dieser Wert vorhanden ist, muss er übereinstimmen, andernfalls wird swiftDialog nicht gestartet.

Zum Beispiel: Wenn die geheime Phrase, die verwendet werden soll, `password` lautet, dann speichern Sie den SHA256-Hash dieser Phrase im `au.csiro.dialog`-Bereich:

      "AuthorisationKey" = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

Starten Sie den Dialog und geben Sie die geheime Phrase an:

      dialog --key "password"

Alternativ können Sie eine Umgebungsvariable `DIALOG_AUTH_KEY` in Ihrer Umgebung oder am Anfang Ihres Skripts setzen und diese anschließend wieder löschen, anstatt den Wert jedes Mal als Argument zu übergeben:

    export DIALOG_AUTH_KEY="password"

    ... hier folgt ein skriptgesteuerter Verarbeitungsschritt ...

    unset DIALOG_AUTH_KEY

Wenn der korrekte Schlüssel nicht angegeben wird, wird das Dialogfenster mit dem Exit-Code `30` beendet

Wenn die Autorisierung erfolgreich ist, wird swiftDialog gestartet und ein kleines Schloss-Symbol erscheint in der oberen rechten Ecke, das eine autorisierte Dialogsitzung anzeigt.

<img src="https://github.com/bartreardon/swiftDialog/assets/3598965/4026888f-0183-4c5e-be8c-9fb137b0faf2" width="500">


Das `--checksum <YourSecretString>`-Argument ist eine praktische Möglichkeit, den benötigten Hash-Wert für eine bestimmte Zeichenkette zu erzeugen. Das Gleiche kann man auch mit folgendem erreichen:

    echo -n "My Secret Passphrase" | shasum -a 256

Achten Sie darauf, `echo -n` zu verwenden, wenn Sie diese Methode nutzen. Die Verwendung von `echo` führt zu einem Zeilenumbruch in der Ausgabe, und die Prüfsumme wird anders ausfallen als erwartet

Es gibt verschiedene Möglichkeiten, einen Schlüssel so zu verstauen, dass er leicht zugänglich ist. Ein guter Ausgangspunkt könnte sein: https://scriptingosx.com/2021/04/get-password-from-keychain-in-shell-scripts/

## Beispielhafte Anwendung

Es gibt verschiedene Möglichkeiten, um sicherzustellen, dass Ihre Skripte erfolgreich sind. Dies ist nur ein Beispiel:

Generieren Sie einen zufälligen geheimen Schlüssel und eine Prüfsumme
```bash
secret=$(uuidgen); checksum=$(echo -n "$secret" | shasum -a 256 | awk '{print $1}'); echo "secret = ${secret}"  && echo "checksum = ${checksum}"
```

Das Ergebnis sollte in etwa so aussehen...

```bash
secret = 85F1C8B0-406E-4F8C-8B76-0C9C4AC6A42D
checksum = 557fce8c82dcf62cf04b233a2534912c083900b7ba84364b5991ff6111181cb8
```

Überprüfen Sie die Prüfsumme anhand von SwiftDialog

```bash
if [[ "${checksum}" == "$(dialog --checksum ${secret})" ]]; then echo "Success"; else echo "checksum failed"; fi
```

Dies bestätigt, dass die generierte Prüfsumme von swiftDialog validiert wird. Wenn alles in Ordnung ist, erstellen Sie ein Konfigurationsprofil für `au.csiro.dialog` mit `AuthorisationKey = ${checksum}` und setzen Sie es bereit.

Für die Logik Ihres Skripts erstellen Sie eine Variable aus einem übergebenen Argument (mit freundlicher Genehmigung von [Installomator](https://github.com/Installomator/Installomator/blob/471f8b44170ef32699c6bffe587a29b89c5f7e8c/fragments/main.sh#L9)).

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

Beim Aufrufen des Skripts sollte die Umgebungsvariable als Argument übergeben werden, anstatt den Wert im Klartext innerhalb des Skripts zu speichern

```bash
dialog_script.sh DIALOG_AUTH_KEY="<secret-here>"
```

Sie können dann `swiftDialog` so oft wie nötig in Ihrem Skript aufrufen, und es wird die Validierung gemäß `DIALOG_AUTH_KEY` durchführen