---
title: "Preajuste 1: Implementación"
description: Configuración para utilizar la opción de configuración predefinida 1 en el modo de inspección
translationSynced: 2026-11-24T22:46:40+00:00
---

Diseño de barra lateral tradicional con icono, barra de progreso y lista de elementos. Ideal para instalaciones de aplicaciones estándar.

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
