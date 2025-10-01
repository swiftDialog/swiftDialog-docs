---
title: Markdown Support
description: Learn how to use markdown formatting in swiftDialog messages
---

## Markdown support

You can specify markdown in your message text to modify the presentation.

Supported markdown follows GitHub style formatting. Tables, indents, code blocks etc are supported

<img width="500" alt="Screenshot 2023-08-10 at 9 06 14 am" src="https://github.com/bartreardon/swiftDialog/assets/3598965/5fd6bb4a-a5b6-46c3-9fc9-7beace658420">

Some notes about markdown support:
   - Due to the way markdown is rendered and how SwiftUI behaves with selections across views, selecting text only works within a single paragraph/block.
   - Inline images to local sources are **not** supported
   - Inline images to URL sources **do** support markdown `![image](https://path.to/image.png)` formatting but **not** `<img src="https://path.to/image.png>` at this time.

### Newlines

In Markdown due to the [definition](https://daringfireball.net/projects/markdown/syntax#p) of how paragraphs and line breaks are handled, a single `\n` is not sufficient to create a new line. You should end a line with **two spaces**, and then a `\n` or you can trigger a new paragraph with a double `\n\n`

You can also use the `<br>` tag to denote a newline which will get interpreted as `  \n` (`[space][space]\n`)

### Examples:

`dialog --message "Line 1  \nLine2  \nLine 3\n\nParagraph 2"`

`dialog --message "Line 1<br>Line2<br>Line 3<br><br>Paragraph 2"`

`dialog --message "Text can include **bold** and _italics_`

`dialog --message "### Heading 3"`

`dialog --message " * point 1\n * point 2\n * point 3"`

`dialog --message "[A link that will open in the default browser](https://some.link.com/)"`

`dialog --message "\![Inline images are also supported](https://upload.wikimedia.org/wikipedia/commons/8/85/Logo-Test.png)"`

**Caution** - When using inline images, you must escape the leading `!` as `\!` otherwise your shell may interpret it as a command.

Suffice to say, things can get a bit crazy so use markdown with caution