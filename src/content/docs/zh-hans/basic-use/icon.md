---
title: 自定义图标
description: 学习如何在 swiftDialog 中设置和自定义图标、图片和覆盖层
translationSynced: 2026-11-25T05:08:59+00:00
---

##### 目录
 - [基本使用方法](#基本使用方法)
 - [稍微更高级的用法](#稍微更高级的用法)
 - [内置图标](#内置图标)
 - [使用 SF Symbols ](#使用-sf-symbols)
 - [图标叠加](#图标叠加层)
 - [图标大小](#图标大小)
 - [隐藏图标](#隐藏图标)
 - [根据界面模式设置图标](#根据用户界面是深色模式还是浅色模式设置不同的图标深色或浅色)

***


使用 `-i` 或 `--icon` 命令行的选项来指定您希望在图标标题区域显示的图标或图片。

### 用途：

`--icon <file | url | text= >`


## 基本使用方法

swiftDialog 接受 `png` 和 `jpg` 格式的图片，并在图标显示区域显示指定的图片。

图像将被调整大小，以适应图像显示区域，该区域的宽度为170点，高度为260点。

虽然 `png` 是默认设置，但如果指定了 `jpg`，图片会以略微圆角的边框呈现，以获得更柔和的视觉效果。

<img src="https://user-images.githubusercontent.com/3598965/111853793-912e3880-8970-11eb-852f-3d5f7e5d2119.png" width=450>

## 稍微更高级的用法
swiftDialog 可以接受一个应用程序的路径，并使用该应用程序的图标作为图像。

e.g. `--icon /Applications/Safari.app`

<img src="https://user-images.githubusercontent.com/3598965/111853901-e36f5980-8970-11eb-80e2-c3fca298627d.png" width=450>

swiftDialog 还可以接受指向图像资源的 URL。

e.g. `--icon "https://user-images.githubusercontent.com/3598965/111854068-84f6ab00-8971-11eb-935b-487f1a15b91f.png"`

<img src="https://user-images.githubusercontent.com/3598965/111854089-a5bf0080-8971-11eb-95fe-a720206bb10a.png" width=450>

## 设置图标的透明度

使用 `--iconalpha` 来设置透明度值。

范围从`0.0`（完全透明）到`1.0`（完全不透明）。

## 备用图标（深色模式）

使用 `:dark=`，并指定一个备用的图标或路径，以便在用户使用深色模式时进行显示。

e.g. `--icon /path/to/light.png:dark=/path/to/dark.png`

## 内置图标

swiftDialog 包含一些内置的图标，这些图标可以与 `--icon` 选项一起使用。

`--icon info`

![信息图标](https://user-images.githubusercontent.com/3598965/111854259-5e853f80-8972-11eb-9476-e2c5ceed3da9.png)

`--icon caution`

![警告标志](https://user-images.githubusercontent.com/3598965/111854239-46adbb80-8972-11eb-9708-e864a71e3e0a.png)

`--icon warning`

![警告图标](https://user-images.githubusercontent.com/3598965/111854248-52997d80-8972-11eb-9f11-52a0b8a8d650.png)

`--icon computer`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/2ee4c788-bc9a-4328-ac1b-1537bf30dcb7">

## 使用 `text=`

您还可以使用 `text=` 前缀，在图标区域显示文本。这对于显示单个字符或表情符号非常有用。

e.g. `--icon text=👍`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/931fa9f5-0f96-4b32-bf6e-cffa28c26e31">


## 使用 SF Symbols

swiftDialog 还可以显示任何 SF Symbol 图标。https://developer.apple.com/sf-symbols/

### SF Symbols 符号语法（CSV 格式）

在为图标或叠加图标指定 SF Symbols 时，可以提供额外的参数来调整颜色和粗细。

  `"SF=sf.symbol.name,colour=<text><hex>,weight=<text>"`

  `color,colour=<text><hex>` 可以使用十六进制格式指定颜色，例如：#00A4C7。 也可以接受苹果公司标准的颜色 `black`、`blue`、`gray`、`green`、`orange`、`pink`、`purple`、`red`、`white`、`yellow`。 如果选项无效，则默认使用系统颜色 `primary`。

特殊颜色 `"auto"`。

当与彩色 SF 图标一起使用时，将采用该图标的默认颜色方案。如果与单色 SF 图标一起使用，则默认颜色为黑色，并且不会遵循暗色模式。

e.g. `dialog -s -i SF=airplane.circle.fill,colour=auto`

![图片](https://user-images.githubusercontent.com/3598965/126090330-8dc612a9-40f9-99e2-caf41d07903e.png)

可以通过添加额外的 `colour2` 或 `color2` 参数来设置颜色渐变，例如 `SF=applelogo,colour=pink,colour2=purple`

![图片](https://user-images.githubusercontent.com/3598965/170815055-e943c2a4-e846-44d5-b323-bb8be1333438.png)

多色 SF Symbols 可以通过 `palette` 参数进行颜色调整，例如 `SF=person.3.sequence.fill,palette=red,green,blue`。

![图片](https://user-images.githubusercontent.com/3598965/171398294-0a74dcad-b5b2-4dd0-b5b2-4dd0-b320-c65d5d5e8d22.png)

SF Symbol 的粗细程度可以通过 `weight` 参数进行设置。

   `weight=<text>` 可以接受以下任何一种值：
    * 细线（默认）。
    * 光。
    * 常规的；规律的；定期的。
    * 中等。
    * 沉重的；大量的。
    * 粗体。

### 动态的 SF Symbols 图标

macOS 14及更高版本支持动画风格的符号。

示例用法：

`--icon sf=rainbow,colour=auto,animation=variable`

目前，我们仅支持以下类型的动画：
 - “变量：”
 - "variable.reversing" (变量反转)
 - "可变迭代"
 - "变量、迭代、反向"
 - "可变累积值"
 - 脉搏；脉冲。
 - "pulse.bylayer" (此处作为产品或服务的名称，不做翻译)

### JSON 图标对象

图标也可以以 JSON 对象的形式进行定义，这样可以实现更直接的控制。这对于具有多个属性的复杂图标配置尤其有用。

**语法：**
```bash
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'
```

**支持的按键：**
- `sf` / `name` / `symbol` - SF 图标名称
- `path` / `icon` / `value` - 图像或应用程序的文件路径。
- `weight` - 字体粗细 (细体、轻体、常规、中等、粗体、加粗)。
- `colour` / `color` - 主要颜色（十六进制或颜色名称）。
- `colour2` / `color2` - 渐变颜色中的辅助颜色。
- `palette` - 用于多色符号的颜色数组。
- `animation` - 动画类型，用于动画符号（macOS 14 及更高版本）。
- `bgcolour` / `bgcolor` - 用于覆盖图标的背景颜色。
- `auto` - 自动配色方案的特殊值。
- `light` / `dark` - 提供浅色/深色模式的选项（嵌套图标对象）。

**示例：**

```bash
# Basic symbol with colour and weight
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'

# Gradient
dialog --icon '{"sf":"applelogo","colour":"pink","colour2":"purple"}'

# Multicolor palette
dialog --icon '{"sf":"person.3.sequence.fill","palette":["red","green","blue"]}'

# Application icon
dialog --icon '{"path":"/Applications/Chess.app"}'

# Light/dark variants
dialog --icon '{"light":{"sf":"sun.max"},"dark":{"sf":"moon"}}'

# Animated symbol (macOS 14+)
dialog --icon '{"sf":"rainbow","colour":"auto","animation":"variable"}'

# Overlay icon with background
dialog --overlayicon '{"sf":"exclamationmark","colour":"yellow","bgcolour":"none"}'
```

适用于：`--icon`、`--overlayicon`、`--listitem` 图标字段、`--checkbox` 图标字段。

**注意：** 当在 `--listitem` 或 `--checkbox` 中使用时，图标字段可以接受嵌套的 JSON 对象。

```bash
dialog --listitem '{"title":"Download","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}'
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}'
```



## 图标叠加层

使用 `-y` 或 `--overlayicon ` 命令选项来指定您希望用作主图标的叠加图标或图像。

覆盖层以正常分辨率的一半显示，并移至主图标显示区域的右下角。使用此选项，您可以将图像组合在一起进行显示。

覆盖图标可以使用与 `--icon` 参数相同的图像类型和位置，包括内置的图像和 SF Symbols。


示例：

`--icon caution --overlayicon /Applications/Safari.app`

`-i caution -y /Applications/Safari.app`

![警告图标，带有 Safari 叠加图标](https://user-images.githubusercontent.com/3598965/111854381-16b2e800-8973-11eb-9cf9-c2b1d8d8b6b7.png)

示例 2：

`--icon /Applications/Google\ Chrome.app --overlayicon warning`

`-i /Applications/Google\ Chrome.app -y warning`

![带有警告标志的 Chrome 图标](https://user-images.githubusercontent.com/3598965/111888622-2e9d7100-8a32-11eb-9693-e53bb2f42692.png)

### 使用 SF Symbols 时，可以添加背景覆盖层

在使用 SF Symbols 时，会添加一个半透明的圆形边框，以突出符号在主要图标之上的显示效果。这是因为许多符号包含一些元素，如果直接作为叠加层使用，效果可能不太理想。

![图片](https://user-images.githubusercontent.com/3598965/173157681-0dd05429-35db-4872-89a1-8a8e42bf44a4.png)

背景外观可以通过一个调整器进行修改，并且其语法在任何可以设置的参数中都是一致的。 此外，如果不需要覆盖背景，还可以指定一个特殊的颜色。 `bgcolor=` `color` `bgcolor=none`

![图片](https://user-images.githubusercontent.com/3598965/173157715-46fda24b-2cfb-417b-835a-ed452888546d.png)

## 图标大小

`--iconsize <float>` 会将图标调整为指定的宽度。 默认宽度为 `170`。

示例 1：

`--icon caution --overlayicon /Applications/Safari.app --iconsize 300`

![图片](https://user-images.githubusercontent.com/3598965/137573508-a2eb2dfc-cf46-4009-8783-66d8e2040724.png)


示例 2：

`--icon /Applications/Firefox.app --iconsize 100 -s`

![图片](https://user-images.githubusercontent.com/3598965/137573587-0e11823b-dc12-4756-ab4c-8442c4d5f050.png)

## 图标位置

`--centreicon` 或者 `--centericon`

将图标位置调整为居中显示。

![图片](https://user-images.githubusercontent.com/3598965/159693524-551b863d-33db-4af0-b971-a9a08161d525.png)

也可以在 swiftDialog 运行期间，通过命令文件进行修改。

`echo "icon: centre" >> /var/tmp/dialog.log`

## 隐藏图标

可以使用以下任一命令完全删除图标：

`--hideicon`

或者。

`--icon none`

## 根据用户界面是深色模式还是浅色模式，设置不同的图标（深色或浅色）

除了某些 SF Symbols 之外，swiftDialog 本身并没有内置的功能来切换深色模式和浅色模式下的图标。

可以通过调用脚本来根据用户界面设置来设置图标。

**zsh / bash** (感谢 [mm2270](https://github.com/mm2270)))

```bash
#!/bin/zsh

icon_path_dark="/path/to/icondark.png"
icon_path_lite="/path/to/iconlite.png"

logged_in_user=$(/usr/sbin/scutil <<< "show State:/Users/ConsoleUser" | /usr/bin/awk '/Name :/ && ! /loginwindow/ {print $3}')

os_color_mode=$(/usr/bin/defaults read /Users/$logged_in_user/Library/Preferences/.GlobalPreferences.plist AppleInterfaceStyle)

if [ "$os_color_mode" = "Dark" ]; then
	icon_path=$icon_path_dark
else
	icon_path=$icon_path_lite
fi
```

或者，可以使用 Python 语言（感谢 [joncrain](https://github.com/joncrain))）。

```python
from Foundation import NSBundle

def is_dark_mode():
    appearanceBundle = NSBundle.bundleWithPath_(
        "/System/Library/PreferencePanes/Appearance.prefPane"
    )
    appearanceShared = appearanceBundle.classNamed_("AppearanceShared")
    app = appearanceShared.sharedAppearanceAccess()
    if app.theme() == 1:
        return False
    else:
        return True

if is_dark_mode():
    content["icon"] = "dark_icon.png"
else:
    content["icon"] = "light_icon.png"
```