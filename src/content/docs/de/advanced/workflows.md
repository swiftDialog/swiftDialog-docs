---
title: swiftDialog Workflow
description: Mehrstufige Dialogabläufe in swiftDialog
translationSynced: 2026-11-20T11:10:24+00:00
---

> **HINWEIS**: Die Workflow-Funktion wurde in swiftDialog Version 3.1 eingeführt.

# Dokumentation der Workflow-Funktionen von swiftDialog

## Übersicht

Die Funktion "**Workflow**" ermöglicht mehrstufige Dialogabläufe in swiftDialog, wodurch Sie Benutzeroberflächen erstellen können, die Benutzern bei der Navigation durch mehrere Bildschirme mit Eingabefeldern und Informationen helfen. Jede "Karte" repräsentiert einen separaten Bildschirm mit eigener Konfiguration, und Benutzer können innerhalb des Workflows vorwärts und rückwärts navigieren.

Die Arbeitsabläufe werden mithilfe von JSON-Konfigurationsdateien definiert, was die Erstellung komplexer, mehrstufiger Dialoge ohne Programmierung erleichtert.

## Wichtigste Merkmale

- **Mehrstufige Arbeitsabläufe:** Teilen Sie komplexe Dialoge in übersichtliche Schritte auf
- **Navigationssteuerelemente:** Automatische Schaltflächen für "Weiter", "Zurück" und "Fertig stellen"
- **Bedingte Verzweigung:** Leiten Sie den Workflow zu verschiedenen Aufgaben basierend auf der Auswahl in einem Dropdown-Menü oder dem Status eines Kontrollkästchens weiter, ohne dass ein separates Skript erforderlich ist
- **Datenkonsistenz:** Die vom Benutzer eingegebenen Daten bleiben erhalten, wenn zwischen den einzelnen Schritten des Arbeitsablaufs gewechselt wird
- **Globale Einstellungen:** Definieren Sie allgemeine Einstellungen einmalig und überschreiben Sie diese bei Bedarf für einzelne Karten
- **Variablenersetzung**: Referenzwerte aus vorherigen Workflow-Karten unter Verwendung der `{fieldname}`-Syntax
- **Validierung:** Pflichtfelder müssen vor dem Weitergehen validiert werden
- **Dynamische Konfiguration:** Jede Karte kann über individuelle Benutzeroberflächenelemente und Einstellungen verfügen
- **Callbacks:** Führen Sie Shell-Skripte aus, wenn Sie zwischen den einzelnen Schritten eines Arbeitsablaufs wechseln

## Grundlegende Konzepte

### Struktur des Arbeitsablaufs

Ein dialogorientierter Arbeitsablauf wird in einer JSON-Konfigurationsdatei mit folgender Struktur definiert:

```json
{
  "workflow": [
    { "title": "Step 1", "message": "First screen..." },
    { "title": "Step 2", "message": "Second screen..." },
    { "title": "Step 3", "message": "Final screen..." }
  ]
}
```

### Globale Konfiguration

Eigenschaften, die auf der obersten Ebene (außerhalb des `workflow`-Arrays) definiert sind, dienen als Standardwerte für alle Workflow-Karten. Einzelne Workflow-Karten können diese Standardwerte überschreiben:

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

### Kartenidentifikation

Die Karten werden automatisch in der Reihenfolge ihrer Position im Array sortiert. Sie können optional eine explizite `id`-Angabe machen, um eine benutzerdefinierte Sortierung vorzunehmen:

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

### Funktionsweise der Schaltflächen

Im Workflow-Modus ändert sich das Verhalten der Schaltfläche automatisch:

- **Schaltfläche 1** (rechte Seite):
  - Zeigt auf den Workflow-Karten 1 bis n-1 den Eintrag "Weiter"
  - Zeigt "Fertig" auf der letzten Karte (oder einen benutzerdefinierten Text über `button1text`).
  - Überprüft die Pflichtfelder, bevor fortgefahren wird
  
