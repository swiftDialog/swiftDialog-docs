---
title: O que há de novo
description: Recursos e atualizações recentes no swiftDialog
translationSynced: 2026-11-25T11:55:02+00:00
---

## swiftDialog 2.5.6

## Correções:

 - Corrigido um problema em que, ao especificar um ícone a partir de um arquivo JSON, era necessário que o ícone estivesse em um array, mesmo que houvesse apenas um único ícone. Resolve o problema nº 493
 - No v2.5.5, clicar em uma notificação fecha as janelas de diálogo. #499
 - Atualização da mensagem da versão do script de diálogo quando nenhum usuário está logado, realizada por @HowardGMac em https://github.com/swiftDialog/swiftDialog/pull/510
 - Utilizar o caminho completo para o comando "scutil" (reenviar) por @MikeRich88 em https://github.com/swiftDialog/swiftDialog/pull/515
 - Adicionada uma margem extra na parte inferior da imagem de ajuda
 - Adiciona uma autorização importante para o envio de notificações, caso seja necessário. #485
 - Corrigir opções ausentes para `--textfield` na seção de ajuda #485

## Contribuições:

### Opções adicionais para trabalhar com notificações

 - Adiciona a capacidade de definir um identificador para uma notificação, permitindo que você substitua facilmente uma notificação por uma versão atualizada. Além disso, oferece a possibilidade de remover uma notificação específica por meio de seu identificador ou remover todas as notificações.

_Exemplo:_

```
dialog --notification --identifier "update.message" --title "Updates" --message "Please update by tonight."
dialog --notification --identifier "update.message" --title "Updates" --message "Please update within the next hour."
dialog --notification --identifier "update.message" --remove
```

Obrigado ao @chrisgrande

### Adicionado o parâmetro "buttonsize" como uma variável na linha de comando e no arquivo de configuração

 - Suporte para tamanhos de botões mini, pequeno e grande, utilizando os tamanhos padrão do macOS. O tamanho do botão será definido como o valor padrão "normal" caso não seja especificado ou seja inválido.
 - Suporte para o tamanho dos botões no modo de edição, para fins de teste e geração de arquivos JSON.

O estilo do botão é aplicado a `button1`, `button2` e ao botão de informações. Ele também é aplicado no layout normal e no layout de botões empilhados.

 Ele não redimensiona o botão de ajuda, que possui um tamanho fixo.

Exemplos:

```
dialog --buttonsize large --commandfile /var/tmp/dialog.txt
echo "buttonsize: mini" >> /var/tmp/dialog.txt   
```

Obrigado(a) ao(à) @k2graham

### Opções para ocultar e exibir a janela de diálogo a partir do arquivo de comandos

 - Adicionados os comandos `hide:` e `show:` à lista de comandos do arquivo de comandos para ocultar e exibir janelas. Isso não impede que as janelas sejam atualizadas enquanto estão ocultas.

Obrigado(a) ao(à) @fabienconus

