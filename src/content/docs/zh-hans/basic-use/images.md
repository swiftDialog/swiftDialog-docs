---
title: 显示图像
description: 学习如何在 swiftDialog 中显示图像、图像标题和图像轮播图
translationSynced: 2026-11-25T06:06:24+00:00
---

## 显示图像

图片可以显示，并且默认情况下会替换消息显示区域。

`--imagecaption` 可用于对每张图片进行简短的单行描述。 如果还存在 `--message`，则它会显示在所有图片和标题的下方。

```
-g, --image  <file> | <url>
  Display an image instead of a message.
  Images will be resized to fit the available display area

    --imagecaption <text>
    Text that will appear underneath the displayed image.
```

任何支持的图像格式都可以作为输入，可以是`<file>`或`<url>`。

示例：

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/129476046-5b0cdef0-346b-4af6-a0eb-e8e72c72715d.png">

### 以 base64 格式存储的图像

在任何可以使用图像的地方，现在都可以使用 Base64 编码的图像，只需在图像数据前加上 "`base64=`" 前缀，例如：`--icon base64=<base64_text>`。

### 多张图片

指定多个`--image`时，将会以轮播图的形式显示图像，轮播图上会显示“下一张”和“上一张”的箭头，以及指示当前正在显示的图像在序列中的位置。

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/148642555-96247bff-8d95-414d-bf96-1fe28e27ed9c.png">

除了静态地显示图像之外，您还可以使用`--autoplay <sec>`功能，让下一张图像在指定秒数（默认为10秒）后自动显示。图像下方会显示一个进度指示器，用于提示何时会进行下一次切换。在显示完最后一张图像后，显示界面将重置，并从第一张图像开始重新播放。

使用 `--hidetimer` 来隐藏在自动播放切换时显示的倒计时指示器。