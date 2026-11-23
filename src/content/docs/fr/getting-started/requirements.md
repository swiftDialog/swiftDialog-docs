---
title: Configuration requise
description: Versions de macOS requises et compatibilité de swiftDialog
translationSynced: 2026-11-23T01:49:50+00:00
---

## Configuration requise pour macOS

swiftDialog est une application binaire universelle développée avec SwiftUI.

### 3.0+
- **Version minimale de macOS requise :** macOS 15 (Sonoma)
- **Architecture :** Binaire universel (Intel et silicium Apple)
- **Framework :** SwiftUI

### 2.3+
- **Version minimale de macOS requise :** macOS 12 (Monterey)

### Versions antérieures
- La dernière version compatible avec **macOS 11 (Big Sur)** est la version [v2.2.1](https://github.com/swiftDialog/swiftDialog/releases/tag/v2.2.1)


## Dépendances

swiftDialog est une application autonome qui ne nécessite aucune dépendance externe. Elle intègre tous les frameworks nécessaires dans son paquet d'installation.

## Autorisations

swiftDialog peut nécessiter certaines autorisations, selon son utilisation.

### Fonctionnement de base
- Aucune autorisation spéciale n'est requise pour l'affichage des boîtes de dialogue de base

### Fonctionnalités avancées
- **Notifications :** L'utilisateur doit accorder les autorisations de notification pour recevoir les notifications système
- **Accès complet au disque :** Peut être nécessaire si vous devez lire ou écrire dans des zones protégées

## Exigences réseau

- **Fonctionnement hors ligne :** swiftDialog fonctionne entièrement en mode hors ligne
- **Opérations en ligne :**
  - Vérification des mises à jour
  - Affichage du contenu web
  - Téléchargement d'images à distance

