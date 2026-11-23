---
title: Inspektionsmodus
description: Einführungsanleitung zur Inspektionsfunktion von swiftDialog – Überwachung von Installationen und Systemkonformität
translationSynced: 2026-11-23T08:35:52+00:00
---


# swiftDialog Inspektionsmodus

Der SwiftDialog Inspect-Modus ist eine neue, integrierte Funktion, die eine Echtzeitüberwachung innerhalb des macOS-Dateisystems ermöglicht. Er verfolgt den Status des Dateisystems (unter Verwendung der Apple FSEvents API) und überwacht gleichzeitig Softwareinstallationen sowie Cache-Ordner, -Dateien und .plist-Inhalte, um Compliance-Prüfungen zu visualisieren. Diese Funktion ist speziell für den Einsatz während der Geräteanmeldung, der Softwarebereitstellung und der Compliance-Prüfung konzipiert und bietet Endbenutzern eine klare Übersicht über ihren Compliance-Status.

## Überblick

Der Inspektionsmodus überwacht kontinuierlich die angegebenen Dateipfade und Cache-Verzeichnisse, um den Status von Anwendungen oder Systemkomponenten zu verfolgen. Er bietet visuelles Feedback durch verschiedene vordefinierte Ansichten, die jeweils für unterschiedliche Anwendungsfälle optimiert sind.


### Wichtigste Merkmale
- Echtzeit-Überwachung des Dateisystems
- Download-Fortschrittserkennung durch Überwachung des Caches
- Verschiedene visuelle Voreinstellungen für unterschiedliche Anwendungsfälle
- Einfache Validierung auf Basis einer Liste (für boolesche Werte, Zeichenketten und Existenzprüfungen).
- Anpassbare Designs und Branding (eingeschränkte Möglichkeiten).
- Automatische Aktivierung von Schaltflächen nach Abschluss

## Erste Schritte

### Grundlegende Verwendung

1. Erstellen Sie eine JSON-Konfigurationsdatei:
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
:::tip[order of items]
Wichtig: `guiIndex` muss eindeutig sein und bestimmt die Reihenfolge der Elemente in der grafischen Benutzeroberfläche. Kleinere Zahlen werden zuerst angezeigt.
:::

2. Starten Sie swiftDialog mit dem Überprüfungsmodus:
```bash
/usr/local/bin/dialog --inspect-mode --inspect-config /path/to/config.json
```

3. Optional: Legen Sie den Umgebungsvariablen-Pfad für die Konfigurationsdatei fest:
```bash
export DIALOG_INSPECT_CONFIG="/path/to/config.json"
/usr/local/bin/dialog --inspect-mode
```

## JSON-Konfigurationsreferenz

### Allgemeine Dialogoptionen

Der Inspektionsmodus unterstützt ein neues `options`-Objekt in der JSON-Konfiguration, mit dem das allgemeine Verhalten des Dialogs gesteuert werden kann. Dies ermöglicht es, Fensterattribute direkt in der Inspektionskonfiguration festzulegen, ohne dass Befehlszeilenargumente übergeben werden müssen.

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

**Verfügbare Optionen:**
- `moveable` (boolesch) - Ermöglicht das Verschieben des Fensters
- `ontop` (boolesch) - Das Fenster immer oberhalb aller anderen Fenster halten
- `resizable` (boolesch) – Ermöglicht das Ändern der Größe des Fensters (impliziert `moveable`).
- `windowbuttons` (String) – Fenster-Schaltflächen aktivieren: `close`, `min`, `max` (durch Kommas getrennt).

**Priorität:** Befehlszeilenparameter haben Vorrang vor JSON-Optionen.

**Nicht unterstützte Optionen:** Alle Optionen, die nicht in der Zulassungsliste enthalten sind, werden ignoriert und eine entsprechende Meldung wird protokolliert.

**Beispiel:**
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

### Schlüssel auf oberster Ebene

