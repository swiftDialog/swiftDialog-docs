---
title: Analyse der Lücken im IPC-Vertrag
description: Eine Lückenanalyse des IPC-Vertrags zwischen swiftDialog und ignitecli, die beobachtete Lücken, Risiken und vorgeschlagene Vertragsklauseln identifiziert, um eine robuste Kommunikation zwischen den beiden Komponenten zu gewährleisten.
translationSynced: 2026-11-20T22:16:22+00:00
---

**Status:** Entwurf zur Überprüfung **Datum:** 2026-06-17 **Umfang:** Laufzeit-Interprozesskommunikation (IPC) zwischen `swiftDialog` (Inspect Mode, Voreinstellungen 1–6) und `ignitecli`, das/die es startet und steuert. **Repositories:**
- swiftDialog — `/Users/henry/Projects/GitHub/swiftDialog`
- ignitecli — `/Users/henry/Projects/GitHub/ignitecli-swift-private`

Dieses Dokument beschreibt den aktuellen IPC-Vertrag und listet anschließend die Bereiche auf, in denen die beiden Seiten nur zufällig übereinstimmen oder in denen eine Garantie angenommen, aber nicht durchgesetzt wird. Jeder Anspruch ist mit einem `file:line`-Verweis versehen, sodass er erneut überprüft werden kann.

---

## 1. Übersicht über die Transportwege

Drei Transportwege sind relevant. Der Vertrag umfasst alle drei; eine zuverlässige Umsetzung darf nicht davon ausgehen, dass einer von ihnen allein zuverlässig ist.

| Transport | Richtung | Kanal / Pfad | Nutzlast | Zuverlässigkeit |
|---|---|---|---|---|
| Verteilte Benachrichtigung (Befehl) | ignitecli → Dialog | `com.swiftdialog.command` **und** `com.ignitecli.command` | `userInfo` Dictionary, als String dargestellt | Bestmöglich, ohne garantierte Reihenfolge, **geht verloren, wenn vor der Registrierung des Beobachters gesendet** |
| Verteilte Benachrichtigung (Ereignis) | Dialog → ignitecli | `com.swiftdialog.event` | `userInfo` Dictionary inkl. `event` und `pid` | Bestmöglich |
| Verteilte Benachrichtigung (Bestätigung) | Dialog → ignitecli | `com.swiftdialog.ack` | `userInfo` Dictionary inkl. `command`, `stepId`, `status`, `pid` | Bestmöglich, **selten genutzt** |
| Auslöse- / Befehlsdatei | ignitecli → Dialog | `--status-log-file` / pro Prozess-ID `.command` | Zeilengetrennt, durch Doppelpunkte getrennt | Beständig, mit Byte-Offset-Verfolgung |
| Bereitschaftsdatei | Dialog → ignitecli | `<trigger>.ready` oder Konfiguration `readinessFile` | JSON | Beständig, auf Vorhandensein geprüft |
| Ereignisdatei | Dialog → ignitecli | Konfiguration `eventFile` oder abgeleiteter Wert `.events` | JSONL | Beständig, am Dateende abgefragt |
| Ergebnisdatei | Dialog → ignitecli | Konfiguration `resultFile` / pro Prozess-ID `.result.json` | JSON | Beständig |
| Veröffentlichte Sitzungen | Dialog → *(niemand)* | `--published-sessions-dir` (Standard `/private/tmp/swiftdialog/sessions/<pid>.json`) | JSON | Beständig, **nicht gelesen** — siehe Lücke 1 |
| ignitecli IPC-Zustand | ignitecli → ignitecli | `/private/tmp/.ignitecli-ipc-<pid>.json` | JSON | Beständig |

**Quellverweise**
- Kanäle: `dialog/Views/Inspect/Core Framework/DistributedNotifications.swift:36`; ignitecli `Sources/Dialog/ActionDispatcher.swift:9`.
- Veröffentlichung auf beiden Kanälen: ignitecli `Sources/Commands/IpcCommand.swift:414`.
- Befehlsdateirouting: `dialog/Views/Inspect/Core Framework/CommandRouter.swift:76`.
- Veröffentlichte Sitzungen: `dialog/Command Line/CommandLineArguments.swift:167`, `dialog/Views/Inspect/Core Framework/PresetCommonHelpers.swift:1134`.
- ignitecli-Zustand: `Sources/Dialog/IpcState.swift:11`.

---

## 2. Ereignis-Vokabular (der Vertrag auf der Leitung)

swiftDialog sendet folgende Ereignistypen (`DistributedNotifications.swift:36`, feste Rohwerte):

