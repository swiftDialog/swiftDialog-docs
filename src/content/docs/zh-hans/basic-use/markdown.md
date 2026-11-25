---
title: Markdown 支持
description: 学习如何在 swiftDialog 消息中使用 Markdown 格式
translationSynced: 2026-11-25T05:11:47+00:00
---

## 支持 Markdown 语法

您可以在消息文本中使用 Markdown 语法来调整显示效果。

支持的 Markdown 格式遵循 GitHub 的风格。 支持表格、缩进、代码块等功能。

<img width="500" alt="Screenshot 2023-08-10 at 9 06 14 am" src="https://github.com/bartreardon/swiftDialog/assets/3598965/5fd6bb4a-a5b6-46c3-9fc9-7beace658420">

### 换行符

在 Markdown 中，由于[段落和换行符的处理定义](https://daringfireball.net/projects/markdown/syntax#p)，单个 `\n` 不足以创建新行。您应该在行尾加上**两个空格**，然后加上 `\n`，或者可以通过双 `\n\n` 触发新段落

您也可以使用`<br>`标签来表示换行，这将会被解释为`  \n`（`[space][space]\n`）。

### 颜色添加/增强

swiftDialog 3+ 包含了支持内联颜色的扩展功能。其语法如下：

```
colour:[Text here]
```

例如，如果您想要绿色文本，可以使用 `green:[My green text here]`。

支持十六进制值，例如：`:a62991[Colourful Text]`

您可以组合多种颜色，例如：`--message ":e74c3c[scarlet], :e67e22[tangerine], :f1c40f[gold], :2ecc71[emerald], :3498db[sapphire], and :9b59b6[amethyst]"`

<img width="400" alt="image" src="/images/markdown_colour.png" />

### 示例：

`dialog --message "Line 1  \nLine2  \nLine 3\n\nParagraph 2"`

`dialog --message "Line 1<br>Line2<br>Line 3<br><br>Paragraph 2"`

`dialog --message "Text can include **bold** and _italics_`

`dialog --message "### Heading 3"`

`dialog --message " * point 1\n * point 2\n * point 3"`

`dialog --message "[A link that will open in the default browser](https://some.link.com/)"`

`dialog --message "\![Inline images are also supported](https://upload.wikimedia.org/wikipedia/commons/8/85/Logo-Test.png)"`

**注意事项** - 在使用内联图片时，必须将开头的 `!` 转义为 `\!`，否则您的 shell 可能会将其解释为命令。