| Schlüssel | Typ | Erforderlich | Standardeinstellung | Beschreibung |
|-----|------|----------|---------|-------------|
| `preset` | Zeichenkette | Nein | "Voreinstellung 1" | Visuelle Anordnung (Voreinstellung 1-7). |
| `title` | Zeichenkette | Nein | "Systemprüfung" oder "Systeminspektion" | Fenstertitel |
| `message` | Zeichenkette | Nein | - | Haupttext der Meldung |
| `icon` | Zeichenkette | Nein | - | Pfad zum Icon oder SF-Symbol (z.B. "sf=schild.fill"). |
| `size` | Zeichenkette | Nein | "Standard" | Fenstergröße: "kompakt", "Standard", "groß" |
| `width` | Ganzzahl | Nein | - | Benutzerdefinierte Fensterbreite (überschreibt die voreingestellte Größe). |
| `height` | Ganzzahl | Nein | - | Benutzerdefinierte Fensterhöhe (ersetzt die voreingestellte Größe). |
| `cachePaths` | Array | Nein | - | Verzeichnisse, die auf Downloads überwacht werden sollen |
| `scanInterval` | Ganzzahl | Nein | 2 | Intervall für den Dateisystem-Scan in Sekunden |
| `button1text` | Zeichenkette | Nein | "OK" | Text für den Haupt-Schaltfläche |
| `button1disabled` | Boolesche Algebra | Nein | falsch | Deaktivieren Sie den Haupt-Schaltfläche zunächst |
| `button2text` | Zeichenkette | Nein | "Abbrechen" | Text für den sekundäre Schaltfläche |
| `button2visible` | Boolesche Algebra | Nein | wahr | Zeigen Sie den sekundäre Schaltfläche |
| `autoEnableButton` | Boolesche Algebra | Nein | wahr | Automatische Aktivierungsschaltfläche nach Abschluss |
| `autoEnableButtonText` | Zeichenkette | Nein | "OK" | Text für die Schaltfläche, wenn die automatische Aktivierung aktiviert ist |
| `items` | Array | Ja | - | Anzeige der zu prüfenden Elemente |

### Visuelle Anpassungseinstellungen

| Schlüssel | Typ | Standardeinstellung | Beschreibung |
|-----|------|---------|-------------|
| `banner` | Zeichenkette | - | Pfad zum Bannerbild (ersetzt das Icon). |
| `bannerHeight` | Ganzzahl | 100 | Höhe des Banners in Pixeln |
| `bannerTitle` | Zeichenkette | - | Titelüberlagerung auf dem Banner |
| `highlightColor` | Zeichenkette | "#808080" | Akzentfarbe (Hexadezimalcode) |
| `backgroundColor` | Zeichenkette | - | Hintergrundfarbe (Hexadezimalcode) |
| `backgroundImage` | Zeichenkette | - | Pfad zum Hintergrundbild |
| `backgroundOpacity` | Doppelt | 1.0 | Transparenz des Hintergrundes (0-1). |
| `textOverlayColor` | Zeichenkette | - | Farbe der Textüberlagerung für Hintergründe |
| `gradientColors` | Array | - | Farbpalette mit Hex-Codes für Farbverläufe |
| `iconBasePath` | Zeichenkette | - | Basisverzeichnis für relative Pfade zu Icons |
| `appearance` | Zeichenkette | "Auto" | Erzwingen Sie das Anzeigen des Inspektionsfensters: `"dark"`, `"light"` oder `"auto"` (entsprechend dem Betriebssystem). Überschreibt die Betriebssystemeinstellungen in beide Richtungen. |

### Konfiguration der Elemente

Jedes Element im `items`-Array benötigt:

| Schlüssel | Typ | Erforderlich | Beschreibung |
|-----|------|----------|-------------|
| `id` | Zeichenkette | Ja | Eindeutige Kennung |
| `displayName` | Zeichenkette | Ja | Anzeigename in der Benutzeroberfläche |
| `guiIndex` | Ganzzahl | Ja | Sortierreihenfolge (beginnend bei 0). |
| `paths` | Array | Ja | Dateipfade, die auf ihre Existenz überprüft werden sollen |
| `icon` | Zeichenkette | Nein | Artikel-spezifisches Icon |
| `plistKey` | Zeichenkette | Nein | Schlüssel zur Validierung in einer Plist-Datei |
| `expectedValue` | Zeichenkette | Nein | Erwarteter Wert der plist-Datei |
| `evaluation` | Zeichenkette | Nein | Bewertungstyp: "gleich", "boolesch", "existiert", "enthält", "bereich" |
| `description` | Zeichenkette | Nein | Eine optionale Beschreibung, die unterhalb des Artikeltitels angezeigt wird (wird durch die Voreinstellungen 1, 2, 3, 5 und 6 generiert). |
<!-- | `subtitle` | String | No | Subtitle text (preset6) | --> <!-- | `category` | Zeichenkette | Nein | Kategoriegruppierung (voreingestellt5) |
| `categoryIcon` | Zeichenkette | Nein | Kategoriesymbol (Voreinstellung 5) | -->


## Erweiterte Funktionen

### Cache-Überwachung

Überwachen Sie Download-Verzeichnisse, um laufende Installationen zu erkennen.

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

Standardmäßig kennzeichnet eine Datei mit der Endung `.pkg`, `.dmg` oder `.download` innerhalb von `cachePaths` ein passendes Element als "*Herunterladen*". Sie können `cacheExtensions` ändern, um diese Liste anzupassen – beispielsweise können Sie `aria2` hinzufügen, damit aria2c's `<name>.aria2`-Teildateien erkannt werden (Problem #617). Der führende Punkt ist optional.

### Überprüfung der Konformität gemäß den PLIST-Richtlinien

Systemkonfiguration mithilfe von plist-Prüfungen validieren:

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

### Benutzerdefinierte Farbwertegrenzen

Definieren Sie benutzerdefinierte Compliance-Stufen und -Farben:

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


### Compliance-Übersichten

Für die Compliance-Berichterstellung, die von plist-Dateien gesteuert wird, fügen Sie ein oberstes `plistSources`-Array hinzu. swiftDialog fasst die referenzierten plist-Dateien in Kategorien zusammen, wobei für jede Kategorie die Anzahl der bestandenen Fälle und die Gesamtanzahl sowie eine Gesamtbewertung angezeigt werden. Diese Informationen werden dann über die `compliance-summary`- und `findings-list`-Inhaltsblöcke (und alle Bento-Elemente) dargestellt und in regelmäßigen Abständen aktualisiert.

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

**`plistSources[]` Eigenschaften:**

| Schlüssel | Typ | Standardeinstellung | Beschreibung |
|-----|------|---------|-------------|
| `path` | Zeichenkette | - | Pfad zur PLIST-Datei |
| `type` | Zeichenkette | - | Quellentyp: `compliance`, `health`, `licenses`, `preferences` oder `custom` |
| `healthyLabel` | Zeichenkette | "Gesund" | Beschriftung für eine bestandene Prüfung <br> (erscheint in Zusammenfassungsseiten, Ergebniszeilen und Bento-Überschriften). |
| `attentionLabel` | Zeichenkette | "Needs Attention" | Etikett für einen fehlgeschlagenen Test |
| `successValues` | Array | - | Werte, die Erfolg signalisieren |
| `expectedValue` | Zeichenkette | - | Erwarteter Wert für die Einhaltung von Vorschriften |
| `findingKey` | Zeichenkette | "Finden" oder "Entdeckung" | Schlüsselwort zum Auslesen der Detailinformationen aus... |
| `timestampKey` | Zeichenkette | Auto | Schlüssel, der den Zeitpunkt der letzten Überprüfung speichert (automatische Versuche `lastComplianceCheck`, `LastUpdateCheck`, `lastCheck`, `timestamp`). |
| `includePattern` | Zeichenkette | - | Regulärer Ausdruck für die Schlüssel, die bei der automatischen Erkennung berücksichtigt werden sollen |
| `excludeKeys` | Array | - | Schlüssel, die von der automatischen Erkennung ausgeschlossen werden sollen |
| `keyMappings` | Array | - | Wie man bestimmte Schlüssel in plist-Dateien interpretiert |
| `maxCheckDetails` | Ganzzahl | 15 | Max: Anzahl der angezeigten Elemente pro Kategorie überprüfen |
| `icon` | Zeichenkette | - | SF-Symbol für die Kategorie |