- **Schaltfläche 2** (linke Seite):
  - Versteckt auf der ersten Karte
  - Zeigt auf den Workflow-Karten 2 bis n die Beschriftung "Vorherige"
  - Keine Validierung bei Rückwärtsbewegung

### Anpassen des Schaltflächen-Textes

Standardmäßig zeigen die Navigationsschaltflächen die Beschriftungen "**Weiter**", "**Zurück**" und "**Fertig**" an. Sie können diese Beschriftungen überschreiben:

- `--nextbuttontext "<text>"` – Text für den "Weiter"-Schaltfläche (Standard: `Next`).
- `--previousbuttontext "<text>"` — Text für den "Zurück"-Schaltfläche (Standard: `Previous`).
- `button1text` (oberste Ebene oder pro Karte) – Text für den abschließenden **Fertigstellen**-Schaltfläche

```bash
dialog --jsonfile config.json --nextbuttontext "Continue" --previousbuttontext "Back"
```

### Navigationsablauf

<img width="650" alt="image" src="/images/navigation-flow.png" />


## Verzweigte Navigation

Standardmäßig werden die Workflow-Karten in der Reihenfolge eines Arrays angezeigt. Sie können dies mit drei optionalen Eigenschaften pro Karte ändern:

| Immobilie | Typ | Zweck |
|---|---|---|
| `branch` | Objekt | Wählen Sie die nächste Karte basierend auf einem Wert auf der aktuellen Karte |
| `nextpage` | Ganzzahl | Statische Überschreibung – Gehen Sie zu dieser Karte `id`, nachdem Sie "Weiter" geklickt haben |
| `finalpage` | boolesch/boolescher Wert | Diese Karte beendet den Arbeitsablauf; der nächste Schritt wird zu "Fertigstellen" |

Wenn der Benutzer auf "Weiter" klickt, löst swiftDialog das Ziel in folgender Reihenfolge:

1. `branch` (falls diese Option aktiviert ist und eine passende Regel gefunden wird)
2. `nextpage` (falls aktiviert)
3. Die nächste Karte in der Reihe
4. Ende des Arbeitsablaufs (wenn keine nächste Aufgabe vorhanden ist oder `finalpage` wahr ist).

Der "Zurück"-Schaltfläche berücksichtigt die Historie: Er navigiert zurück zur Karte, von der der Benutzer tatsächlich kam, und nicht einfach nur zum vorherigen Eintrag ("aktueller Index - 1"). Dies funktioniert korrekt auch bei Verzweigungen.

> swiftDialog überprüft nicht auf Schleifen oder unerreichbare Elemente. Wenn Ihr Workflow sich selbst wiederholen kann, wird der Benutzer einfach zu diesen Elementen zurückkehren. Überprüfen Sie in diesem Fall die Logik des Workflows, um sicherzustellen, dass dies nicht unbeabsichtigt geschieht.

### Verzweigung ausgehend von einer Auswahlliste

Der `branch.field`-Wert stimmt mit dem Wert des Feldes `name` (bevorzugt) oder mit seinem `title`/`label` überein. Bei einem Dropdown-Menü wird der ausgewählte Wert mit den Schlüsseln in `branch.map` verglichen:

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

`branch.default` ist optional. Wenn ein Wert eingestellt ist und dieser Wert nicht in `map` vorhanden ist, wird der Workflow zu der entsprechenden Ausweichkarte weitergeleitet.

### Verzweigung ausgehend von einer Kontrollkästchen-Option

Für ein einzelnes Boolesches Feld sollte die Kurzschreibweise `ifTrue` / `ifFalse` anstelle von `map` verwendet werden:

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

Sie können `map` auch mit den Schlüsseln `"true"` und `"false"` verwenden, wenn Sie dies bevorzugen, aber `ifTrue`/`ifFalse` ist verständlicher.

### Statische `nextpage` Überschreibung

Wenn Sie keine dynamische Routenführung benötigen, aber eine Karte verwenden möchten, um schneller voranzukommen, setzen Sie `nextpage`:

```json
{ "id": 3, "title": "Optional details", "nextpage": 10 }
```

### Frühzeitiges Beenden des Arbeitsablaufs

