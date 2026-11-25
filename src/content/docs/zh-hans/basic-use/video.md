---
title: 视频显示
description: 学习如何在 swiftDialog 中显示视频和视频内容，包括对 YouTube 和 Vimeo 的支持
translationSynced: 2026-11-25T05:13:20+00:00
---

## 视频显示

视频可以代替消息显示。 如果指定了视频，默认对话框的大小将切换为 900x600，以适应 16:9 的视频比例。 可以使用 `--width` 和 `--height` 参数来指定自定义大小。

```
--video  <file> | <url>
  Display a video instead of a message.
  Videos will be resized to fit the available display area (depending on video resolution, some letterboxing may occur)

    --videocaption <text>
    Text that will appear underneath the displayed video.

    --autoplay
    Video will start playing automatically on launch without requiring the user to press play
```

只要是 Quicktime 能够支持的视频格式，理论上都可以播放。如果使用网址，必须使用到视频资源的完整路径。

示例：`--title "Video Demo" --video /Users/Shared/Videos/day4session3.mp4`

![图片](https://user-images.githubusercontent.com/3598965/138063195-19011cc7-840f-4701-9209-8405ffabcbeb.png)

### YouTube 和 Vimeo 支持（需要 swiftDialog 2.0 或更高版本）

要嵌入YouTube或Vimeo视频，可以将视频ID作为参数传递给`--video`命令，可以使用`youtubeid=`或`vimeoid=`作为前缀。

通常可以在 YouTube 或 Vimeo 网站的网址（URL）中找到该标识符（ID）。

YouTube 示例：

`dialog --video youtubeid=XXXXXXXXXX`

Vimeo 示例：

`dialog --video vimeoid=XXXXXXXXXX`

_注意：对于私密 Vimeo 视频的 ID，您可能还需要在嵌入 URL 中捕获其他信息。这将表示为附加的 `h=YYYYYYYY` - 因此 swiftDialog 的完整嵌入命令将是 `dialog --video "vimeoid=XXXXXXXXXX?h=YYYYYYYY"`。_


## 更新正在进行的对话，添加新的网页或视频内容

发送以下命令，以使用新的网页或视频内容更新对话框。

```bash
echo "webcontent: https://some.website.com" >> /var/tmp/dialog.log
echo "video: https://some.website.com/video.mov" >> /var/tmp/dialog.log
echo "video: /path/to/file.mov" >> /var/tmp/dialog.log
```

不过，需要注意以下几点：目前，您无法直接在现有网页或视频内容上进行更新。要切换到另一个网站，您需要先清除现有内容，然后再上传新的内容。

```bash
echo "webcontent: none" >> /var/tmp/dialog.log
echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log
```

虽然你可以将它们串联起来，但那样的方法也 `echo "webcontent: none" >> /var/tmp/dialog.log && echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log` 有效。