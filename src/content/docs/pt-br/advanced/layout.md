---
title: Layout
description: Personalização da ordem e organização dos elementos de diálogo
translationSynced: 2026-11-25T11:30:55+00:00
---

## Ordenação personalizada da visualização

`--vieworder <csv>`

Com exceção das imagens e do conteúdo das mensagens, os elementos da janela podem ser reorganizados.

A ordem padrão é:
 > textfile
 > webcontent
 > listitem
 > checkbox
 > textfield
 > radiobutton
 > dropdown

 Esses elementos podem ser reorganizados para atender às necessidades de exibição, especificando a ordem desejada em uma lista CSV de itens, por exemplo: `--vieworder "dropdown, textfield, checkbox"`. Esses valores são opções de linha de comando e devem ser digitados em inglês.

 <img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/1b69abc7-4367-4eac-9e2d-a208ea47a60f" width="750px">