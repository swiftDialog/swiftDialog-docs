---
title: 在移动设备管理（MDM）部署中，使用分阶段的策略实施
description: 使用“门控节奏”类型的步骤，可以创建一个基于实际系统状态的、属性驱动的部署界面，适用于使用Fleet、Jamf、Intune等工具的移动设备管理（MDM）部署
translationSynced: 2026-11-25T05:39:30+00:00
---

这种“分阶段触发”的步骤将部署界面转化为一个**基于属性的**流程：每个消息都会显示，直到满足一个**真实条件**，然后才会进入下一阶段。这些条件是从实际系统状态中读取的，因此界面永远不会在真正完成之前显示“完成”状态。

这与特定的移动设备管理 (MDM) 系统无关。它读取的信号——例如已安装的应用程序、软件包安装记录以及在 `/Library/Managed Preferences/` 下管理的移动配置文件——是由 **Fleet、Jamf、Intune、Mosyle、Kandji、Munki、Installomator** 以及其他类似工具以相同的方式生成的。 以下示例以 **Fleet** 为例进行说明，但其中没有任何内容是特定于 Fleet 的。

## 它如何适应推广计划？

MDM 系统负责执行各项任务（例如安装软件、配置设置），而 swiftDialog 则可以**监控**这些操作。

| 部署任务。 | 节奏属性。 | 它显示的内容。 |
|---|---|---|
| 已安装应用程序。 | `app` (`bundleId`) | `NSWorkspace.urlForApplication(withBundleIdentifier:)` |
| 软件包已安装。 | `file` | 收据于 `/var/db/receipts/<pkgid>.bom`。 |
| “Profile”和“mobileconfig”功能已成功部署。 | **`managedpref`** (`domain`+`key`) | `/Library/Managed Preferences/<domain>.plist` (设备) 或 `…/<user>/<domain>.plist`。 |
| 基于脚本的配置。 | `file` | 一个脚本会访问的标记文件。 |
| 不可直接观察的检查。 | `source:"ipc"` | 一个 MDM 脚本调用了以下组件：`cadence:satisfy:<id>` (osquery、Installomator 日志、MDM API)。 |

**混合驱动：**大多数条目原生轮询（无编排器，可离线 / 在登录窗口运行）；少数 `source:"ipc"` 条目由 MDM 脚本推进，用于无法直接观察的内容。IPC 动词是 `cadence:satisfy:<id>`（也是 `advance` / `goto`）。

`timeout` 如果某个任务永远无法完成，系统会自动进入一种“强制前进”状态，这样即使某个策略执行失败，也不会导致用户界面卡住。

## 两个阶段

由于登录窗口/设置向导阶段**没有用户会话**（没有用户应用程序，只有设备级别的配置），因此使用两个配置方案，启动器会根据不同的会话选择其中一个。

### 阶段A：登录窗口 / 设置向导（仅适用于设备级别）
```json
{
  "preset": "5", "stepType-note": "device phase",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Setting up your Mac",
    "cadenceInterval": 1.0, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "mdm",      "message": "Confirming management…", "sfSymbol": "checkmark.shield.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.mdm", "key": "AccessRights", "evaluation": "exists", "scope": "device" }, "timeout": 600 },
      { "id": "filevault","message": "Enabling disk encryption…", "sfSymbol": "lock.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.MCX.FileVault2", "key": "Enable", "evaluation": "equals", "expectedValue": "On", "scope": "device" }, "timeout": 900 },
      { "id": "rosetta",  "message": "Installing base packages…", "sfSymbol": "shippingbox.fill",
        "attribute": { "type": "file", "path": "/var/db/receipts/com.company.baseline.bom" }, "timeout": 900 }
    ]
  }]
}
```

