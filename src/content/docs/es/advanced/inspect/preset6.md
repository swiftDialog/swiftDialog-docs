---
title: "Preajuste 6: Orientación"
description: Configuración para utilizar la opción predefinida número 6 en el modo de inspección
translationSynced: 2026-11-24T22:51:27+00:00
---

Navegación lateral moderna con un diseño limpio.

Características:
- Navegación lateral vertical
- Diseño moderno e innovador para el contenedor IntroStep
- Bloques de contenido para la visualización de contenido enriquecido
- Monitoreo de archivos de comandos externos
- Soporte para máquinas de estado de procesamiento
- Persistencia del estado

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