Markieren Sie eine Karte als "final", um den Arbeitsablauf dort zu beenden:

```json
{ "id": 99, "title": "Summary", "finalpage": true }
```

Auf der letzten Karte zeigt Schaltfläche 1 den Text "Fertig" an und schließt das Dialogfenster, wenn sie angeklickt wird, unabhängig davon, wie viele weitere Workflow-Karten sich noch im Array befinden.

## Anwendungsbeispiele

### Beispiel 1: Ein einfacher, dreistufiger Assistent

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

Führen Sie es aus:
```bash
dialog --jsonfile /path/to/config.json
```

### Beispiel 2: Verwendung von Variablensubstitution

Die Variablensubstitution ermöglicht es Ihnen, Werte aus vorherigen Workflow-Schritten mithilfe der `{fieldname}`-Syntax zu referenzieren:

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

Die Platzhalter `{First Name}` und `{Last Name}` in Karte 2 werden durch die Werte ersetzt, die in Karte 1 eingegeben wurden.

### Beispiel 3: Globale Standardeinstellungen mit Überschreibungen

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

### Beispiel 4: Datenerfassung in mehreren Schritten

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

### Beispiel 5: Fortschrittsbalken mit Karten

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

### Beispiel 6: Validierung von Pflichtfeldern

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

Wenn Benutzer versuchen, auf "Weiter" zu klicken, ohne die erforderlichen Felder auszufüllen, wird eine Fehlermeldung angezeigt.

## Erweiterte Funktionen

### Eigenschaften, die für bestimmte Arbeitsabläufe relevant sind

Jede Standardeigenschaft von swiftDialog kann in einem Workflow verwendet werden. Häufig verwendete Eigenschaften sind:

