---
title: 建造者模式
description: 编辑对话窗口的属性和外观，并将结果输出为 JSON 配置文件
translationSynced: 2026-11-25T05:39:54+00:00
---


## swiftDialog 构件套件

要启用该功能，请运行 `dialog --builder`。 启动后，会显示一个额外的窗口，允许您更新内容和对话框的属性，并实时查看结果。

您可以将结果导出为 **JSON** 格式，或者导出为可以直接运行的 `dialog` **命令行指令**，以便根据您的设计重新创建对话。

**请注意：** 此功能尚未完全覆盖 swiftDialog 的所有功能，某些设置可能不可用，或者不会出现在生成的输出中。开发工作仍在进行中。

<img width="500" alt="image" src="/builder/builder_main.png" />

<div className="not-content" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin: 2rem 0; align-items: flex-start;">

<div style="align-self: flex-start;">

### 基础
 - [标题](/zh-hans/builder/title/)
 - [消息](/zh-hans/builder/message/)
 - [图标](/zh-hans/builder/icon/)
 - [侧边栏](/zh-hans/builder/sidebar/)
 - [窗口](/zh-hans/builder/window/)
 - [按钮](/zh-hans/builder/buttons/)

</div>

<div style="align-self: flex-start;">

### 高级
 - [复选框](/zh-hans/builder/checkboxes/)
 - [图片](/zh-hans/builder/images/)
 - [列表项](/zh-hans/builder/listitems/)
 - [媒体](/zh-hans/builder/media/)
 - [文本字段](/zh-hans/builder/textfields/)

</div>

</div>

### 输出

“输出”视图会显示当前的设计，可以选择以 **JSON** 格式或 **命令行** 方式呈现，可以通过标签栏进行切换。 在这里，您可以将内容**复制到剪贴板**或**保存为文件**。 页脚中的“导出命令”按钮可以复制构建器中的任何位置的命令行。