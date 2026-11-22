---
title: Gated-Kadenz bei einer MDM-Bereitstellung
description: Mit dem Schritttyp "gated-cadence" kann eine attributgesteuerte Bereitstellungsoberfläche erstellt werden, die sich basierend auf dem tatsächlichen Systemzustand dynamisch anpasst. Dies ist besonders geeignet für MDM-Bereitstellungen mit Tools wie Fleet, Jamf und Intune.
translationSynced: 2026-11-20T22:12:33+00:00
---

Der "gated-cadence"-Schritt wandelt einen Bereitstellungsbildschirm in eine **attributgesteuerte** Sequenz um: Jede Meldung wird angezeigt, bis eine **tatsächliche Bedingung** erfüllt ist, woraufhin sie zur nächsten Meldung übergeht. Die Bedingungen werden aus dem tatsächlichen Systemzustand gelesen, sodass der Bildschirm niemals "fertig" anzeigt, bevor er es tatsächlich ist.

Dies ist **unabhängig von MDM-Lösungen**. Die Informationen, die es ausliest – installierte Anwendungen, Paketbestätigungen und **mobileconfig-basierte Einstellungen unter `/Library/Managed Preferences/`** – werden auf die gleiche Weise von **Fleet, Jamf, Intune, Mosyle, Kandji, Munki, Installomator** und ähnlichen Systemen bereitgestellt. Die folgenden Beispiele verwenden **Fleet** als konkretes Beispiel, aber nichts davon ist speziell für Fleet entwickelt.

## Wie es in einen Ausrollprozess passt

Das MDM-System erledigt die Aufgaben (installiert Software, verteilt Profile); swiftDialog überwacht diesen Prozess.

| Bereitstellungsvorgang | Kadenzattribut | Was es liest |
|---|---|---|
| App installiert | `app` (`bundleId`) | `NSWorkspace.urlForApplication(withBundleIdentifier:)` |
| Paket installiert | `file` | Quittung an `/var/db/receipts/<pkgid>.bom` |
| **Profil / mobileconfig-Datei hinzugefügt.** | **`managedpref`** (`domain`+`key`) | `/Library/Managed Preferences/<domain>.plist` (Gerät) oder `…/<user>/<domain>.plist` |
| Skriptgesteuerte Konfiguration | `file` | eine Markierungsdatei, die das Skript bearbeitet |
| Nicht sichtbare Prüfung | `source:"ipc"` | Ein MDM-Skript ruft `cadence:satisfy:<id>` auf (osquery, Installomator-Protokoll, MDM-API). |

**Hybride Lösung:** Die meisten Einträge werden direkt erfasst (ohne Orchestrator, funktioniert offline / im Anmeldefenster); einige `source:"ipc"` Einträge werden durch ein MDM-Skript erweitert, um Informationen zu erfassen, die nicht direkt beobachtet werden können. Der IPC-Befehl ist `cadence:satisfy:<id>` (auch `advance` / `goto`).

Ein `timeout` auf einem Eintrag erzwingt den Fortschritt, falls eine Aufgabe niemals abgeschlossen wird, sodass eine fehlerhafte Richtlinie die Benutzeroberfläche nicht blockieren kann.

## Zwei Phasen

Da die Anmeldebildschirm-/Einrichtungsassistenten-Phase **keine Benutzersitzung** beinhaltet (keine Benutzeranwendungen, sondern nur geräteweite verwaltete Einstellungen), werden zwei Konfigurationen verwendet, wobei der Launcher basierend auf der jeweiligen Sitzung eine davon auswählt.

### Phase A – Anmeldefenster / Installationsassistent (nur für das Gerät).
```json
{
  "preset": "5", "stepType-note": "device phase",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Setting up your Mac",
    "cadenceInterval": 1.0, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "mdm",      "message": "Confirming management…", "sfSymbol": "checkmark.shield.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.mdm", "key": "AccessRights", "evaluation": "exists", "scope": "device" }, "timeout": 600 },
      { "id": "filevault","message": "Enabling disk encryption…", "sfSymbol": "lock.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.MCX.FileVault2", "key": "Enable", "evaluation": "equals", "expectedValue": "On", "scope": "device" }, "timeout": 900 },
      { "id": "rosetta",  "message": "Installing base packages…", "sfSymbol": "shippingbox.fill",
        "attribute": { "type": "file", "path": "/var/db/receipts/com.company.baseline.bom" }, "timeout": 900 }
    ]
  }]
}
```

