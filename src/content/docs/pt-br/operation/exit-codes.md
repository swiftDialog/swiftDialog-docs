---
title: Códigos de saída
description: Compreendendo os códigos de saída e os valores de retorno do swiftDialog
translationSynced: 2026-11-25T11:50:31+00:00
---

Quando a janela swiftDialog é fechada, ela retorna um código de saída que pode ser usado para determinar qual ação, se alguma, foi realizada

|Código de saída|Causa|
|---------|-----|
|0|O usuário clicou no botão padrão (botão 1).|
|2|O usuário clicou no Botão 2|
|3|O usuário clicou no botão "Informações"|
|5|Saiu do sistema através do comando especificado no arquivo de comandos `quit:`|
|10|O programa foi encerrado porque o usuário usou `cmd+q` (ou a combinação de teclas cmd+quitkey).|
|20|Saiu porque `--timer` atingiu 0|
|201|Um recurso de imagem não foi encontrado|
|202|Um recurso de arquivo não foi encontrado|
|203|Um valor de cor inválido foi utilizado|

Mais detalhes nesta página: [Capturando a saída do diálogo para processamento posterior](/pt-br/operation/capturing-output)