---
title: Requisitos del sistema
description: Requisitos de versión de macOS y compatibilidad para swiftDialog
translationSynced: 2026-11-24T22:12:18+00:00
---

## Requisitos de macOS

swiftDialog es una aplicación binaria universal desarrollada con SwiftUI.

### 3.0+
- **Versión mínima de macOS:** macOS 15 (Sonoma).
- **Arquitectura**: Binario universal (Intel y silicio de Apple).
- **Marco de trabajo**: SwiftUI

### 2.3+
- **Versión mínima de macOS:** macOS 12 (Monterey).

### Versiones anteriores
- La última versión que es compatible con **macOS 11 (Big Sur)** es la [v2.2.1](https://github.com/swiftDialog/swiftDialog/releases/tag/v2.2.1)


## Dependencias

swiftDialog es una aplicación independiente que no requiere dependencias externas. Incluye todos los marcos de trabajo necesarios dentro del paquete de la aplicación.

## Permisos

swiftDialog puede requerir ciertos permisos dependiendo de su uso:

### Funcionamiento básico
- No se requieren permisos especiales para mostrar diálogos básicos

### Características avanzadas
- **Notificaciones:** El usuario debe conceder los permisos de notificación para recibir notificaciones del sistema
- **Acceso completo al disco:** Puede ser necesario si se requiere leer o escribir en ubicaciones protegidas

## Requisitos de la red

- **Funcionamiento sin conexión:** swiftDialog funciona completamente sin necesidad de conexión a internet
- **Operaciones en línea:**
  - Verificando si hay actualizaciones
  - Mostrar contenido web
  - Descarga de imágenes remotas

