---
title: Tela de login
description: Executando diálogos swiftDialog no contexto da tela de login do macOS
translationSynced: 2026-11-25T11:52:01+00:00
---

## Suporte para janela de login (a partir da versão 2.5.0).

`--loginwindow`

No swiftDialog 2.5, é possível exibir janelas de diálogo na tela de login.

Diálogos padrão são suportados, com ou sem `--blurscreen`

## Requisitos

Para executar em um contexto de janela de login, você precisará configurar o seguinte:

 - Um script que inicia a caixa de diálogo swiftDialog com a configuração desejada
   - Inclua o argumento `--loginwindow`
 - Um agente de inicialização

### Configuração do LaunchAgent

#### Configuração manual

O exemplo a seguir ilustra um LaunchAgent básico:

```xml
<plist version="1.0">
<dict>
	<key>OnDemand</key>
	<false/>
	<key>LaunchOnlyOnce</key>
	<true/>
	<key>ProgramArguments</key>
	<array>
		<string>/path/to/script.sh</string>
	</array>
	<key>LimitLoadToSessionType</key>
	<string>LoginWindow</string>
	<key>Label</key>
	<string>com.swiftDialog.example-login-window</string>
</dict>
</plist>
```

Nomeie-o adequadamente, por exemplo, "`com.swiftDialog.example-login-window.plist`", e instale-o em "`/Library/LaunchAgents/`"

#### Utilizando o Outset

A ferramenta de código aberto Macadmins [Outset](https://github.com/macadmins/outset/) possui funcionalidades para executar programas na janela de login.

Além de simplificar o processo, você também terá acesso a controles que impedem que um usuário desative itens de login. Consulte a [wiki do Outset](https://github.com/macadmins/outset/wiki/Deployment#login-items-management)] para mais detalhes.

Coloque seu script no diretório `/usr/local/outset/login-window/`, com as permissões definidas como `root:root` `0755` (`-rwxr-xr-x`), e o programa "outset" gerenciará a execução do script quando a janela de login aparecer.

### Considerações

Você precisará considerar o que acontece após a execução do script. Se você não deseja que ele seja executado sempre que a tela de login for exibida, será necessário incluir condições no seu script para que ele não execute nenhuma ação ou se desinstale automaticamente quando não for mais necessário.

### Exemplo de caso de uso

#### Política de Uso Aceitável da Organização

O exemplo a seguir é um diálogo de política de uso aceitável que exige que a caixa de seleção seja marcada e inclui conteúdo de um arquivo Markdown (exemplo: [AcceptableUsePolicy.md](https://github.com/user-attachments/files/15521093/AcceptableUsePolicy.md)]) e é exibido no modo `--eula`. Ele seria exibido sempre que a janela de login fosse apresentada.

```bash
dialog --message "/path/to/AcceptableUsePolicy.md" --height 50% --width 35% --style centred --icon sf=rectangle.and.pencil.and.ellipsis,colour=accent --title "{COMPANY-NAME} Acceptable Use" --button1disabled --checkbox "I Agree",enableButton1 --quitkey A --eula --blurscreen --loginwindow
```
<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/4139ae63-f420-439f-8aaa-152f8fcc91b9" width=500px>