---
title: 复选框
description: 在 swiftDialog 中创建交互式复选框和开关
translationSynced: 2026-11-25T05:20:58+00:00
---

复选框可以用来提供多种选项，用户可以选择或不选择这些选项，然后系统会根据用户的选择进行处理。

## 基本使用方法

指定一个或多个`--checkbox <text>`参数后，对话框会显示一个复选框，其标签为`<text>`。

### 风格

复选框也可以以开关的形式显示，而不是传统的复选框样式。

默认情况下，它会以一个复选框的形式显示在标签旁边。

![图片](https://user-images.githubusercontent.com/3598965/235893894-1d4c26ba-1afc-4e9f-a58d-16a36c27787f.png)

使用`--checkboxstyle switch`选项可以更改为开关式设计。

![图片](https://user-images.githubusercontent.com/3598965/235894156-c8cf82e7-d627-43a4-b11e-3acfc296a3e2.png)

如果您更喜欢更大尺寸的开关样式，可以在开关样式设置中指定此项。

选项有 `mini`、`small`、`regular` 或 `large`。

`--checkboxstyle switch,large`

![图片](https://user-images.githubusercontent.com/3598965/235894351-71200445-5871-4e27-b792-2a983a34514c.png)
## 高级用法

当使用[JSON配置](/zh-hans/advanced/json-configuration)来设置对话框的选项时，可以选择性地使用复选框参数。

JSON 数据采用以下格式：

```json
{
  "checkbox" : [
	  {"label" : "<label>", "checked" : false, "disabled" : false, "icon" : "<file|url>" }
	],
 "checkboxstyle" : {
    "style" : "switch",
    "size"  : "regular"
	}
}
```

`"checked" : [true|false]` - 如果设置为`true`，则会初始化复选框为已选中状态。默认情况下，复选框为未选中状态。

`"disabled" : [true|false]` - 如果设置为`true`，则会禁用复选框，无论其当前状态如何。

`"icon" : "<file|url>"` - 当 `checkboxstyle` 设置为 `switch` 时，该参数以 JSON 格式提供；否则，将被忽略。

<img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-16aa041aeeca8ffc.png" width=400>

### 每个论点的 JSON 配置

从版本 3.1.1 开始，复选框也可以通过 `--checkbox` 以 JSON 对象的形式进行配置（而不是使用整个配置文件中的 JSON）。 这种方式提供了更直接的控制，尤其适用于复杂的配置。

**语法：**
```bash
dialog --checkbox '{"label":"Enable telemetry","checked":true,"enableButton1":true}'
```

**特性：**
- `label` - 复选框的标签文本。
- `checked` - 初始状态（真/假，默认：假）。
- `disabled` - 确定复选框是否被禁用（真/假，默认为假）。
- `enableButton1` - 当此复选框被选中（为真）时，启用按钮 1。
- `icon` - 图标路径或 JSON 格式的图标对象（仅在 `switch` 样式下使用）。

**示例：**

```bash
# Basic checkbox
dialog --checkbox '{"label":"I agree to terms"}'

# Checked by default
dialog --checkbox '{"label":"Enable notifications","checked":true}'

# Checkbox that enables Button 1
dialog --checkbox '{"label":"I understand","enableButton1":true}' --button1disabled

# Checkbox with icon (switch style)
dialog --checkbox '{"label":"Enable feature","checked":true,"icon":"/System/Library/CoreServices/Software Update.app"}' --checkboxstyle switch

# Checkbox with JSON icon object
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}' --checkboxstyle switch
```

**注意：** 当使用`enableButton1`时，也应设置`--button1disabled`，以防止用户在勾选复选框之前点击按钮。

### 完整的JSON配置文件

仍然支持完整的 JSON 配置文件格式。

```json
{
  "checkbox" : [
    {"label" : "Option 1", "checked" : true, "disabled" : true },
    {"label" : "Option 2", "checked" : true, "disabled" : false },
    {"label" : "Option 3", "checked" : false }
  ],
  "checkboxstyle" : {
    "style" : "switch",
    "size" : "large"
  }
}
```

### 示例

以下 JSON 示例和相应的对话截图展示了这些设置的工作方式。

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true, "disabled" : false },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5" },
	  {"label" : "Option 6", "disabled" : true }
	]
}
```

![图片](https://user-images.githubusercontent.com/3598965/150663608-6ee03207-0558-4769-a016-44fe5822fccb.png)

## 使用复选框来控制按钮1的状态

您可以使用复选框来控制默认按钮的状态。这在您希望确保用户在继续之前选择了某个必选项时非常有用。

示例：

`dialog --checkbox "I Agree",enableButton1 --button1disabled`

<img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/5a4d2ce4-ea37-447d-86d1-a12ca9d4807e"> <img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/ec12eb71-b6f9-466e-ad32-cb8812bc759c">

这也可以通过 JSON 文件进行设置。

```json
{
  "checkbox" : [
    {"label" : "I Agree", "enableButton1" : true }
  ],
  "button1disabled" : true
}
```

 > 重要的是，一开始应将按钮1设置为禁用状态，否则用户可能会在复选框被选中之前点击该按钮。 默认情况下，该设置并未启用。 此外，应说明，同时设置复选框的`disabled`属性和`enablebutton1`属性是不推荐的，因为这会导致复选框无法被访问。

## 输出

结果会输出到标准输出，默认情况下，其格式如下：
```
Option 1 : true
Option 2 : true
Option 3 : false
Option 4 : true
Option 5 : false
Option 6 : false
```

您可以选择指定`--json`参数，以JSON格式获取结果。

```json
{
  "Option 2" : true,
  "Option 4" : true,
  "Option 5" : false,
  "Option 6" : true,
  "Option 1" : true,
  "Option 3" : false
}
```