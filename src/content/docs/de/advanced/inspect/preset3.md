---
title: Voreinstellung 3 – Kompakt
description: Konfiguration für die Verwendung von Voreinstellung 3 im Inspektionsmodus
translationSynced: 2026-11-20T22:13:17+00:00
---

Dies ist ein komprimiertes Listenformat mit einem Logo oder einem oberen Bannerbild. Es scrollt automatisch durch die Einträge und hebt die aktuell installierten Elemente hervor.

<img width="500" alt="image" src="/inspect/preset_3.png" />

```json
{
  "highlightColor" : "#5856D6",
  "icon" : "SF=list.bullet.rectangle.fill",
  "items" : [
    {
      "displayName" : "Safari",
      "icon" : "/Applications/Safari.app",
      "id" : "safari",
      "paths" : [
        "/Applications/Safari.app"
      ]
    },
    {
      "displayName" : "Calculator",
      "icon" : "/System/Applications/Calculator.app",
      "id" : "calculator",
      "paths" : [
        "/System/Applications/Calculator.app"
      ]
    },
    {
      "displayName" : "TextEdit",
      "icon" : "/System/Applications/TextEdit.app",
      "id" : "textedit",
      "paths" : [
        "/System/Applications/TextEdit.app"
      ]
    }
  ],
  "message" : "Installing essentials...(example)",
  "preset" : "3",
  "secondaryColor" : "#AF52DE",
  "title" : "Quick Install"
}
```

