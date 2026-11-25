---
title: swiftDialog 工作流程
description: swiftDialog 中的多步骤对话流程
translationSynced: 2026-11-25T05:34:47+00:00
---

> **注意：** 工作流功能是在 swiftDialog 3.1 版本中引入的。

# swiftDialog 工作流程功能文档

## 概述

“工作流程”功能 memungkinkan swiftDialog 实现多步骤的对话流程，让您可以创建类似向导的用户界面，引导用户完成多个输入和信息展示页面。 每个卡片代表一个独立的页面，并具有自己的配置，用户可以通过“工作流程”界面进行前后导航。

工作流程通过 JSON 配置文件进行定义，这使得创建复杂的多步骤对话变得容易，而无需编写代码。

## 主要特点

- **多步骤工作流程：** 将复杂的对话分解为易于管理的步骤。
- **导航控制：** 自动的“下一页”、“上一页”、“完成”按钮。
- **条件分支：** 根据下拉菜单的选择或复选框的状态，将流程引导至不同的工作卡，无需任何回调脚本。
- **数据持久性：** 用户输入的内容在工作流程卡片之间切换时会被保存。
- **全局默认设置：** 定义一次常用的设置，然后可以针对每个卡片进行个性化修改。
- **变量替换：** 使用 `{fieldname}` 语法，可以引用之前工作流程卡中的参考值。
- **验证：** 在继续之前，需要对必填字段进行验证。
- **动态配置：** 每个卡片可以拥有独特的界面元素和设置。
- **回调函数：** 在工作流程卡片之间切换时，执行 shell 脚本。

## 基本概念

### 工作流程结构

一个基于工作流程的对话定义在一个 JSON 配置文件中，其结构如下：

```json
{
  "workflow": [
    { "title": "Step 1", "message": "First screen..." },
    { "title": "Step 2", "message": "Second screen..." },
    { "title": "Step 3", "message": "Final screen..." }
  ]
}
```

### 全局配置

位于根级别（即不在 `workflow` 数组内的）的属性，将作为所有工作流程卡的默认设置。单个工作流程卡可以覆盖这些默认设置：

```json
{
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertNoteIcon.icns",
  "button1text": "Continue",
  "workflow": [
    { "title": "Step 1", "message": "Uses default icon" },
    { "title": "Step 2", "icon": "SF=checkmark.circle", "message": "Custom icon" }
  ]
}
```

### 卡片识别

卡片会根据它们在数组中的位置自动排序。 您可以选择指定一个自定义的排序规则 `id`。

```json
{
  "workflow": [
    { "id": 0, "title": "First" },
    { "id": 10, "title": "Second" },
    { "id": 5, "title": "Third (will be displayed second)" }
  ]
}
```

## 导航

### 按钮行为

在工作流程模式下，按钮的行为会自动改变：

- **按钮 1** (右侧)：
  - 在工作流程卡片 1 到 n-1 上显示“下一步”字样。
  - 在最后一张卡片上显示“完成”字样（或者通过`button1text`自定义文本）。
  - 在继续下一步之前，会验证必填字段是否已填写。
  
- **按钮 2**（左侧）：
  - 隐藏在第一张卡片上。
  - 在工作流程卡片2到n上显示“上一个”字样。
  - 反向操作时，不进行验证。

### 自定义按钮文本

默认情况下，导航按钮显示“下一页”、“上一页”和“完成”。您可以修改这些按钮的显示内容：

- `--nextbuttontext "<text>"` — “下一步”按钮上的文字（默认值：`Next`）。
- `--previousbuttontext "<text>"` — “上一页”按钮的文本（默认值：`Previous`）。
- `button1text` (顶级或每个卡片) — 用于“**完成**”按钮的文本。

```bash
dialog --jsonfile config.json --nextbuttontext "Continue" --previousbuttontext "Back"
```

### 导航流程

<img width="650" alt="image" src="/images/navigation-flow.png" />


## 分层导航

默认情况下，工作流程卡片会按照数组的顺序进行访问。 您可以通过以下三个可选的、针对每个卡片的属性来更改此顺序：

| 房产；财产。 | 类型。 | 目的。 |
|---|---|---|
| `branch` | 物体；目标；对象；目的。 | 根据当前牌上的某个字段值，选择下一张牌。 |
| `nextpage` | 整数。 | 静态覆盖 — 在“下一步”后，转到这张卡片 `id`。 |
| `finalpage` | 布尔型。 | 这张卡片会终止工作流程；下一步操作变为“完成”。 |

