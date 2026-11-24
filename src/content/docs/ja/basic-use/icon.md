---
title: アイコンのカスタマイズ方法。
description: swiftDialogで、アイコン、画像、およびオーバーレイの設定とカスタマイズ方法を学びましょう。
translationSynced: 2026-11-23T22:43:14+00:00
---

##### 目次
 - [基本的な使い方](#基本的な使い方)
 - [少し高度な使い方](#より高度な利用方法)
 - ](#組み込みアイコン) 内蔵アイコン。
 - [SF Symbolsの使用方法](#sf-symbols-の利用方法)
 - アイコンのオーバーレイ](#アイコンのオーバーレイ機能)
 - [アイコンサイズ](#アイコンのサイズ)
 - アイコンを非表示にする](#アイコンを非表示にする)
 - [ライトモードまたはダークモードのアイコンを設定します。](#uiがダークモードかライトモードかによってアイコンの色をそれぞれ暗色または明色に設定します)

***


アイコンのタイトル領域に表示するアイコンや画像を指定するには、`-i` または `--icon` のコマンドラインオプションを使用してください。

### 用途：

`--icon <file | url | text= >`


## 基本的な使い方。

swiftDialogは、`png`および`jpg`形式の画像に対応しており、指定された画像をアイコン表示領域に表示します。

画像は、幅170ポイント、高さ260ポイントの表示領域に合わせてリサイズされます。

`png`が推奨されますが、もし`jpg`が指定された場合は、画像は角がわずかに丸められて表示され、より柔らかい印象になります。

<img src="https://user-images.githubusercontent.com/3598965/111853793-912e3880-8970-11eb-852f-3d5f7e5d2119.png" width=450>

## より高度な利用方法。
swiftDialogは、アプリケーションのパスを受け取り、そのアプリケーションのアイコンを画像として使用します。

e.g. `--icon /Applications/Safari.app`

<img src="https://user-images.githubusercontent.com/3598965/111853901-e36f5980-8970-11eb-80e2-c3fca298627d.png" width=450>

swiftDialogは、画像ファイルへのURLも受け付けます。

e.g. `--icon "https://user-images.githubusercontent.com/3598965/111854068-84f6ab00-8971-11eb-935b-487f1a15b91f.png"`

<img src="https://user-images.githubusercontent.com/3598965/111854089-a5bf0080-8971-11eb-95fe-a720206bb10a.png" width=450>

## アイコンの透明度設定。

透明度を設定するには、`--iconalpha`を使用します。

その範囲は、`0.0` (完全に透明) から `1.0` (完全に不透明) までです。

## 代替アイコン（ダークモード用）

`:dark=` を使用し、ユーザーがダークモードで表示されている場合に、代替のアイコンやパスを指定してください。

e.g. `--icon /path/to/light.png:dark=/path/to/dark.png`

## 組み込みアイコン。

swiftDialogには、組み込みのアイコンがいくつか用意されており、これらは`--icon`オプションで使用できます。

`--icon info`

![Info Icon](https://user-images.githubusercontent.com/3598965/111854259-5e853f80-8972-11eb-9476-e2c5ceed3da9.png)

`--icon caution`

![Caution Icon](https://user-images.githubusercontent.com/3598965/111854239-46adbb80-8972-11eb-9708-e864a71e3e0a.png)

`--icon warning`

![警告アイコン](https://user-images.githubusercontent.com/3598965/111854248-52997d80-8972-11eb-9f11-52a0b8a8d650.png)

`--icon computer`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/2ee4c788-bc9a-4328-ac1b-1537bf30dcb7">

## 使用する`text=`

アイコン領域にテキストを表示する場合、`text=`というプレフィックスを使用することもできます。これは、単一の文字や絵文字を表示するのに便利です。

e.g. `--icon text=👍`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/931fa9f5-0f96-4b32-bf6e-cffa28c26e31">


## SF Symbols の利用方法。

swiftDialogは、任意のSF Symbolのアイコンを表示することも可能です。https://developer.apple.com/sf-symbols/

### SF Symbolのシンタックス（CSV形式）

アイコンやオーバーレイアイコンにSFシンボルを指定する際に、色や太さを調整するための追加パラメータが利用可能です。

  `"SF=sf.symbol.name,colour=<text><hex>,weight=<text>"`

  `color,colour=<text><hex>` は16進数形式で指定します。例：#00A4C7。標準のAppleカラーも受け付けます：`black`、`blue`、`gray`、`green`、`orange`、`pink`、`purple`、`red`、`white`、`yellow`。オプションが無効な場合のデフォルトはシステムの`primary`カラーです。

特別カラー `"auto"`。

マルチカラーのSFシンボルで使用する場合、シンボルのデフォルトのカラー設定が適用されます。モノクロのSFシンボルで使用する場合は、デフォルトで黒色になり、ダークモードへの対応は行われません。

e.g. `dialog -s -i SF=airplane.circle.fill,colour=auto`

![image](https://user-images.githubusercontent.com/3598965/126090330-8dc612a9-40f9-99e2-caf41d07903e.png)

色のグラデーションは、追加の引数（例えば、`colour2`または`color2`）を指定することで設定できます。`SF=applelogo,colour=pink,colour2=purple`

![image](https://user-images.githubusercontent.com/3598965/170815055-e943c2a4-e846-44d5-b323-bb8be1333438.png)

マルチカラーのSFシンボルは、`palette`という引数を使用して色付けすることができます。例えば、`SF=person.3.sequence.fill,palette=red,green,blue`のように。

![image](https://user-images.githubusercontent.com/3598965/171398294-0a74dcad-b5b2-4dd0-b5b2-4dd0-b320-c65d5d5e8d22.png)

SFシンボルの太さ（ウェイト）は、`weight`という引数で設定できます。

   `weight=<text>` は、以下のいずれかの値を許容します。
    * `thin`（デフォルト）
    * `light`
    * `regular`
    * `medium`
    * `heavy`
    * `bold`

### アニメーション化されたSFアイコン。

macOS 14以降のバージョンでは、アニメーションされたSF記号に対応しています。

使用例：

`--icon sf=rainbow,colour=auto,animation=variable`

現時点では、以下のアニメーション形式でのサポートのみ提供しています。
 - "変数":
 - "変数：リバース機能"
 - "変数。反復処理。"
 - "変数。反復処理。逆順。"
 - "variable.cumulative" (変数.累積)
 - 脈拍
 - "pulse.bylayer"

### JSON アイコンオブジェクト。

アイコンは、より詳細な制御を行うために、JSONオブジェクトとして指定することも可能です。これは、複数のプロパティを持つ複雑なアイコン設定を行う場合に特に有効です。

**構文:**
```bash
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'
```

**対応キー:**
- `sf` / `name` / `symbol` - SFシンボルの名前
- `path` / `icon` / `value` - 画像ファイルまたはアプリケーションへのファイルパス。
- `weight` - 文字の太さ (細、薄、標準、中、太、濃字)
- `colour` / `color` - 基本色 (16進数表記または色名)
- `colour2` / `color2` - グラデーションに使用する、セカンダリカラー。
- `palette` - 多色表示に対応した記号の色を設定するためのカラーパレット。
- `animation` - アニメーションシンボルのアニメーションタイプ (macOS 14 以降)。
- `bgcolour` / `bgcolor` - オーバーレイアイコンの背景色。
- `auto` - 自動カラーテーマに使用される特別な値。
- `light` / `dark` - 明るいモードと暗いモードのバリエーション (ネストされたアイコンオブジェクト)

**例：**

```bash
# Basic symbol with colour and weight
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'

# Gradient
dialog --icon '{"sf":"applelogo","colour":"pink","colour2":"purple"}'

# Multicolor palette
dialog --icon '{"sf":"person.3.sequence.fill","palette":["red","green","blue"]}'

# Application icon
dialog --icon '{"path":"/Applications/Chess.app"}'

# Light/dark variants
dialog --icon '{"light":{"sf":"sun.max"},"dark":{"sf":"moon"}}'

# Animated symbol (macOS 14+)
dialog --icon '{"sf":"rainbow","colour":"auto","animation":"variable"}'

# Overlay icon with background
dialog --overlayicon '{"sf":"exclamationmark","colour":"yellow","bgcolour":"none"}'
```

対応機種：`--icon`、`--overlayicon`、`--listitem`のアイコン欄、`--checkbox`のアイコン欄。

**注意:** `--listitem` または `--checkbox` で使用する場合、アイコンフィールドにはネストされたJSONオブジェクトを入力できます。

```bash
dialog --listitem '{"title":"Download","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}'
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}'
```



## アイコンのオーバーレイ機能。

メインアイコンの上に表示するアイコンや画像を指定するには、`-y` または `--overlayicon ` のコマンドラインオプションを使用してください。

オーバーレイは、通常解像度の半分で表示され、メインのアイコン表示領域の右下に配置されます。このオプションを使用すると、複数の画像を組み合わせて表示することができます。

オーバーレイアイコンは、`--icon` パラメータで指定される画像の種類と配置をすべてサポートします。これには、組み込みのものやSF Symbolsなどが含まれます。


例：

`--icon caution --overlayicon /Applications/Safari.app`

`-i caution -y /Applications/Safari.app`

![caution icon with safari Overlay Icon](https://user-images.githubusercontent.com/3598965/111854381-16b2e800-8973-11eb-9cf9-c2b1d8d8b6b7.png)

例2：

`--icon /Applications/Google\ Chrome.app --overlayicon warning`

`-i /Applications/Google\ Chrome.app -y warning`

![Chromeのアイコンに警告表示が重なって表示されています。](https://user-images.githubusercontent.com/3598965/111888622-2e9d7100-8a32-11eb-9693-e53bb2f42692.png)

### SF Symbolsを使用する際に、背景を重ねて表示する。

SF Symbolsを使用する際、半透明の四角い形状（スクエア）が追加されます。これは、多くのシンボルが主要なアイコンの上に重ねて表示される場合に、シンボルを目立たせるためです。なぜなら、シンボルの中には、重ねて表示するのに適さない要素が含まれていることがあるからです。

![image](https://user-images.githubusercontent.com/3598965/173157681-0dd05429-35db-4872-89a1-8a8e42bf44a4.png)

背景の表示は、`bgcolor=`という設定項目で調整でき、設定方法も、`color`を設定できる場所と共通です。また、背景に色を重ねるのが不要な場合は、特別なカラーコードである`bgcolor=none`を指定することも可能です。

![image](https://user-images.githubusercontent.com/3598965/173157715-46fda24b-2cfb-417b-835a-ed452888546d.png)

## アイコンのサイズ。

`--iconsize <float>` アイコンのサイズを、指定された幅に調整します。デフォルトの幅は`170`です。

例1：

`--icon caution --overlayicon /Applications/Safari.app --iconsize 300`

![image](https://user-images.githubusercontent.com/3598965/137573508-a2eb2dfc-cf46-4009-8783-66d8e2040724.png)


例2：

`--icon /Applications/Firefox.app --iconsize 100 -s`

![image](https://user-images.githubusercontent.com/3598965/137573587-0e11823b-dc12-4756-ab4c-8442c4d5f050.png)

## アイコンの配置場所。

`--centreicon` または `--centericon`

アイコンの位置を中央に配置するように変更します。

![image](https://user-images.githubusercontent.com/3598965/159693524-551b863d-33db-4af0-b971-a9a08161d525.png)

swiftDialogが実行中に、コマンドファイルを使用して設定を変更することも可能です。

`echo "icon: centre" >> /var/tmp/dialog.log`

## アイコンを非表示にする。

アイコンは、以下のいずれかのコマンドを使用することで、完全に削除できます。

`--hideicon`

または

`--icon none`

## UIがダークモードかライトモードかによって、アイコンの色をそれぞれ暗色または明色に設定します。

一部のSF Symbolsを除き、swiftDialogには、ダークモードとライトモードの間でアイコンを切り替えるための組み込み機能は用意されていません。

UIの設定に基づいてアイコンを設定することは、呼び出しスクリプト内で実現可能です。

**zsh / bash** (mm2270様、ありがとうございます](https://github.com/mm2270))

```bash
#!/bin/zsh

icon_path_dark="/path/to/icondark.png"
icon_path_lite="/path/to/iconlite.png"

logged_in_user=$(/usr/sbin/scutil <<< "show State:/Users/ConsoleUser" | /usr/bin/awk '/Name :/ && ! /loginwindow/ {print $3}')

os_color_mode=$(/usr/bin/defaults read /Users/$logged_in_user/Library/Preferences/.GlobalPreferences.plist AppleInterfaceStyle)

if [ "$os_color_mode" = "Dark" ]; then
	icon_path=$icon_path_dark
else
	icon_path=$icon_path_lite
fi
```

または、Pythonでも可能です（[joncrain](https://github.com/joncrain)]様、ありがとうございます）。

```python
from Foundation import NSBundle

def is_dark_mode():
    appearanceBundle = NSBundle.bundleWithPath_(
        "/System/Library/PreferencePanes/Appearance.prefPane"
    )
    appearanceShared = appearanceBundle.classNamed_("AppearanceShared")
    app = appearanceShared.sharedAppearanceAccess()
    if app.theme() == 1:
        return False
    else:
        return True

if is_dark_mode():
    content["icon"] = "dark_icon.png"
else:
    content["icon"] = "light_icon.png"
```