### Phase B – Desktop-Umgebung nach der Anmeldung (vollständige Funktionalität).
```json
{
  "preset": "5",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Installing your apps",
    "cadenceInterval": 0.5, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "edge",    "message": "Installing Microsoft Edge…", "sfSymbol": "globe",
        "attribute": { "type": "app", "bundleId": "com.microsoft.edgemac" }, "timeout": 600 },
      { "id": "office",  "message": "Installing Office…", "sfSymbol": "doc.fill",
        "attribute": { "type": "app", "bundleId": "com.microsoft.Word" }, "timeout": 1200 },
      { "id": "vpn",     "message": "Applying VPN profile…", "sfSymbol": "network",
        "attribute": { "type": "managedpref", "domain": "com.company.vpn", "key": "Enabled", "evaluation": "boolean", "expectedValue": "true", "scope": "device" }, "timeout": 600 },
      { "id": "compliance","message": "Running compliance check…", "sfSymbol": "checkmark.seal.fill",
        "attribute": { "source": "ipc" }, "timeout": 600 }
    ]
  }]
}
```
Der `compliance` Eintrag ist `source:"ipc"`: Ein MDM-Skript führt die Überprüfung durch (mit osquery / einer Anbieter-API) und führt dann `… ipc send "cadence:satisfy:compliance"` aus.

## Versand (Beispiel: Fleet-Modell – gleiche Form für jedes MDM-System).
1. **Paket:** swiftDialog + der Launcher + beide Cadence-JSON-Dateien.
2. **Profil (mobileconfig):** Konfiguration des Starters: Welche Einstellungen pro Sitzung, welche Optionen für das Anmeldefenster.
   (Der Launcher liest seine eigenen, von ihm verwalteten Einstellungen auf die gleiche Weise – unter `/Library/Managed Preferences/`.)
3. **LaunchAgents** (Gerät + Anmeldefenster), um swiftDialog in der richtigen Sitzung zu starten.
4. **GitOps / Richtlinien:** die Profile und die Software, auf die die Kadenz wartet, sowie das kleine Skript, das `cadence:satisfy` für jeden `source:"ipc"`-Eintrag sendet.

Erstellen Sie die Mobileconfig-Dateien und die GitOps-Artefakte mit den `contour` / `fleet-gitops`-Tools, die das Profil anhand des von Apple vorgegebenen Schemas validieren.

## Individuelles Branding und Claims pro Mandant aus verwalteten Einstellungen

Für Mehr-Mandanten-Rollouts können die *Claims* (Anspruchsdefinitionen) und die Marke/Akzentfarbe aus einer verwalteten Einstellung gelesen werden, anstatt sie fest festzulegen, sodass jedes Mandanten-MDM-Profil eigene Werte liefert, ohne die ausgelieferte Konfiguration zu verändern. Beide verwenden ein(e) `ManagedValueRef`:

| Schlüssel | Typ | Beschreibung |
|---|---|---|
| `domain` | Zeichenkette | Domäne mit vorgegebenen Präferenzen, z.B. `nl.root3.support` |
| `key` | Zeichenkette | Schlüsselwert innerhalb dieses Bereichs (der Helligkeitswert für Farben). |
| `darkKey` | Zeichenkette | Optionaler Schlüssel für den Dunkelmodus (nur Farben). |

- `cadenceRef` — Liest die Konfigurationsdaten für die Kadenz (die `CadenceEntry` Dictionaries) aus einer verwalteten Präferenz, anstatt aus einem eingebetteten `cadence` Array.
- `brandColorRef` — Liest die Marken-/Akzentfarbe (hell, optional auch dunkel) aus einer verwalteten Einstellung.

```json
{
  "cadenceRef":    { "domain": "nl.root3.support", "key": "claims" },
  "brandColorRef": { "domain": "nl.root3.support", "key": "brandColor", "darkKey": "brandColorDark" }
}
```

Da die Werte aus `/Library/Managed Preferences/<domain>.plist` resultieren, verhalten sie sich wie die oben genannten `managedpref`-Attribute und übernehmen das gleiche Verhalten, nämlich "werden sofort aktualisiert, sobald das Profil geladen wird".

<!-- REVIEW: cadenceRef / brandColorRef are documented as top-level keys (alongside the inline `cadence` array). Confirm this matches how they're consumed for all presets. -->

## Anmerkungen
- `managedpref` liest die Datei direkt und schaltet sofort frei, sobald das Profil geladen ist (kein CFPreferences-Cache-Verzug). `evaluation:"exists"` = "Profil vorhanden"; `equals`/`boolean` = "ein bestimmter Wert wird erzwungen".
- In der Anmeldephase existiert nur der Gerätebereich; benutzerbezogene verwaltete Einstellungen und `app`-Prüfungen gehören in Phase B.
- Bei der Rückkehr zu einer abgeschlossenen Kadenz (Zurück) werden die Schritte in schnellem Abspielmodus bei `cadenceMinDwell` wiederholt und dann gestoppt – die Kadenz wird nicht erneut geprüft oder blockiert.
