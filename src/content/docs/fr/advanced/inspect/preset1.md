---
title: "Préréglage 1 - Deployment"
description: Configuration pour l'utilisation du préréglage 1 en mode d'inspection
translationSynced: 2026-11-23T04:22:20+00:00
---

Mise en page de barre latérale classique, avec icône, barre de progression et liste d'éléments. Idéal pour les installations d'applications standard.

<img width="500" alt="image" src="/inspect/preset_1.png" />

```json
{
  "highlightColor" : "#007AFF",
  "icon" : "SF=arrow.down.app.fill",
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
  "preset" : "1",
  "title" : "App Deployment"
}
```