当用户点击“下一步”按钮时，swiftDialog 会按照以下顺序解析目标地址：

1. `branch` (如果已设置且找到了匹配的规则)
2. `nextpage` (如果已设置)
3. 卡片队列中的下一个卡片。
4. 工作流程结束（如果不存在下一个步骤，或者 `finalpage` 为真）。

“上一步”按钮具有历史记录功能：它会返回用户实际进入的那个页面，而不是简单地返回“当前索引 - 1”。 这种功能在不同分支下都能正常工作。

> swiftDialog 不会检查是否存在循环或无法访问的卡片。如果您的工作流程可以自我循环，用户只会重新访问那些卡片。如果这不是您的意图，请检查工作流程的逻辑。

### 从下拉菜单中展开

`branch.field` 的值与字段的 `name`（首选）或其 `title`/`label` 匹配。对于下拉菜单，所选值将与 `branch.map` 中的键进行比较：

```json
{
  "workflow": [
    {
      "id": 1,
      "title": "Choose your path",
      "message": "Pick an option to control which card appears next.",
      "selectitems": [
        {
          "name": "userType",
          "title": "Account type",
          "values": ["Admin", "Standard", "Guest"],
          "default": "Standard"
        }
      ],
      "branch": {
        "field": "userType",
        "map": {
          "Admin":    10,
          "Standard": 20,
          "Guest":    30
        },
        "default": 99
      }
    },
    { "id": 10, "title": "Admin setup", "nextpage": 99 },
    { "id": 20, "title": "Standard setup", "nextpage": 99 },
    { "id": 30, "title": "Guest setup", "nextpage": 99 },
    { "id": 99, "title": "Summary", "finalpage": true }
  ]
}
```

`branch.default`是可选的。如果设置了该选项，并且所选值未出现在`map`中，则工作流程将进入到指定的备用卡片。

### 从复选框开始的分支

对于单个布尔字段，请使用 `ifTrue` / `ifFalse` 这种简写方式，而不是 `map`：

```json
{
  "id": 5,
  "checkbox": [
    { "name": "wantsExtras", "label": "Show advanced options" }
  ],
  "branch": {
    "field": "wantsExtras",
    "ifTrue":  6,
    "ifFalse": 99
  }
}
```

您也可以使用 `map` 结合键 `"true"` 和 `"false"`，但这会让内容读起来不够清晰。 `ifTrue`/`ifFalse` 的表达方式更易于理解。

### 静态覆盖 `nextpage`

如果不需要动态路由，但希望一张卡片可以跳过某些步骤，请设置 `nextpage`：

```json
{ "id": 3, "title": "Optional details", "nextpage": 10 }
```

### 提前结束工作流程

您可以将任意卡片标记为“最终状态”，以停止在该环节的工作流程。

```json
{ "id": 99, "title": "Summary", "finalpage": true }
```

在最后一个卡片上，按钮 1 显示“完成”字样，当用户点击该按钮时，对话框会被关闭，而不会受到数组中还剩余多少工作流程卡片数量的影响。

## 使用示例

### 示例 1：简单三步引导流程

```json
{
  "title": "Setup Wizard",
  "icon": "SF=gearshape.2",
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to the setup wizard. Click Continue to begin."
    },
    {
      "title": "Enter Information",
      "message": "Please provide your details:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email Address", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Setup is complete! Click Finish to close this wizard.",
      "button1text": "Finish"
    }
  ]
}
```

运行它。
```bash
dialog --jsonfile /path/to/config.json
```

### 示例 2：使用变量替换

变量替换功能允许您使用 `{fieldname}` 语法，引用之前工作流程卡片中的值。

```json
{
  "title": "User Registration",
  "workflow": [
    {
      "title": "Personal Information",
      "message": "Step 1: Enter your details",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true }
      ]
    },
    {
      "title": "Confirmation",
      "message": "Hello {First Name} {Last Name}! Please confirm your information is correct.",
      "infobox": "**Name:** {First Name} {Last Name}"
    }
  ]
}
```

卡片 2 中的 `{First Name}` 和 `{Last Name}` 占位符将分别替换为卡片 1 中输入的值。

### 示例 3：全局默认设置，并可进行覆盖

```json
{
  "icon": "SF=info.circle",
  "width": 600,
  "height": 400,
  "workflow": [
    {
      "title": "Introduction",
      "message": "This card uses the default icon and size."
    },
    {
      "title": "Custom Layout",
      "icon": "SF=wrench.and.screwdriver",
      "width": 800,
      "height": 500,
      "message": "This card has a custom icon and larger size."
    },
    {
      "title": "Back to Normal",
      "message": "This card reverts to default icon and size."
    }
  ]
}
```

