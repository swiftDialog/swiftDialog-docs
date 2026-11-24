---
title: "Modo 4: Tostado"
description: Configuración para utilizar la configuración predefinida número 4 en el modo de inspección
translationSynced: 2026-11-24T22:51:21+00:00
---


Ventana de tamaño mínimo de 550x180 píxeles que muestra un elemento a la vez. Permite una navegación fluida desde la introducción hasta los elementos y el resumen, todo dentro de una misma ventana compacta.

Modos de progreso:
 - "compartida" — Barra de progreso única que muestra "X de Y completado" (por defecto).
 - "perItem" — Progreso indeterminado por elemento; avanza automáticamente al completarse

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
