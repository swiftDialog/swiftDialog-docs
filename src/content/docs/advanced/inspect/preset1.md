---
title: Preset 1 - Deployment
description: Configuration for using Inspect Mode Preset 1
---

Traditional sidebar layout with icon, progress bar, and item list. Best for standard application installations.

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
