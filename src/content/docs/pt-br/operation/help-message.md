---
title: Mensagens de Ajuda
description: Adicionar mensagens de ajuda contextual às janelas de diálogo
translationSynced: 2026-11-25T11:53:12+00:00
---

## Mensagens de Ajuda

As mensagens de ajuda podem ser uma forma de fornecer informações adicionais, se necessário, sem ocupar espaço extra na janela de diálogo

`--helpmessage <text>`

`<text>` aceitará formatação em Markdown para mensagens

Quando disponível, um botão de "ajuda" adicional aparecerá ao lado do botão padrão.


![image](https://user-images.githubusercontent.com/3598965/216032093-2aede3aa-4cda-402c-9cd7-fa4edb506cfc.png)

Clicar nele exibirá a mensagem de ajuda em uma janela pop-up

![image](https://user-images.githubusercontent.com/3598965/216032203-35960f72-24f5-491e-8d75-b6b43e4a123c.png)

A altura da página exibida será ajustada de acordo com o tamanho da mensagem.

### `--helpimage`

Adicione uma imagem com `--helpimage /path/to/image.png`.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/d4c4504f-2e6f-4e83-882f-be0e799c9ffc" />

Suporta os argumentos padrão para ícones, incluindo códigos QR:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/1c4c99bc-8548-4547-b16b-0dd02cc2c02d" />

### `--helpalignment`

`--helpalignment [left | centre | center | right]`

Define o alinhamento do texto do conteúdo da mensagem na tela de ajuda. O alinhamento padrão corresponde à configuração de alinhamento atual.

### `--helpsheetbuttontext`

`--helpsheetbuttontext <text>`

Define o texto que aparece no botão usado para fechar a janela de ajuda. O valor padrão é `OK`.