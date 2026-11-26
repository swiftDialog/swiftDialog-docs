---
title: Listas de itens
description: Criar listas ordenadas dinâmicas com indicadores de status e ícones
translationSynced: 2026-11-25T11:25:21+00:00
---

As listas de itens permitem exibir um número razoável de itens em uma lista organizada. Se a lista for mais longa do que a área visível, ela se tornará uma lista com barra de rolagem.

Listas podem ser exibidas em diálogos, utilizando qualquer uma das opções de personalização existentes, com exceção de imagens, que ocupam toda a área de exibição da mensagem.

<hr />
Existem três maneiras de criar uma lista de itens:

### 1) Linha de comando

Especifique um ou mais `--listitem <text>` itens como um argumento de linha de comando. A lista será construída na ordem especificada.

Os ícones dos itens da lista podem ser definidos usando argumentos de linha de comando `--listitem "<text>,icon=<image>"`, no entanto, se você precisar de opções mais avançadas, deve usar o formato JSON.

### 2) JSON

Ao utilizar JSON como fonte de configuração, especifique os itens como um array de uma dimensão.

#### Básico

O método básico é uma forma simples de iniciar uma lista de itens que não possuem um status definido.

```json
{
  "listitem" : ["Item 1", "Item 2", "Item 3"]
}
```

#### Avançado

O recurso "Avançado" permite que você inicialize uma lista e, opcionalmente, defina um ícone, um status e um texto de status

```json
{
  "listitem" : [
    {"title" : "Item One", "icon" : "/path/to/image", "status" : "pending", "statustext" : "Pending"},
    {"title" : "Item Two", "icon" : "/path/to/SomeApp.app", "status" : "wait", "statustext" : "Waiting"},
    {"title" : "Item Three", "icon" : "https://some.url/image", "status" : "success", "statustext" : "Winning"}
  ]
}
```

##### Opções de status

O status dos itens da lista pode ser um dos seguintes: `wait`, `success`, `fail`, `error`, `pending` ou `progress`, e um ícone apropriado será exibido na área de status.

Ao usar `progress` como um status, um indicador de progresso circular será exibido como o ícone de status. Adicionar um número, por exemplo, `progress: 20`, fará com que o indicador se mova para a posição correta, representando a porcentagem a ser preenchida. O indicador de progresso aceita qualquer valor entre `0` e `100`

<img width="599" alt="image" src="https://user-images.githubusercontent.com/3598965/182604151-3eabe9b5-3f77-4949-9b88-c522676e3314.png">

#### Configuração JSON para argumentos

A partir da versão 3.1.1, os itens da lista também podem ser especificados como objetos JSON através de `--listitem` (em vez de usar o objeto JSON de configuração completo). Isso oferece um controle mais direto e é especialmente útil para configurações complexas que envolvem objetos de ícones aninhados.

**Sintaxe:**
```bash
dialog --listitem '{"title":"Download","status":"wait","statustext":"Working…"}'
```

**Características:**
- `title` - O texto da etiqueta do item da lista
- `status` - Indicador de status: `wait`, `success`, `fail`, `error`, `pending`, `progress` ou `progress:<value>` (0-100).
- `statustext` - Texto de status exibido ao lado do indicador de status
- `icon` - Caminho para o ícone, URL ou **objeto de ícone JSON aninhado**

**Objetos de Ícones Aninhados:**

O campo `icon` aceita objetos JSON para a configuração avançada de ícones:

```bash
# Basic list item with SF Symbol
dialog --listitem '{"title":"Processing","status":"wait","icon":{"sf":"gear","colour":"blue"}}'

# List item with animated icon
dialog --listitem '{"title":"Downloading","status":"progress:50","icon":{"sf":"arrow.triangle.turn","colour":"green","animation":"variable"}}'

# List item with gradient icon
dialog --listitem '{"title":"Installing","status":"wait","icon":{"sf":"arrow.down.circle","colour":"pink","colour2":"purple"}}'

# List item with application icon
dialog --listitem '{"title":"App Installation","status":"success","icon":{"path":"/Applications/MyApp.app"}}'
```

**Vários itens:**

```bash
dialog --listitem '{"title":"Step 1","status":"success","statustext":"Complete"}' \
       --listitem '{"title":"Step 2","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}' \
       --listitem '{"title":"Step 3","status":"pending"}'
```

**Observação:** Ao utilizar o formato JSON por argumento, cada `--listitem` é independente. O formato JSON de configuração completa ainda é suportado para inicialização em lote.


### 3) Como um comando enviado para o arquivo de comandos

Envie os itens como valores separados por vírgula

`echo "list: Item 1, Item 2, Item 3" >> /var/tmp/dialog.log`


## Atualização de uma lista existente

As entradas em uma lista já exibida podem ser atualizadas com um status, enviando comandos para o arquivo de comandos.


#### Básico

A sintaxe básica necessária é a seguinte:

`echo listitem: <list item title>: <status text> >> /var/tmp/dialog.log`

 - `<list item title>` deve corresponder ao nome/título do item da lista e diferencia maiúsculas de minúsculas
 - `<status text>` pode ser qualquer sequência de texto em formato Unicode
   - Se uma das palavras-chave de status suportadas for enviada, um indicador correspondente será exibido em vez de texto

#### Avançado

A sintaxe avançada permite que você atualize o texto de status e o indicador de status, além de referenciar o item da lista por índice. As palavras-chave são separadas em uma lista delimitada por vírgulas (isso significa que os campos `title` e `statustext` não podem conter texto que inclua vírgulas):

`listitem: [title: <title>|index: <index>], status: <status>, statustext: <text>`

`<index>` Começa em 0

e.g.

`listitem: index: 0, status: complete, statustext: Item 1 on the list has completed`

Novos itens podem ser adicionados ao final de uma lista existente com o comando `add:`, e itens podem ser removidos com o comando `delete:`. Ao adicionar uma linha, os campos "status" e "statustext" são opcionais.

Exemplos:

`echo "listitem: add, title: <title>, statustext: <text>, status: <status>" >> /var/tmp/dialog.log`

Excluir por índice: `echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log`

Excluir por referência ao título `echo "listitem: title: Some Row Title, delete:" >> /var/tmp/dialog.log`

É possível adicionar ou remover itens de uma lista, mesmo quando a lista não está visível no momento.

## Mostrar ou ocultar uma lista

A lista pode ser configurada para ser exibida ou ocultada, sem que isso afete o conteúdo da lista.

exibir `echo "list: show`

esconder `echo "list: hide`

## Removendo uma lista

Uma lista existente pode ser removida enviando o comando `list: clear` para o arquivo de comandos.

Limpar uma lista remove todas as entradas e status associados a ela.

## Exemplos


`echo "list: Test item 1, Test item 2, Test item 3" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151488006-ba027af7-0736-47b2-abdd-ba847491f086.png)

Em seguida, ao enviar os seguintes comandos, o status da lista será atualizado

`echo "listitem: Test item 1: Complete ✅" >> /var/tmp/dialog.log`

`echo "listitem: Test item 2: There was an error processing this item ❌" >> /var/tmp/dialog.log`

`echo "listitem: Test item 3: wait" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151486051-967e760e-f164-467f-8bd6-dcccba3c7504.png)

#### Formato JSON avançado

![image](https://user-images.githubusercontent.com/3598965/163742836-22fd32e8-8010-467f-a518-b4d348619698.png)