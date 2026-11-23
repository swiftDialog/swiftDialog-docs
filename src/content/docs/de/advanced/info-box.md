---
title: Informationsfeld
description: Anzeigen zusätzlicher Informationen in einem separaten Bereich
translationSynced: 2026-11-23T08:35:52+00:00
---

## Infobox – `--infobox`

Die Infobox ist der Bereich unterhalb des Icons, in dem das Icon angezeigt wird.

Es verwendet eine kleinere Schriftart in einer alternativen Farbe und eignet sich gut zur Anzeige von zusätzlichen Informationen, wie beispielsweise Systeminformationen.

`--infobox` akzeptiert jeden Text, der im Markdown-Format verfasst ist.

#### Beispiel:

`--infobox "### Additional Info\n\n#### Item 1  \n - Point one  \n - Point two  \n#### Item 2  \n - Point three  \n - Point four"`

![Screenshot 2024-09-10 at 4:13:59 PM](https://github.com/user-attachments/assets/d78c2abc-976b-4bb7-b6e8-ff0c487cfe01)

## Breite der Infobox - `--infoboxwidth`

Standardmäßig hat die Infobox die gleiche Breite wie die Icon-Spalte. `--infoboxwidth <number>` legt die Breite des Textbereichs der Infobox (in Punkten) unabhängig von der Icon-Größe fest, sodass Sie die Infobox verbreitern können, ohne das Icon zu vergrößern.

`--infoboxwidth 300`