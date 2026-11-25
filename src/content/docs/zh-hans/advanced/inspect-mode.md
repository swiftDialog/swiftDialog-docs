---
title: 检查模式
description: swiftDialog 的“检查模式”入门指南：用于监控安装情况和系统合规性
translationSynced: 2026-11-25T06:08:57+00:00
---


# swiftDialog 检查模式

SwiftDialog 的“检查模式”是一个新的内置功能，可以在 macOS 文件系统中进行实时监控。它跟踪文件系统的状态（利用苹果的 FSEvents API），同时监控应用程序的安装过程，并检查缓存文件夹、文件和 plist 文件的内容，以可视化合规性检查结果。该功能专门设计用于设备注册、软件部署和合规性审计过程，为最终用户提供清晰的合规性状态信息。

## 概述

“检查模式”会持续监控指定的文件夹路径和缓存目录，以跟踪应用程序或系统组件的状态。它通过各种预设的界面布局提供直观的反馈，每个布局都针对不同的使用场景进行优化。


### 主要特点
- 实时文件系统监控。
- 通过缓存监控来检测下载进度。
- 为不同场景提供多种视觉预设。
- 基于plist文件的简单验证（布尔值、字符串和存在性）。
- 可定制的主题和品牌标识（功能有限）。
- 完成操作后，自动启用按钮。

## 入门指南

### 基本用法

1. 创建一个 JSON 配置文件：
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
重要提示：`guiIndex` 必须是唯一的，它决定了图形用户界面 (GUI) 中各项元素的排列顺序。数值越小的元素会首先显示。
:::

2. 启动 swiftDialog 并启用检查模式：
```bash
/usr/local/bin/dialog --inspect-mode --inspect-config /path/to/config.json
```

3. 可以选择性地设置配置文件路径的环境变量：
```bash
export DIALOG_INSPECT_CONFIG="/path/to/config.json"
/usr/local/bin/dialog --inspect-mode
```

## JSON 配置文件参考

### 通用对话选项

检查模式支持一个新的 `options` 对象，它位于 JSON 配置文件中，用于控制对话框的整体行为。 这允许您直接在检查配置中设置窗口属性，而无需传递命令行参数。

```json
{
  "options": {
    "moveable": true,
    "ontop": true,
    "resizable": true,
    "windowbuttons": "min,max,close"
  }
}
```

**可选项：**
- `moveable` (布尔值) - 允许拖动窗口。
- `ontop` (布尔值) - 将窗口置于所有其他窗口之上。
- `resizable` (布尔类型) - 允许调整窗口大小（意味着启用`moveable`）。
- `windowbuttons` (字符串) - 启用窗口按钮：`close`、`min`、`max` (用逗号分隔)。

**优先级：** 命令行参数的优先级高于 JSON 配置选项。

**不支持的选项：** 任何不在允许列表中的选项将被忽略，并会记录相关信息。

