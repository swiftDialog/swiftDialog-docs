---
title: Prise en charge de Markdown
description: Apprenez à utiliser la mise en forme Markdown dans les messages de swiftDialog
translationSynced: 2026-11-23T03:04:18+00:00
---

## Prise en charge de Markdown

Vous pouvez utiliser le langage Markdown dans le corps de votre message pour modifier sa présentation.

La syntaxe Markdown prise en charge suit le formatage du style GitHub. Les tableaux, les indentations, les blocs de code, etc., sont supportés

<img width="500" alt="Screenshot 2023-08-10 at 9 06 14 am" src="https://github.com/bartreardon/swiftDialog/assets/3598965/5fd6bb4a-a5b6-46c3-9fc9-7beace658420">

### Nouvelles lignes

En Markdown, en raison de la [définition](https://daringfireball.net/projects/markdown/syntax#p) de la manière dont les paragraphes et les sauts de ligne sont gérés, un simple caractère de retour à la ligne `\n` n'est pas suffisant pour créer une nouvelle ligne. Vous devez terminer une ligne avec **deux espaces**, puis un retour à la ligne `\n`, ou vous pouvez déclencher un nouveau paragraphe avec un double retour à la ligne `\n\n`

Vous pouvez également utiliser la balise `<br>` pour indiquer un saut de ligne, qui sera interprété comme `  \n` (`[space][space]\n`).

### Extensions de couleur

swiftDialog 3+ comprend des extensions pour prendre en charge l'utilisation de couleurs intégrées. La syntaxe est la suivante :

```
colour:[Text here]
```

Par exemple, si vous souhaitez afficher du texte en vert, vous pouvez utiliser `green:[My green text here]`

Les valeurs hexadécimales sont également prises en charge, par exemple : `:a62991[Colourful Text]`

Vous pouvez combiner plusieurs couleurs, par exemple `--message ":e74c3c[scarlet], :e67e22[tangerine], :f1c40f[gold], :2ecc71[emerald], :3498db[sapphire], and :9b59b6[amethyst]"`

<img width="400" alt="image" src="/images/markdown_colour.png" />

### Exemples :

`dialog --message "Line 1  \nLine2  \nLine 3\n\nParagraph 2"`

`dialog --message "Line 1<br>Line2<br>Line 3<br><br>Paragraph 2"`

`dialog --message "Text can include **bold** and _italics_`

`dialog --message "### Heading 3"`

`dialog --message " * point 1\n * point 2\n * point 3"`

`dialog --message "[A link that will open in the default browser](https://some.link.com/)"`

`dialog --message "\![Inline images are also supported](https://upload.wikimedia.org/wikipedia/commons/8/85/Logo-Test.png)"`

**Attention** – Lors de l'utilisation d'images intégrées, vous devez échapper le caractère `!` en utilisant `\!`, sinon votre interpréteur de commandes risque de l'interpréter comme une commande.

