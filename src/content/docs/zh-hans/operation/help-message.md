---
title: 帮助信息
description: 为对话框添加上下文帮助信息
translationSynced: 2026-11-25T05:49:10+00:00
---

## 帮助信息

帮助信息可以提供额外的详细信息，而无需占用额外的对话空间。

`--helpmessage <text>`

`<text>` 将支持 Markdown 格式用于消息的排版。

当出现可选功能时，一个“帮助”按钮会显示在默认按钮的旁边。


![图片](https://user-images.githubusercontent.com/3598965/216032093-2aede3aa-4cda-402c-9cd7-fa4edb506cfc.png)

点击它会弹出一个窗口，显示帮助信息。

![图片](https://user-images.githubusercontent.com/3598965/216032203-35960f72-24f5-491e-8d75-b6b43e4a123c.png)

显示的页面高度会根据消息的大小进行调整。

### `--helpimage`

添加一张图片。`--helpimage /path/to/image.png`

<img width="550" alt="image" src="https://github.com/user-attachments/assets/d4c4504f-2e6f-4e83-882f-be0e799c9ffc" />

支持标准的图标参数，包括二维码。

<img width="550" alt="image" src="https://github.com/user-attachments/assets/1c4c99bc-8548-4547-b16b-0dd02cc2c02d" />

### `--helpalignment`

`--helpalignment [left | centre | center | right]`

设置帮助提示信息内容的对齐方式。默认对齐方式与当前消息的对齐设置一致。

### `--helpsheetbuttontext`

`--helpsheetbuttontext <text>`

设置用于关闭帮助窗口的按钮上的标签。默认值为 `OK`。