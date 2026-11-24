---
title: 画像の表示。
description: swiftDialogで、画像、画像の説明文、および画像スライドショーの表示方法を学びましょう。
translationSynced: 2026-11-23T22:49:14+00:00
---

## 画像の表示。

画像を表示することができ、デフォルトでは、画像がメッセージ表示領域を置き換えます。

`--imagecaption` は、各画像に対する短い一行の説明に使用できます。また、`--message` も存在する場合、画像やキャプションの下に表示されます。

```
-g, --image  <file> | <url>
  Display an image instead of a message.
  Images will be resized to fit the available display area

    --imagecaption <text>
    Text that will appear underneath the displayed image.
```

サポートされている画像形式であれば、どちらかの形式で入力できます。`<file>` `<url>`

例：

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/129476046-5b0cdef0-346b-4af6-a0eb-e8e72c72715d.png">

### Base64形式の画像データ。

画像が使用できる場所であれば、現在はbase64形式で指定できるようになりました。例えば、`base64=`というプレフィックスを付けて指定します。`--icon base64=<base64_text>`

### 複数の画像。

複数の`--image`を指定すると、画像がカルーセル形式で表示され、次の画像/前の画像への移動ボタンと、現在表示されている画像がシーケンスの中でどの位置にあるかを示すインジケーターが表示されます。

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/148642555-96247bff-8d95-414d-bf96-1fe28e27ed9c.png">

画像を表示するだけでなく、`--autoplay <sec>`を使用することで、指定した秒数（デフォルトは10秒）経過後に次の画像を表示させることができます。画像表示の下には、進行状況を示すインジケーターが表示され、次の画面切り替えがいつ行われるかを示します。最後の画像が表示された後、表示はリセットされ、最初の画像から再開されます。

自動再生時のトランジション中に表示されるカウントダウンインジケーターを非表示にするには、`--hidetimer`を使用してください。