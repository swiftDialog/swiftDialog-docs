---
title: 构建模式 - 消息区域
description: 编辑对话窗口的属性和外观，并将结果输出为 JSON 配置文件
translationSynced: 2026-11-25T05:41:15+00:00
---

消息编辑器允许您修改消息内容。

<img width="500" alt="image" src="/builder/builder_message.png" />

使用 Markdown 语法来美化消息内容。

<img width="500" alt="image" src="/builder/builder_message_populated.png" />

<img width="500" alt="image" src="/builder/builder_message_dialog.png" />

### 属性

以下属性可以进行设置。点击“重置”按钮可以恢复这些设置到默认值。

#### 文本对齐

将文本左对齐、居中对齐或右对齐。

#### 垂直位置

启用后，垂直位置将设置为居中，而不是顶部对齐。

#### 颜色

设置消息颜色。

#### Markdown 源代码

除了直接在文本框中输入内容外，您还可以通过“从文件…”按钮或“URL/加载”字段，从Markdown文件或URL中加载内容。构建器会将内容加载到预览区域，而导出的JSON/命令会引用该文件或URL（以便在运行时进行加载）。使用“内联编辑”按钮可以切换回直接编辑文本。

ℹ️ 注意：字体调整功能不可用。

[返回](/zh-hans/builder/builder/)