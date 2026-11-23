---
title: "Préréglage 3 - Compact"
description: Configuration pour l'utilisation du préréglage 3 en mode d'inspection
translationSynced: 2026-11-23T04:25:37+00:00
---

Voici une présentation sous forme de liste condensée, avec un logo ou une image de bannière en haut. Elle permet une navigation automatique entre les éléments, en mettant en évidence les installations actuelles.

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