**Inhaltsblöcke, die die zusammengefassten Daten darstellen:**

- `compliance-summary` — Eine Übersichtsleiste mit dem Gesamtstatus sowie separaten Statistikkarten für jede Kategorie.
- `findings-list` — Eine kategorisiert aufgegliederte, offengelegte Liste einzelner Prüfungen.

Bento-Zellen binden außerdem automatisch an dieselben Daten: Die Untertitel und die Farbe der Icons einer Zelle werden in Echtzeit aktualisiert, wobei keine zusätzlichen Schemafelder erforderlich sind. <br>

## Vollständige Beispiele

### Grundlegender Installationsprogramm für Anwendungen

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
:::tip[iconBasePath]
Definieren Sie einen Basispfad für Artikel-Icons, um die Konfiguration zu vereinfachen. Bildnamen werden, falls verfügbar, von `iconBasePath` geladen. Andernfalls geben Sie den vollständigen Pfad für einen Artikel an.
:::


## Fehlerbehebung

### Konfiguration wird nicht geladen
- Überprüfen Sie die JSON-Syntax mit `jq` oder mit Online-Validatoren
- Überprüfen Sie die Dateiberechtigungen (die Datei muss lesbar sein).
- Stellen Sie sicher, dass die Umgebungsvariable korrekt gesetzt und exportiert wurde

### Objekte werden nicht erkannt
- Überprüfen Sie die exakten Dateipfade (Groß- und Kleinschreibung beachten).
- Überprüfen Sie, ob für den Zugriff auf bestimmte Pfade Administratorrechte erforderlich sind
- Verwenden Sie `cachePaths` zur Erkennung von Downloads
- Erhöhen Sie den Wert `scanInterval` für langsamere Systeme

### Debug-Modus
Aktivieren Sie die Debug-Ausgabe:
```bash
/usr/local/bin/dialog --inspect-mode --debug
```

```bash
export DIALOG_DEBUG=1
/usr/local/bin/dialog --inspect-mode
```

### Häufig verwendete Umgebungsvariablen
- `DIALOG_INSPECT_CONFIG`: Pfad zur Konfigurationsdatei im JSON-Format
- `DIALOG_DEBUG`: Debug-Protokollierung aktivieren
- `DIALOG_COMMAND_FILE`: Pfad zur benutzerdefinierten Befehlsdatei

## Bewährte Praktiken

1. **Einfach anfangen:** Beginnen Sie mit den Voreinstellungen und einer minimalen Konfiguration
2. **Testpfade:** Überprüfen Sie, ob alle Dateipfade existieren oder in Zukunft existieren werden
3. **Cache-Überwachung nutzen**: Eine Funktion zur Erkennung von Downloads hinzufügen `cachePaths`
4. **Icon-Verwaltung**: Speichern Sie Icons an einem zentralen Ort mit `iconBasePath`
5. **Zustände von Schaltflächen:** Verwenden Sie `autoEnableButton` für eine bessere Benutzererfahrung
6. **Geeignete Voreinstellungen:** Wählen Sie Voreinstellungen basierend auf dem Anwendungsfall:
   - Installationsverfolgung: Voreinstellung 1 oder 2 oder 3
   - Anzeigefeld für die Konformität: Voreinstellung 4


