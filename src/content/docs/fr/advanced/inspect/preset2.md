---
title: "Préréglage 2 - Cards"
description: Configuration pour l'utilisation du préréglage 2 du mode d'inspection
translationSynced: 2026-11-23T04:24:25+00:00
---

Comporte un logo ou une image de bannière en haut, ainsi qu'une présentation épurée des éléments de type "carte". Idéal pour les déploiements personnalisés.

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
