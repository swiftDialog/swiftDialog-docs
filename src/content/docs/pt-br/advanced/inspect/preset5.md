---
title: Predefinição 5 - Unificada
description: Configuração para usar a predefinição 5 do modo de inspeção
translationSynced: 2026-11-25T11:38:30+00:00
---

Portal de Autoatendimento Pré-Configurado: Visualização Web Personalizada com Autenticação Opcional

Suportes:
- Telas de introdução e encerramento opcionais, desenvolvidas nativamente com SwiftUI, para fluxos de configuração personalizados
- URLs simples e não autenticadas (por exemplo, SOFA, documentação).
- Portais autenticados com injeção de token
- Tematização multi-marca através da configuração de aplicativos MDM

Fluxo: Telas de introdução (opcional) → Visualizador WebView → Telas de finalização (opcional).

<img width="500" alt="image" src="/inspect/preset_5a.png" /> <img width="500" alt="image" src="/inspect/preset_5b.png" />


```json
{
  "highlightColor" : "#007AFF",
  "introSteps" : [
    {
      "content" : [
        {
          "content" : "This is a two-step starter. Edit config.json to add more steps, change layouts, or customise the content.",
          "type" : "text"
        },
        {
          "items" : [
            "Step types: intro, deployment, carousel, guide, showcase, bento, processing, portal, outro",
            "55+ content block types available",
            "Add branding, forms, compliance checks"
          ],
          "type" : "bullets"
        }
      ],
      "continueButtonText" : "Next",
      "heroImage" : "SF=macbook.gen2",
      "heroImageSize" : 180,
      "id" : "welcome",
      "showBackButton" : false,
      "stepType" : "intro",
      "subtitle" : "Your starter Preset 5 workflow (example)",
      "title" : "Welcome"
    },
    {
      "continueButtonText" : "Finish",
      "heroImage" : "SF=arrow.down.app.fill",
      "id" : "apps",
      "items" : [
        {
          "displayName" : "Safari",
          "guiIndex" : 0,
          "icon" : "/Applications/Safari.app",
          "id" : "safari",
          "paths" : [
            "/Applications/Safari.app"
          ]
        },
        {
          "displayName" : "Calculator",
          "guiIndex" : 1,
          "icon" : "/System/Applications/Calculator.app",
          "id" : "calculator",
          "paths" : [
            "/System/Applications/Calculator.app"
          ]
        },
        {
          "displayName" : "TextEdit",
          "guiIndex" : 2,
          "icon" : "/System/Applications/TextEdit.app",
          "id" : "textedit",
          "paths" : [
            "/System/Applications/TextEdit.app"
          ]
        }
      ],
      "showBackButton" : true,
      "stepType" : "deployment",
      "subtitle" : "Simulated deployment step",
      "title" : "App Installation"
    }
  ],
  "preset" : "5"
}
```