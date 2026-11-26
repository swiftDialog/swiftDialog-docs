---
title: Arquivo de comandos
description: Atualização dinâmica de diálogos com conteúdo novo, utilizando arquivos de comando
translationSynced: 2026-11-25T11:21:31+00:00
---

Algum conteúdo dos diálogos pode ser atualizado em tempo real, mesmo após o lançamento. Isso é facilitado pelo envio de comandos para um arquivo de comandos, que o Dialog lê e interpreta.

---

Para permitir que comandos sejam enviados ao diálogo a partir do mesmo script, ele deve ser iniciado em segundo plano.

```sh
/usr/local/bin/dialog & sleep 0.1
```

O `sleep 0.1` concede 100 milissegundos para que o sistema Dialogue inicialize antes do envio do primeiro comando.

O caminho padrão para o arquivo de comandos é `/var/tmp/dialog.log`. É possível definir um caminho personalizado usando o argumento `--commandfile`:

```sh
dialog --commandfile /var/tmp/my.log
```

Envie comandos utilizando:

```sh
echo "<command>: <value>" >> /var/tmp/dialog.log
```

---

## Conteúdo

| Comando | Descrição |
|---|---|
| `title: <text>` | Atualizar o título da caixa de diálogo |
| `title: none` | Ocultar a área do título |
| `titlefont: <params>` | Atualiza as propriedades da fonte do título. Aceita pares separados por espaços: `key=value`, `size=<float>`, `weight=<value>`, `colour=<color\|hex>`, `name=<fontname>`, `shadow=<bool>` |
| `message: <text>` | Substitua o conteúdo da mensagem. Suporta Markdown. |
| `message: + <text>` | Anexar à mensagem existente (adiciona uma quebra de linha antes do novo conteúdo). |
| `message: /path/to/file.md` | Carregar o conteúdo da mensagem a partir de um arquivo Markdown local |
| `alignment: [left\|center\|right]` | Defina o alinhamento do texto da mensagem |

---

## Ícone

| Comando | Descrição |
|---|---|
| `icon: <path\|url\|SF Symbol>` | Altere o ícone exibido |
| `icon: none` | Ocultar o ícone |
| `icon: centre` / `icon: center` | Mova o ícone para a posição central |
| `icon: left` / `icon: default` | Mova o ícone de volta para a posição padrão, à esquerda |
| `icon: size: <num>` | Altere o tamanho do ícone |
| `iconalpha: <float>` | Definir a opacidade do ícone (0,0: transparente → 1,0: opaco). |
| `overlayicon: <path\|url\|SF Symbol>` | Defina o ícone de sobreposição |
| `overlayicon: none` | Ocultar o ícone sobreposto |

---

## Banner e fundo

| Comando | Descrição |
|---|---|
| `bannerimage: <path\|url>` | Defina a imagem de cabeçalho |
| `bannerimage: none` | Remova a imagem do banner |
| `bannertext: enable` | Exibir o título como texto de banner (define a cor da fonte para branco). |
| `bannertext: disable` | Restaurar a aparência padrão do título |
| `bannertext: shadow` | Ativar a sombra projetada no texto do título do banner |
| `bannertext: <text>` | Defina o texto do título do banner e habilite o modo de texto do banner |

---

## Imagens e Mídia

| Comando | Descrição |
|---|---|
| `image: <path\|url>` | Exibir uma imagem (adiciona a imagem ao carrossel, caso já haja imagens sendo exibidas). |
| `image: show` | Mostrar a imagem atual |
| `image: hide` | Ocultar a imagem atual |
| `image: clear` | Remova todas as imagens |
| `imagecaption: <text>` | Posicione a legenda abaixo da imagem exibida |
| `video: <path\|url>` | Exibe um vídeo. Compatível com atalhos `youtube=<id>` e `vimeo=<id>`. |
| `video: none` | Remova o vídeo |
| `webcontent: <url>` | Carregar um URL na área de conteúdo da web |
| `webcontent: none` | Remova o conteúdo da web |

---

## Botões

| Comando | Descrição |
|---|---|
| `button1: enable` / `button1: show` | Ativar o Botão 1 |
| `button1: disable` / `button1: hide` | Desativar o Botão 1 |
| `button1text: <text>` | Botão "Atualizar" - rótulo 1 |
| `button2: enable` / `button2: show` | Ativar o Botão 2 |
| `button2: disable` / `button2: hide` | Desativar o Botão 2 |
| `button2text: <text>` | Botão "Atualizar" (label 2) |
| `buttonsize: [mini\|small\|regular\|large]` | Definir o tamanho do botão |
| `infobutton: <text>` | Atualizar o texto do botão "Informações" |
| `infotext: <text>` | Atualize a área de texto informativa |
| `infotext: disable` / `infotext: hide` | Ocultar o texto informativo |
| `infotext: reset` / `infotext: clear` | Limpar o valor do texto informativo |

---

## Caixa de informações

| Comando | Descrição |
|---|---|
| `infobox: <text>` | Substitua o conteúdo da caixa de informações. Suporta Markdown. |
| `infobox: + <text>` | Adicionar o conteúdo à caixa de informações existente |
| `infobox: /path/to/file.md` | Carregar o conteúdo da caixa de informações a partir de um arquivo Markdown local |