| Ereignistyp | Rohwert | Wird gesendet, wenn | Wichtige Felder |
|---|---|---|---|
| `ready` | `ready` | Die Benutzeroberfläche ist bereit für Befehle | `triggerFile`, `preset?`, `itemCount?`, `items?`, `ackChannel` |
| `exit` | `exit` | Wird gleich beendet | `triggerFile`, `exitCode?`, `completedCount?`, `failedCount?`, `resultFile?` |
| `deferred` | `defer` | Benutzer hat aufgeschoben | `duration`, `seconds`, `exitCode`, `resultFile` |
| `button` | `button` | Klick auf eine Schaltfläche | `stepId`, `button`, `action` |
| `step` | `step` | Schrittwechsel | `stepId`, `action` (z. B. `completed`, `all_complete`) |
| `selection` | `selection` | Auswahl aus Picker/Raster bestätigt | `key`, `values` |

Voreinstellung 6 wird bestätigt, dass `step`, `button` und `selection` (`Preset6.swift:1251`, `:1116`, `:1638`) gesendet werden.

Akzeptierte Befehle (ignitecli → Dialog), weitergeleitet in `CommandRouter.swift:76–163`: `success`, `failure`, `warning`, `complete`, `navigate`/`goto`, `next`/`prev`/`back`, `reset`, `progress`, `update_guidance`, `update_message`, `batch_update`, `display_data`, `recheck`, `set`, `item`, `listitem`, `select`. Verkürzte `userInfo`-Schlüssel werden auf diese erweitert (`DistributedNotifications.swift:177`).

---

## 3. Lücken

Sortiert nach Schweregrad. Jede Lücke beschreibt die **beobachtete Realität**, das **Risiko** und einen **vorgeschlagenen Vertragsbestandteil** (normative Formulierung für eine zukünftige gemeinsame Spezifikation).

### Lücke 1 – Verzeichnis für veröffentlichte Sitzungen ist beschreibbar, wird von ignitecli nie gelesen. **HOCH**

**Beobachtet.** swiftDialog schreibt eine pro-PID-Datei zur Erkennung unter `/private/tmp/swiftdialog/sessions/<pid>.json` (`PresetCommonHelpers.swift:1134`, CLI `CommandLineArguments.swift:167`). Eine Suche über den gesamten `Sources/`-Ordner von ignitecli findet **keinen Leser** für dieses Verzeichnis. ignitecli entdeckt Sitzungen ausschließlich über seine eigene Datei `/private/tmp/.ignitecli-ipc-<pid>.json` (`IpcState.swift:11`), die es beim Start schreibt.

Zwei parallele Register beschreiben denselben Sachverhalt (welcher Dialog ist aktiv und welche Trigger-Datei ist dafür zuständig), werden aber niemals abgeglichen:

| Register | swiftDialog schreibt | ignitecli liest |
|---|---|---|
| `…/swiftdialog/sessions/<pid>.json` | ✅ | ❌ |
| `…/.ignitecli-ipc-<pid>.json` | ❌ | ✅ |

**Risiko.** ignitecli kann sich nur an einen Dialog anbinden, den es selbst gestartet hat. Wenn ignitecli seine eigene Statusdatei verliert (z. B. durch einen Absturz, Neustart oder separaten Aufruf), ist der laufende Dialog nicht wiederherstellbar, selbst wenn swiftDialog ihn anzeigt. Die kürzlich eingeführte Erkennungsfunktion bringt ihrem einzigen internen Nutzer keinen Nutzen.

**Vorgeschlagene Klausel.**
> swiftDialog SOLL für jede aktive Sitzung einen Erkennungsdatensatz veröffentlichen. ignitecli SOLL das veröffentlichte Sitzungsverzeichnis als maßgebliche Erkennungsquelle behandeln und SOLL in der Lage sein, eine dort gefundene Sitzung zu übernehmen (Lesen von `triggerFile`, `resultFile`, `readinessFile`, `ackChannel`, `pid`), ohne sie selbst gestartet zu haben. igniteclis eigene Statusdatei DARF als Startzeit-Cache verbleiben, DARF ABER NICHT die einzige Quelle der Wahrheit sein.

**Offene Entscheidung (Eigentümer: ignitecli).** Ist das Sitzungsverzeichnis für die Wiederherstellung durch ignitecli vorgesehen oder für *externe* Tools (Überwachung/MDM)? Diese Entscheidung bestimmt, ob ignitecli einen Pfad zum "Entdecken und Übernehmen" bekommt oder ob dies bewusst außerhalb des Kernsystems bleibt.

### Lücke 2 – Ereignisdatei-Pfad wird durch zwei unterschiedliche Regeln abgeleitet. **MITTEL**

