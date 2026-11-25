---
title: 演示脚本
description: 完整的应用程序选择和安装演示脚本
translationSynced: 2026-11-25T05:43:29+00:00
---

一个完整的演示套件可以在 https://github.com/swiftDialog/demo 处找到。

## swiftDialog 完整演示套件

这是一组 zsh 脚本集合，通过一个交互式、自助导览的方式，展示了 [swiftDialog](https://github.com/swiftDialog/swiftDialog)) 的所有主要功能。

## 要求

- macOS 15 或更高版本。
- [**swiftDialog 3 or newer**](https://github.com/swiftDialog/swiftDialog/releases)

## 快速入门指南

```zsh
# clone this repo
git clone https://github.com/swiftDialog/demo.git swiftDialog-demo

# or download the zip
curl -sL "https://github.com/swiftDialog/demo/archive/refs/heads/main.zip" -o swiftDialog-demo.zip && unzip swiftDialog-demo.zip -d swiftDialog-demo

cd swiftDialog-demo
./run_demos.zsh
```

主控制器本身就使用了 swiftDialog，您可以选择带有复选框的演示示例，然后逐个进行体验。

## 用于 swiftDialog 内容创作的人工智能技能

**初次使用 swiftDialog？** 建议从官方的 [swiftDialog Builder 页面](https://swiftdialog.app/builder/builder/)) 开始，用于了解基本功能和进行可视化原型设计。然后，可以使用仓库中提供的技能包，将这些理解转化为符合仓库风格的 shell 脚本。 Builder 工具非常有用，但它并不全面，也无法替代最终的尺寸调整、清理和工作流程决策。

### 可用技能

**[`codex-swiftdialog-builder`](skills/codex-swiftdialog-builder/)** — 适用于 GitHub Copilot / OpenAI Codex。

- [`SKILL.md`](skills/codex-swiftdialog-builder/SKILL.md) — Codex 工作流程和层级选择]
- [`references/`](skills/codex-swiftdialog-builder/references/) — 演示地图制作和内容创作指南]
- [`assets/templates/`](skills/codex-swiftdialog-builder/assets/templates/) — 启动脚本示例]
- 包含一种Jamf/root用户运行模式，以及一种所有权转移模式，适用于以命令文件形式启动的工作流程。`/var/tmp` `root`

**[`claude-swiftdialog-builder`](skills/claude-swiftdialog-builder/)** —— 献给克劳德·索内特。

- [`CLAUDE.md`](skills/claude-swiftdialog-builder/CLAUDE.md) — Claude的工作流程和层级选择。]
- [`references/`](skills/claude-swiftdialog-builder/references/) — 演示地图制作和内容创作指南]
- [`templates/`](skills/claude-swiftdialog-builder/templates/) — 启动脚本示例]
- 包含一种Jamf/root用户运行模式，以及一种所有权转移模式，适用于以命令文件形式启动的工作流程。`/var/tmp` `root`

这两个技能都遵循相同的代码仓库规范，并且产生完全相同的脚本输出，请选择与您的AI平台相匹配的那个。请参考[`skills/README.md`](skills/README.md))以获取详细的使用说明。

这些是为人工智能助手准备的技能包，而不是可以在该软件套件中直接运行的演示程序。

## 人工智能辅助的开发平台

在了解了演示模块并掌握了 swiftDialog 的功能后，可以使用 [`playground/`](playground/)) 目录，借助人工智能的辅助，创建您自己的自定义脚本。该环境包含一份全面的、循序渐进的指南，它将向您展示如何：

- 利用捆绑提供的技能，与人工智能助手（如Claude、Copilot）进行协作。
- 为您的工作流程选择合适的级别（基础对话 → 表单 → 进度更新 → 检查模式）。
- 跟随详细的、基于实际场景的案例，了解具体的提示语以及预期的AI交互方式。
- 为 macOS 管理任务（例如：用户入职、合规性检查、软件部署、监控、以及涉及危险操作的确认）构建可用于生产环境的脚本。

**从这里开始：** [`playground/README.md`](playground/README.md)) —— 您的工作空间，用于人工智能辅助的 swiftDialog 脚本开发。

## 演示索引

