---
title: "Préréglage 6 - Guidance"
description: Configuration pour l'utilisation du préréglage 6 en mode d'inspection
translationSynced: 2026-11-23T04:26:39+00:00
---

Navigation latérale moderne avec un design épuré.

Caractéristiques :
- Navigation latérale verticale
- Design épuré et moderne pour le conteneur IntroStep
- Blocs de contenu pour l'affichage de contenu enrichi
- Surveillance des fichiers de commandes externes
- Prise en charge des machines d'état de traitement
- Persistance de l'état

<img width="500" alt="image" src="/inspect/preset_6a.png" />

<img width="500" alt="image" src="/inspect/preset_6b.png" />

<img width="500" alt="image" src="/inspect/preset_6c.png" />

```json
{
  "highlightColor" : "#007AFF",
  "items" : [
    {
      "displayName" : "Overview",
      "guidanceContent" : [
        {
          "content" : "Welcome to the sidebar navigation layout. Users can navigate between sections.",
          "type" : "text"
        },
        {
          "content" : "Edit config.json to add more sections, change icons, or customise the content blocks.",
          "type" : "info"
        }
      ],
      "guidanceTitle" : "Welcome",
      "icon" : "SF=house.fill",
      "id" : "overview"
    },
    {
      "displayName" : "Applications",
      "guidanceContent" : [
        {
          "content" : "This section could list available applications or provide self-service options.",
          "type" : "text"
        },
        {
          "items" : [
            "Safari — Web browser",
            "Calculator — Quick math",
            "TextEdit — Text editor"
          ],
          "type" : "bullets"
        }
      ],
      "guidanceTitle" : "Applications",
      "icon" : "SF=app.badge.fill",
      "id" : "apps"
    },
    {
      "displayName" : "Help & Support",
      "guidanceContent" : [
        {
          "content" : "Add links, contact info, or troubleshooting guides here.",
          "type" : "text"
        },
        {
          "action" : "url",
          "content" : "Open Apple Support",
          "icon" : "safari.fill",
          "type" : "button",
          "url" : "https://support.apple.com"
        }
      ],
      "guidanceTitle" : "Help & Support",
      "icon" : "SF=questionmark.circle.fill",
      "id" : "help"
    }
  ],
  "preset" : "6",
  "title" : "Service Portal"
}
```