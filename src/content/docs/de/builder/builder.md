---
title: Bauernmodus
description: Bearbeiten Sie die Eigenschaften und das Aussehen eines Dialogfensters und geben Sie die Ergebnisse als JSON-Konfigurationsdatei aus
translationSynced: 2026-11-23T00:04:08+00:00
---


## swiftDialog Baukasten

Um die Funktion zu aktivieren, führen Sie `dialog --builder` aus. Beim Aufruf wird ein zusätzliches Fenster angezeigt, in dem Sie Inhalte und Dialogeigenschaften aktualisieren und die Ergebnisse in Echtzeit sehen können.

Sie können das Ergebnis dann als **JSON** oder als eine ausführbare `dialog` **Befehlszeilenanweisung** exportieren, um den Dialog so neu zu erstellen, wie Sie ihn entworfen haben.

** HINWEIS: Diese Funktion deckt nicht alle Funktionen von swiftDialog vollständig ab, und einige Einstellungen sind möglicherweise nicht verfügbar oder werden im generierten Ergebnis nicht angezeigt. Die Entwicklung wird fortgesetzt. **

<img width="500" alt="image" src="/builder/builder_main.png" />

<div className="not-content" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin: 2rem 0; align-items: flex-start;">

<div style="align-self: flex-start;">

### Grundlegend
 - [Titel](/de/builder/title/)
 - [Nachricht](/de/builder/message/)
 - [Symbol](/de/builder/icon/)
 - [Seitenleiste](/de/builder/sidebar/)
 - [Fenster](/de/builder/window/)
 - [Knöpfe](/de/builder/buttons/)

</div>

<div style="align-self: flex-start;">

### Fortgeschritten
 - [Kontrollkästchen](/de/builder/checkboxes/)
 - [Bilder](/de/builder/images/)
 - [Listenpunkte](/de/builder/listitems/)
 - [Medien](/de/builder/media/)
 - [Textfelder](/de/builder/textfields/)

</div>

</div>

### Ausgabe

Die Ansicht "Ausgabe" zeigt das aktuelle Design entweder im **JSON-Format** oder als **Befehlszeilenaufruf** – wechseln Sie zwischen diesen Optionen mit der Registerkartennavigation. Von dort aus können Sie den Inhalt in die **Zwischenablage kopieren** oder eine **Datei speichern**. Der Button "Exportbefehl" im Fußbereich kopiert die Befehlszeile von jeder beliebigen Stelle im Editor.