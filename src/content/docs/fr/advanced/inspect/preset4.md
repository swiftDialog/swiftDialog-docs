---
title: "Préréglage 4 - Toast"
description: Configuration pour utiliser le préréglage 4 en mode inspection
translationSynced: 2026-11-23T04:26:25+00:00
---


Fenêtre minimale (environ 550 x 180 pixels) affichant un seul élément à la fois. Permet une navigation fluide : introduction → éléments → résumé, le tout dans une fenêtre compacte.

Modes de progression :
 - "partagé" — Une seule barre de progression indiquant "X sur Y terminé" (par défaut).
 - "par élément" : progression indeterminée pour chaque élément, avance automatiquement une fois la tâche terminée

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
