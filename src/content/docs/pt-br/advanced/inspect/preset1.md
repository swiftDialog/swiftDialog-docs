---
title: Predefinição 1 - Implantação
description: Configuração para usar a predefinição 1 do modo de inspeção
translationSynced: 2026-11-25T11:32:22+00:00
---

Layout de barra lateral tradicional, com ícone, barra de progresso e lista de itens. Ideal para instalações de aplicativos padrão.

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
