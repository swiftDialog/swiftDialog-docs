---
title: Demonstrationskripte
description: Vollständiges Drehbuch für eine Demonstration zur Auswahl und Installation von Anwendungen
translationSynced: 2026-11-23T00:10:09+00:00
---

Eine umfassende Demo-Sammlung finden Sie unter https://github.com/swiftDialog/demo

## swiftDialog: Umfassende Demo-Suite

Eine Sammlung von Zsh-Skripten, die alle wichtigen Funktionen von [swiftDialog](https://github.com/swiftDialog/swiftDialog) anhand einer interaktiven, selbstgesteuerten Tour demonstrieren.

## Anforderungen

- macOS 15 oder eine neuere Version
- [**swiftDialog Version 3 oder neuer**](https://github.com/swiftDialog/swiftDialog/releases)

## Schnellstartanleitung

```zsh
# clone this repo
git clone https://github.com/swiftDialog/demo.git swiftDialog-demo

# or download the zip
curl -sL "https://github.com/swiftDialog/demo/archive/refs/heads/main.zip" -o swiftDialog-demo.zip && unzip swiftDialog-demo.zip -d swiftDialog-demo

cd swiftDialog-demo
./run_demos.zsh
```

Der Hauptcontroller verwendet selbst swiftDialog – wählen Sie die Demo-Versionen mit Kontrollkästchen aus und gehen Sie dann jede einzelne durch.

## KI-Kenntnisse für die Erstellung von swiftDialog-Inhalten

**Neu bei swiftDialog?** Beginnen Sie mit der offiziellen [swiftDialog Builder-Seite](https://swiftdialog.app/builder/builder/)], um sich einen Überblick zu verschaffen und visuelle Prototypen zu erstellen. Verwenden Sie anschließend eines der im Repository enthaltenen Skill-Packs, um dieses Verständnis in Skripte im Repository-Stil umzuwandeln. Der Builder ist nützlich, aber er ist nicht umfassend und ersetzt nicht die endgültige Anpassung der Größe, die Bereinigung und die Entscheidungen bezüglich des Arbeitsablaufs.

### Verfügbare Fähigkeiten

**[`codex-swiftdialog-builder`](skills/codex-swiftdialog-builder/)** — Für GitHub Copilot / OpenAI Codex

- [`SKILL.md`](skills/codex-swiftdialog-builder/SKILL.md) — Workflow in Codex und Auswahl der Serviceebenen]
- [`references/`](skills/codex-swiftdialog-builder/references/) — Anleitungen zur Erstellung von Demo-Inhalten und zur Gestaltung von Lernmaterialien
- [`assets/templates/`](skills/codex-swiftdialog-builder/assets/templates/) — Startskripts für Shell-Umgebungen]
- Enthält ein Jamf/root-Ausführungs-`/var/tmp` sowie ein Übergabemuster für Berechtigungen, das für Befehls- und Dateiverarbeitungsprozesse verwendet wird, die als `root` gestartet werden

**[`claude-swiftdialog-builder`](skills/claude-swiftdialog-builder/)** — Für Claude Sonnet

- [`CLAUDE.md`](skills/claude-swiftdialog-builder/CLAUDE.md) — Claude: Arbeitsablauf und Auswahl der Preismodelle]
- [`references/`](skills/claude-swiftdialog-builder/references/) — Anleitungen zur Erstellung von Demo-Inhalten und zur Gestaltung von Lernmaterialien
- [`templates/`](skills/claude-swiftdialog-builder/templates/) — Startskripts für Shell-Umgebungen]
- Enthält ein Jamf/root-Ausführungs-`/var/tmp` sowie ein Übergabemuster für Berechtigungen, das für Befehls- und Dateiverarbeitungsprozesse verwendet wird, die als `root` gestartet werden

Beide Funktionen folgen den gleichen Konventionen für das Repository und erzeugen identische Skriptausgaben – wählen Sie diejenige, die zu Ihrer KI-Plattform passt. Weitere Informationen zur Verwendung finden Sie unter [`skills/README.md`](skills/README.md)].

