---
title: Botões e Comportamento dos Botões
description: Aprenda como configurar o texto, as ações e o comportamento dos botões no swiftDialog
translationSynced: 2026-11-25T11:01:39+00:00
---

A janela de diálogo pode exibir até três botões.

Os botões são exibidos na parte inferior da janela de diálogo.

![Área dos botões de diálogo](https://user-images.githubusercontent.com/3598965/111854511-b4a6b280-8973-11eb-943d-e9843a6dc0fa.png)

## Botão 1 – O botão padrão
Por padrão, um único botão é exibido, com o rótulo "**OK**". O botão padrão está sempre presente, está associado à tecla **_Enter_** e fecha o aplicativo de diálogo com o código de saída `0`.

A etiqueta do botão padrão pode ser modificada com uma quantidade arbitrária de texto, utilizando a opção `--button1text`.

e.g. `--button1text "Enter to Continue"`

![Texto do botão 1 ](https://user-images.githubusercontent.com/3598965/111854635-4f9f8c80-8974-11eb-9f3c-ddbc62880209.png)

A ação também pode ser modificada utilizando a opção `--button1action`, portanto, além de simplesmente sair do aplicativo Dialog, é possível realizar outras ações

Nesta fase, as ações estão limitadas à abertura de um endereço URL no navegador padrão do usuário.

e.g. `--button1action "https://github.com/"`

## Botão 2 – O botão de cancelar
O segundo botão está oculto por padrão. Ele pode ser exibido usando a opção `-2` ou `--button2`, que mostrará o botão com o rótulo padrão de "**Cancelar**". O segundo botão está associado à tecla **_Esc_** e fecha o aplicativo de diálogo com o código de saída `2`.

A etiqueta do segundo botão pode ser modificada com uma quantidade arbitrária de texto, utilizando a opção `--button2text`. Ao utilizar esta opção, não é necessário invocar a opção `--button2`. A exibição do botão é implícita caso você esteja modificando a etiqueta de texto.

Exemplo:

`--button2text "I Don't Care"`

`-2 "I Don't Care"`

![Botão 2: Não me importo ](https://user-images.githubusercontent.com/3598965/111854834-7a3e1500-8975-11eb-8b00-e77756c9a917.png)

O botão 2 não possui outras ações implementadas.

## O botão "Mais informações"
O botão "Mais informações" está oculto por padrão. Ele pode ser exibido usando a opção `-3` ou `--infobutton`, que mostrará o botão com o rótulo padrão de "**Mais informações**". Clicar no botão fechará a janela swiftDialog com um código de saída de `3`

Se o argumento `--infobuttonaction` estiver presente, clicar no botão "Mais Informações" fará com que apenas a ação `--infobuttonaction` seja executada e a janela swiftDialog não será fechada automaticamente. Se o argumento `--quitoninfo` for adicionado, o comportamento de fechamento será restabelecido.

A etiqueta do botão de informações pode ser modificada com uma quantidade arbitrária de texto, utilizando a opção `--infobuttontext`. Ao usar essa opção, não é necessário utilizar a opção `--infobutton`. A exibição do botão é implícita quando você está modificando a etiqueta de texto.

Exemplo:

`--infobuttontext "Click here for more details"`

![Botão de Informação: clique para obter mais detalhes](https://user-images.githubusercontent.com/3598965/111854992-5cbd7b00-8976-11eb-9f3b-4e93c76db6f3.png)

A ação também pode ser modificada utilizando a opção `--infobuttonaction`, portanto, além de simplesmente sair do aplicativo Dialog, é possível realizar outras ações

Nesta fase, as ações estão limitadas à abertura de um endereço URL no navegador padrão do usuário.

e.g. `--infobuttonaction "https://github.com/"`

## Símbolos dos botões

Define o símbolo SF a ser usado, além do texto do botão

### Sintaxe CSV

```bash
--button1symbol <sf symbol name>[,position,rendering mode,size,color]
--button2symbol <sf symbol name>[,position,rendering mode,size,color]
--infobuttonsymbol <sf symbol name>[,position,rendering mode,size,color]
```

Aceita o nome do símbolo SF como argumento

Propriedades opcionais fornecidas como valores separados por vírgula (em qualquer ordem):
 - posição: uma das opções são: `leading`, `trailing`, `top`, `bottom` - padrão: `leading`
 - modo de renderização: um dos seguintes: `hierarchical`, `monochrome`, `multicolour`, `palette` - padrão: `monochrome`
 - paleta: adicione duas ou três cores no formato `palette=cor1-cor2-cor3`
   - Exemplo: `palette=red-green-blue`
 - tamanho: no formato `size=<num>`
 - cor: no formato color=<text|hex>
   - Se o modo de renderização multicolorida estiver definido, a cor será ignorada

Exemplo:

`--button1symbol heart.fill,color=red`

<img width="400" alt="image" src="/images/button_symbol.png" />

### Sintaxe de Objetos JSON

A partir da versão 3.1.1, os símbolos dos botões também podem ser especificados como objetos JSON, permitindo um controle mais preciso.

```bash
--button1symbol '{"name":"checkmark.circle","colour":"green","position":"trailing"}'
--button2symbol '{"name":"xmark.circle","colour":"red","position":"leading"}'
--infobuttonsymbol '{"name":"info.circle","colour":"blue"}'
```

**Características:**
- `name` - Nome do símbolo SF (obrigatório).
- `position` - Posição do símbolo: `leading`, `trailing`, `top`, `bottom` (padrão: `leading`)
- `colour` / `color` - Cor do símbolo (em hexadecimal ou nome).
- `size` - Tamanho do símbolo em pontos
- `rendering` - Modo de renderização: `hierarchical`, `monochrome`, `multicolour`, `palette`
- `palette` - Conjunto de 2 a 3 cores para símbolos multicoloridos (separadas por vírgula em CSV, em formato de array em JSON).

**Exemplos:**

```bash
# Basic symbol with colour
dialog --button1symbol '{"name":"checkmark.circle","colour":"green"}'

# Symbol with position and size
dialog --button2symbol '{"name":"xmark.circle","colour":"red","position":"leading","size":20}'

# Multicolor symbol with palette
dialog --button1symbol '{"name":"person.3.sequence.fill","rendering":"palette","palette":["red","green","blue"]}'

# Symbol with all options
dialog --button1symbol '{"name":"heart.fill","colour":"pink","position":"trailing","size":24,"rendering":"hierarchical"}'
```

**Observação:** Ao utilizar `rendering: palette`, a paleta deve ser um array no formato JSON: `["red","green","blue"]`. Em formato CSV, utilize hífens para unir os elementos: `palette=red-green-blue`.

## Posição do botão

Por padrão, o botão "Button1" e o botão "Button2" estão localizados à direita, enquanto o botão "Infobutton" está localizado à esquerda.

Usar `--buttonstyle center` posicionará os botões 1 (e 2, se presentes) na parte inferior central da janela de diálogo

<img width="412" alt="buttoncenter" src="https://github.com/bartreardon/swiftDialog/assets/3598965/4081016a-7c70-41a9-95e8-4f1afb08a635">

`--infobuttontext` e `--infotext` não são compatíveis quando a opção `--buttonstyle center` é utilizada

## Estilo "empilhamento" para botões

`--buttonstyle stack`

Exibe o botão 1 e o botão 2 em uma disposição vertical que ocupa toda a largura.

<img width="250" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/f6003ee0-a2ac-4305-8073-c8b1504ed295">

`--infobuttontext` e `--infotext` não são compatíveis quando a opção `--buttonstyle stack` é utilizada

## Comportamento das teclas `[return]` e `[enter]`

Sem campos de entrada, o elemento de controle de entrada com foco no diálogo é `button1`, e tanto `[enter]` quanto `[return]` ativarão o botão, pois este é o único elemento interativo na janela e, portanto, recebe o foco padrão do teclado. O resultado é que isso fecha o diálogo (assumindo que o botão esteja ativo e não desabilitado).

A tecla `[return]` sempre ativa o botão1, a menos que um campo de edição esteja em foco. A tecla `[enter]` só funciona no elemento que está em foco (por isso, ela serve para fechar a janela de diálogo em sistemas que não possuem elementos de entrada).

Em um campo de texto de uma única linha, `[return]` não permite a inserção de quebras de linha, portanto, a ação padrão é executada e a janela de diálogo é fechada (a ação padrão é ativada). Em contraste, `[enter]` não tem efeito, pois também não permite a inserção de quebras de linha, mas, como não tem controle sobre a ação padrão, nada acontece.

Em um campo de texto de várias linhas (por exemplo, `--textfield` com `editor` habilitado), a tecla `[return]` *pode* inserir uma quebra de linha, e essa ação tem prioridade sobre qualquer atribuição padrão que ela possa ter (por exemplo, a ação de apertar o botão1 para fechar a janela). A tecla `[return]` também funciona como esperado e insere uma nova linha.

### Alterando o comportamento padrão de `[return]`, `[enter]` ou `[esc]`

Se você não deseja que os comportamentos padrão de `[return]`, `[enter]` ou `[esc]` fechem a janela de diálogo, você pode usar a opção `--hidedefaultkeyboardaction` para alterar esse comportamento. Essa opção modifica as teclas padrão `[return]` ou `[escape]`, exigindo também a combinação de `cmd`+`shift` para que sejam ativadas. Isso ajuda a evitar o fechamento acidental de janelas de diálogo.

## Códigos de retorno

Os seguintes códigos de retorno são enviados após cada ação. Eles podem ser ignorados ou utilizados em um script de chamada para realizar ações adicionais.

| Nome do botão | Opcional | Tecla de atalho | Código de retorno |
| ----------- | -------- | ------ | ----------- |
| `button1`   | Não       | Enter   | 0           |
| `button2`   | Sim      | Esc    | 2           |
| `infobutton` | Sim      |        | 3           |

## Desabilitar botões

Os botões Button1 e Button2 podem ser desabilitados na inicialização usando um dos seguintes comandos:

`--button1disabled`

`--button2disabled`

O botão 1 pode ser completamente ocultado definindo o texto do botão para `none`

_Observe que isso também desativa o uso da tecla [Enter] para fechar uma janela de diálogo, portanto, certifique-se de ter uma forma de permitir que a janela de diálogo seja fechada._