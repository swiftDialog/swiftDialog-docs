---
title: Campos de texto
description: Criar campos de entrada de texto com diversas propriedades e validações
translationSynced: 2026-11-25T11:27:17+00:00
---

A opção `--textfield` permite que você especifique uma área onde o usuário pode inserir algum texto antes de fechar a janela de diálogo

Ela recebe um parâmetro como texto e utiliza esse parâmetro como o rótulo do campo de texto, tanto na interface de diálogo quanto na saída dos relatórios

Os resultados são enviados para a saída padrão (stdout) quando o programa "dialog" é encerrado, no seguinte formato:

`<textfield text> : <user input>`

ou, se estiver usando a opção `--json` para habilitar a saída em formato JSON:

```json
{
"<textfield text>" : "<user input>"
}
```

## Exemplos

Se você estiver utilizando o seguinte diálogo:

`dialog --textfield "Textfield 1"`

Exibirá a seguinte caixa de diálogo:

![image](https://user-images.githubusercontent.com/3598965/235908715-5f24a167-5ad1-4f81-aa7e-30faf5590b1c.png)

O usuário insere uma resposta:

![image](https://user-images.githubusercontent.com/3598965/235908865-40b37eac-874b-4ceb-a4e7-e8701ebdf790.png)

que resultará no seguinte resultado:

`Textfield 1 : This is what the user entered`

ou ao utilizar `--json`

```json
{
"Textfield 1" : "This is what the user entered"
}
```

## Campos de texto adicionais

É possível especificar múltiplos campos de texto adicionando opções extras ao chamar a função `dialog`. `--textfield`

e.g. `dialog --textfield "Textfield 1" --textfield "Textfield 2"`

![image](https://user-images.githubusercontent.com/3598965/235909015-2c4f187b-a86d-4281-84ff-09afa6b87857.png)

Você pode especificar quantos campos de texto forem necessários. Cada campo de texto será exibido como um campo separado na saída.

Você pode precisar ajustar o tamanho da janela de diálogo `--height` se estiver adicionando vários campos de texto, para que eles caibam

Exemplo:

`dialog --textfield "First Name" --textfield "Surname" --textfield "Age" --textfield "Favourite Colour"`

Isso resulta no seguinte resultado:

```
First Name : Joe
Surname : Bloggs
Age : 32
Favourite Colour : Red
```

`--json`
```json
{
"First Name" : "Joe",
"Surname" : "Bloggs",
"Age" : "32",
"Favourite Colour" : "Red"
}
```

## Modificadores de campo de texto

Os modificadores são adicionados ao rótulo do campo de texto como valores separados por vírgula:

```sh
--textfield "<label>,<modifier>,<modifier>=<value>"
```

| Modificador | Descrição |
|---|---|
| `name=<text>` | Utilize este valor como a chave de saída, em vez do rótulo |
| `required` | O campo deve ser preenchido antes que a janela de diálogo seja fechada |
| `secure` | Ocultar a digitação enquanto o usuário insere os caracteres (campo de senha). |
| `passwordfill` | Habilitar o preenchimento automático de senhas do macOS em um campo `secure` |
| `prompt="<text>"` | Texto de exemplo exibido dentro do campo (não será incluído na saída). |
| `value="<text>"` | Preencher o campo com um valor padrão (que pode ser editado). |
| `regex=<pattern>` | Exigir que o conteúdo do campo corresponda à expressão regular |
| `regexerror=<text>` | Mensagem de erro personalizada exibida quando a expressão regular não é atendida |
| `editor` | Editor de texto com várias linhas, em vez de um campo de uma única linha |
| `isdate` | Substitua o campo de texto por um seletor de data. A saída será formatada como uma string de data curta. |
| `fileselect` | Adicione um botão "Selecionar" que abre uma janela para escolher um arquivo |
| `filetype=<types>` | Restrinja a seleção de arquivos aos tipos especificados (separados por espaço). Utilize as extensões dos arquivos (por exemplo, `png jpg`) ou as palavras-chave de tipo `folder`, `image`, `movie`, `video`, `audio`. |
| `path=<path>` | Defina o diretório inicial para o seletor de arquivos |
| `confirm` | Adicione um campo de confirmação cujo conteúdo deve corresponder ao campo principal |

### Nome

`name=<text>` Substitui o rótulo pela chave nos resultados. Útil quando você deseja um rótulo amigável, mas um nome de chave mais limpo nos resultados.

### Seguro

`secure` Oculta a entrada enquanto ela é digitada e exibe um ícone de cadeado. O conteúdo ainda é retornado como texto simples na saída padrão.

```sh
--textfield "Password,secure"
```

![image](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

### Preenchimento automático de senhas

`passwordfill` Ativa a função de preenchimento automático de senhas no macOS. Deve ser utilizada em conjunto com `secure`.

```sh
--textfield "Password,secure,passwordfill"
```

### Obrigatório

`required` Impede que a janela swiftDialog seja fechada até que o campo tenha um valor. Os campos obrigatórios são marcados com um `*` e são destacados quando o usuário tenta fechar a janela sem preenchê-los.

```sh
--textfield "Full Name,required"
```

![image](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)

### Prompt

`prompt="<text>"` Exibe um texto de exemplo dentro do campo. Esse texto desaparece assim que o usuário começa a digitar e não é incluído na saída. Não é suportado em campos `secure`.

```sh
--textfield "Name,prompt="Enter your full name""
```

![image](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

### Valor

`value="<text>"` Preenche o campo com um valor padrão que o usuário pode editar.

```sh
--textfield "Default Value Test",value="Some default value"
```

![image](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

### Expressões regulares e erros de expressão regular

`regex=<pattern>` exige que o conteúdo do campo corresponda à expressão regular antes que a janela "swiftDialog" seja fechada. `regexerror=<text>` define a mensagem que é exibida quando o padrão não é encontrado.

A menos que o padrão permita explicitamente, um campo `regex` não pode estar vazio.

```sh
--textfield "Product Code",prompt="Enter 5 digit code",regex="\d{5}",regexerror="Must be a five digit number"
```

![image](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

Utilize `--textfieldlivevalidation` para exibir uma sobreposição de cor verde/vermelha no campo enquanto o usuário digita, fornecendo feedback imediato sobre se a expressão regular está sendo satisfeita.

### Editor

`editor` apresenta uma área de texto maior, com várias linhas, em vez de um campo de uma única linha.

```sh
--textfield "Notes,editor"
```

![image](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

### Seletor de datas

Use o modificador `date` ou `time` para substituir o campo de texto por um seletor de data e hora do macOS. O valor selecionado é retornado como uma string formatada.

```sh
--textfield "Start Date,date"
--textfield "Start Time,time"
--textfield "Start Date and Time,date,time"
```

Observação: O modificador `isdate` foi descontinuado em favor de `date` e `time`.

#### Limites de data

Utilize `mindate=` e `maxdate=` para restringir o intervalo de datas selecionáveis:

```sh
--textfield "Pick a day,date,mindate=20260901,maxdate=20260930"
--textfield "No earlier than today,date,mindate=20260928"
--textfield "Before end of year,date,maxdate=20261231"
```

**Formato:** As datas devem estar no formato `YYYYMMDD` (independente da região). Separadores são aceitos e removidos (por exemplo, `2026-09-30` → `20260930`). Datas inválidas são ignoradas e a restrição não é aplicada.

#### Formato de data

Use `format=` para especificar o formato de retorno, utilizando a sintaxe strftime:

```sh
--textfield "Select date,date,format=+%Y-%m-%d"
--textfield "Get epoch,date,value=20260901,format=+%s"
```

Formatos de string comuns:
- `+%Y-%m-%d` - Formato ISO 8601 (por exemplo, `2026-09-29`).
- `+%s` - Timestamp Unix (segundos desde a época).
- `+%x` - Representação de data específica da localização
- `+%D` - Formato americano (por exemplo, `09/29/26`).

#### Inicializando o seletor de datas

Use `value=` para definir a data inicial. O seletor aceita vários formatos:

```sh
--textfield "Start date,date,value=2026-09-30"
--textfield "Start date,date,value=September 30, 2026"
--textfield "Start date,date,value=1759132800"
```

Formatos suportados: ISO 8601, formatos específicos da localidade, 12/24 horas, carimbos de data e hora do sistema (epoch), e linguagem natural.

### Selecionar arquivo

`fileselect` Adiciona um botão "**Selecionar**" que abre um seletor de arquivos padrão. O caminho selecionado é inserido no campo e retornado na saída.

```sh
--textfield "Config File,fileselect"
```

Use `filetype` para restringir as opções de seleção. Os valores devem ser separados por espaços e podem ser extensões de arquivo ou palavras-chave que representam tipos:

| Valor | Seleciona |
|---|---|
| `folder` | Apenas diretórios |
| `image` | Qualquer tipo de imagem |
| `movie` / `video` | Qualquer tipo de vídeo |
| `audio` | Qualquer tipo de áudio |
| `<extension>` | Arquivos que correspondam a essa extensão (por exemplo, `png`, `pdf`). |

```sh
--textfield "Select an image,fileselect,filetype=png jpg"
--textfield "Select a folder,fileselect,filetype=folder"
```

Use `path=<path>` para definir o diretório que o seletor de arquivos abrirá:

```sh
--textfield "Log File,fileselect,path=/var/log"
```

![image](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

### Confirmar

`confirm` adiciona um segundo campo abaixo do campo principal. Ambos os campos devem conter o mesmo valor antes que o swiftDialog aceite a entrada. Útil para confirmação de senhas.

```sh
--textfield "Password,secure,required,confirm"
```

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### Combinando Modificadores

Os modificadores podem ser combinados livremente (quando compatíveis):

```sh
--textfield "<label>,secure,required,prompt="<prompt_text>""
--textfield "<label>,required,regex="\d{5}",regexerror="Five digits required",prompt="00000""
--textfield "<label>,fileselect,filetype="jpeg jpg png",path=/Users/Shared"
```

### Formato JSON

Os campos de texto podem ser especificados em formato JSON de duas maneiras:

#### Configuração JSON completa

Ao utilizar um arquivo de configuração JSON ou `--jsonstring`/`--jsonfile`, especifique os campos de texto como um array:

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "date" : true, "mindate" : "20260901", "maxdate" : "20260930", "format" : "+%Y-%m-%d"},
    {"title" : "<label>", "time" : true, "value" : "14:30"},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

#### Configuração JSON para análise de argumentos

A partir da versão 3.1.1, os campos de texto também podem ser especificados como objetos JSON por meio de `--textfield` (em vez de usar modificadores separados por vírgula). Isso oferece um controle mais direto e é especialmente útil para configurações complexas.

**Sintaxe:**
```bash
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'
```

**Características:**
- `title` - O texto do rótulo do campo
- `name` - Nome alternativo para a chave de saída
- `required` - O campo deve ser preenchido (verdadeiro/falso).
- `secure` - Ocultar o texto digitado (campo de senha) à medida que é inserido.
- `passwordfill` - Ativar o preenchimento automático de senhas do macOS (requer `secure`).
- `prompt` - Texto de exemplo exibido dentro do campo
- `value` - Preencher o campo com um valor padrão
- `regex` - Exigir que o conteúdo do campo corresponda à expressão regular
- `regexerror` - Mensagem de erro personalizada exibida quando a expressão regular não é satisfeita
- `editor` - Editor de texto de várias linhas, em vez de um campo de uma única linha
- `date` - Substituir o campo por um seletor de datas (verdadeiro).
- `time` - Substituir o campo por um seletor de horário (verdadeiro).
- `mindate` - Data mínima selecionável (formato AAAA MM DD).
- `maxdate` - Data máxima selecionável (formato AAAA MM DD).
- `format` - Formato de retorno utilizando a sintaxe strftime (por exemplo, `+%Y-%m-%d`, `+%s`).
- `fileselect` - Adicione um botão "Selecionar" que abre uma janela para escolher um arquivo
- `filetype` - Restringir o seletor de arquivos a tipos específicos (extensões ou palavras-chave separadas por espaços).
- `path` - Diretório inicial para a janela de seleção de arquivos
- `confirm` - Adicionar um campo de confirmação que deve corresponder ao campo principal

**Exemplos:**

```bash
# Basic required field with prompt
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'

# Secure field with password fill
dialog --textfield '{"title":"Password","secure":true,"passwordfill":true,"prompt":"Enter password"}'

# Date picker with bounds
dialog --textfield '{"title":"Select Date","date":true,"mindate":"20260901","maxdate":"20260930","format":"+%Y-%m-%d"}'

# Time picker with default value
dialog --textfield '{"title":"Select Time","time":true,"value":"14:30"}'

# File picker with restrictions
dialog --textfield '{"title":"Select Config","fileselect":true,"filetype":"json plist","path":"/Library/Preferences"}'

# Multi-line editor
dialog --textfield '{"title":"Notes","editor":true}'

# Regex validation
dialog --textfield '{"title":"Product Code","prompt":"Enter 5 digit code","regex":"\\d{5}","regexerror":"Must be a five digit number"}'

# Confirmation field
dialog --textfield '{"title":"Password","secure":true,"required":true,"confirm":true}'
```

**Campos de seleção de data:**
- Use `"date": true` ou `"time": true` (ou ambos) para criar um seletor
- `"mindate"` e `"maxdate"` aceitam datas no formato `YYYYMMDD` (os separadores são removidos).
- `"format"` Define o formato de retorno usando a sintaxe strftime
- `"value"` Define a data/hora inicial em múltiplos formatos (ISO, local, época, linguagem natural).

**Todos os modificadores são suportados:** Todos os modificadores disponíveis no formato CSV também estão disponíveis como chaves JSON.

**Campos de texto múltiplos:**

```bash
dialog --textfield '{"title":"First Name","required":true}' \
       --textfield '{"title":"Last Name","required":true}' \
       --textfield '{"title":"Email","regex":".+@.+\\..+","prompt":"user@example.com"}'
```

**Observação:** Ao utilizar o formato JSON por argumento, cada `--textfield` é independente. O formato JSON de configuração completa ainda é suportado para inicialização em lote.

## Comportamento do teclado

Pressionar a tecla **Enter** em qualquer campo de texto de uma única linha aciona a ação do Botão 1, o que é equivalente a clicar no botão padrão. Isso não se aplica a `editor` campos.