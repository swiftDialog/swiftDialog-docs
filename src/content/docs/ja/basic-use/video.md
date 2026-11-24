---
title: 動画の表示。
description: swiftDialogで動画やビデオコンテンツを表示する方法を学びましょう。YouTubeやVimeoへの対応も含まれます。
translationSynced: 2026-11-23T22:49:19+00:00
---

## 動画の表示。

動画は、メッセージの代わりに表示できます。指定した場合、デフォルトのダイアログサイズは、16:9のアスペクト比の動画を表示できるよう、900x600に変わります。カスタムサイズは、`--width`および`--height`のオプションを使用して指定できます。

```
--video  <file> | <url>
  Display a video instead of a message.
  Videos will be resized to fit the available display area (depending on video resolution, some letterboxing may occur)

    --videocaption <text>
    Text that will appear underneath the displayed video.

    --autoplay
    Video will start playing automatically on launch without requiring the user to press play
```

QuickTimeでサポートされているビデオ形式であれば、基本的にどの形式でも再生可能です。URLを使用する場合は、ビデオファイルへの完全なパスを指定する必要があります。

`--title "Video Demo" --video /Users/Shared/Videos/day4session3.mp4`

![image](https://user-images.githubusercontent.com/3598965/138063195-19011cc7-840f-4701-9209-8405ffabcbeb.png)

### YouTubeおよびVimeoへの対応（swiftDialog バージョン2.0以降が必要です）。

YouTubeまたはVimeoの動画を埋め込むには、動画のIDをパラメータとして、`--video`コマンドに、`youtubeid=`または`vimeoid=`のプレフィックスを付けて渡すことができます。

通常、IDはYouTubeまたはVimeoのURL内に記載されています。

YouTubeの例：

`dialog --video youtubeid=XXXXXXXXXX`

Vimeoの例：

`dialog --video vimeoid=XXXXXXXXXX`

_注: プライベートVimeoビデオのIDの場合、埋め込みURLから追加情報をキャプチャする必要があることもあります。これは追加の`h=YYYYYYYY`として表現され、したがってswiftDialogの完全な埋め込みコマンドは`dialog --video "vimeoid=XXXXXXXXXX?h=YYYYYYYY"`となります。_


## 実行中のダイアログに、新しいウェブコンテンツや動画コンテンツを追加する。

以下のコマンドを送信して、ダイアログに新しいウェブコンテンツや動画コンテンツを追加します。

```bash
echo "webcontent: https://some.website.com" >> /var/tmp/dialog.log
echo "video: https://some.website.com/video.mov" >> /var/tmp/dialog.log
echo "video: /path/to/file.mov" >> /var/tmp/dialog.log
```

ただし、いくつか注意点があります。現在、ウェブページや動画コンテンツをその場で更新することはできません。別のウェブサイトに切り替えるには、まず現在のコンテンツを消去し、その後で新しいコンテンツを送信する必要があります。

```bash
echo "webcontent: none" >> /var/tmp/dialog.log
echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log
```

それらを組み合わせて使うこともできるので、それもまた有効です。`echo "webcontent: none" >> /var/tmp/dialog.log && echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log`