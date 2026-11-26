---
title: Tela cheia
description: Criando janelas de diálogo em tela cheia para apresentações e para o modo kiosk
translationSynced: 2026-11-25T11:31:05+00:00
---

A opção de ocupar a tela inteira é suportada através das opções de linha de comando `--fullscreen` ou `-f`.

Nessa configuração, apenas o banner, o título, o ícone e a mensagem são exibidos. Outras opções ainda podem ser especificadas, mas não serão mostradas. No entanto, a janela de diálogo continuará a responder à entrada do teclado (teclas "escape" e "enter") e será fechada com o código de saída apropriado.

A área de exibição ajustará automaticamente o tamanho para diferentes resoluções, de 1024x640 até 5K. (Aceitamos doações de monitores XDR para testes com resoluções de 6K).

As opções terão um comportamento ligeiramente diferente no modo de tela cheia em comparação com o modo normal.

### `--bannerimage` `-n`

As imagens de banner são exibidas centralizadas na parte superior da tela e ocuparão no máximo 95% da largura da área de exibição e 10% da altura da área de exibição. Isso permite a exibição de imagens de banner longas e estreitas, se necessário.

Exibir um banner também exibe uma linha horizontal abaixo, com aproximadamente 95% da largura da área de exibição.

### `--title` `-t`

O título será exibido na parte superior da tela ou logo abaixo de um banner, ocupando toda a largura da tela.

### `--icon` `-i`

As imagens de ícones são exibidas centralizadas, abaixo do título. Formatos de imagem padrão são aceitos, no entanto, esta exibição não suporta a opção de sobreposição de ícones.

### `--message` `-m`

A área de mensagens ocupará todo o espaço disponível na tela, abaixo do título, da barra de ferramentas e dos ícones. Ela será centralizada vertical e horizontalmente e ocupará toda a largura da tela.

Se forem utilizados o banner, o título e o ícone, a área de mensagem ocupará os 40-50% inferiores da tela (uma área maior está disponível em telas maiores). Se o ícone e o banner forem omitidos, os 60-75% inferiores da tela serão utilizados.

Cada linha de texto na área de mensagem terá um espaçamento duplo, com um máximo de 12 linhas.

## Exemplos

Estes exemplos mostram como a tela em tela cheia aparece em um monitor padrão de 13 polegadas, com as áreas de conteúdo destacadas.

### Visualização simples, que exibe apenas o título e a mensagem

<img width="1000" alt="Screenshot1" src="https://user-images.githubusercontent.com/3598965/114690586-306d0280-9d5a-11eb-9504-1e2d25f93711.png">


### Utilizando todas as opções, incluindo a imagem de fundo e o ícone

<img width="1000" alt="Screenshot2" src="https://user-images.githubusercontent.com/3598965/114690604-3531b680-9d5a-11eb-94c5-242693f6d335.png">