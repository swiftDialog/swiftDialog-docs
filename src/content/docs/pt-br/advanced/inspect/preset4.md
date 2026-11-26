---
title: Configuração 4 - Torrada
description: Configurações para usar a predefinição 4 do modo de inspeção
translationSynced: 2026-11-25T11:38:27+00:00
---


Visualização mínima de aproximadamente 550x180 pixels, exibindo um item por vez. Suporta o fluxo de navegação "introdução → itens → resumo", tudo dentro da mesma janela compacta.

Modos de progresso:
 - "compartilhada" — Barra de progresso única que exibe "X de Y concluídos" (padrão).
 - "por item" — Barra de progresso indeterminada para cada item, que avança automaticamente ao ser concluído

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
