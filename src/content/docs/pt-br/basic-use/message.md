---
title: Personalizando a área de mensagens
description: Aprenda como configurar e personalizar o texto da mensagem, as propriedades da fonte e o posicionamento no swiftDialog
translationSynced: 2026-11-25T10:42:55+00:00
---

Utilize a opção de linha de comando `-m` ou `--message` para especificar o que você deseja exibir na área de mensagem da caixa de diálogo.

Exemplo:

`--message "This is the detail of an Important Message that you should read"`

`-m "This is the detail of an Important Message that you should read"`

A área de mensagens pode ocupar 2/3 da largura da janela de diálogo ou a largura total, caso a área de ícones não esteja sendo exibida.

As mensagens serão automaticamente formatadas para caber na largura da área de exibição e, se excederem essa largura, serão exibidas em várias linhas. Caso ultrapassem a área de exibição total disponível, elas poderão ser roladas.


<img width="400" alt="image" src="/images/lorem_ipsum_1.png" />

<img width="400" alt="image" src="/images/lorem_ipsum_2.png" />

### Obtenção de conteúdo

Além de fornecer uma string de texto, você pode, em vez disso, fornecer o caminho ou a URL para um arquivo Markdown. Qualquer arquivo que termine com `.md` será tratado como um arquivo de origem Markdown.

Exemplo:

`--message "/path/to/content.md"`

`--message "https://www.example.com/example.md"`

## Posicionamento da mensagem

`--messagealignment` e `--messageposition` permitem que você defina a posição onde a mensagem aparece no diálogo. Isso é útil para criar diálogos com a mensagem centralizada vertical e horizontalmente.

<img width="200" alt="image" src="/images/lorem_ipsum_3.png" />

## Modificando a fonte, a cor, o tamanho e o alinhamento da mensagem

`--alignment [left | centre | center | right]`

Defina o alinhamento da mensagem. O padrão é `left`

`--messagefont <text>`

Permite modificar a fonte, o tamanho e a cor do texto da mensagem.

`color,colour=<text><hex>`

> `<text>` Pode ser qualquer uma das cores padrão da Apple: `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Se a opção for inválida, a cor padrão será a cor primária do sistema (geralmente `black` se estiver no modo claro ou `white` se estiver no modo escuro).

> `<hex>` é especificado em formato hexadecimal, por exemplo, #00A4C7

`size=<float>` Aceita qualquer valor numérico de ponto flutuante (por exemplo, 15.7, 20, 32.0).

`name=<fontname>` - aceita o nome de qualquer fonte instalada


`--message "Welcome to swiftDialog" --messagefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`


<img width="400" alt="image" src="/images/message_font.png" />

### Utilizando cores adicionais na mensagem

Usar `colour=<value>` define a cor base da mensagem, mas você pode definir a cor de palavras ou letras individuais usando o formato `:colour[text]`.

Exemplo:

`--message ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/message_colour.png" />

