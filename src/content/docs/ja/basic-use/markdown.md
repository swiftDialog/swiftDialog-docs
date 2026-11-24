---
title: Markdown形式のサポート。
description: swiftDialogメッセージで、マークダウン形式の書式設定を使用する方法を学びましょう。
translationSynced: 2026-11-23T22:49:21+00:00
---

## マークダウン形式のサポート。

メッセージの内容にMarkdown記法を使用することで、表示形式を調整することができます。

サポートされているマークダウンは、GitHubのスタイルに準拠したフォーマットに対応しています。表、インデント、コードブロックなども利用可能です。

<img width="500" alt="Screenshot 2023-08-10 at 9 06 14 am" src="https://github.com/bartreardon/swiftDialog/assets/3598965/5fd6bb4a-a5b6-46c3-9fc9-7beace658420">

### 改行。

Markdownでは、段落や改行の扱いに関する[定義](https://daringfireball.net/projects/markdown/syntax#p)]により、単に1つの記号`\n`だけでは新しい行を作成できません。行の末尾に**2つのスペース**を配置し、その後ろに改行記号`\n`を置くか、または2つの改行記号`\n\n`を連続して配置することで、新しい段落を開始することができます。

「`<br>`」タグは、改行を示すために使用することもできます。この場合、改行は「`  \n`」（「`[space][space]\n`」）として解釈されます。

### カラーエクステンション

swiftDialog 3+ には、テキスト内に色を埋め込むための機能拡張が含まれています。その構文は以下の通りです。

```
colour:[Text here]
```

例えば、緑色のテキストを表示したい場合は、`green:[My green text here]` を使用することができます。

16進数表記もサポートされています。例：`:a62991[Colourful Text]`

複数の色を組み合わせて使用することができます。`--message ":e74c3c[scarlet], :e67e22[tangerine], :f1c40f[gold], :2ecc71[emerald], :3498db[sapphire], and :9b59b6[amethyst]"`

<img width="400" alt="image" src="/images/markdown_colour.png" />

### 例：

`dialog --message "Line 1  \nLine2  \nLine 3\n\nParagraph 2"`

`dialog --message "Line 1<br>Line2<br>Line 3<br><br>Paragraph 2"`

`dialog --message "Text can include **bold** and _italics_`

`dialog --message "### Heading 3"`

`dialog --message " * point 1\n * point 2\n * point 3"`

`dialog --message "[A link that will open in the default browser](https://some.link.com/)"`

`dialog --message "\![Inline images are also supported](https://upload.wikimedia.org/wikipedia/commons/8/85/Logo-Test.png)"`

**注意** - インライン画像を挿入する際、先頭の`!`は必ず`\!`に変換してください。そうしないと、シェルの解釈によりコマンドとして扱われてしまう可能性があります。

