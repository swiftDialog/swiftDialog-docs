---
title: System Requirements
description: macOS version requirements and compatibility for swiftDialog
---

## macOS Requirements

swiftDialog is a universal binary app written using SwiftUI.

### 3.0+
- **Minimum macOS version**: macOS 15 (Sonoma)
- **Architecture**: Universal Binary (Intel and Apple Silicon)
- **Framework**: SwiftUI

### 2.3+
- **Minimum macOS version**: macOS 12 (Monterey)

### Legacy Versions
- The last version that supports **macOS 11 (Big Sur)** is [v2.2.1](https://github.com/swiftDialog/swiftDialog/releases/tag/v2.2.1)


## Dependencies

swiftDialog is a standalone application with no external dependencies. It includes all necessary frameworks within the application bundle.

## Permissions

swiftDialog may require certain permissions depending on usage:

### Basic Operation
- No special permissions required for basic dialog display

### Advanced Features
- **Notifications**: User must grant notification permissions for system notifications
- **Full Disk Access**: May be required if reading/writing to protected locations

## Network Requirements

- **Offline Operation**: swiftDialog works completely offline
- **Online Operations**:
  - Checking for updates
  - Displaying web content
  - Downloading remote images

