---
title: Apresentação
description: Criando diálogos para o modo de apresentação de processos e tarefas em andamento
translationSynced: 2026-11-25T11:31:46+00:00
---

## Modo de Apresentação

`--presentation` ou `--style presentation`

O modo de apresentação é um modo de saída do swiftDialog que não permite interação do usuário e é destinado a exibir um processo ou tarefa em andamento.

Atualizar a tela exigirá o uso de um [arquivo de comandos](/pt-br/advanced/command-file) e comandos apropriados.

A interface é dividida em duas áreas principais de conteúdo e um rodapé que contém uma barra de progresso e botões.

## Área de Informações

A parte esquerda de 1/3 da janela contém uma área de informações e pode exibir apenas uma das seguintes opções:

### Padrão

Uma cor de fundo que representa a preferência de cor de destaque do usuário.

Você pode, opcionalmente, aplicar os seguintes modificadores:
 - `--infobox <text>` para exibir texto (formato Markdown suportado).
   - O texto está centralizado verticalmente
 - `--background color=<color|hex>` para definir a cor de fundo
   - Se nenhuma cor for especificada, a cor de destaque do sistema será utilizada
 - `--icon <image>` para exibir um ícone no canto superior esquerdo
 - `--iconsize <int>` para definir o tamanho do ícone.

### Imagem

Especifique um ou mais `--image <image>` para preencher esta área com uma imagem

Várias imagens serão exibidas em sequência, como um carrossel. Inclua `--autoplay <sec>` para que as imagens girem.

**Dicas**
* Para obter os melhores resultados, utilize imagens com orientação vertical (retrato)
* As imagens serão redimensionadas para preencher a área, e pode ocorrer corte se forem utilizadas várias imagens com proporções diferentes.

Execute o modo de apresentação com `--debug` e, após fechar a janela de diálogo, um tamanho de imagem recomendado para a janela atual será incluído na saída do registro de depuração.

e.g.

    DEBUG: O tamanho ideal da imagem da barra lateral para esta dimensão da janela seria: largura: 492,0 e altura: 636,0

### Conteúdo da web

Especifique `--webcontent <url>` para exibir o conteúdo de um arquivo HTML.

**Dica**
* Se estiver utilizando um arquivo local, faça referência ao arquivo utilizando `file:///path/to/file.html`

## Área de conteúdo

Os dois terços direitos da janela são dedicados ao conteúdo, que pode ser apresentado em uma das seguintes formas:

### Padrão

Qualquer `--message <text>` em qualquer um dos formatos suportados.

### Lista

Um ou mais itens da lista <item>, em qualquer um dos formatos suportados.

## Rodapé

Como a exibição do progresso e de outros conteúdos atualizáveis é a principal função do modo de apresentação, a barra de status da janela está sempre visível e dedicada a uma barra de progresso de largura total e a botões.

## Exemplos

**Conteúdo apenas em texto**

`dialog --presentation --infobox "<markdown>" --icon "<image>" --message "<markdown>"`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/7e5ebb1b-6fe1-4005-ab6f-47ef7396801c" width="500px">

**Visualização da web na área de informações e itens de lista na área de conteúdo.**

`dialog --presentation --infobox "<url>" --listitem ...<items>...`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db20a3b0-f683-4e7f-baf6-89ca56d9684e" width="500px">