---
title: Voreinstellung 4 – Toast
description: Konfiguration für die Verwendung von Voreinstellung 4 im Inspektionsmodus
translationSynced: 2026-11-20T22:17:03+00:00
---


Minimalistische Anzeige mit einer Größe von ca. 550 x 180 Pixel, die jeweils nur ein Element zeigt. Unterstützt den Ablauf "Einführung → Elemente → Zusammenfassung", wobei alles in einem kompakten Fenster angezeigt wird.

Fortschrittsmodi:
 - "gemeinsam" – Eine einzelne Fortschrittsanzeige, die "X von Y abgeschlossen" anzeigt (Standardeinstellung).
 - "perItem" – Unbestimmter Fortschritt pro Element, automatische Fortschrittsanzeige bei Abschluss

<img width="500" alt="image" src="/inspect/preset_4a.png" /> <img width="500" alt="image" src="/inspect/preset_4b.png" />


```json
{
  "highlightColor" : "#FF9500",
  "icon" : "SF=bell.badge.fill",
  "introScreen" : {
    "buttonText" : "Begin",
    "subtitle" : "Checking 3 applications...",
    "title" : "Software Check"
  },
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
  "preset" : "4",
  "summaryScreen" : {
    "buttonText" : "Close",
    "subtitle" : "All applications installed successfully.",
    "title" : "All Done"
  },
  "title" : "Background Install"
}
```
