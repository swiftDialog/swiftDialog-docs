---
title: Voreinstellung 2 – Karten
description: Konfiguration für die Verwendung von Voreinstellung 2 im Inspektionsmodus
translationSynced: 2026-11-20T22:13:18+00:00
---

Zeigt ein Logo oder ein obere Bannergrafik und bietet eine übersichtliche Darstellung der einzelnen Karten. Ideal für Anwendungen mit Branding.

<img width="500" alt="image" src="/inspect/preset_2.png" />

```json
{
  "highlightColor" : "#34C759",
  "icon" : "SF=rectangle.split.3x1.fill",
  "items" : [
    {
      "displayName" : "Safari",
      "icon" : "/Applications/Safari.app",
      "id" : "safari",
      "paths" : [
        "/Applications/Safari.app"
      ],
      "showBundleInfo" : "all"
    },
    {
      "displayName" : "Calculator",
      "icon" : "/System/Applications/Calculator.app",
      "id" : "calculator",
      "paths" : [
        "/System/Applications/Calculator.app"
      ],
      "showBundleInfo" : "all"
    },
    {
      "displayName" : "TextEdit",
      "icon" : "/System/Applications/TextEdit.app",
      "id" : "textedit",
      "paths" : [
        "/System/Applications/TextEdit.app"
      ],
      "showBundleInfo" : "all"
    }
  ],
  "message" : "Installing applications...(example)",
  "preset" : "2",
  "title" : "App Catalog"
}
```
