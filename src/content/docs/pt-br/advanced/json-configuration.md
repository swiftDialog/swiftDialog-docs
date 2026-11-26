---
title: Configuração em JSON
description: Utilizando JSON para definir as opções de diálogo em configurações complexas
translationSynced: 2026-11-25T11:18:32+00:00
---

Em vez de usar inúmeras opções de linha de comando para construir diálogos complexos, você pode usar as opções `--jsonfile` ou `--jsonstring` para definir parâmetros.

O formato JSON utiliza as mesmas opções especificadas na linha de comando, com algumas exceções e considerações.

Observação:
 - As opções da linha de comando podem ser usadas em conjunto com o formato JSON, mas quaisquer opções definidas no JSON terão prioridade
 - Para suportar caracteres literais `\n` no texto da mensagem, `--jsonstring` exige que a entrada em formato JSON esteja em uma única linha contínua

Exemplo:

```json
{
  "title" : "An Important Message",
  "titlefont" : "colour=red",
  "icon" : "/Applications/Remote Desktop.app",
  "hideicon" : true,
  "infobutton" : true,
  "quitoninfo" : true,
  "image" : "/Users/Shared/Pictures/Image 1.jpg",
  "imagecaption" : "Test image 1"
}
```

## Diferenças em relação às opções de linha de comando

Opções que podem ser utilizadas várias vezes podem ser inseridas como um array.

Por exemplo, para especificar várias imagens e legendas, utilize um `image` array com `imagename, caption`

```json
{
  "image" : [
    {"imagename" : "/Users/Shared/Pictures/Image 1.jpg", "caption" : "Test image 1"},
    {"imagename" : "/Users/Shared/Pictures/Image 2.jpg", "caption" : "Test image 2"},
    {"imagename" : "/Users/Shared/Pictures/Image 3.jpg", "caption" : "Test image 3"}
  ]
}
```

As caixas de seleção podem ser definidas como "marcada" e/ou "desabilitada". O padrão é `"disabled" : false` e não precisa ser especificado

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5", "checked" : false },
	  {"label" : "Option 6", "checked" : true }
	]
}
```

Para múltiplas `textfield` opções, especifique um único campo de texto contendo os nomes dos campos, formatados como um array

```json
{
  "textfield" : ["Text Entry 1", "Text Entry 2", "Text Entry 3"]
}
```

### Strings e valores booleanos

A maioria das opções será transmitida como valores de string, exigindo o uso de aspas para os valores especificados. No entanto, alguns valores podem ser especificados como valores booleanos (`true` ou `false`, sem aspas). As opções que aceitam um valor booleano são:

```json
{
  "button2" : false
  "infobutton" : false
  "hideicon" : false
  "moveable" : false
  "ontop" : false
  "small" : false
  "big" : false
  "fullscreen" : false
  "json" : false
  "ignorednd" : false
  "hidetimerbar" : false
  "quitoninfo" : false
}
```

### Opções não disponíveis no formato JSON

Existem diversas opções que não podem ser utilizadas diretamente a partir do formato JSON, pois não fazem sentido em um ambiente de produção. São elas:

* `--jh` - Utilizado como uma substituição direta para aceitar as opções de linha de comando do JamfHelper.
* `--listfonts` - Utilizado durante a fase de prototipagem para exibir uma lista de fontes disponíveis
* `--help` - Exibe mensagens de ajuda e encerra o programa. Utilizado durante a fase de prototipagem
* `--demo` - Exibe uma janela de diálogo utilizando apenas as configurações padrão. Utilizado durante a fase de prototipagem
* `--version` - Exibe informações sobre a versão do diálogo e encerra o programa.
* `--showlicense` - Imprime informações da licença e encerra o programa
* `--coffee` - imprime informações sobre o café e encerra a execução

## Exemplo: como gerar arquivos JSON em Python e passá-los como um arquivo ou uma string

```python
#!/usr/bin/python3

import json
import os

# set to false to generate an intermediate json file
# set to true to pass generated json in as a string
stringinput = True

dialog_app = "/Library/Application Support/Dialog/Dialog.app/Contents/MacOS/Dialog"

contentDict = {"title" : "An Important Message",
            "titlefont" : "name=Chalkboard,colour=#3FD0a2,size=40",
            "message" : "This is a **very important** messsage and you _should_ read it carefully\n\nThis is on a new line",
            "icon" : "/Applications/Safari.app",
            "hideicon" : false,
            "infobutton" : true,
            "quitoninfo" : true
            }

jsonString = json.dumps(contentDict)

if stringinput:
    print("Using string Input")
    os.system("'{}' --jsonstring '{}'".format(dialog_app, jsonString))
else:
    print("Using file Input")

    # create a temporary file
    jsonTMPFile = "/tmp/dialog.json"
    f = open(jsonTMPFile, "w")
    f.write(jsonString)
    f.close()

    os.system("'{}' --jsonfile {}".format(dialog_app, jsonTMPFile))

    # clean up
    os.remove(jsonTMPFile)
```