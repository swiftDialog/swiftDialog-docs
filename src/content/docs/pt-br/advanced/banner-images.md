---
title: Imagens para banners
description: Exibir imagens no topo das janelas de diálogo, com a opção de adicionar um texto de título sobreposto à imagem
translationSynced: 2026-11-25T11:29:43+00:00
---

Use a opção de linha de comando `-n` ou `--bannerimage` para especificar uma imagem a ser exibida no topo da janela de diálogo.

Uso:

`--bannerimage <file | url | colour= >`

O uso de uma imagem de banner desativará a exibição da área da imagem do ícone. Isso é equivalente a usar a opção `--hideicon`

## Uso básico

O componente Dialog aceita imagens nos formatos png e jpg e exibe a imagem especificada na área do banner. A imagem do banner tem, no máximo, 150 pontos de altura e ocupa toda a largura da janela do diálogo. Em conjunto com a opção `-s` ou `--small`, a altura da imagem do banner é limitada a 100 pontos

Qualquer tamanho de imagem pode ser utilizado. A área de exibição da imagem se ajustará ao tamanho da imagem do banner que você deseja usar, até uma altura máxima de 150 pontos.

<img width="727" alt="Banner Image Small" src="https://user-images.githubusercontent.com/3598965/112744135-fcb77c00-8fe8-11eb-8fac-437c86872eae.png">

Uma altura específica pode ser definida usando a opção `--bannerheight`. Isso substituirá a altura padrão.

Além disso, uma cor sólida pode ser especificada usando o prefixo `colour=`. A cor pode ser definida como um valor hexadecimal ou um nome de cor.

Exemplo:

`--bannerimage colour=red` ou `--bannerimage colour=#ff0000`

Por padrão, uma sobreposição sutil de gradiente, que varia do branco para uma cor e, finalmente, para o preto, é aplicada a cores sólidas. Para desativar essa função, adicione `,nogradient`.

`--bannerimage colour=red,nogradient`

### Banners com efeito de gradiente

Um gradiente linear pode ser especificado usando o prefixo `gradient=`. Forneça duas ou mais cores separadas por vírgula, e, opcionalmente, defina a direção com `:angle=<degrees>`:

```sh
--bannerimage "gradient=red,blue"
--bannerimage "gradient=red,orange,yellow:angle=135"
```

Convenções de ângulo: `0` = de baixo para cima, `90` = da esquerda para a direita (padrão), `180` = de cima para baixo, `270` = da direita para a esquerda.

Se apenas uma cor for fornecida a `gradient=`, o resultado será idêntico a `colour=` (uma sobreposição de branco para a cor especificada e, em seguida, para preto).

## Texto do título dentro da área do banner

`--bannertitle`

Com este comando, você pode optar por exibir o texto do título dentro do banner, utilizando o recurso []. Ao fazer isso, a cor do texto será definida como branca por padrão, mas essa configuração pode ser alterada com os [modificadores de personalização da fonte do título](/basic-use/customizing-title#customising-title-font-properties)].

Você pode usá-lo como uma opção para `--title`, ou pode fornecer uma string para exibir como título. Se tanto `--title` quanto `--bannertitle` receberem argumentos de string, `--bannertitle` terá prioridade.

Todos os modificadores `--titlefont` se aplicam ao texto do título do banner, incluindo `shadow`, `colour`, `size`, `weight`, `alignment` e `offset`.

`--titlefont shadow=1` Adiciona uma sombra abaixo do texto.

Se `--subtitle` também estiver definido, a legenda será exibida abaixo do título, dentro da área do banner, utilizando a mesma fonte, mas em um tamanho menor.

![image](https://user-images.githubusercontent.com/3598965/216027666-5e4433d5-9e1e-4590-b34d-8d7943cbe5a5.png)