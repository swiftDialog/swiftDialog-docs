---
title: Selecione listas e botões de opção
description: Criar listas suspensas e grupos de botões de opção para a seleção pelo usuário
translationSynced: 2026-11-25T11:26:08+00:00
---

O componente "Dialog" tem a capacidade de receber uma lista de valores e exibi-los em um menu suspenso, com a opção de selecionar um valor padrão.

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)

## Como usar


### Título da lista de seleção

`--selecttitle <text>(,radio|required|searchable|multiselect|name="<text>")`

A etiqueta pode ser definida para a lista através da opção de linha de comando `--selecttitle`. Por exemplo: `--selecttitle "Select an Option"`

![image](https://user-images.githubusercontent.com/3598965/122635336-9ee98a80-d126-11eb-8839-f859eb19688e.png)


O nome será exibido na saída do swiftDialog no STDOUT, juntamente com o valor do item selecionado. Para uma lista de seleção única, o formato de saída padrão será:
```
    "SelectedOption" : "<value>"
    "SelectedIndex" : <index>
    "<name>" : "<value>"
    "<name>" index : "<index>"
```

Vários argumentos `--selecttitle` podem ser especificados. Argumentos relacionados `--selectvalues` e `--selectdefault` podem ser especificados e são associados a uma lista de opções na ordem em que são apresentados

Se forem utilizadas listas de seleção múltipla, os atributos "SelectedOption" e "SelectedIndex" não serão representados.

A exibição de itens selecionados ocorre apenas se o código de saída do componente swiftDialog for 0

### Selecionar valores da lista

`--selectvalues <text><csv>`

Os valores são especificados em formato CSV e são passados por meio da opção de linha de comando `--selectvalues`, por exemplo: `--selectvalues "Option 1,Option 2,Option 3,Option 4, Option 5"`

![image](https://user-images.githubusercontent.com/3598965/122635303-6053d000-d126-11eb-94f1-6950f0e3d43e.png)

### Selecionar lista padrão

`--selectdefault <text>`

A opção padrão pode ser definida usando a opção de linha de comando `--selectdefault`, por exemplo: `--selectdefault "Option 4"`

![image](https://user-images.githubusercontent.com/3598965/122635358-c2143a00-d126-11eb-80b2-475a62b6ed9a.png)

Se um valor padrão não for especificado e o usuário não selecionar nenhum item da lista, nenhum resultado será exibido.


Exemplo de saída:
```
    SelectedOption: Option 1
    SelectedIndex: 0
```

A exibição de itens selecionados só ocorre se o código de saída do programa Dialog for 0

### Configuração JSON para argumentos individuais

Listas selecionáveis também podem ser definidas usando objetos JSON através de `--selectitem` (ou `--selecttitle`, com um valor JSON). Isso oferece um controle mais direto sobre as propriedades de cada item.

**Sintaxe:**
```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU","required":true}'
```

**Características:**
- `title` - O rótulo para a lista de opções
- `values` - Array de valores de opção
- `default` - O valor selecionado por padrão
- `required` - Indica se o campo é obrigatório (ignorado para botões de opção).
- `style` - Estilo de exibição: `list`, `radio`, `searchable` ou `multiselect`
- `name` - Nome alternativo para a chave de saída

**Exemplos:**

```bash
# Basic JSON item
dialog --selectitem '{"title":"Size","values":["S","M","L"],"default":"M"}'

# Searchable with required field
dialog --selectitem '{"title":"Region","values":["AU","US","UK"],"required":true,"style":"searchable"}'

# Radio button group
dialog --selectitem '{"title":"Priority","values":["Low","Medium","High"],"style":"radio"}'

# Mix JSON with positional arguments
dialog --selectitem '{"title":"Color","values":["red","green","blue"]}' --selectdefault "red"
```

Os elementos JSON são independentes dos argumentos posicionais `--selectvalues/--selecttitle/--selectdefault`. Ao utilizar JSON, os valores são filtrados da lista de rótulos posicionais para evitar duplicações.

## Esquema JSON

Listas selecionáveis podem ser especificadas usando JSON para um controle mais direto.

### Arquivo JSON de configuração completa.

```json
{
  "selectitems" : [
    {
      "title" : "Select Item",
      "name" : "altname",
      "values" : ["red","green","blue"],
      "default" : "red",
      "required" : false,
      "style" : "default | radio | searchable | multiselect"
    }
  ]
}
```

### JSON para argumentos

Itens individuais também podem ser definidos usando `--selectitem` ou `--selecttitle`, juntamente com um objeto JSON:

```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU"}'
dialog --selecttitle '{"title":"Size","values":["S","M","L"],"required":true}'
```

Observação: `--selecttitle` trata os objetos JSON da mesma forma que `--selectitem`.

### Exemplos:

```json
"selectitems" : [
  {"title" : "Select 1", "values" : ["one","two","three"]},
  {"title" : "Select 2", "values" : ["red","green","blue"], "default" : "red"}
]
```

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)


```json
"selectitems" : [
  {"title" : "Pick One", "values" : ["One","Two","Three"], "style" : "radio"}
]
```

![image](https://github.com/bartreardon/swiftDialog/assets/3598965/1d2659c6-9048-440b-9246-2756ec097a24)


## Modificadores

### Nome

Faz com que a saída seja registrada com o texto especificado `name`, em vez de usar o título

```bash
% dialog --selecttitle "Alternate Name",name=alt --selectvalues "Option One, Option Two, Option Three"

"SelectedOption" : "Option One"
"SelectedIndex" : 0
"alt" : "Option One"
"alt" index : "0"
```

### Pesquisável

O `searchable` modificador adiciona um campo de pesquisa à lista. Ao digitar no campo de texto, a lista será filtrada.

<img width="550" alt="image" src="/images/select_1.png" />

<img width="550" alt="image" src="/images/select_2.png" />

### Rádio

O modificador `radio` alterará a lista de seleção para exibir um grupo com botões de opção. Ao usar `radio` sem especificar um item padrão, o primeiro item da lista se tornará o item selecionado por padrão. Portanto, o uso de botões de opção *sempre* força a seleção de um dos valores, e modificadores como `required` são ignorados.

`--selecttitle "Radio buttons",radio --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235897669-c08fdd79-aa14-4fec-8c6d-a930861a122f.png)

### Obrigatório

O `required` modificador fará com que essa lista específica se torne um campo obrigatório que deve ter um valor antes que a janela de diálogo (swiftDialog) seja fechada

`--selecttitle "Required item",required --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235898090-5f7e9fac-2913-413f-ae85-c850ae86ee6b.png)

![image](https://user-images.githubusercontent.com/3598965/235898473-6fb9749f-3406-4f8d-b112-b214e95dccd4.png)

### Multiseleção

O `multiselect` modificador permite a seleção de mais de uma opção da lista. Os itens selecionados aparecem como etiquetas que podem ser removidas, e o resultado é uma lista de valores escolhidos, separados por vírgulas.

`--selecttitle "Choose options",multiselect --selectvalues "Option One, Option Two, Option Three, Option Four"`

Ao utilizar `multiselect`, os valores selecionados são retornados como uma única string separada por vírgulas:

```
"Choose options" : "Option One, Option Three"
```

Ou, em formato JSON:
```json
{
  "Choose options" : "Option One, Option Three"
}
```

## Estilo Global

`--selectstyle [list | radio | searchable | multiselect]`

Define o estilo de exibição para **todos** os itens da lista de seleção no diálogo. É o equivalente global de definir o modificador de estilo em cada `--selecttitle` individualmente. Os modificadores de estilo por lista em `--selecttitle` têm precedência sobre esta configuração global.

| Valor | Descrição |
|---|---|
| `list` | Menu suspenso padrão (padrão). |
| `radio` | Grupo de botões de opção |
| `searchable` | Lista suspensa com um campo de texto para filtro |
| `multiselect` | Campo de pesquisa que permite múltiplas seleções |

## Adicionando seções à lista

Adicione três ou mais hífens `---` à sua lista sempre que precisar de um separador

`--selectvalues "Option One, Option Two, ---, Option Three, Option Four, ---, Option Five"`

![image](https://user-images.githubusercontent.com/3598965/235900591-96ace495-5205-459c-9b2e-4bcd3ede00ee.png)

**OBSERVAÇÃO: cada `---` será contado no índice, mesmo que o separador em si não seja selecionável. No exemplo acima, haverá 7 itens no array da lista, mesmo que apenas 5 sejam exibidos no menu. Por favor, leve isso em consideração ao criar suas listas de opções.**

## Saída

Ao ser finalizado, o programa Dialog exibirá o valor selecionado pelo usuário (ou o valor padrão, caso tenha sido definido e o usuário não tenha selecionado nenhuma opção) em `stdout`. Essa saída pode ser analisada por um script e utilizada de acordo.

Existem duas linhas na saída.
* A primeira linha é o texto do item da lista e será exibida como `SelectedOption: <text of item>`
* A segunda linha representa o índice do item selecionado e estará no formato `SelectedIndex: <index of item>`

O índice começa em `0`, então, se o terceiro item da lista for selecionado, o resultado de `SelectedIndex` será `SelectedIndex: 2`

## Exemplo de saída de leitura

Considerando a seguinte saída:
```
 SelectedOption: Option 4
 SelectedIndex: 3
```

Utilize os comandos "grep" e "awk" para extrair o valor que você deseja processar

` | grep "SelectedOption" | awk -F ": " '{print $NF}'`

ou

` | grep "SelectedIndex" | awk -F ": " '{print $NF}'`

## Adicionando listas de seleção múltipla

Para adicionar múltiplas listas de seleção, basta especificar múltiplas instâncias de `--selectvalues` `--selecttitle` e `--selectdefault`. O título e o valor padrão serão atribuídos na ordem em que forem fornecidos.


### Seleção múltipla de resultados

Quando se utilizam listas de seleção múltipla, a saída é modificada para permitir a análise das diversas listas nomeadas. Por exemplo, se utilizarmos o JSON acima e selecionarmos "dois" e "vermelho", o resultado será o seguinte:

```
Select 1 : two
Select 1 index : 1
Select 2 : red
Select 2 index : 0
```

Se a saída for enviada no formato JSON, o resultado seria o seguinte:

```json
{
  "Select 1" : {
    "selectedIndex" : 1,
    "selectedValue" : "two"
  },
  "Select 2" : {
    "selectedIndex" : 0,
    "selectedValue" : "red"
  }
}
```