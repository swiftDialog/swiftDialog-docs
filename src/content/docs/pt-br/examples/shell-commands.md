---
title: Comandos do Shell
description: Recurso experimental para executar comandos do shell a partir de ações de botões
translationSynced: 2026-11-25T11:50:20+00:00
---

A versão 1.1.2 introduz um recurso experimental através do comando `button1shellaction`


```
--button1shellaction <command>
                << EXPERIMENTAL >>
                Runs the specified shell command using zsh
                Command input and output is not sanitised or checked.
                If your command fails, Dialog still exits 0
```

Ele recebe um único parâmetro de texto e o passa para um shell para execução, por exemplo:

` --button1shellaction "say thank you for running dialog"`

Atualmente, não há nenhuma validação de entrada nem de saída. Se o comando especificado terminar com um erro, o Dialog ainda será encerrado `0` com o código de saída do botão 1. O status do comando será exibido na tela, incluindo o código de saída do comando, por exemplo:

```
.../Dialog.app/Contents/MacOS/Dialog --button1shellaction "bad command here"
zsh:1: command not found: bad
```

A saída do comando será direcionada diretamente para a saída padrão (stdout), permitindo que você visualize ou processe os resultados conforme necessário.

## Ações do Shell para outros botões

Os botões 2 e 3 (cancelar e informações) fecharão a janela de diálogo com os códigos 2 e 3, respectivamente. Esses códigos de saída podem ser detectados e interpretados. Se um administrador desejar executar alguma ação no terminal após o processamento de qualquer uma dessas ações, recomendo capturar o status de saída da janela de diálogo e processá-lo de acordo.

## Considerações

O comando não é executado em segundo plano, portanto, a janela do "Dialog" permanecerá visível, mas não responsiva, enquanto o comando estiver sendo executado. Após a conclusão da execução, a janela do "Dialog" será fechada. Tenha isso em mente se você pretende executar um comando que possa levar algum tempo para ser concluído.

O comando do shell também herda as permissões do processo que o invocou. Se o Dialog for executado a partir da conta de administrador (root), o comando do shell também terá privilégios de administrador.