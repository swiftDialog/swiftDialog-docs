---
title: Caixa de informações
description: Exibir informações adicionais em uma área de conteúdo secundária
translationSynced: 2026-11-25T11:29:16+00:00
---

## Caixa de informações - `--infobox`

A caixa de informações é a área localizada abaixo de onde o ícone é exibido.

Ela exibe uma fonte menor, utilizando uma cor secundária, e é útil para apresentar informações adicionais, como detalhes do sistema.

`--infobox` aceita qualquer texto formatado em Markdown.

#### Exemplo:

`--infobox "### Additional Info\n\n#### Item 1  \n - Point one  \n - Point two  \n#### Item 2  \n - Point three  \n - Point four"`

![Captura de tela de 10 de setembro de 2024, às 16:13:59](https://github.com/user-attachments/assets/d78c2abc-976b-4bb7-b6e8-ff0c487cfe01)

## Largura da caixa de informações - `--infoboxwidth`

Por padrão, a caixa de informações compartilha a largura da coluna de ícones. `--infoboxwidth <number>` define a largura da área de texto da caixa de informações (em pontos) de forma independente do tamanho do ícone, permitindo que você aumente a largura da caixa de informações sem aumentar o tamanho do ícone.

`--infoboxwidth 300`