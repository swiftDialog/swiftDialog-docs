---
title: Befehlsdatei
description: Aktualisierung von Dialogen mit neuen Inhalten in Echtzeit mithilfe von Befehlsdateien
translationSynced: 2026-11-23T08:35:52+00:00
---

Einige Dialoginhalte können auch nach dem Start aktualisiert werden. Dies wird dadurch ermöglicht, dass Befehle an eine Befehlsdatei gesendet werden, die Dialog dann liest und interpretiert.

---

Der Dialog muss im Hintergrund gestartet werden, damit Befehle von demselben Skript an ihn gesendet werden können.

```sh
/usr/local/bin/dialog & sleep 0.1
```

Das System gibt Dialog 100 Millisekunden Zeit, um sich zu initialisieren, bevor der erste Befehl gesendet wird. `sleep 0.1`

Der Standardpfad für die Befehlsdatei ist `/var/tmp/dialog.log`. Ein benutzerdefinierter Pfad kann mit dem Argument `--commandfile` festgelegt werden:

```sh
dialog --commandfile /var/tmp/my.log
```

Befehle senden über:

```sh
echo "<command>: <value>" >> /var/tmp/dialog.log
```

---

## Inhalt

| Befehl | Beschreibung |
|---|---|
| `title: <text>` | Aktualisieren Sie den Titel des Dialogfensters |
| `title: none` | Titelbereich ausblenden |
| `titlefont: <params>` | Aktualisiert die Schriftart-Eigenschaften des Titels. Akzeptiert durch Leerzeichen getrennte Paare: `key=value`, `size=<float>`, `weight=<value>`, `colour=<color\|hex>`, `name=<fontname>`, `shadow=<bool>` |
| `message: <text>` | Ersetzen Sie den Nachrichteninhalt. Unterstützt Markdown. |
| `message: + <text>` | Fügt den vorhandenen Nachrichteninhalten neuen Text hinzu (fügt vor dem neuen Inhalt eine neue Zeile ein). |
| `message: /path/to/file.md` | Laden Sie den Inhalt einer Nachricht aus einer lokalen Markdown-Datei |
| `alignment: [left\|center\|right]` | Legen Sie die Ausrichtung des Textes in der Nachricht fest |

---

## Icon

| Befehl | Beschreibung |
|---|---|
| `icon: <path\|url\|SF Symbol>` | Ändern Sie das angezeigte Icon |
| `icon: none` | Icon ausblenden |
| `icon: centre` / `icon: center` | Verschieben Sie das Icon in die Mitte |
| `icon: left` / `icon: default` | Verschieben Sie das Icon zurück in die Standardposition links |
| `icon: size: <num>` | Ändern Sie die Größe des Icons |
| `iconalpha: <float>` | Transparenz des Icons einstellen (0.0 = transparent → 1.0 = undurchsichtig). |
| `overlayicon: <path\|url\|SF Symbol>` | Legen Sie das Icon für die Overlay-Funktion fest |
| `overlayicon: none` | Verbergen Sie das Icon für die Overlay-Funktion |

---

## Banner und Hintergrund

| Befehl | Beschreibung |
|---|---|
| `bannerimage: <path\|url>` | Legen Sie das Bannerbild fest |
| `bannerimage: none` | Entfernen Sie das Bannerbild |
| `bannertext: enable` | Zeigen Sie den Titel als Bannertext an (legt die Schriftfarbe auf Weiß). |
| `bannertext: disable` | Standardmäßiges Titel-Layout wiederherstellen |
| `bannertext: shadow` | Aktivieren Sie den Weichzeichner-Effekt für den Text im Banner-Titel |
| `bannertext: <text>` | Legen Sie den Text für den Titelbereich fest und aktivieren Sie den Textmodus für den Banner |

---

## Bilder und Medien