Dies sind Funktionspakete für KI-Assistenten, keine ausführbaren Demonstrationen innerhalb der Software.

## Entwicklungsumgebung mit Unterstützung durch Künstliche Intelligenz

Nachdem Sie die Demo-Umgebung erkundet und die Funktionen von swiftDialog verstanden haben, können Sie mit Hilfe von KI-Unterstützung Ihre eigenen, benutzerdefinierten Skripte erstellen, indem Sie das [`playground/`](playground/)]-Verzeichnis verwenden. Die interaktive Lernumgebung enthält eine umfassende, schrittweise Anleitung, die Ihnen zeigt, wie Sie:

- Nutzen Sie KI-Assistenten (wie Claude oder Copilot) mit den integrierten Funktionen
- Wählen Sie die passende Stufe für Ihren Arbeitsablauf (grundlegende Dialoge → Formulare → Fortschrittsanzeigen → Inspektionsmodus).
- Folgen Sie detaillierten, praxisnahen Szenarien mit präzisen Anweisungen und erwarteten Interaktionen mit der KI
- Erstellen Sie Produktionsskripte für Verwaltungsaufgaben unter macOS (Einrichtung, Compliance, Bereitstellung, Überwachung, Bestätigung vor destruktiven Aktionen).

**Starten Sie hier:** [`playground/README.md`](playground/README.md) – Ihr Arbeitsbereich für die schnelle Entwicklung von Dialogskripten mit Unterstützung durch künstliche Intelligenz.

## Demo-Index

