---
title: Baumodus – Textfelder
description: Bearbeiten Sie die Eigenschaften und das Erscheinungsbild eines Dialogfensters und geben Sie die Ergebnisse als JSON-Konfigurationsdatei aus
translationSynced: 2026-11-23T08:35:52+00:00
---

Konfigurieren Sie `--textfield` Einträge

<img width="500" alt="image" src="/builder/builder_textfields.png" />

Klicken Sie auf die `[+]`-Schaltfläche, um einen neuen Eintrag hinzuzufügen

Klicken Sie auf das Papierkorb-Icon, um einen Eintrag zu löschen

Ziehen Sie den Griff (☰) links von einer Zeile, um die Einträge neu anzuordnen


<img width="500" alt="image" src="/builder/builder_textfields_popualated.png" />


## Eigenschaften

Die folgenden Eigenschaften können eingestellt werden

#### Formatieren Sie die Ausgabe als JSON

Legt das Ausgabeformat fest. Diese Eigenschaft wird mit [Kontrollkästchen](/de/builder/checkboxes/)] geteilt

#### Erforderlich

Setzt das `required`-Flag.

#### Bestätigen

Setzt das `confirm`-Flag. Durch Aktivierung dieser Option wird ein zusätzliches Textfeld für den konfigurierten Eintrag angezeigt

#### Datei auswählen

Aktiviert die `fileselect`-Schaltfläche

##### Dateityp

Wird mit `fileselect` verwendet. Geben Sie den gewünschten Dateityp (oder mehrere Dateitypen in einer CSV-Datei) ein, z. B. `"png,jpg"`

##### Anfangspfad

Wird mit `fileselect` verwendet. Legt den anfänglichen Pfad fest, der beim Anzeigen des Dateiauswahldialogs verwendet wird

#### Titel

Legt den Titel/die Beschriftung des Textfelds fest

#### Name

Legt den Namen des Textfelds fest. Wenn diese Option verwendet wird, repräsentiert dieser Wert den jeweiligen Eintrag in der Ausgabe anstelle der Beschriftung

#### Standardwert

Legen Sie den Standardwert fest, der im Textfeld angezeigt werden soll. Dieser Inhalt wird in der Ausgabe erscheinen

#### Schnell

Legt einen Text fest, der im Textfeld angezeigt wird. Dieser Inhalt wird nicht in der Ausgabe erscheinen

#### Reguläre Ausdrücke

Legen Sie einen regulären Ausdruck fest, dem der Inhalt des Textfelds entsprechen muss

#### Regex-Fehler

Legen Sie fest, welche Fehlermeldung angezeigt werden soll, wenn der Inhalt eines Textfelds nicht mit dem angegebenen regulären Ausdruck übereinstimmt

[Zurück](/de/builder/builder/)