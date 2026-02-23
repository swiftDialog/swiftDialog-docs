---
title: Preset 4 - Toast
description: Configuration for using Inspect Mode Preset 4
---


Minimal ~550×180 window showing one item at a time.
Supports intro → items → summary flow, all in the same compact window.

Progress modes:
 - "shared"  — Single progress bar showing "X of Y completed" (default)
 - "perItem" — Indeterminate progress per item, auto-advances on completion

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
