---
title: 情報ボックス
description: セカンダリコンテンツ領域に、追加情報を表示します。
translationSynced: 2026-11-23T22:57:29+00:00
---

## 情報ボックス - `--infobox`

情報表示領域は、アイコンが表示されている領域の下にある部分です。

これは、別の色合いでより小さなフォントを表示し、システム情報など、補足的な情報を表示するのに役立ちます。

`--infobox` は、マークダウン形式で記述されたテキストであれば、どのような内容でも受け付けます。

#### 例：

`--infobox "### Additional Info\n\n#### Item 1  \n - Point one  \n - Point two  \n#### Item 2  \n - Point three  \n - Point four"`

申し訳ありませんが、画像ファイルが提供されていないため、翻訳できません。画像の内容について説明していただければ、翻訳を試みることができます。](https://github.com/user-attachments/assets/d78c2abc-976b-4bb7-b6e8-ff0c487cfe01)

## 情報ボックスの幅 - `--infoboxwidth`

デフォルトでは、情報ボックスはアイコン列と同じ幅になります。`--infoboxwidth <number>`は、アイコンのサイズに関係なく、情報ボックスのテキスト領域の幅（ポイント単位）を個別に設定できるようにします。これにより、アイコンを大きくせずに、情報ボックスを広げることができます。

`--infoboxwidth 300`