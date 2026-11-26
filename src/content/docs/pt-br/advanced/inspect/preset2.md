---
title: Predefinição 2 - Cartões
description: Configurações para usar a predefinição 2 do modo de inspeção
translationSynced: 2026-11-25T11:38:21+00:00
---

Apresenta um logotipo ou uma imagem de banner superior, com uma exibição simplificada dos itens do cartão. Ideal para implementações com identidade visual própria.

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
