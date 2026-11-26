---
title: Imagens de fundo
description: Adicionar imagens de fundo e marcas d'água às janelas de diálogo
translationSynced: 2026-11-25T11:29:46+00:00
---

## Imagens de fundo

As imagens podem ser exibidas em segundo plano, como parte da janela principal de diálogo, e podem ser usadas para inserir uma marca d'água ou outra imagem por trás do conteúdo normal da janela.

![image](https://user-images.githubusercontent.com/3598965/171406081-8e9e5363-56fc-46f9-baa8-ff881a4a4af3.png)

Os fundos podem ser controlados através dos seguintes recursos:

### `--background`

```
-bg, --background <file | url | colour= >
```

Exibe o arquivo selecionado como imagem de fundo. Se a imagem for maior do que o tamanho padrão da janela de diálogo (820x380) e nenhuma opção de tamanho de janela for fornecida (especificamente, a altura da janela), a altura da janela de diálogo será ajustada para que a imagem preencha toda a largura da janela, que é 820 por padrão, ou o valor especificado usando `--width`

Alternativamente, uma cor sólida pode ser especificada usando o prefixo `colour=`. A cor pode ser definida como um valor hexadecimal ou por um nome de cor.

Por exemplo: `--background colour=red` ou `--background colour=#ff0000`

Por padrão, um efeito de gradiente sutil é aplicado a cores sólidas. Para desativá-lo, adicione `,nogradient`.

`--background colour=red,nogradient`

Um gradiente linear pode ser especificado usando o prefixo `gradient=`. Forneça duas ou mais cores separadas por vírgula, e, opcionalmente, defina a direção com `:angle=<degrees>`:

```sh
--background "gradient=red,blue"
--background "gradient=red,orange,yellow:angle=135"
```

Convenções de ângulo: `0` = de baixo para cima; `90` = da esquerda para a direita (padrão); `180` = de cima para baixo; `270` = da direita para a esquerda.

Se apenas uma cor for fornecida para `gradient=`, o resultado será idêntico ao de `colour=`.


### `--bgalpha`

```
-ba, --bgalpha <number>
```

Define a opacidade ou transparência da camada de fundo. Pode ser qualquer número entre `0` (totalmente transparente) e `1` (totalmente opaco). O valor padrão é `0.5`


### --bgposition

```
-bp, --bgposition [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]
```

Posiciona a imagem de fundo na janela. Funciona melhor se as dimensões da imagem forem menores do que a janela principal, como, por exemplo, o logotipo de uma empresa. A posição padrão é `centre`


### --bgfill

```
-bf, --bgfill [fill | fit]
```

Especifica como o diálogo deve exibir a imagem dentro da janela

`fill` Redimensiona a imagem para preencher toda a janela. A imagem pode ser cortada, se necessário. `fit` Redimensiona a imagem para que ela se encaixe na janela, mas não a corta, o que pode resultar em bordas pretas em áreas não transparentes (se a imagem de origem for um arquivo PNG).

O padrão é `none`, o que exibirá a imagem na resolução original

## Fundo da tela - `--screenbackground`

```
--screenbackground <file | url>
```

Exibe a imagem especificada em tela cheia, por trás da janela de diálogo — ao contrário de `--background`, que fica *dentro* da janela de diálogo. Todas as outras funções da janela de diálogo permanecem disponíveis, mas o usuário não pode interagir com nenhum outro aplicativo até que a janela swiftDialog seja fechada (semelhante a `--blurscreen`, mas exibindo uma imagem em vez de um efeito de desfoque).

```sh
dialog --screenbackground /path/to/wallpaper.jpg
dialog --screenbackground https://example.com/background.png
```