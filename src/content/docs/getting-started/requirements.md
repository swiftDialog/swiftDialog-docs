---
title: System Requirements
description: macOS version requirements and compatibility for swiftDialog
---

## macOS Requirements

swiftDialog is a universal binary app written using SwiftUI.

### Current Version (2.3+)
- **Minimum macOS version**: macOS 12 (Monterey)
- **Architecture**: Universal Binary (Intel and Apple Silicon)
- **Framework**: SwiftUI

### Legacy Support
- The last version that supports **macOS 11 (Big Sur)** is [v2.2.1](https://github.com/swiftDialog/swiftDialog/releases/tag/v2.2.1)
- Versions prior to 2.0 may support older macOS versions

## Hardware Requirements

swiftDialog runs on all Macs that support the minimum macOS version:

### Intel Macs
- Any Intel Mac that can run macOS 12 or later

### Apple Silicon Macs
- All M1, M2, M3, and newer Apple Silicon Macs
- Runs natively without Rosetta 2

## Dependencies

swiftDialog is a standalone application with no external dependencies. It includes all necessary frameworks within the application bundle.

## Permissions

swiftDialog may require certain permissions depending on usage:

### Basic Operation
- No special permissions required for basic dialog display

### Advanced Features
- **Notifications**: User must grant notification permissions for system notifications
- **Full Disk Access**: May be required if reading/writing to protected locations
- **Screen Recording**: Required if capturing screen content

## Network Requirements

- **Offline Operation**: swiftDialog works completely offline
- **Online Features**:
  - Checking for updates
  - Displaying web content
  - Downloading remote images

## Storage Requirements

- **Application Size**: Approximately 10-15 MB
- **Runtime Storage**: Minimal (temporary files for command processing)