### B阶段：登录后的桌面环境（完整信号）
```json
{
  "preset": "5",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Installing your apps",
    "cadenceInterval": 0.5, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "edge",    "message": "Installing Microsoft Edge…", "sfSymbol": "globe",
        "attribute": { "type": "app", "bundleId": "com.microsoft.edgemac" }, "timeout": 600 },
      { "id": "office",  "message": "Installing Office…", "sfSymbol": "doc.fill",
        "attribute": { "type": "app", "bundleId": "com.microsoft.Word" }, "timeout": 1200 },
      { "id": "vpn",     "message": "Applying VPN profile…", "sfSymbol": "network",
        "attribute": { "type": "managedpref", "domain": "com.company.vpn", "key": "Enabled", "evaluation": "boolean", "expectedValue": "true", "scope": "device" }, "timeout": 600 },
      { "id": "compliance","message": "Running compliance check…", "sfSymbol": "checkmark.seal.fill",
        "attribute": { "source": "ipc" }, "timeout": 600 }
    ]
  }]
}
```
这个条目 `compliance` 的内容是 `source:"ipc"`：一个移动设备管理 (MDM) 脚本会执行检查（使用 osquery 或厂商提供的 API），然后 `… ipc send "cadence:satisfy:compliance"`。

## （以 Fleet 为例，无论使用哪种 MDM 解决方案，其形状都是相同的。）
1. **包含内容：** swiftDialog 软件 + 启动程序 + 两个 Cadence 格式的 JSON 文件。
2. **配置（mobileconfig）:** 配置启动器，包括每个会话的配置以及登录窗口的设置选项。
   （启动器以同样的方式读取其自身管理的偏好设置——在`/Library/Managed Preferences/`下。）
3. **LaunchAgents**（设备 + 登录窗口）用于在正确的会话中启动 swiftDialog。
4. **GitOps / 策略：** 这指的是 Cadence 监控的配置和软件，以及相关的脚本。
   对于任何条目，都会发出信号 `cadence:satisfy`。`source:"ipc"`

使用`contour`/`fleet-gitops`工具生成移动配置文件（mobileconfig）以及GitOps相关的文件，该工具会验证配置文件是否符合苹果的规范。

## 为每个租户定制的品牌和权益，基于个性化偏好设置

对于多租户部署，设备的“激活码”和“品牌/颜色”等信息可以从配置管理系统中读取，而不是硬编码在系统中。这样，每个租户的移动设备管理（MDM）配置可以提供自己的值，而无需修改出厂设置。两者都使用一个 `ManagedValueRef`:

| 关键词。 | 类型。 | 描述。 |
|---|---|---|
| `domain` | 字符串。 | 受控偏好域，例如：`nl.root3.support` |
| `key` | 字符串。 | 该领域的一个关键参数是颜色的亮度值。 |
| `darkKey` | 字符串。 | 可选的深色模式样式键（仅限颜色）。 |

- `cadenceRef` — reads the cadence claims array (the `CadenceEntry` dicts) from a managed preference, instead of an inline `cadence` array.
- `brandColorRef` —— 从预设的偏好设置中读取品牌/色号（浅色，可选深色）。

```json
{
  "cadenceRef":    { "domain": "nl.root3.support", "key": "claims" },
  "brandColorRef": { "domain": "nl.root3.support", "key": "brandColor", "darkKey": "brandColorDark" }
}
```

因为这些值是从`/Library/Managed Preferences/<domain>.plist`中计算出来的，所以它们与上述的`managedpref`属性一样，具有“在配置文件加载时立即生效”的特性。

<!-- REVIEW: cadenceRef / brandColorRef are documented as top-level keys (alongside the inline `cadence` array). Confirm this matches how they're consumed for all presets. -->

## 注释
- `managedpref` 它直接读取文件，因此一旦配置文件加载完成，就会立即开始执行（无需等待）。
  CFPreferences 缓存延迟。`evaluation:"exists"` = "配置文件存在"; `equals`/`boolean` = "强制使用特定值"。
- 在登录窗口阶段，只有设备级别的范围生效；用户级别的配置和检查则不生效。`app`
  应属于第二阶段。
- 返回到已完成的节奏段落（返回），进行**快速回放**，然后停止。它能做到这一点。`cadenceMinDwell`
  不要重新安装门或悬挂物品。