### 示例 4：跨多个步骤的数据收集

```json
{
  "title": "System Configuration",
  "icon": "/System/Library/PreferencePanes/Appearance.prefPane/Contents/Resources/AppIcon.icns",
  "workflow": [
    {
      "title": "Network Settings",
      "message": "Configure network preferences:",
      "selectitems": [
        {
          "title": "Network Type",
          "values": ["WiFi", "Ethernet", "VPN"],
          "default": "WiFi"
        }
      ]
    },
    {
      "title": "User Preferences",
      "message": "Set user preferences:",
      "checkbox": [
        { "label": "Enable notifications", "checked": true },
        { "label": "Auto-update", "checked": true },
        { "label": "Send analytics", "checked": false }
      ]
    },
    {
      "title": "Summary",
      "message": "Review your settings:",
      "infobox": "**Network:** {Network Type}\\n\\n**Notifications:** {Enable notifications}\\n**Auto-update:** {Auto-update}\\n**Analytics:** {Send analytics}"
    }
  ]
}
```

### 示例 5：带有卡片的进度指示器

```json
{
  "title": "Installation Wizard",
  "workflow": [
    {
      "title": "Preparing (1 of 3)",
      "message": "Preparing installation...",
      "progress": 100,
      "progresstext": "Checking system requirements"
    },
    {
      "title": "Installing (2 of 3)",
      "message": "Installing software...",
      "progress": 100,
      "progresstext": "Copying files"
    },
    {
      "title": "Complete (3 of 3)",
      "message": "Installation complete!",
      "icon": "SF=checkmark.circle.fill",
      "progress": 100,
      "progresstext": "Finished"
    }
  ]
}
```

### 示例 6：必填字段验证

```json
{
  "title": "Registration Form",
  "workflow": [
    {
      "title": "Account Details",
      "message": "All fields marked with * are required",
      "textfield": [
        { "title": "Username", "required": true, "prompt": "Enter username" },
        { "title": "Password", "required": true, "secure": true },
        { "title": "Confirm Password", "required": true, "secure": true }
      ]
    },
    {
      "title": "Contact Information",
      "message": "Please provide at least one contact method",
      "textfield": [
        { "title": "Email", "required": true },
        { "title": "Phone", "required": false }
      ]
    }
  ]
}
```

如果用户尝试点击“下一步”，但未填写必填字段，则会显示一个错误提示页面。

## 高级功能

### 工作流程特定的属性

任何标准的 swiftDialog 属性都可以用于工作流程中。 常见的属性包括：

