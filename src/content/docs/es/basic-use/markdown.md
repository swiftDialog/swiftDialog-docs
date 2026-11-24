---
title: Soporte para Markdown
description: Aprenda a utilizar el formato Markdown en los mensajes de swiftDialog
translationSynced: 2026-11-24T22:21:57+00:00
---

## Soporte para Markdown

Puede utilizar formato Markdown en el texto de su mensaje para modificar su presentación.

El formato Markdown admitido sigue el estilo de GitHub. Se admiten tablas, sangrías, bloques de código, etc

<img width="500" alt="Screenshot 2023-08-10 at 9 06 14 am" src="https://github.com/bartreardon/swiftDialog/assets/3598965/5fd6bb4a-a5b6-46c3-9fc9-7beace658420">

### Saltos de línea

En Markdown, debido a la [definición](https://daringfireball.net/projects/markdown/syntax#p) de cómo se manejan los párrafos y los saltos de línea, un solo carácter`\n` no es suficiente para crear una nueva línea. Debe finalizar una línea con **dos espacios**, seguido de un salto de línea`\n`, o puede iniciar un nuevo párrafo con un doble salto de línea`\n\n`

También puede utilizar la etiqueta `<br>` para indicar un salto de línea, que se interpretará como `  \n` (`[space][space]\n`).

### Extensiones de color

swiftDialog 3+ incluye extensiones para admitir colores incrustados. La sintaxis es la siguiente:

```
colour:[Text here]
```

Por ejemplo, si deseaba texto en color verde, podría utilizar `green:[My green text here]`

Los valores hexadecimales también son admitidos, por ejemplo: `:a62991[Colourful Text]`

Puede combinar varios colores, por ejemplo, `--message ":e74c3c[scarlet], :e67e22[tangerine], :f1c40f[gold], :2ecc71[emerald], :3498db[sapphire], and :9b59b6[amethyst]"`

<img width="400" alt="image" src="/images/markdown_colour.png" />

### Ejemplos:

`dialog --message "Line 1  \nLine2  \nLine 3\n\nParagraph 2"`

`dialog --message "Line 1<br>Line2<br>Line 3<br><br>Paragraph 2"`

`dialog --message "Text can include **bold** and _italics_`

`dialog --message "### Heading 3"`

`dialog --message " * point 1\n * point 2\n * point 3"`

`dialog --message "[A link that will open in the default browser](https://some.link.com/)"`

`dialog --message "\![Inline images are also supported](https://upload.wikimedia.org/wikipedia/commons/8/85/Logo-Test.png)"`

**Precaución:** Al utilizar imágenes incrustadas, es necesario escapar el carácter inicial `!` transformándolo en `\!`, de lo contrario, su sistema operativo podría interpretarlo como un comando.