- `01_basic_styles.zsh` — `--style` (Hinweis, Vorsicht, Warnung, zentriert), Überschreibungen des Stils
- `02_title_message.zsh` – `--title`, `--titlefont`, `--message`, `--messagefont`, `--messagealignment`, `--messageposition`, `--bannertitle`, Titel: "kein"
- `03_icons.zsh` – `--icon` (SF-Symbole, Apps, Systemfunktionen, QR-Code, Farbpalette, automatische Farbkorrektur, Gewicht), `--iconsize`, `--iconalpha`, `--centreicon`, `--overlayicon`, `--hideicon`
- `04_buttons.zsh` – `--button1text`, `--button1symbol`, `--button1disabled`, `--button2text`, `--button2symbol`, `--infobuttontext`, `--infobuttonsymbol`, `--infobuttonaction`, `--buttonstyle` (Mitte, Stapel), `--buttonsize`, `--buttontextsize`, `--hidedefaultkeyboardaction`
- `05_images_banners.zsh` — `--image`, `--imagecaption`, `--bannerimage`, `--bannertitle`, `--bannertext`, `--background`, `--bgalpha`, `--bgposition`, `--bgfill`
- `06_progress_timer.zsh` – `--progress` (absolut, Inkrement, Zurücksetzen, Fertigstellung), `--progresstext`, `--progresstextalignment`, `--timer`, `--hidetimerbar`, Fortschrittsmitteilungen für die Befehlsdatei
- `07_text_fields.zsh` – `--textfield` (erforderlich, sicher, schnell, Wert, regulärer Ausdruck, Fehler beim regulären Ausdruck, Bestätigung, Dateiauswahl, Dateityp, Pfad, Name), `--textfieldlivevalidation`
- `08_dropdowns.zsh` — `--selecttitle`, `--selectvalues`, `--selectdefault`, Modifikatoren (erforderlich, Radio-Button, durchsuchbar, Mehrfachauswahl, Name), Trennzeichen
- `09_checkboxes.zsh` – `--checkbox` (Namenszusatz), `--checkboxstyle` (Kontrollkästchen, Schalter, Größen)
- `10_list_items.zsh` – `--listitem` (Status, Statusbeschreibung, benutzerdefinierte Symbole), `--liststyle`, `--enablelistselect`, Befehlsdatei (Liste:, Listenelement:, hinzufügen, löschen, Index).
- `11_window_options.zsh` — `--width`, `--height`, `--big`, `--small`, `--position`, `--positionoffset`, `--moveable`, `--ontop`, `--resizable`, `--windowbuttons`, `--appearance`, `--showdockicon`, `--dockiconbadge`
- `12_command_file.zsh` — Vollständige Befehlsdatei-Übersicht: Titel: (title:), Schriftart für Titel: (titlefont:), Meldung: (message:), (mit Möglichkeit zur Ergänzung: +append), Ausrichtung: (alignment:), Symbol: (icon:), Überlagerungssymbol: (overlayicon:), Transparenz des Symbols: (iconalpha:), Text für Schaltfläche 1: (button1text:), Schaltfläche 1: (button1:), Informationstext: (infotext:), Informationsfeld: (infobox:), Symbolposition: (icon: centre/left)
- `13_notifications.zsh` — `--notification`, `--subtitle`, `--identifier`, `--remove`
- `14_mini_presentation.zsh` — `--mini` (mit Fortschrittsanzeige), `--presentation` (mit Listenpunkt, Infobox, Fortschrittsanzeige)
- `15_web_video.zsh` – `--webcontent`, `--video` (youtube = Abkürzung), `--videocaption`, `--autoplay`
- `16_json_input.zsh` – `--jsonstring`, `--jsonfile`, JSON-Arrays für Kontrollkästchen, Auswahlmöglichkeiten, Textfelder und Bilder
- `17_fullscreen_blur.zsh` — `--fullscreen`, `--blurscreen`, `--hideotherapps`
- `18_misc_features.zsh` — `--helpmessage`, `--infotext`, `--infobox`, `--vieworder`, `--quitkey`, `--sound`, `--showsoundcontrols`, `--displaylog`, `--loghistory`, `--debug`, `--eula`, `--alwaysreturninput`, Erklärung zur Authentifizierungsschlüssel/Checksumme
- `19_inspect_mode.zsh` –, `--inspect-mode`, `--inspect-config`, `--published-sessions-dir`, `stepType: "cadence"`, `cadenceStyle: "carousel"`, Taktfrequenz (IPC) (`cadence:satisfy`, `cadence:advance`, `cadence:goto`), Neugestaltung von Voreinstellung 3, Logo im Fußbereich, erzwungenes `appearance`, `cacheExtensions` mit `aria2`
- `20_branched_workflows.zsh` – Array der obersten Ebene, `workflow`, `branch.map`, `branch.default`, `branch.ifTrue`, `branch.ifFalse`, `nextpage`, `finalpage`, mit Berücksichtigung der Historie. Vorherige Seite

## Ausführen einzelner Demonstrationen

Jedes Demo-Skript ist ein eigenständiges Programm.

```zsh
./demos/06_progress_timer.zsh
./demos/12_command_file.zsh
```

## Anmerkungen

- Demonstrationen, die `--blurscreen` oder `--fullscreen` verwenden, übernehmen kurzzeitig die Anzeige
- Die Demoanwendungen für Benachrichtigungen benötigen die entsprechenden Berechtigungen für die Funktion swiftDialog
- Einige Bildbeispiele verwenden Systemhintergrundbilder, die je nach macOS-Version variieren können
- Demo 19 konzentriert sich nun auf die Aktualisierung der Version 3.1.0b4, einschließlich des "Cadence Carousel", des überarbeiteten "Preset 3 Compact"-Designs, der Sitzungspublikation und einer Beispiel-JSON-Datei für verwaltete Präferenzen.
- Die Demos 19 und 20 benötigen **swiftDialog in der Version 3.1.0b4 oder neuer**, um Funktionen für Zeitplanung und verzweigte Arbeitsabläufe unterstützen zu können.
- Weitere Informationen zu den hier beschriebenen Funktionen finden Sie in den Versionshinweisen von [swiftDialog v3.1.0b4]](https://github.com/swiftDialog/swiftDialog/releases/tag/v3.1.0b4).