**Beobachtet.** swiftDialog löst den Ereignisdateipfad als `config.eventFile ?? readinessFile(.ready → .events)` auf (identisch in `Preset5.swift:4834`, `Preset1.swift:460`, `Preset2.swift:533` und Voreinstellung 6). Die ignitecli-Vorlagen legen `eventFile` **immer explizit fest** (`Sources/Resources/templates/*/config.json` → `/tmp/__WORKFLOW_NAME__.events`). Sie stimmen nur überein, weil die Konfiguration den Schlüssel immer setzt.

**Risiko.** Eine Konfiguration, die einen benutzerdefinierten `readinessFile`-Pfad setzt und `eventFile` weglässt, veranlasst swiftDialog, einen Pfad abzuleiten, den igniteclis `wait-step` nicht überwacht. `wait-step` (`IpcCommand.swift` WaitStep, Abfrage alle 2 Sekunden) hängt dann bis zu seinem Timeout, ohne eine Diagnose auszugeben, die auf den Pfadunterschied hinweist.

**Vorgeschlagene Klausel.**
> Der Ereignisdatei-Pfad SOLL durch genau eine Regel abgeleitet werden, die von beiden Seiten gemeinsam verwendet wird. Wenn beide Seiten ableiten (statt eine explizite Angabe von `eventFile` zu verlangen), SOLL der Ableitungsalgorithmus hier wörtlich festgelegt und durch einen Test auf jeder Seite abgedeckt werden. Ein `wait-step`-Timeout SOLL den gelösten Ereignisdatei-Pfad in seiner Fehlermeldung enthalten.

### Lücke 3 – Wartevorgänge prüfen nicht auf Prozess-Lebendigkeit. **MITTEL**

**Beobachtet.** `wait-exit` prüft `kill(pid, 0)` (`IpcState.swift:58`) und bemerkt einen toten Dialog. `wait-ready` und `wait-step` warten auf eine Benachrichtigung oder eine Dateiänderung; `wait-step` bemerkt eine tote PID nur, wenn seine frühe Prüfung zufällig greift, andernfalls verbrät es das volle Timeout (`IpcCommand.swift` WaitStep, `:376`).

**Risiko.** Ein Dialog, der mitten in einem Schritt abstürzt, verwandelt einen schnellen, klaren Fehler in ein generisches Timeout von 2–600 Sekunden ohne Angabe einer Ursache.

**Vorgeschlagene Klausel.**
> Jeder Wartevorgang (`wait-ready`, `wait-step`, `wait-exit`) SOLL bei jedem Tick `kill(pid, 0)` abfragen, im selben Takt wie seine Datei- oder Benachrichtigungsprüfung, und SOLL schnell fehlschlagen mit `Dialog-PID <n> ist vor <Bedingung> beendet` statt eines generischen Timeouts.

### Lücke 4 – Bestätigungskanal existiert an beiden Enden, wird aber nicht als Sperre verwendet. **MITTEL**

**Beobachtet.** swiftDialog sendet nach jedem weitergeleiteten Befehl eine Bestätigung an `com.swiftdialog.ack` (`CommandRouter.swift:351`). ignitecli hat `waitAck()` (`Sources/Dialog/DialogOrchestrator.swift:151`), aber die meisten Arbeitsabläufe rufen es nicht auf; der Standard-Übertragungsmodus ist "Feuer und vergessen" über einen bestenfalls zuverlässigen Transport.

**Risiko.** Eine verlorene `navigate`-Benachrichtigung, die einen nachfolgend vorgeladenen Batch sperrt, entsynchronisiert den gesamten Ablauf stillschweigend. Idempotente Neuzeichnungen tolerieren Verlust; befehle, die auf eine bestimmte Reihenfolge angewiesen sind, nicht.

**Vorgeschlagene Klausel.**
> Befehle, deren Wirkung spätere Befehle bedingt (`navigate`, `goto`, `reset`, `batch_update`, der eine Navigation vorausgeht), SOLL mit aktiviertem Ack-Wait gesendet werden. ignitecli SOLL den Befehl wiederholen oder einen Fehler melden, wenn für einen solchen Befehl keine Bestätigung innerhalb des Ack-Timeouts eintrifft. Feuer-und-vergessen bleibt für idempotente Aktualisierungen erlaubt (`progress`, `update_message`, `display_data`).

### Lücke 5 – Trigger-Datei-Wiedergabe wurde zweimal gefixt, niemand besitzt sie. **GERING–MITTEL**

**Beobachtet.** ignitecli löscht IPC-Dateien vor dem Start (`DialogLauncher.swift:199`), um zu verhindern, dass swiftDialog veraltete `success:`-Zeilen wiedergibt (das Voreinstellung-5-Durchblitzen). swiftDialog zeichnet unabhängig davon den anfänglichen Byte-Offset auf, um bereits vorhandene Inhalte zu überspringen (`CommandRouter.swift:79`). Zwei unabhängige Korrekturen schützen vor derselben Gefahr.