| Befehl | Beschreibung |
|---|---|
| `image: <path\|url>` | Zeigen Sie ein Bild (fügt es dem Karussell hinzu, falls bereits ein Bild angezeigt wird). |
| `image: show` | Zeigen Sie das aktuelle Bild |
| `image: hide` | Das aktuelle Bild ausblenden |
| `image: clear` | Entfernen Sie alle Bilder |
| `imagecaption: <text>` | Platzieren Sie die Bildunterschrift unterhalb des angezeigten Bildes |
| `video: <path\|url>` | Zeigt ein Video. Unterstützt die Kurzformen `youtube=<id>` und `vimeo=<id>`. |
| `video: none` | Entfernen Sie das Video |
| `webcontent: <url>` | Eine URL in den Bereich für Webinhalte einfügen |
| `webcontent: none` | Entfernen Sie die Web-Inhalte |

---

## Schaltflächen

| Befehl | Beschreibung |
|---|---|
| `button1: enable` / `button1: show` | Aktivieren Sie Schaltfläche 1 |
| `button1: disable` / `button1: hide` | Deaktivieren Sie Schaltfläche 1 |
| `button1text: <text>` | Beschriftung für Schaltfläche 1 aktualisieren |
| `button2: enable` / `button2: show` | Aktivieren Sie Schaltfläche 2 |
| `button2: disable` / `button2: hide` | Deaktivieren Sie Schaltfläche 2 |
| `button2text: <text>` | Beschriftung für Schaltfläche 2 |
| `buttonsize: [mini\|small\|regular\|large]` | Setzen Sie die Größe der Schaltfläche |
| `infobutton: <text>` | Aktualisieren Sie die Beschriftung der Info-Schaltfläche |
| `infotext: <text>` | Aktualisieren Sie den Textbereich mit Informationen |
| `infotext: disable` / `infotext: hide` | Informationstext ausblenden |
| `infotext: reset` / `infotext: clear` | Löschen Sie den Wert des Informationstexts |

---

## Infobox

| Befehl | Beschreibung |
|---|---|
| `infobox: <text>` | Ersetzen Sie den Inhalt des Infobox-Bereichs. Markdown-Formatierung wird unterstützt. |
| `infobox: + <text>` | Fügen Sie den folgenden Inhalt zur bestehenden Infobox hinzu |
| `infobox: /path/to/file.md` | Laden Sie den Inhalt des Infoboxes aus einer lokalen Markdown-Datei |

---

## Fortschrittsbalken

| Befehl | Beschreibung |
|---|---|
| `progress: <int>` | Setzen Sie den Fortschrittsbalken auf einen bestimmten Wert |
| `progress: increment` | Erhöhen Sie den Fortschrittsbalken um einen Schritt |
| `progress: increment <n>` | Erhöhen Sie die Fortschrittsbalken um `n` Schritte |
| `progress: complete` | Setzen Sie den Fortschrittsbalken auf den maximalen Wert |
| `progress: reset` / `progress: indeterminate` | Setzen Sie die Fortschrittsbalken in den unbestimmten Modus zurück |
| `progress: show` / `progress: enable` / `progress: create` | Zeigen Sie die Fortschrittsbalken |
| `progress: hide` / `progress: disable` / `progress: delete` / `progress: remove` | Verbergen Sie die Fortschrittsbalken |
| `progresstext: <text>` | Aktualisieren Sie die Beschriftung unterhalb der Fortschrittsbalken |

---

## Listen

| Befehl | Beschreibung |
|---|---|
| `list: <csv>` | Ersetzen Sie die Liste durch neue, durch Kommas getrennte Einträge |
| `list: clear` | Alle Elemente in der Liste löschen und die Liste ausblenden |
| `list: show` | Zeigen Sie die Liste |
| `list: hide` | Verbergen Sie die Liste, ohne ihren Inhalt zu löschen |

### Aktualisierung von Listeneinträgen

Aktualisieren Sie einen bestehenden Eintrag anhand des Titels (einfaches Formular):

```sh
echo "listitem: My Item: success" >> /var/tmp/dialog.log
echo "listitem: My Item: Processing..." >> /var/tmp/dialog.log
```

Aktualisieren Sie ein Element mit vollständiger Kontrolle mithilfe von durch Kommas getrennten Eigenschaften:

```sh
echo "listitem: title: My Item, status: success, statustext: Done" >> /var/tmp/dialog.log
echo "listitem: index: 0, status: fail, statustext: Error occurred" >> /var/tmp/dialog.log
```

Fügen Sie ein neues Element am Ende der Liste hinzu:

