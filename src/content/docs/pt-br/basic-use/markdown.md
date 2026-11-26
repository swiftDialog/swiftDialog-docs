---
title: Suporte a Markdown
description: Aprenda como usar a formatação Markdown nas mensagens do swiftDialog
translationSynced: 2026-11-25T11:10:10+00:00
---

## Suporte a Markdown

Você pode usar a formatação Markdown no texto da sua mensagem para alterar a apresentação.

O formato Markdown suportado segue o estilo de formatação do GitHub. Tabelas, indentação, blocos de código, etc., são suportados

<img width="500" alt="Screenshot 2023-08-10 at 9 06 14 am" src="https://github.com/bartreardon/swiftDialog/assets/3598965/5fd6bb4a-a5b6-46c3-9fc9-7beace658420">

### Quebras de linha

Em Markdown, devido à [definição](https://daringfireball.net/projects/markdown/syntax#p)] de como os parágrafos e as quebras de linha são tratados, um único caractere de quebra de linha `\n` não é suficiente para criar uma nova linha. Você deve finalizar uma linha com **dois espaços**, seguido de uma quebra de linha `\n`, ou pode iniciar um novo parágrafo com duas quebras de linha `\n\n`

Você também pode usar a tag `<br>` para indicar uma quebra de linha, que será interpretada como `  \n` (`[space][space]\n`).

### Extensões de cabelo coloridas

O swiftDialog 3+ inclui extensões para suporte à exibição de cores embutidas. A sintaxe é a seguinte:

```
colour:[Text here]
```

Por exemplo, se você quisesse texto na cor verde, poderia usar `green:[My green text here]`

Os valores hexadecimais também são suportados, por exemplo: `:a62991[Colourful Text]`

Você pode combinar várias cores, por exemplo: `--message ":e74c3c[scarlet], :e67e22[tangerine], :f1c40f[gold], :2ecc71[emerald], :3498db[sapphire], and :9b59b6[amethyst]"`

<img width="400" alt="image" src="/images/markdown_colour.png" />

### Exemplos:

`dialog --message "Line 1  \nLine2  \nLine 3\n\nParagraph 2"`

`dialog --message "Line 1<br>Line2<br>Line 3<br><br>Paragraph 2"`

`dialog --message "Text can include **bold** and _italics_`

`dialog --message "### Heading 3"`

`dialog --message " * point 1\n * point 2\n * point 3"`

`dialog --message "[A link that will open in the default browser](https://some.link.com/)"`

`dialog --message "\![Inline images are also supported](https://upload.wikimedia.org/wikipedia/commons/8/85/Logo-Test.png)"`

**Atenção** – Ao utilizar imagens embutidas, é necessário escapar o caractere `!`, substituindo-o por `\!`, caso contrário, o seu shell pode interpretá-lo como um comando.