**Risiko:** Wenn eine der beiden zurückfällt – swiftDialog liest wieder ab Offset 0, oder ignitecli lässt die Bereinigung in einem neuen Pfad aus –, kehrt der Fehler stillschweigend zurück.

**Vorgeschlagene Klausel.**
> swiftDialog SOLL jeden Inhalt der Trigger-Datei ignorieren, der vor dem Senden von `ready` vorhanden ist. Diese Garantie SOLL auf der swiftDialog-Seite besessen und getestet werden; die vor dem Start durch ignitecli durchgeführte Bereinigung ist Verteidigung in die Tiefe, nicht die primäre Garantie.

### Lücke 6 – Keine Authentifizierung auf keinem Transport (akzeptiert, aber nicht ausgesprochen). **NIEDRIG**

**Beobachtet.** Keine Absender-Validierung bei verteilten Benachrichtigungen (die API bietet keine); die Befehls-/Trigger-Datei ist für alle beschreibbar; das Sitzungsverzeichnis ist für alle lesbar und aufzählbar. Jeder lokale Prozess kann den Dialog steuern oder fälschen und kann laufende PIDs sowie Trigger-Pfade aufzählen. Das neue Sitzungsverzeichnis *erweitert* diese Offenlegungsfläche.

**Risiko.** Akzeptabel unter einem lokalen Vertrauensmodell "gleicher Benutzer"; gefährlich, wenn diese Annahme verletzt wird (gemeinsamer Host, Mitnutzer mit geringeren Rechten).

**Vorgeschlagene Klausel.**
> Die IPC-Vertrauensgrenze ist "gleicher Benutzer, gleicher Host, lokal". Alle Transporte gehen von einem kooperierenden lokalen Absender aus. Dies ist eine bewusste, dokumentierte Annahme; kein Transport bietet Authentifizierung oder Integrität. Jede Nutzung außerhalb dieser Grenze liegt außerhalb des Geltungsbereichs und wird nicht unterstützt.

---

## 4. Schweregrad-Zusammenfassung und Sequenzierung

| # | Lücke | Schweregrad | Behebung bei |
|---|---|---|---|
| 1 | Sitzungsverzeichnis nur beschreibbar | HOCH | ignitecli (Leser) |
| 2 | Zwei Ereignisdatei-Regeln | MITTEL | beide (gemeinsame Regel) |
| 3 | Wartevorgänge prüfen nicht auf Lebendigkeit | MITTEL | ignitecli |
| 4 | Ack nicht als Sperre verwendet | MITTEL | ignitecli (Richtlinie) |
| 5 | Wiedergabe zweimal gefixt | GERING–MITTEL | swiftDialog (übernimmt die Garantie) |
| 6 | Keine Authentifizierung, nicht ausgesprochen | NIEDRIG | nur Dokument |

**Empfohlene Reihenfolge.** Zuerst diesen Vertrag festschreiben (Lücken 5–6 sind rein dokumentarisch und können sofort abgeschlossen werden). Dann **Lücke 1 + Lücke 2 zusammen** umsetzen – ignitecli SOLL das veröffentlichte Sitzungsverzeichnis als maßgebliche Erkennungsquelle nutzen und die Ereignisdatei-Ableitung auf eine Regel zusammenführen. Dadurch werden die kürzlichen swiftDialog-IPC-Commits zu etwas, das ignitecli tatsächlich verwendet. Lücken 3–4 sind unabhängige ignitecli-Robustheitskorrekturen, die danach folgen können.

---

## 5. Verifizierungsprotokoll

Die in diesem Dokument gemachten Aussagen wurden am 17. Juni 2026 gegen die Quellen überprüft:

- Sitzungsverzeichnis wird von ignitecli nicht gelesen – Suche in `Sources/` nach `swiftdialog/sessions` / `publishedSessions`: kein Verbraucher.
- Voreinstellung 6 sendet `step`, `button`, `selection` — `Preset6.swift:1116,1152,1251,1638`.
- Ereignisdatei-Pfad, doppelte Ableitung — `Preset1.swift:460`, `Preset2.swift:533`, `Preset5.swift:4834`; explizites `eventFile` in ignitecli `Sources/Resources/templates/*/config.json`.
- Bestätigung gesendet, aber optional — `CommandRouter.swift:351`, ignitecli `DialogOrchestrator.swift:151`.
- Lebendigkeit nur in `wait-exit` — `IpcState.swift:58`.
- Vorab-Bereinigung vs. Byte-Offset-Überspringen — `DialogLauncher.swift:199`, `CommandRouter.swift:79`.
