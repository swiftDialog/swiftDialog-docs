---
title: Lançador de Interface de Linha de Comando (CLI) do Dialog
description: Como o executável da interface de linha de comando (CLI) do Dialog funciona e quais são as opções de nível de utilitário
translationSynced: 2026-11-25T11:53:34+00:00
---

O comando `dialog` disponível em `/usr/local/bin/dialog` não é o próprio aplicativo Dialog — é um lançador de linha de comando (CLI) leve (`dialogcli`) que envolve o arquivo executável Dialog.app. Compreender o que ele faz é útil ao implantar ou criar scripts com o swiftDialog.

---

## O que o lançador faz

Ao executar `dialog`, o lançador:

1. Localiza o arquivo executável do Dialog.app em relação ao caminho do próprio aplicativo, dentro do pacote de instalação.
2. Cria o arquivo de comando em `/var/tmp/dialog.log` (ou no caminho especificado em `--commandfile`) se ele ainda não existir. Se o caminho for um link simbólico, o programa de inicialização é interrompido para evitar riscos de segurança.
3. Identifica o usuário da interface gráfica atual, utilizando `SCDynamicStoreCopyConsoleUser`. Se nenhum usuário da interface gráfica estiver ativo e `--loginwindow` não for especificado, o programa de inicialização é encerrado com o código `1`.
4. Executa o diálogo no contexto correto do usuário. Quando chamado como usuário root (por exemplo, a partir de uma política da Jamf ou de um LaunchDaemon), o lançador utiliza `launchctl asuser` para executar o Dialog como o usuário da interface gráfica que está logado, garantindo que a janela apareça na sessão de exibição correta.
5. **Passa automaticamente** — o PID próprio do lançador é injetado como `--pid`, para que o Dialog possa monitorar o processo que o invocou e encerrar a execução caso este seja finalizado. `--pid <pid>`
6. **Notificações com estilo específico para rotas** — quando tanto `--notification` quanto `--style alert` ou `--style banner` são utilizados, o aplicativo lançador encaminha a chamada para o aplicativo auxiliar de notificação integrado apropriado, em vez do executável principal do Dialog.

---

## Criando o link simbólico

O instalador inclui uma `--link` opção que cria um `/usr/local/bin/dialog` link simbólico apontando para ele mesmo. Isso deve ser executado como usuário root:

```sh
sudo Dialog.app/Contents/MacOS/dialog --link
```

Normalmente, essa tarefa é realizada automaticamente pelo pacote de instalação do swiftDialog.

---

## Opções de utilidade

Essas opções são gerenciadas diretamente pelo programa Dialog e são úteis principalmente para tarefas de administração ou scripts de implantação.

### `--setappicon <file>`

Define o ícone do aplicativo swiftDialog para o arquivo de imagem especificado e, em seguida, encerra o programa imediatamente. Isso também atualiza os ícones de quaisquer aplicativos auxiliares de notificação integrados.

```sh
dialog --setappicon /path/to/custom-icon.png
```

Esta é uma operação única – o Dialog não exibirá nenhuma janela. Ela foi projetada para personalização após a instalação, permitindo que o ícone da barra de tarefas e as notificações estejam de acordo com a identidade visual da sua organização.

### `--callingpid <int>`

Monitora o identificador de processo (ID) especificado. Se esse processo for encerrado, o Dialog será automaticamente fechado com o código `40`.

```sh
dialog --title "Installing..." --callingpid 12345
```

Isso é injetado automaticamente pelo `dialogcli` launcher (usando seu próprio PID), portanto, o Dialog será encerrado se o script ou processo que o invocou for finalizado. É possível fornecer um PID diferente explicitamente, o que faria com que o Dialog estivesse vinculado a um processo diferente, no entanto, esse caso de uso não é suportado.

O código de saída **40** é retornado quando o Dialog é encerrado devido à finalização do processo monitorado.
