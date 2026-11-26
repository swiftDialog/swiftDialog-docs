---
title: Começando com o swiftDialog
description: Introdução ao swiftDialog, uma ferramenta moderna para macOS que facilita a criação de janelas de diálogo para administradores
translationSynced: 2026-11-25T10:35:53+00:00
---

`dialog -s --title "Welcome to swiftDialog" --message "Hi There.  <br>It's really nice to see you 🙂"`

![swiftDialog Exemplo de Boas-Vindas](https://github.com/user-attachments/assets/1a06df20-860f-4c0c-bd14-cdb572604048)

O objetivo do swiftDialog é servir como uma ferramenta auxiliar para administradores de sistemas macOS, que podem utilizá-lo através de scripts para exibir uma janela de diálogo que apresenta informações ao usuário e registra a ação que o usuário realizou. Essas informações podem ser posteriormente utilizadas para processamento adicional em scripts ou simplesmente para exibir alguma informação específica.

O swiftDialog aceita entradas pela linha de comando, utilizando uma ou mais [opções de linha de comando](/pt-br/advanced/command-line-options) para indicar ao swiftDialog o que exibir e como exibir.

Existem diversas opções disponíveis que podem ser utilizadas para personalizar o conteúdo que você deseja exibir, variando desde exibições informativas muito simples até processamentos mais complexos, que incluem campos de texto, listas suspensas, exibição de imagens e muito mais.

## Executando o swiftDialog

O instalador **.pkg** da página [releases](https://github.com/swiftDialog/swiftDialog/releases) instalará o swiftDialog em `/usr/local/bin/dialog`, que também deve estar no `$PATH` padrão do macOS.

Para chamar o dialog a partir do seu script, você pode usar o caminho completo ou confiar em `$PATH`

```bash
$ dialog --title ...
```

ou

```bash
$ /usr/local/bin/dialog --title ...
```

No nível mais básico, o dialog pode simplesmente usar as opções de linha de comando `--title` e `--message` para exibir uma janela com a mensagem desejada.

O swiftDialog pode realizar muito mais do que isso, e você deve consultar a página [Opções de Linha de Comando](/pt-br/advanced/command-line-options) para obter uma lista completa das opções disponíveis, ou chamar o dialog com a opção `--help`.

## Links rápidos

### Características básicas

- [Personalizando o título do swiftDialog](/pt-br/basic-use/title)
- [Personalização da exibição de mensagens no swiftDialog](/pt-br/basic-use/message)
- [Personalizando a imagem exibida na área de ícone do swiftDialog](/pt-br/basic-use/icon)
- [Adicionando uma imagem de banner](/pt-br/advanced/banner-images)
- [Personalizando os botões e o comportamento dos botões](/pt-br/basic-use/buttons)

### Recursos avançados

- [Caixa de Informações](/pt-br/advanced/info-box)
- [Imagens para banners](/pt-br/advanced/banner-images)
- [Mensagem de Ajuda](/pt-br/operation/help-message)
- [Menus suspensos e botões de opção](/pt-br/advanced/select-lists)
- [Campos de Texto](/pt-br/advanced/textfields)
- [Caixas de seleção](/pt-br/advanced/checkboxes)
- [Temporizador com Barra de Progresso](/pt-br/advanced/timer-progress)
- [Tamanho e comportamento da janela](/pt-br/advanced/window-size)
- [Modo de Tela Cheia](/pt-br/advanced/full-screen)
- [Modo de Apresentação](/pt-br/advanced/presentation)
- [Listas de itens](/pt-br/advanced/item-lists)
- [Notificações do Sistema](/pt-br/advanced/notifications)
- [Modificando o atalho CMD+Q](/pt-br/operation/command-q)
- [Variáveis internas](/pt-br/operation/builtin-variables)

## Suporte

O swiftDialog foi criado, em parte, como um exercício de aprendizado sobre como desenvolver aplicativos usando SwiftUI, e, em parte, para atender à necessidade de uma forma de comunicar informações aos usuários de Mac em um estilo que eu considerava adequado.

O suporte pode ser oferecido [criando um chamado](https://github.com/swiftDialog/swiftDialog/issues). Sugestões de novas funcionalidades também são bem-vindas.

## Contato

Você pode entrar em contato com o autor no canal #swiftdialog do [Slack da comunidade Macadmins](https://www.macadmins.org/slack) (nome de usuário @bartreardon – geralmente presente no canal #anzmac). No entanto, por favor, direcione quaisquer dúvidas de suporte ou perguntas gerais para o GitHub, pelo menos para que seu problema possa ser rastreado e resolvido. Obrigado! 😃
