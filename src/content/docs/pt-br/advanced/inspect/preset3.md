---
title: Predefinição 3 - Compacta
description: Configuração para usar a predefinição 3 do modo de inspeção
translationSynced: 2026-11-25T11:38:20+00:00
---

Esta é uma lista compacta, com um logotipo ou imagem de cabeçalho. Ela rola automaticamente pelos itens, destacando as instalações atuais.

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