---

## Barra de progresso

| Comando | Descrição |
|---|---|
| `progress: <int>` | Defina a barra de progresso para um valor específico de etapa |
| `progress: increment` | Aumente a barra de progresso em um passo |
| `progress: increment <n>` | Aumente a barra de progresso em `n` etapas |
| `progress: complete` | Defina a barra de progresso para o valor máximo |
| `progress: reset` / `progress: indeterminate` | Redefina a barra de progresso para o modo indeterminado |
| `progress: show` / `progress: enable` / `progress: create` | Mostre a barra de progresso |
| `progress: hide` / `progress: disable` / `progress: delete` / `progress: remove` | Ocultar a barra de progresso |
| `progresstext: <text>` | Atualize a legenda abaixo da barra de progresso |

---

## Listas

| Comando | Descrição |
|---|---|
| `list: <csv>` | Substitua a lista por novos itens, separados por vírgulas |
| `list: clear` | Limpar todos os itens da lista e ocultar a lista |
| `list: show` | Mostrar a lista |
| `list: hide` | Ocultar a lista sem apagar seu conteúdo |

### Atualização de itens da lista

Atualizar um item existente pelo título (formulário simplificado):

```sh
echo "listitem: My Item: success" >> /var/tmp/dialog.log
echo "listitem: My Item: Processing..." >> /var/tmp/dialog.log
```

Atualize um item com controle total, utilizando propriedades separadas por vírgula:

```sh
echo "listitem: title: My Item, status: success, statustext: Done" >> /var/tmp/dialog.log
echo "listitem: index: 0, status: fail, statustext: Error occurred" >> /var/tmp/dialog.log
```

Adicionar um novo item ao final da lista:

```sh
echo "listitem: add:, title: New Item, status: wait, statustext: Pending" >> /var/tmp/dialog.log
```

Excluir um item:

```sh
echo "listitem: title: My Item, delete:" >> /var/tmp/dialog.log
echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log
```

**Propriedades disponíveis `listitem`:**

| Propriedade | Descrição |
|---|---|
| `title: <text>` | Correspondência por título |
| `index: <int>` | Corresponda o item pelo índice (baseado em zero). |
| `subtitle: <text>` | Defina o subtítulo do item |
| `icon: <path\|url\|SF Symbol>` | Defina o ícone do item |
| `iconalpha: <float>` | Definir a opacidade do ícone do item |
| `status: <status>` | Defina o ícone de status. Escolha uma das opções: `wait`, `success`, `fail`, `error`, `pending`, `progress`, ou um nome de símbolo SF (opcionalmente com um sufixo de cor, por exemplo, `lock.shield.fill-green`). |
| `statustext: <text>` | Defina o texto do rótulo de status |
| `progress: <float>` | Defina um valor de progresso inline (exibe um status no formato de barra de progresso). |
| `action: <url>` | URL a ser aberta quando o item for clicado |
| `add:` | Adicionar um novo item à lista |
| `delete:` | Excluir o item selecionado |

---

## Mensagem de Ajuda

| Comando | Descrição |
|---|---|
| `helpmessage: <text>` | Atualize o conteúdo da mensagem de ajuda. Suporta Markdown. |

---

## Janela

| Comando | Descrição |
|---|---|
| `width: <num>` | Altere a largura da janela |
| `height: <num>` | Altere a altura da janela |
| `position: <position>` | Mova a janela. Uma das opções `top`, `bottom`, `left`, `right`, `centre`, ou uma combinação (por exemplo, `topright`) deve ser selecionada. |

---

## Visibilidade da janela

| Comando | Descrição |
|---|---|
| `activate:` | Traga a janela de diálogo para o primeiro plano |
| `show:` | Exibir a janela de diálogo |
| `hide:` | Ocultar a janela de diálogo |
| `minimize:` / `minimise:` | Minimize a janela de diálogo para a barra de dock |
| `maximize:` / `maximise:` | Restaurar uma janela de diálogo minimizada |
| `blurscreen: enable` | Ative o efeito de desfoque da tela |
| `blurscreen: disable` | Desative o efeito de desfoque da tela |

---

## Ícone da barra de tarefas

| Comando | Descrição |
|---|---|
| `showdockicon: enable` / `showdockicon: true` / `showdockicon: 1` | Exibir o ícone de "Diálogo" na barra de aplicativos |
| `showdockicon: <any other value>` | Ocultar o ícone da caixa de diálogo na barra de aplicativos |
| `dockicon: <file\|url>` | Defina uma imagem personalizada como o ícone da barra de aplicativos |
| `dockicon: none` / `dockicon: default` | Restaure o ícone padrão da barra de diálogo |
| `dockiconbadge: <text>` | Exibir um indicador na barra de aplicativos |
| `dockiconbadge: none` / `dockiconbadge: remove` | Remova o indicador (ou "badge") do ícone da barra de aplicativos |
| `bounce:` | Clique uma vez no ícone do Dock (apenas para fins informativos). |
| `bounce: critical` | Mantenha pressionado o ícone do Dock até que a janela apareça em primeiro plano |

---

## Sair

| Comando | Descrição |
|---|---|
| `quit:` | Sair do diálogo com o código de saída 5 |
