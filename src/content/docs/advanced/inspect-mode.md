---
title: Inspect Mode
description: Starter guide to swiftDialog's Inspect Mode - monitoring installations and system compliance
---


# swiftDialog Inspect Mode

The SwiftDialog Inspect Mode is a new built-in feature that enables real-time monitoring within the macOS filesystem. It tracks filesystem status (utilizing Apple's FSEvents API) while monitoring application installations and inspecting cache folders, files, and plist content to visualize compliance checks. This feature is specifically designed for use during device enrollment, software deployment, and compliance auditing, providing end users with clear visibility into their compliance status.

## Overview

Inspect Mode continuously monitors the specified file paths and cache directories to track the status of applications or system components. It provides visual feedback through various preset layouts, each tailored for different use cases.


### Key Features
- Real-time file system monitoring
- Download progress detection via cache monitoring
- Multiple visual presets for different scenarios
- Plist-based simple validation (bool, string, and exists)
- Customizable theming and branding (limited)
- Auto-enabling buttons upon completion

## Getting Started

### Basic Usage

1. Create a JSON configuration file:
```json
{
  "title": "Application Installation",
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}

```
:::tip[order of items]
Important: guiIndex must be unique and sets the order of the items in the GUI. Lower numbers are displayed first.
:::

2. Set the environment variable:
```bash
export DIALOG_INSPECT_CONFIG="/path/to/config.json"
```

3. Launch swiftDialog with inspect flag:
```bash
/usr/local/bin/dialog --inspect
```

## JSON Configuration Reference

### Root Level Keys

| Key | Type | Required | Default | Description |
|-----|------|----------|---------|-------------|
| `preset` | String | No | "preset1" | Visual layout preset (preset1-7) |
| `title` | String | No | "System Inspection" | Window title |
| `message` | String | No | - | Main message text |
| `icon` | String | No | - | Icon path or SF Symbol (e.g., "sf=shield.fill") |
| `size` | String | No | "standard" | Window size: "compact", "standard", "large" |
| `width` | Integer | No | - | Custom window width (overrides size) |
| `height` | Integer | No | - | Custom window height (overrides size) |
| `cachePaths` | Array | No | - | Directories to monitor for downloads |
| `scanInterval` | Integer | No | 2 | File system scan interval in seconds |
| `button1text` | String | No | "OK" | Primary button text |
| `button1disabled` | Boolean | No | false | Disable primary button initially |
| `button2text` | String | No | "Cancel" | Secondary button text |
| `button2visible` | Boolean | No | true | Show secondary button |
| `autoEnableButton` | Boolean | No | true | Auto-enable button when complete |
| `autoEnableButtonText` | String | No | "OK" | Button text when auto-enabled |
| `items` | Array | **Yes** | - | Array of items to inspect |

### Visual Customization Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `banner` | String | - | Banner image path (overrides icon) |
| `bannerHeight` | Integer | 100 | Banner height in pixels |
| `bannerTitle` | String | - | Title overlay on banner |
| `highlightColor` | String | "#808080" | Accent color (hex) |
| `backgroundColor` | String | - | Background color (hex) |
| `backgroundImage` | String | - | Background image path |
| `backgroundOpacity` | Double | 1.0 | Background opacity (0-1) |
| `textOverlayColor` | String | - | Text overlay color for backgrounds |
| `gradientColors` | Array | - | Array of hex colors for gradient |
| `iconBasePath` | String | - | Base path for relative icon paths |

### Items Configuration

Each item in the `items` array requires:

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `id` | String | **Yes** | Unique identifier |
| `displayName` | String | **Yes** | Display name in UI |
| `guiIndex` | Integer | **Yes** | Sort order (0-based) |
| `paths` | Array | **Yes** | File paths to check for existence |
| `icon` | String | No | Item-specific icon |
<!-- | `subtitle` | String | No | Subtitle text (preset6) | -->
| `plistKey` | String | No | Plist key to validate |
| `expectedValue` | String | No | Expected plist value |
| `evaluation` | String | No | Evaluation type: "equals", "boolean", "exists", "contains", "range" |
<!-- | `category` | String | No | Category grouping (preset5) |
| `categoryIcon` | String | No | Category icon (preset5) | -->

## Preset Layouts

### Preset 1: Classic Sidebar
Traditional sidebar layout with icon, progress bar, and item list. Best for standard application installations.

```json
{
  "preset": "preset1",
  "title": "Installing Applications",
  "icon": "sf=apps.iphone.badge.plus"
}
```
<img width="500" alt="image" src="/inspect/preset_1.png" />

### Preset 2: Card Style
Features a logo or top banner image with streamlined Card item display. Ideal for branded deployments.

```json
{
  "preset": "preset2",
  "banner": "/path/to/banner.png",
  "bannerHeight": 120,
  "bannerTitle": "Company Setup"
}
```
<img width="500" alt="image" src="/inspect/preset_2.png" />

### Preset 3: Condensed List
This is a condensed list layout with a logo or top banner image. Automatically scrolls through items, highlighting current installations.

```json
{
  "preset": "preset3",
  "sideMessage": ["Installing core apps...", "Please wait..."],
  "sideInterval": 5
}
```

<img width="500" alt="image" src="/inspect/preset_3.png" />

### Preset 4: Dashboard
Modern dashboard layout with cards and status indicators. Great for system compliance overview screens.

```json
{
  "preset": "preset4",
  "style": "cards",
  "highlightColor": "#007AFF",
  "gradientColors": ["#1e3c72", "#2a5298", "#7e8ba3"],
}
```

<img width="500" alt="image" src="/inspect/preset_4.png" />

## Advanced Features

### Cache Monitoring

Monitor download directories to detect in-progress installations:

```json
{
  "cachePaths": [
    "/Library/Managed Installs/Cache",
    "/Library/Application Support/Installomator/Downloads",
    "/Library/Application Support/JAMF/Downloads", 
    "/Library/Application Support/AirWatch/Data/Munki/Managed Installs/Cache"
  ],
  "scanInterval": 5
}
```

The system will detect `.pkg`, `.dmg`, and `.download` files matching item IDs.

### Plist Compliance Validation

Validate system configuration using plist checks:

```json
{
  "preset": "preset5",
  "items": [{
    "id": "findmymac",
    "displayName": "Find My Mac Status",
    "guiIndex": 0,
    "paths": ["/Library/Preferences/com.apple.FindMyMac.plist"],
    "plistKey": "FMMEnabled",
    "expectedValue": "true",
    "evaluation": "boolean"
  }]
}
```

### Custom Color Thresholds

Define custom compliance levels and colors:

```json
{
  "colorThresholds": {
    "excellent": 0.95,
    "good": 0.80,
    "warning": 0.60,
    "excellentColor": "#00C853",
    "goodColor": "#2196F3",
    "warningColor": "#FF9800",
    "criticalColor": "#F44336"
  }
}
```
## Example Card design

```json
  {
    "preset": "preset4",
    "title": "Security Compliance",
    "icon": "sf=shield.checkered,colour=#16a34a,weight=bold",
    "items": [
      {
        "id": "os_gatekeeper",
        "displayName": "Gatekeeper",
        "guiIndex": 0,
        "paths": ["/Library/Preferences/com.apple.systempolicy.control.plist"],
        "plistKey": "EnableAssessment",
        "expectedValue": "true",
        "evaluation": "boolean",
        "icon": "sf=shield.lefthalf.filled,colour=#16a34a,weight=bold"
      },
      {
        "id": "ssh_disable",
        "displayName": "SSH Disabled",
        "guiIndex": 2,
        "paths": ["/System/Library/LaunchDaemons/ssh.plist"],
        "plistKey": "Disabled",
        "expectedValue": "true",
        "evaluation": "boolean",
        "icon": "sf=network.badge.shield.half.filled,colour=#0891b2,weight=bold"
      }
    ]
  }
```

<img width="500" alt="image" src="/inspect/preset_4_compliance.png" />

## Complete Examples

### Basic Application Installer

```json
{
  "title": "Installing Office Suite",
  "message": "Please wait while we install your applications",
  "preset": "preset1",
  "icon": "sf=apps.iphone.badge.plus",
  "iconBasePath":"/Users/Shared/icons/",
  "cachePaths": ["/Users/Shared/Downloads"],
  "button1text": "Please Wait...",
  "button1disabled": true,
  "autoEnableButton": true,
  "autoEnableButtonText": "Continue",
  "items": [
    {
      "id": "microsoft_word",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"],
      "icon": "Microsoft Word.png"
    },
    {
      "id": "microsoft_excel",
      "displayName": "Microsoft Excel",
      "guiIndex": 1,
      "paths": ["/Applications/Microsoft Excel.app"],
      "icon": "Microsoft Excel.png"
    },
    {
      "id": "microsoft_powerpoint",
      "displayName": "Microsoft PowerPoint",
      "guiIndex": 2,
      "paths": ["/Applications/Microsoft PowerPoint.app"],
      "icon": "Microsoft PowerPoint.png"
    }
  ]
}
```
:::tip[iconBasePath]
Define a base path for item icons to simplify configuration, image names are loaded from `iconBasePath` when available. Otherwise, specify full path for an item.
:::


## Troubleshooting

### Configuration Not Loading
- Verify JSON syntax using `jq` or online validators
- Check file permissions (must be readable)
- Ensure environment variable is properly exported

### Items Not Detecting
- Verify exact file paths (case-sensitive)
- Check if paths require admin privileges
- Use `cachePaths` for download detection
- Increase `scanInterval` for slower systems

### Debug Mode
Enable debug output:
```bash
export DIALOG_DEBUG=1
/usr/local/bin/dialog --inspect
```

### Common Environment Variables
- `DIALOG_INSPECT_CONFIG`: Path to configuration JSON
- `DIALOG_DEBUG`: Enable debug logging
- `DIALOG_COMMAND_FILE`: Custom command file path

## Best Practices

1. **Start Simple**: Begin with preset1 and minimal configuration
2. **Test Paths**: Verify all file paths exist or will exist
3. **Use Cache Monitoring**: Add `cachePaths` for download detection
4. **Icon Management**: Store icons in a central location with `iconBasePath`
5. **Button States**: Use `autoEnableButton` for better UX
6. **Appropriate Presets**: Choose presets based on use case:
   - Installation tracking: Preset 1 or 2 or 3
   - Compliance display: Preset 4