好的，请提供需要翻译的英文文本。
```json
{
  "title": "Application Installation",
  "options": {
    "moveable": true,
    "ontop": true
  },
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

### 根级别键

| 关键词。 | 类型。 | 必需的。 | 默认设置。 | 描述。 |
|-----|------|----------|---------|-------------|
| `preset` | 字符串。 | 不。 | “预设1” | 视觉布局预设（预设1-7）。 |
| `title` | 字符串。 | 不。 | “系统检查” | 窗口标题。 |
| `message` | 字符串。 | 不。 | - | 主要信息文本。 |
| `icon` | 字符串。 | 不。 | - | 图标路径或SF Symbols（例如："sf=shield.fill"）。 |
| `size` | 字符串。 | 不。 | “标准” | 窗户尺寸：小号、标准号、大号。 |
| `width` | 整数。 | 不。 | - | 自定义窗口宽度（会覆盖默认尺寸）。 |
| `height` | 整数。 | 不。 | - | 自定义窗口高度（会覆盖尺寸设置）。 |
| `cachePaths` | 数组。 | 不。 | - | 需要监控以检测下载的目录。 |
| `scanInterval` | 整数。 | 不。 | 2 | 文件系统扫描间隔（单位：秒）。 |
| `button1text` | 字符串。 | 不。 | 好的。 | 主要按钮的文本。 |
| `button1disabled` | 布尔代数。 | 不。 | 错误。 | 最初禁用主按钮。 |
| `button2text` | 字符串。 | 不。 | “取消” | 辅助按钮文本。 |
| `button2visible` | 布尔代数。 | 不。 | 正确。 | 显示辅助按钮。 |
| `autoEnableButton` | 布尔代数。 | 不。 | 正确。 | 完成操作后，自动启用按钮。 |
| `autoEnableButtonText` | 字符串。 | 不。 | 好的。 | 自动启用时的按钮文本。 |
| `items` | 数组。 | 是的。 | - | 待检查的项目列表。 |

### 视觉自定义设置选项

| 关键词。 | 类型。 | 默认设置。 | 描述。 |
|-----|------|---------|-------------|
| `banner` | 字符串。 | - | 横幅图片路径（会覆盖图标）。 |
| `bannerHeight` | 整数。 | 100 | 横幅的高度（以像素为单位）。 |
| `bannerTitle` | 字符串。 | - | 横幅上的标题覆盖。 |
| `highlightColor` | 字符串。 | "#808080" | 强调颜色（十六进制代码） |
| `backgroundColor` | 字符串。 | - | 背景颜色（十六进制代码） |
| `backgroundImage` | 字符串。 | - | 背景图片路径。 |
| `backgroundOpacity` | 双倍。 | 1.0 | 背景透明度（0-1）。 |
| `textOverlayColor` | 字符串。 | - | 背景图的文本叠加颜色。 |
| `gradientColors` | 数组。 | - | 用于渐变的十六进制颜色值数组。 |
| `iconBasePath` | 字符串。 | - | 用于相对图标路径的基础路径。 |
| `appearance` | 字符串。 | “自动” 或 “自动模式” | 强制显示检查窗口：`"dark"`、`"light"` 或 `"auto"` (遵循操作系统)。 这会覆盖操作系统中的相关设置，无论方向如何。 |

### 项目配置

数组中的每个元素需要：`items`

| 关键词。 | 类型。 | 必需的。 | 描述。 |
|-----|------|----------|-------------|
| `id` | 字符串。 | 是的。 | 唯一标识符。 |
| `displayName` | 字符串。 | 是的。 | 在用户界面中显示的名称。 |
| `guiIndex` | 整数。 | 是的。 | 排序方式（从0开始）。 |
| `paths` | 数组。 | 是的。 | 需要检查的文件路径，以确认其是否存在。 |
| `icon` | 字符串。 | 不。 | 特定商品的图标。 |
| `plistKey` | 字符串。 | 不。 | 用于验证的 plist 键。 |
| `expectedValue` | 字符串。 | 不。 | 预期的plist值。 |
| `evaluation` | 字符串。 | 不。 | 评估类型： "equals"（等于）、"boolean"（布尔值）、"exists"（存在）、"contains"（包含）、"range"（范围）。 |
| `description` | 字符串。 | 不。 | 可选的描述信息会显示在商品标题下方（由预设选项 1、2、3、5 和 6 渲染）。 |
<!-- | `subtitle` | String | No | Subtitle text (preset6) | --> <!-- | `category` | 字符串 | 否 | 分类分组（预设5） |
| `categoryIcon` | 字符串。 | 不。 | 类别图标（预设5）。 | -->


## 高级功能

### 缓存监控

监控下载目录，以检测正在进行的安装过程。

```json
{
  "cachePaths": [
    "/Library/Managed Installs/Cache",
    "/Library/Application Support/Installomator/Downloads",
    "/Library/Application Support/JAMF/Downloads", 
    "/Library/Application Support/AirWatch/Data/Munki/Managed Installs/Cache"
  ],
  "scanInterval": 5,
  "cacheExtensions": ["download", "pkg", "dmg", "aria2"]
}
```

默认情况下，以 `.pkg`、`.dmg` 和 `.download` 结尾的文件，在 `cachePaths` 目录下，会被标记为“正在下载”。可以通过设置 `cacheExtensions` 来修改这个列表，例如，添加 `aria2` 以便检测 aria2c 的 `<name>.aria2` 部分文件（问题 #617）。 开头的点是可选的。

### Plist 规范性验证

使用 plist 检查来验证系统配置。

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

### 自定义颜色阈值

定义自定义的合规级别和颜色。

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


### 合规仪表盘

对于基于 plist 文件的合规性报告，添加一个顶层数组 `plistSources`。 swiftDialog 将引用的 plist 文件按照类别进行汇总，并计算通过次数、总次数以及总体得分，然后通过 `compliance-summary` 和 `findings-list` 内容块（以及任何 Bento 单元）进行展示，并定期刷新。

```json
{
  "plistSources": [
    {
      "path": "/Library/Preferences/com.company.compliance.plist",
      "type": "compliance",
      "healthyLabel": "Compliant",
      "attentionLabel": "Action Required"
    }
  ],
  "guidance": [
    { "type": "compliance-summary" },
    { "type": "findings-list" }
  ]
}
```

**`plistSources[]` 属性：**

| 关键词。 | 类型。 | 默认设置。 | 描述。 |
|-----|------|---------|-------------|
| `path` | 字符串。 | - | plist 文件的路径。 |
| `type` | 字符串。 | - | 数据来源类型：`compliance`、`health`、`licenses`、`preferences` 或 `custom`。 |
| `healthyLabel` | 字符串。 | “健康” | 用于表示通过的检查项的标签<br>（出现在摘要卡片、发现行以及便当式视图的子标题中）。 |
| `attentionLabel` | 字符串。 | “需要关注” | 用于标识失败的检查结果的标签。 |
| `successValues` | 数组。 | - | 体现成功的价值观。 |
| `expectedValue` | 字符串。 | - | 合规的预期价值。 |
| `findingKey` | 字符串。 | 发现；找到。 | 用于读取检测结果详细信息的子键。 |
| `timestampKey` | 字符串。 | 自动。 | 用于记录上次检查时间的键（自动尝试次数：`lastComplianceCheck`, `LastUpdateCheck`, `lastCheck`, `timestamp`）。 |
| `includePattern` | 字符串。 | - | 用于自动发现功能的键的正则表达式。 |
| `excludeKeys` | 数组。 | - | 需要从自动发现功能中排除的密钥。 |
| `keyMappings` | 数组。 | - | 如何理解特定的plist键。 |
| `maxCheckDetails` | 整数。 | 15 | 每个类别显示的最大项目数量。 |
| `icon` | 字符串。 | - | SF 图标，用于该类别。 |

**用于显示汇总数据的模块。**

- `compliance-summary` — 一个横幅，显示总体状态，以及每个类别的统计信息卡片。
- `findings-list` — 一份按类别分组的、可公开查看的个人检查清单。

Bento 单元格还可以自动链接到相同的数据：单元格的副标题和图标颜色会根据实时数据自动更新，无需额外的 schema 字段。<br>

## 完整示例

### 基础应用程序安装程序

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
定义项目图标的基础路径以简化配置，图像名称在可用时从 `iconBasePath` 加载。否则，为项目指定完整路径。
:::


## 故障排除

### 配置未加载
- 使用 `jq` 或在线验证工具来验证 JSON 语法。
- 检查文件权限（必须可读）。
- 确保环境变量已正确设置。

### 无法检测到的设备/物品
- 请确认文件路径是否完全正确（区分大小写）。
- 检查路径是否需要管理员权限。
- 使用 `cachePaths` 用于检测下载。
- 增加数值，以提高较慢系统的性能。`scanInterval`

### 调试模式
启用调试输出：
```bash
/usr/local/bin/dialog --inspect-mode --debug
```

```bash
export DIALOG_DEBUG=1
/usr/local/bin/dialog --inspect-mode
```

### 常用的环境变量
- `DIALOG_INSPECT_CONFIG`: 配置文件 JSON 文件的路径。
- `DIALOG_DEBUG`: 启用调试日志。
- `DIALOG_COMMAND_FILE`: 自定义命令文件路径。

## 最佳实践

1. **从简单开始：** 从预设配置1开始，并尽量保持配置简洁。
2. **测试路径：** 验证所有文件路径是否存在，或者将来会存在。
3. **使用缓存监控功能：** 添加 `cachePaths` 以进行下载检测。
4. **图标管理：** 将图标存储在中心位置，方便管理。`iconBasePath`
5. **按钮状态：** 使用 `autoEnableButton` 可以提升用户体验。
6. **合适的预设：** 根据使用场景选择预设。
   - 安装跟踪：预设1或2或3。
   - 合规显示：预设模式 4。


