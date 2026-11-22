---
title: Voreinstellung 5 – Einheitlich
description: Konfiguration für die Verwendung von Voreinstellung 5 im Inspektionsmodus
translationSynced: 2026-11-20T22:17:07+00:00
---

Selbstbedienungsportal: Vordefinierte, markenbezogene Webansicht mit optionaler Authentifizierung

Unterstützt:
- Optionale native SwiftUI-Einführungs- und -Abschlussbildschirme für markenspezifische Einrichtungsprozesse
- Einfache, nicht authentifizierte URLs (z. B. SOFA, Dokumentation).
- Authentifizierte Portale mit Token-Einfügung
- Themenvorlagen für mehrere Marken über die MDM-App-Konfiguration

Ablauf: Einführungsscreens (optional) → Webansicht des Portals → Abschluss-Screens (optional).

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