---
title: 背景画像
description: ダイアログウィンドウに背景画像や透かしを追加する。
translationSynced: 2026-11-23T22:51:51+00:00
---

## 背景画像

画像は、メインのダイアログウィンドウの背景として表示することができ、これにより、通常のダイアログの内容の背後にウォーターマークやその他の画像を配置することができます。

![image](https://user-images.githubusercontent.com/3598965/171406081-8e9e5363-56fc-46f9-baa8-ff881a4a4af3.png)

背景の設定は、以下のコントロールを使用して調整できます。

### `--background`

```
-bg, --background <file | url | colour= >
```

選択されたファイルを背景画像として表示します。画像がデフォルトのダイアログサイズ（820x380）よりも大きい場合、またはウィンドウのサイズに関するオプションが指定されていない（特にウィンドウの高さ）場合、ダイアログウィンドウの高さを調整し、画像がウィンドウの全幅を占めるようにします。デフォルトでは820ピクセルですが、指定することも可能です。`--width`

代替として、色の指定には、`colour=`という接頭辞を使用して、単色を指定することができます。色の指定は、16進数表記または色名で行うことができます。

例：`--background colour=red` または `--background colour=#ff0000`

デフォルトでは、単色にわずかなグラデーションが適用されます。これを無効にするには、"`,nogradient`" を追加してください。

`--background colour=red,nogradient`

線形グラデーションは、`gradient=`という接頭辞を使用して指定できます。 カンマで区切られた2つ以上の色を指定し、必要に応じて、`:angle=<degrees>`を使用して方向を設定できます。

```sh
--background "gradient=red,blue"
--background "gradient=red,orange,yellow:angle=135"
```

角度の定義：`0` = 下から上へ、`90` = 左から右へ (デフォルト)、`180` = 上から下へ、`270` = 右から左へ。

もし、`gradient=`に色が1つだけ供給される場合、結果は`colour=`と同じになります。


### `--bgalpha`

```
-ba, --bgalpha <number>
```

背景レイヤーの透明度を設定します。値は、`0`（完全に透明）から`1`（完全に不透明）の間の任意の数値で指定できます。デフォルト値は`0.5`です。


### --背景位置

```
-bp, --bgposition [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]
```

背景画像をウィンドウ内に配置します。特に、会社のロゴなど、メインのダイアログウィンドウよりも画像サイズが小さい場合に効果的です。デフォルトの位置は`centre`です。


### --背景色設定

```
-bf, --bgfill [fill | fit]
```

このダイアログは、ウィンドウの枠内に画像をどのように表示するかを設定します。

`fill` は画像をウィンドウ全体に拡大表示します。必要に応じて画像は切り抜かれます。`fit` は画像をウィンドウに収めるようにリサイズしますが、切り抜きは行わず、透明でない領域（PNG画像ソースを使用する場合）にレターボックスが生じる可能性があります。

デフォルトは`none`で、これは画像が実際の解像度で表示されることを意味します。

## 画面の背景 - `--screenbackground`

```
--screenbackground <file | url>
```

指定された画像を **フルスクリーンで、ダイアログウィンドウの背景に表示** します。`--background`とは異なり、`--background`はダイアログウィンドウの _内側_ に表示されます。他のすべてのダイアログ機能は引き続き利用可能ですが、swiftDialogが終了するまでユーザーは他のアプリとやり取りできません（`--blurscreen`と同様ですが、ぼかしの代わりに画像が表示されます）。

```sh
dialog --screenbackground /path/to/wallpaper.jpg
dialog --screenbackground https://example.com/background.png
```