- 布局：`width`，`height`，`position`
- 内容：`title`，`message`，`icon`，`iconsize`
- **输入：** `textfield`，`selectitems`，`checkbox`，`radio`
- 显示：`image`，`video`，`webcontent`，`listitem`
- **进度：** `progress`，`progresstext`
- 信息：`infobox`，`helpmessage`
- **样式**: `messagefont`, `alignment`, `bannerimage`
- 导航：`branch`，`nextpage`，`finalpage`（请参阅“分层导航”](#分层导航)）。

### 输入字段的命名

为了确保变量替换功能正常工作，输入字段的命名应保持一致。

```json
{
  "textfield": [
    { "title": "First Name" }  // Referenced as {First Name}
  ],
  "selectitems": [
    { "title": "Department", "values": ["IT", "HR", "Sales"] }  // Referenced as {Department}
  ]
}
```

如果一个字段没有显式的`title`，你可以使用一个`name`属性：

```json
{
  "textfield": [
    { "title": "Your Name", "name": "username" }  // Referenced as {username}
  ]
}
```

### 数据持久性

用户输入会自动保存，当：
- 点击“下一步”按钮，可以进入下一张卡片。
- 点击“上一步”按钮可以返回。

当用户返回到之前的页面时，他们的输入内容会被恢复。

### 访问卡片数据

当用户点击最后一个卡片上的“完成”按钮时，所有收集到的输入数据将以 JSON 格式输出到标准输出（stdout）。

```json
{
  "First Name": "John",
  "Last Name": "Doe",
  "Email Address": "john.doe@example.com",
  "Department": "IT",
  "Enable notifications": true
}
```

### 关于预付款的回调机制

使用 `--onadvance` 选项，可以在工作流卡片之间切换时执行一个 shell 命令。

```bash
dialog --jsonfile config.json --onadvance "/path/to/script.sh"
```

该脚本接收：
- 卡片索引（从0开始）。
- 卡片识别码（如果已指定）。
- 当前卡片信息以 JSON 格式通过标准输入接收。

脚本应该以以下方式退出：
- **退出码 0：** 允许继续。
- **退出码非零：** 阻止进程继续执行，并显示错误信息。

示例回调脚本：
```bash
#!/bin/bash
# script.sh - Validate email format before advancing

input=$(cat)
email=$(echo "$input" | jq -r '.["Email Address"]')

if [[ ! "$email" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$ ]]; then
    echo "Invalid email address format"
    exit 1
fi

exit 0
```

## 最佳实践

### 1. 保持工作流程的专注性
每张卡片应该只有一个明确的目的。不要在同一张卡片上添加过多的字段，以免让用户感到困惑。

### 2. 使用具有描述性的标题
卡片标题应清晰地表明用户所处的步骤。
```json
{ "title": "Step 1: Personal Information" }
{ "title": "Step 2: Contact Details" }
{ "title": "Step 3: Review & Confirm" }
```

### 3. 提供背景信息
使用消息字段来解释用户需要执行的操作：
```json
{
  "title": "Account Setup",
  "message": "Create your account by choosing a username and password. Your username must be at least 6 characters."
}
```

### 4. 使用必填字段验证
请将必填字段标记为“必填”，以确保数据的完整性。
```json
{ "title": "Email", "required": true }
```

### 5. 提供摘要卡片
请包含一张最终的审查卡，上面应显示所有收集到的信息。
```json
{
  "title": "Review Your Information",
  "message": "Please verify everything is correct before proceeding.",
  "infobox": "**Name:** {Full Name}\\n**Email:** {Email}\\n**Department:** {Department}"
}
```

### 6. 考虑导航流程
- 不要让第一张卡片需要用户输入大量信息，而是要让用户更容易上手。
- 将最重要的数据收集工作安排在早期进行。
- 保存确认/审核信息，以便最终确认卡片。

### 7. 保持一致的排版风格
为确保界面的一致性，设置全局默认设置。
```json
{
  "icon": "SF=person.crop.circle",
  "width": 700,
  "height": 450,
  "messagefont": "size=13",
  "workflow": [ /* ... */ ]
}
```

## 限制与注意事项

1. **命令文件更新：** 在使用命令文件进行工作流模式时，某些动态更新功能可能无法按预期工作。工作流模式主要用于收集输入信息，而不是用于动态状态更新。

2. **按钮自定义：** 按钮 1 和 按钮 2 的功能由工作流模式控制，在工作流模式下，这两个按钮的功能无法完全自定义。

3. **退出码：** 在工作流模式下，对话框只有在以下情况下才会退出：
   - 用户点击了最后一张卡片上的“完成”按钮（退出码为0）。
   - 用户取消操作（退出码可能不同）。
   - 验证失败，用户选择取消操作。

4. **变量范围：** 来自之前工作流程卡片的变量只能在后续卡片中使用，而不能在之前的卡片中使用。变量的替换是单向的。

5. **字段命名：** 为了正确进行变量替换，请在字段标题中使用字母、数字和空格。特殊字符可能会导致问题。

## 故障排除

### 卡片未显示
- 使用 `jsonlint` 或类似工具检查 JSON 语法。
- 确保数组位于根级别。`workflow`
- 确认至少定义了一个卡片。

### 未被替换的变量
- 确保字段名称完全匹配（区分大小写）。
- 请检查变量引用是否使用了花括号：`{fieldname}`
- 确认所参考的字段是否位于之前的卡片上，而不是当前或未来的卡片上。

### 验证功能无法正常工作
- 确认`"required": true`已设置在相关字段中。
- 检查该字段是否具有 `title` 或 `name` 属性。
- 使用带有 `--debug` 标志的调试日志进行审查。

### “上一页”按钮未显示
- 请确认您不在第一个工作流程卡片上（在第一个卡片上，上一张卡片是隐藏的）。
- 请确认工作流模式是否已启用（即工作流数组是否存在）。

### 分行误操作，将款项转入错误的账户
- 确认 `branch.field` 是否与字段的 `name` 相匹配（如果未设置名称，则与字段的 `title`/`label` 相匹配）。
- 对于下拉菜单，映射键与用户选择的值进行完全相同的比较，大小写和空格都非常重要。
- 对于复选框，建议优先使用 `ifTrue`/`ifFalse` 这样的映射键，而不是 `"true"`/`"false"`。
- 检查 swiftDialog 的日志，无效的`nextpage`/`branch`目标会在加载时被报告。

## 完整示例：员工入职引导工具

```json
{
  "title": "Employee Onboarding",
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/UserIcon.icns",
  "width": 750,
  "height": 500,
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome to the Company!",
      "message": "## Welcome Aboard!\\n\\nThis wizard will guide you through the onboarding process.\\n\\nClick Continue to get started.",
      "icon": "SF=hands.clap.fill",
      "iconsize": 120
    },
    {
      "title": "Personal Information",
      "message": "Please provide your personal details (all fields required):",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true },
        { "title": "Employee ID", "required": true },
        { "title": "Work Email", "required": true, "prompt": "name@company.com" }
      ]
    },
    {
      "title": "Department Assignment",
      "message": "Select your department and role:",
      "selectitems": [
        {
          "title": "Department",
          "values": ["Engineering", "Marketing", "Sales", "HR", "Finance"],
          "default": "Engineering"
        },
        {
          "title": "Role",
          "values": ["Manager", "Senior", "Mid-level", "Junior"],
          "default": "Mid-level"
        }
      ]
    },
    {
      "title": "System Preferences",
      "message": "Configure your system preferences:",
      "checkbox": [
        { "label": "Enable email notifications", "checked": true },
        { "label": "Join company Slack", "checked": true },
        { "label": "Subscribe to company newsletter", "checked": true },
        { "label": "Opt-in to mentorship program", "checked": false }
      ]
    },
    {
      "title": "Review & Confirm",
      "message": "Please review your information before completing the onboarding process:",
      "icon": "SF=checkmark.circle",
      "infobox": "**Name:** {First Name} {Last Name}\\n**Employee ID:** {Employee ID}\\n**Email:** {Work Email}\\n\\n**Department:** {Department}\\n**Role:** {Role}\\n\\n**Email Notifications:** {Enable email notifications}\\n**Slack:** {Join company Slack}\\n**Newsletter:** {Subscribe to company newsletter}\\n**Mentorship:** {Opt-in to mentorship program}",
      "button1text": "Complete Onboarding"
    }
  ]
}
```

将此内容保存为 `onboarding.json`，然后运行。
```bash
dialog --jsonfile onboarding.json
```

## 集成示例：Shell 脚本

以下是一个完整的 shell 脚本示例，它使用了工作流模式并处理了输出结果：

```bash
#!/bin/bash

# onboarding.sh - Employee onboarding with swiftDialog workflow

DIALOG="/usr/local/bin/dialog"
CONFIG="/tmp/onboarding_config.json"

# Create the JSON configuration
cat > "$CONFIG" << 'EOF'
{
  "title": "Employee Onboarding",
  "icon": "SF=person.crop.circle.badge.checkmark",
  "width": 700,
  "height": 450,
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to Company XYZ! This wizard will set up your account."
    },
    {
      "title": "Enter Details",
      "message": "Please provide your information:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Onboarding complete for {Full Name}!",
      "infobox": "We'll send a confirmation to {Email}"
    }
  ]
}
EOF

# Run dialog and capture output
if output=$("$DIALOG" --jsonfile "$CONFIG" 2>&1); then
    echo "Onboarding completed successfully!"
    echo "Collected data:"
    echo "$output" | jq .
    
    # Extract specific fields
    full_name=$(echo "$output" | jq -r '.["Full Name"]')
    email=$(echo "$output" | jq -r '.Email')
    
    echo "Processing onboarding for $full_name ($email)..."
    
    # Add your custom logic here
    # - Create user account
    # - Send welcome email
    # - Configure systems
    
else
    echo "Onboarding was cancelled or failed"
    exit 1
fi

# Cleanup
rm -f "$CONFIG"
```

## 摘要

swiftDialog中的工作流功能提供了一种强大的方法，可以使用简单的JSON配置来创建多步骤、类似向导的界面。其主要优势包括：

- **简化复杂的工作流程** - 将复杂的过程分解为易于管理的步骤。
- **内置导航** - 自动显示“下一页”、“上一页”、“完成”按钮。
- **数据收集** - 轻松收集并验证用户在多个界面上的输入信息。
- **灵活的配置** - 可以使用全局默认设置，也可以为每个工作流程单独设置参数。
- **变量替换** - 在后续的工作流程卡片中，可以引用之前工作流程卡片中的值。
- **无需编写代码** - 所有配置均以 JSON 格式定义。

有关 swiftDialog 各个选项和参数的更多信息，请参考 swiftDialog 的主文档，或者使用 `dialog --help`。