```sh
echo "listitem: add:, title: New Item, status: wait, statustext: Pending" >> /var/tmp/dialog.log
```

Einen Eintrag löschen:

```sh
echo "listitem: title: My Item, delete:" >> /var/tmp/dialog.log
echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log
```

**Verfügbare `listitem` Eigenschaften:**

| Eigenschaft | Beschreibung |
|---|---|
| `title: <text>` | Element nach Titel suchen |
| `index: <int>` | Vergleichen Sie Elemente anhand ihres Index (beginnend bei 0). |
| `subtitle: <text>` | Setzen Sie die Untertitel für das Element |
| `icon: <path\|url\|SF Symbol>` | Legen Sie das Icon für das Element fest |
| `iconalpha: <float>` | Legt die Transparenz des Icons für ein Element fest |
| `status: <status>` | Legen Sie das Status-Icon fest. Wählen Sie eines von `wait`, `success`, `fail`, `error`, `pending`, `progress` oder geben Sie einen Namen für ein SF-Symbol an (optional mit einer Farbzusatz, z. B. `lock.shield.fill-green`). |
| `statustext: <text>` | Legen Sie den Text für die Statusanzeige fest |
| `progress: <float>` | Einen Inline-Fortschrittswert festlegen (zeigt einen Fortschrittsbalken-Status an). |
| `action: <url>` | Die URL, die geöffnet wird, wenn auf das Element geklickt wird |
| `add:` | Fügen Sie einen neuen Eintrag zur Liste hinzu |
| `delete:` | Löschen Sie das übereinstimmende Element |

---

## Hilfemeldung

| Befehl | Beschreibung |
|---|---|
| `helpmessage: <text>` | Aktualisieren Sie den Inhalt der Hilfenachricht. Markdown-Formatierung wird unterstützt. |

---

## Fenster

| Befehl | Beschreibung |
|---|---|
| `width: <num>` | Ändern Sie die Fensterbreite |
| `height: <num>` | Ändern Sie die Fensterhöhe |
| `position: <position>` | Verschieben Sie das Fenster. Eine der folgenden Optionen `top`, `bottom`, `left`, `right`, `centre` oder eine Kombination (z. B. `topright`) ist möglich. |

---

## Fensteransicht

| Befehl | Beschreibung |
|---|---|
| `activate:` | Bringen Sie das Dialogfenster in den Vordergrund |
| `show:` | Das Dialogfenster wieder anzeigen |
| `hide:` | Dialogfenster ausblenden |
| `minimize:` / `minimise:` | Minimieren Sie das Dialogfenster, sodass es im Dock angezeigt wird |
| `maximize:` / `maximise:` | Ein minimiertes Dialogfenster wiederherstellen |
| `blurscreen: enable` | Aktivieren Sie den Unschärfe-Effekt für den Bildschirm |
| `blurscreen: disable` | Deaktivieren Sie den Unschärfe-Effekt des Bildschirms |

---

## Dock-Icon

| Befehl | Beschreibung |
|---|---|
| `showdockicon: enable` / `showdockicon: true` / `showdockicon: 1` | Zeigen Sie das Dialog-Icon in der Dock-Leiste an |
| `showdockicon: <any other value>` | Verbergen Sie das Dialog-Icon in der Dock-Leiste |
| `dockicon: <file\|url>` | Legen Sie ein benutzerdefiniertes Bild als Icon für die Anwendungsleiste fest |
| `dockicon: none` / `dockicon: default` | Setzen Sie das Standardsymbol für das Dialogfenster-Dock zurück |
| `dockiconbadge: <text>` | Zeigen Sie ein Icon auf dem Dock-Icon an |
| `dockiconbadge: none` / `dockiconbadge: remove` | Entfernen Sie das Icon für die Anzahl der Elemente in der Dockleiste |
| `bounce:` | Das Dock-Icon einmal hüpfen lassen (nur informativ). |
| `bounce: critical` | Das Dock-Icon kontinuierlich hüpfen lassen, bis das Fenster in den Vordergrund gebracht wird |

---

## Beenden

| Befehl | Beschreibung |
|---|---|
| `quit:` | Dialog zur Beendigung mit dem Exit-Code 5 |