- `01_basic_styles.zsh` — `--style` (警示、注意、警告，居中)，样式覆盖。
- `02_title_message.zsh` — `--title`, `--titlefont`, `--message`, `--messagefont`, `--messagealignment`, `--messageposition`, `--bannertitle`, 标题 "无"。
- `03_icons.zsh` — `--icon` (SF Symbols、应用程序、内置功能、二维码、调色板、自动色彩、粗细)，`--iconsize`，`--iconalpha`，`--centreicon`，`--overlayicon`，`--hideicon`
- `04_buttons.zsh`、`--button1text`、`--button1symbol`、`--button1disabled`、`--button2text`、`--button2symbol`、`--infobuttontext`、`--infobuttonsymbol`、`--infobuttonaction`、`--buttonstyle`（居中、堆叠）、`--buttonsize`、`--buttontextsize`、`--hidedefaultkeyboardaction`。
- `05_images_banners.zsh` — `--image`, `--imagecaption`, `--bannerimage`, `--bannertitle`, `--bannertext`, `--background`, `--bgalpha`, `--bgposition`, `--bgfill`
- `06_progress_timer.zsh` — `--progress` (绝对值、增量、重置、完成)，`--progresstext`，`--progresstextalignment`，`--timer`，`--hidetimerbar`，命令文件进度更新。
- `07_text_fields.zsh` — `--textfield` (必需，安全，快速，数值，正则表达式，正则表达式错误，确认，文件选择，文件类型，路径，名称)，`--textfieldlivevalidation`
- `08_dropdowns.zsh` — `--selecttitle`, `--selectvalues`, `--selectdefault`，修饰符（必需，单选，可搜索，多选，名称），分隔符。
- `09_checkboxes.zsh` — `--checkbox` (名称修饰符)，`--checkboxstyle` (复选框、开关、尺寸)。
- `10_list_items.zsh` — `--listitem` (状态、状态文本、自定义SF符号)，`--liststyle`，`--enablelistselect`，命令文件（列表：、列表项：、添加、删除、索引）。
- `11_window_options.zsh` — `--width`, `--height`, `--big`, `--small`, `--position`, `--positionoffset`, `--moveable`, `--ontop`, `--resizable`, `--windowbuttons`, `--appearance`, `--showdockicon`, `--dockiconbadge`
- `12_command_file.zsh` — 完整命令文件说明：标题 (title:)、标题字体 (titlefont:)、消息 (message:)（支持追加内容）、对齐方式 (alignment:)、图标 (icon:)、覆盖图标 (overlayicon:)、图标透明度 (iconalpha:)、按钮 1 的文本 (button1text:)、按钮 1 (button1:)、信息文本 (infotext:)、信息框 (infobox:)、图标位置 (icon: centre/left)。
- `13_notifications.zsh` — `--notification`, `--subtitle`, `--identifier`, `--remove`
- `14_mini_presentation.zsh` — `--mini` (带进度条)，`--presentation` (带列表项、信息框、进度条)。
- `15_web_video.zsh` - `--webcontent`，`--video` (youtube = 快捷方式)，`--videocaption`，`--autoplay`。
- `16_json_input.zsh` — `--jsonstring`, `--jsonfile`, JSON arrays for checkboxes, selectitems, textfields, images
- `17_fullscreen_blur.zsh` — `--fullscreen`, `--blurscreen`, `--hideotherapps`
- `18_misc_features.zsh` — `--helpmessage`, `--infotext`, `--infobox`, `--vieworder`, `--quitkey`, `--sound`, `--showsoundcontrols`, `--displaylog`, `--loghistory`, `--debug`, `--eula`, `--alwaysreturninput`，身份验证密钥/校验和说明。
- `19_inspect_mode.zsh` - `--inspect-mode`，`--inspect-config`，`--published-sessions-dir`，`stepType: "cadence"`，`cadenceStyle: "carousel"`，cadence IPC（`cadence:satisfy`，`cadence:advance`，`cadence:goto`），预设3的重新设计，页脚logo，强制`appearance`，`cacheExtensions`，以及`aria2`。
- `20_branched_workflows.zsh` -- 顶级 `workflow` 数组， `branch.map`, `branch.default`, `branch.ifTrue`, `branch.ifFalse`, `nextpage`, `finalpage`，具有历史记录功能。 上一篇。

## 运行独立演示

每个演示脚本都是独立的。

```zsh
./demos/06_progress_timer.zsh
./demos/12_command_file.zsh
```

## 注释

- 使用`--blurscreen`或`--fullscreen`的演示程序会短暂地控制显示画面。
- 用于演示通知功能的示例需要授予 swiftDialog 通知权限。
- 某些图像示例使用了系统桌面图片，这些图片可能会因macOS版本的不同而有所差异。
- 演示版本 19 现在主要关注 v3.1.0b4 版本的检查和刷新功能，包括节奏轮播图、预设 3 的精简设计、会话发布功能，以及一个配套的、可管理的偏好设置示例 JSON 文件。
- 演示版本 19 和 20 需要 **swiftDialog v3.1.0b4 或更高版本**，以支持节奏控制和分支工作流程。
- 请参考 [swiftDialog v3.1.0b4] 的版本说明，以了解此处所涵盖的具体功能。](https://github.com/swiftDialog/swiftDialog/releases/tag/v3.1.0b4)