- **Layout**: `width`, `height`, `position`
- **Inhalt**: `title`, `message`, `icon`, `iconsize`
- **Eingabe**: `textfield`, `selectitems`, `checkbox`, `radio`
- **Anzeige**: `image`, `video`, `webcontent`, `listitem`
- **Fortschritt**: `progress`, `progresstext`
- **Information**: `infobox`, `helpmessage`
- **Gestaltung**: `messagefont`, `alignment`, `bannerimage`
- **Navigation**: `branch`, `nextpage`, `finalpage` (siehe [Verzweigte Navigation](#verzweigte-navigation)]).

### Benennung von Eingabefeldern

Damit die Variablensubstitution korrekt funktioniert, sollten die Eingabefelder eine konsistente Namensgebung aufweisen:

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

Wenn ein Feld keine explizite `title`-Angabe hat, können Sie eine `name`-Eigenschaft verwenden:

```json
{
  "textfield": [
    { "title": "Your Name", "name": "username" }  // Referenced as {username}
  ]
}
```

### Datenpersistenz

Die Benutzereingaben werden automatisch gespeichert, wenn:
- Klicken Sie auf "Weiter", um zur nächsten Karte zu gelangen
- Klicken Sie auf "Zurück", um zur vorherigen Seite zu gelangen

Wenn Benutzer zu einer vorherigen Ansicht zurückkehren, werden ihre Eingaben wiederhergestellt.

### Zugriff auf Kartendaten

Wenn der Benutzer auf "Fertigstellen" in der letzten Karte klickt, werden alle erfassten Eingaben im JSON-Format an die Standardausgabe (stdout) ausgegeben.

```json
{
  "First Name": "John",
  "Last Name": "Doe",
  "Email Address": "john.doe@example.com",
  "Department": "IT",
  "Enable notifications": true
}
```

### Rückrufe bezüglich Vorauszahlungen

Verwenden Sie die Option `--onadvance`, um einen Shell-Befehl auszuführen, wenn Sie zwischen den einzelnen Elementen des Arbeitsablaufs wechseln.

```bash
dialog --jsonfile config.json --onadvance "/path/to/script.sh"
```

Das Skript empfängt:
- Indexkarte (mit Null-basiertem Index).
- Kartennummer (falls angegeben)
- Aktuelle Kartendaten werden als JSON-Format über die Standardeingabe (stdin) empfangen

Das Skript sollte mit folgendem Ergebnis beendet werden:
- **Exit-Code 0:** Fortsetzung zulassen
- **Exit-Code ungleich Null:** Fortschritt stoppen und Fehlermeldung anzeigen

Beispiel für ein Callback-Skript:
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

## Bewährte Praktiken

### 1. Arbeitsabläufe fokussiert gestalten
Jede Karte sollte einen einzigen, klaren Zweck haben. Vermeiden Sie es, Benutzer mit zu vielen Feldern auf einer einzigen Karte zu überfordern.

### 2. Verwenden Sie aussagekräftige Titel
Die Titel der einzelnen Karten sollten klar anzeigen, in welchem Schritt sich der Benutzer befindet.
```json
{ "title": "Step 1: Personal Information" }
{ "title": "Step 2: Contact Details" }
{ "title": "Step 3: Review & Confirm" }
```

### 3. Kontext angeben
Verwenden Sie das Nachrichtenfeld, um zu erklären, was der Benutzer tun muss:
```json
{
  "title": "Account Setup",
  "message": "Create your account by choosing a username and password. Your username must be at least 6 characters."
}
```

### 4. Verwenden Sie die Pflichtfeldvalidierung
Markieren Sie die Pflichtfelder, um sicherzustellen, dass alle erforderlichen Daten vollständig erfasst werden.
```json
{ "title": "Email", "required": true }
```

### 5. Zusammenfassungskarten bereitstellen
Fügen Sie eine abschließende Zusammenfassungskarte bei, die alle gesammelten Informationen enthält:
```json
{
  "title": "Review Your Information",
  "message": "Please verify everything is correct before proceeding.",
  "infobox": "**Name:** {Full Name}\\n**Email:** {Email}\\n**Department:** {Department}"
}
```

### 6. Berücksichtigen Sie den Navigationsablauf
- Gestalten Sie die erste Seite so, dass sie keine umfangreichen Eingaben erfordert – führen Sie die Benutzer behutsam ein
- Führen Sie die wichtigsten Datenerfassungsmaßnahmen so früh wie möglich durch
- Speichern Sie die Bestätigung/Überprüfung für die endgültige Kreditkarte

### 7. Achten Sie auf ein konsistentes Layout
Definieren Sie globale Standardeinstellungen für ein einheitliches Erscheinungsbild:
```json
{
  "icon": "SF=person.crop.circle",
  "width": 700,
  "height": 450,
  "messagefont": "size=13",
  "workflow": [ /* ... */ ]
}
```

## Einschränkungen und Hinweise

1. **Aktualisierungen von Befehlsdateien:** Bei Verwendung des Workflow-Modus mit einer Befehlsdatei funktionieren möglicherweise nicht alle dynamischen Aktualisierungen wie erwartet. Das Workflow-Modus ist für die Datenerfassung konzipiert und nicht für dynamische Statusaktualisierungen.

2. **Anpassung der Schaltflächen:** Das Verhalten der Schaltfläche 1 und der Schaltfläche 2 wird durch den Workflow-Modus gesteuert und kann im Workflow-Modus nicht vollständig angepasst werden.

3. **Exit-Codes:** Im Workflow-Modus schließt sich das Dialogfenster nur dann, wenn:
   - Der Benutzer klickt auf "Fertigstellen" auf der letzten Karte (Exit-Code: 0).
   - Benutzer hat den Vorgang abgebrochen (der Rückgabewert variiert).
   - Die Validierung ist fehlgeschlagen, und der Benutzer entscheidet sich, den Vorgang abzubrechen

4. **Variablenbereich:** Variablen, die in vorherigen Workflow-Karten definiert wurden, stehen nur in nachfolgenden Karten zur Verfügung, nicht in früheren Workflow-Karten. Die Ersetzung von Variablen erfolgt nur in eine Richtung.

5. **Feldbezeichnungen:** Verwenden Sie für eine korrekte Variablensubstitution alphanumerische Zeichen und Leerzeichen in den Feldbezeichnungen. Sonderzeichen können zu Problemen führen.

## Fehlerbehebung

### Karten werden nicht angezeigt
- Überprüfen Sie die JSON-Syntax mit `jsonlint` oder einem ähnlichen Tool
- Stellen Sie sicher, dass das `workflow`-Array sich auf der obersten Ebene befindet
- Stellen Sie sicher, dass mindestens eine Karte definiert ist

### Variablen werden nicht ersetzt
- Stellen Sie sicher, dass die Feldnamen exakt übereinstimmen (Groß- und Kleinschreibung beachten).
- Stellen Sie sicher, dass Variablennamen geschweifte Klammern verwenden: `{fieldname}`
- Überprüfen Sie, ob das referenzierte Feld sich auf einer früheren Karte befand und nicht auf der aktuellen oder einer zukünftigen Karte

### Validierung funktioniert nicht
- Bestätigen Sie, dass die Einstellungen für die Felder korrekt sind. `"required": true`
- Überprüfen Sie, ob das Feld eine Eigenschaft mit dem Wert `title` oder `name` besitzt
- Überprüfen Sie die Debug-Protokolle mit dem `--debug`-Flag

### Vorherige Schaltfläche wird nicht angezeigt
- Bitte überprüfen Sie, ob Sie sich nicht auf der ersten Workflow-Karte befinden (die vorherige Karte ist auf der ersten Karte ausgeblendet).
- Überprüfen Sie, ob der Workflow-Modus tatsächlich aktiviert ist (d.h. ob ein Workflow-Array vorhanden ist).

### Die Filiale hat die falsche Karte verwendet
- Überprüfen Sie, ob der Wert `branch.field` mit dem Wert des Felds `name` übereinstimmt (oder mit dessen `title`/`label`, falls kein Name festgelegt wurde).
- Bei Auswahllisten werden die Schlüssel, die mit den Einträgen verknüpft sind, exakt mit dem vom Benutzer ausgewählten Wert verglichen – Groß- und Kleinschreibung sowie Leerzeichen sind dabei relevant
- Für Kontrollkästchen ist es vorzuziehen, die Schlüssel ``ifTrue``/``ifFalse`` anstelle von ``"true"``/``"false"`` zu verwenden
- Überprüfen Sie das swiftDialog-Protokoll – ungültige Ziele (targets) `nextpage` / `branch` werden beim Laden des Programms angezeigt

## Vollständiges Beispiel: Assistent für die Einarbeitung neuer Mitarbeiter

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

Speichern Sie dies als `onboarding.json` und führen Sie es aus:
```bash
dialog --jsonfile onboarding.json
```

## Integrationsbeispiel: Shell-Skript

Hier ist ein vollständiges Beispiel für ein Shell-Skript, das den Workflow-Modus verwendet und die Ausgabe verarbeitet:

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

## Zusammenfassung

Die Workflow-Funktion in swiftDialog bietet eine leistungsstarke Möglichkeit, mehrstufige, dialogorientierte Benutzeroberflächen mithilfe einer einfachen JSON-Konfiguration zu erstellen. Zu den wichtigsten Vorteilen gehören:

- **Vereinfachung komplexer Arbeitsabläufe** – Aufteilung komplizierter Prozesse in übersichtliche, handhabbare Schritte
- **Integrierte Navigation** – Automatische Schaltflächen für "Nächste", "Vorherige" und "Fertig"
- **Datenerfassung:** Erfassen und validieren Sie problemlos Benutzereingaben auf verschiedenen Bildschirmen
- **Flexible Konfiguration** – Nutzen Sie globale Standardeinstellungen und Workflow-spezifische Überschreibungen
- **Variablenersetzung** – Verweisen Sie in späteren Workflow-Schritten auf Werte, die in vorherigen Schritten festgelegt wurden
- **Keine Programmierkenntnisse erforderlich** – Definieren Sie alles in JSON

Für weitere Informationen zu den einzelnen Optionen und Parametern von swiftDialog, konsultieren Sie bitte die Hauptdokumentation von swiftDialog oder nutzen Sie `dialog --help`.
