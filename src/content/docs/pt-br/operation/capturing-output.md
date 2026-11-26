---
title: Captura da saída do diálogo
description: Métodos para capturar a entrada do usuário e processar os resultados da interação
translationSynced: 2026-11-25T11:50:46+00:00
---

Existem várias maneiras de obter informações do sistema Dialog ou de saber qual ação um usuário realizou, ou qualquer dado que foi inserido.

## Códigos de retorno

O diálogo mais básico sempre terá pelo menos um botão que, quando clicado, fechará a janela com um código de retorno de `0`.

Os botões opcionais, que são ativados por meio de `--button2`, `--infobutton` (ou derivados), retornarão um código específico (`2` ou `3`) dependendo de qual botão foi clicado.

Os seguintes códigos de retorno são enviados após cada ação. Eles podem ser ignorados ou utilizados em um script de chamada para realizar ações adicionais

| Ação      | Opcional | Tecla de atalho | Código de retorno |
| ----------- | -------- | ------ | ----------- |
| `button1`   | Não       | Entrar  | 0           |
| `button2`   | Sim      | Esc    | 2           |
| `infobutton` | Sim      |        | 3           |
| \<timer\>   | Sim      |        | 4           |
| arquivo de comando `quit:` | Sim |    | 5           |
| `--quitkey` | Sim      | Cmd+Q  | 10          |
| Falha na autenticação | Sim  |        | 30          |
| Recurso de imagem não encontrado | |    | 201         |
| Arquivo não encontrado |       |        | 202         |


Para processar o código de retorno no seu script, basta capturar o resultado de `$?` no Bash ou através da linguagem de script que você escolheu.

Exemplo: processamento de códigos de retorno em `zsh`:

```zsh
#!/bin/zsh
dialog ...<options_here>
case $? in
  0)
  echo "Pressed OK"
  # Button 1 processing here
  ;;
  2)
  echo "Pressed Cancel Button (button 2)"
  # Button 2 processing here
  ;;
  3)
  echo "Pressed Info Button (button 3)"
  # Button 3 processing here
  ;;
  4)
  echo "Timer Expired"
  # Timer ran out code here
  ;;
  5)
  echo "quit: command used"
  # post quit: command code here
  ;;
  10)
  echo "User quit with cmd+q"
  # User quit code here
  ;;
  30)
  echo "Key Authorisation Failed"
  # Key auth failure code here
  ;;
  201)
  echo "Image resource not found"
  ;;
  202)
  echo "Image for icon not found"
  ;;
  *)
  echo "Something else happened"
  ;;
esac
```


## Saída padrão

Além dos códigos de retorno, a saída será enviada para `sdtout` se um ou mais `--textfield` ou `--selectvalues` forem apresentados. A saída padrão não é formatada, a menos que seja necessário separar o rótulo da saída usando um caractere `:`.

Considerando o seguinte diálogo e a entrada do usuário:

`dialog --textfield "text 1" --textfield "text 2" --selecttitle "make selection" --selectvalues "one,two,three,four"`

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/127793083-b07b4b46-8da6-46ee-a4ce-fcca84949a31.png">

O resultado seria o seguinte:

```
 SelectedOption : three
 SelectedIndex : 2
text 1 : one
text 2 : two
```

`SelectedOption` é o texto da opção do menu suspenso que foi selecionada. `SelectedIndex` é o índice da opção selecionada (os índices começam em 0, então o índice 2 significa que a terceira opção listada foi selecionada).

Os campos de texto são apresentados usando o rótulo fornecido no diálogo, que será utilizado como rótulo na saída. Portanto, no exemplo acima:

`text 1` exibe o texto que o usuário inseriu no campo de texto rotulado como "texto 1", e o mesmo acontece com `text 2`

Para separar essas informações, você pode usar `awk` para processar cada linha de saída que for de seu interesse, por exemplo.
```bash
/usr/local/bin/dialog <...> | grep "SelectedOption" | awk -F " : " '{print $NF}'
```

Para um processamento mais avançado, você pode passar o parâmetro `--json`, que formatará a saída como JSON para ser processada por um analisador JSON (por exemplo, em Python).

A saída JSON para o exemplo acima teria a seguinte aparência:
```json
{
"SelectedOption" : "three",
"SelectedIndex" : 2,
"text 1" : "one",
"text 2" : "two"
}
```

## Exemplos adicionais

Capturando a saída e o código de retorno usando Python:
```python
import subprocess

result = subprocess.Popen("/usr/local/bin/dialog <...>")
text = result.communicate()[0]   # contents of stdout
return_code = result.returncode  # return code
```