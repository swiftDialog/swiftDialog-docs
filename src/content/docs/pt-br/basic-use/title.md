---
title: Personalizando o título
description: Aprenda como definir e personalizar o texto do título e as propriedades da fonte no swiftDialog
translationSynced: 2026-11-25T10:43:19+00:00
---

## Definindo o título

Utilize a opção de linha de comando `-t` ou `--title` para especificar o que você deseja exibir na área de título da janela de diálogo.

Exemplo:

`--title "An Important Message"`

`-t "An Important Message"`

A área do título é uma seção retangular e preenchida na parte superior da janela de diálogo. Se o texto for mais longo do que o tamanho disponível na janela, ele será truncado.

![image](https://user-images.githubusercontent.com/3598965/125153474-47739300-e197-11eb-8b46-85b3cb13194a.png)

## Personalizando as propriedades da fonte do título

Use a opção de linha de comando `--titlefont` para definir as propriedades da fonte do título.

### Sintaxe CSV

As propriedades da fonte são expressas na forma de `property=value`, e múltiplas propriedades são separadas por uma vírgula.

As propriedades que podem ser modificadas são:
 * `colour=<hex_value>` (alternativamente `color=<hex_value>`)
   * especificado em formato hexadecimal, por exemplo, #00A4C7
 * `size=<float>`
   * Aceita qualquer valor decimal, por exemplo, 30, 65, 72.3
 * `weight=<text>`
   * Aceita qualquer um dos seguintes valores: `thin`, `light`, `regular`, `medium`, `heavy` ou `bold` (padrão).
 * `name=<fontname>`
   * Aceita um nome de fonte ou uma família de fontes. A lista de nomes disponíveis pode ser obtida usando o comando `--listfonts` ou consultando o aplicativo "Font Book" do macOS.
 * `alignment=[left|right]`
   * Posiciona o texto do título alinhado à esquerda ou à direita
 * `offset=<float>`
   * Desloca o texto do título horizontalmente pelo número de pontos especificado. Valores positivos movem o texto para a direita, enquanto valores negativos movem o texto para a esquerda. Ao usar `alignment=right`, a direção do deslocamento é automaticamente invertida, de modo que um valor positivo ainda move o texto em direção à borda direita.
 * `shadow`
   * Adiciona uma sombra projetada ao texto (booleano, não é necessário especificar um valor).

 > **CUIDADO:** Tenha cuidado ao combinar nomes de fontes e espessuras. Ao especificar uma fonte ou família de fontes por nome, certas espessuras podem não estar disponíveis. Se isso ocorrer, a espessura da fonte especificada será ignorada.

Você pode utilizar um ou mais parâmetros, e a ordem em que eles são especificados não é importante. Por exemplo, se você deseja apenas modificar o tamanho, pode usar o seguinte:

`--titlefont "size=60"`

Exemplo 1: `--titlefont "colour=#00A4C7,weight=light,size=60"`

Este exemplo define a cor para o valor `#00A4C7`, o peso para `light` e o tamanho da fonte para `60`, e será exibido da seguinte forma:

<img width="400" alt="image" src="/images/titlefont1.png" />

Exemplo 2: `--titlefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`

Este exemplo define a cor para o valor `#D054A0 `, o tamanho para `40` e utiliza o nome da fonte "Chalkboard-Bold".

<img width="400" alt="image" src="/images/titlefont2.png" />

Exemplo – Alinhamento à esquerda/direita:

`--titlefont alignment=left` - `--titlefont alignment=right`

<img width="400" alt="image" src="/images/titlefont_left.png" /> <img width="400" alt="image" src="/images/titlefont_right.png" />

### Sintaxe de Objetos JSON

A partir da versão 3.1.1, `--titlefont` e `--messagefont` também podem ser especificados como objetos JSON para um controle mais preciso:

```bash
--titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'
--messagefont '{"size":24,"colour":"red","weight":"medium"}'
```

**Características:**
- `name` - Nome ou família da fonte
- `size` - Tamanho da fonte em pontos
- `colour` / `color` - Cor do texto (código hexadecimal ou nome).
- `weight` - Espessura da fonte: `thin`, `light`, `regular`, `medium`, `heavy`, `bold`
- `alignment` - Alinhamento do texto: `left`, `right` (apenas título).
- `offset` - Deslocamento horizontal em pontos (apenas para o título).
- `shadow` - Adicionar sombra projetada (booleano).

**Exemplos:**

```bash
# Title font with all properties
dialog --titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'

# Message font with size and colour
dialog --messagefont '{"size":24,"colour":"#FF0000","weight":"medium"}'

# Title font with alignment and offset
dialog --titlefont '{"size":36,"colour":"blue","alignment":"right","offset":20}'
```

**Observação:** A chave `shadow` agora é suportada no formato JSON (anteriormente, estava disponível apenas no formato CSV).

### Utilizando cores no título

Usar `colour=<value>` define a cor base do texto, mas é possível definir a cor de palavras ou letras individuais usando o formato `:colour[text]`

Exemplo:

`--title ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/title_colour.png" />

## Legenda

Use `--subtitle <text>` para exibir uma linha de texto secundária abaixo do título, utilizando a mesma fonte, mas em um tamanho menor.

```sh
dialog --title "System Update" --subtitle "Please save your work before continuing"
```

O título secundário (ou legenda) herda o mesmo nome de fonte, espessura e cor do título principal, mas é exibido em um tamanho `titlefont size − 10pt`.

#### Ocultar a área do título

Use a palavra-chave `none` para ocultar a área do título. Isso removerá a barra de título e a linha de separação horizontal

e.g. `--title none`




