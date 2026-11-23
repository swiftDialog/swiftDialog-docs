---
title: "Préréglage 5 - Unified"
description: Configuration pour l'utilisation du préréglage 5 en mode inspection
translationSynced: 2026-11-23T04:26:32+00:00
---

Portail d'auto-service : Vue Web personnalisée avec authentification optionnelle

Supports :
- Écrans d'introduction et de conclusion optionnels, conçus avec SwiftUI, pour personnaliser les processus de configuration et renforcer l'image de marque
- Simples URL non authentifiées (par exemple, SOFA, la documentation).
- Portails authentifiés avec injection de jetons
- Personnalisation multi-marques via la configuration d'application MDM

Flux : Écrans d'introduction (facultatifs) → Navigateur web intégré → Écrans de conclusion (facultatifs).

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