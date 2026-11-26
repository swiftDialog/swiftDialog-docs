---
title: Notificações
description: Enviar notificações do sistema usando o swiftDialog em vez de exibir janelas de diálogo
translationSynced: 2026-11-25T11:36:48+00:00
---

## Notificações

O swiftDialog permite que você envie notificações utilizando o argumento `--notification`. Isso indica que o swiftDialog deve enviar uma notificação em vez de exibir uma janela de diálogo.

As notificações utilizam os mesmos argumentos `--title`, `--message` e `--icon` para exibir texto e mídia. Quaisquer outros argumentos que não estejam listados nesta página serão ignorados.

Existe um argumento adicional `--subtitle` que adiciona uma legenda à notificação.

### Estilos de notificação (versão 3.1 e posteriores).

A partir da versão 3.1, o swiftDialog direciona as notificações por meio de aplicativos auxiliares específicos, integrados dentro de `Dialog.app`. Utilize o argumento `--style` para selecionar o tipo de notificação:

| `--style` valor | Comportamento | Função auxiliar utilizada |
|---|---|---|
| `banner` | Notificação do sistema que aparece brevemente e desaparece automaticamente | `Dialog Banner` |
| `alert` | Notificação do sistema que permanece visível até que o usuário a desative | `Dialog Alert` |
| `pseudo` | Banner de notificação simulada (o mesmo que `pseudo-banner`). | Aplicativo principal |
| `pseudo-banner` | Notificação falsa que desaparece automaticamente após um determinado período de tempo | Aplicativo principal |
| `pseudo-alert` | Notificação simulada que permanece visível até que o usuário interaja com ela | Aplicativo principal |

O valor padrão quando `--style` é omitido depende das configurações de notificação do sistema configuradas para o aplicativo.

> #### Caminho de compatibilidade (obsoleto na versão 3.1)
>
> Fazer chamadas `--notification` **sem** `--style` ainda funciona para garantir a compatibilidade com versões anteriores, mas a conexão é roteada através do pacote principal `Dialog.app`. Este método está obsoleto e gerará um aviso no fluxo de erro padrão:
> Em uma versão futura, o envio de uma notificação sem `--style` será configurado, por padrão, para `--style banner`.

Para garantir que os tipos de estilo sejam configurados corretamente para as notificações do sistema, implemente um arquivo de configuração mobileconfig que pré-aprova as notificações para os aplicativos auxiliares relevantes (`au.csiro.dialog.notifier.banner` e `au.csiro.dialog.notifier.alert`), definindo o estilo de notificação desejado.

### Use

Enviar uma notificação básica em formato de banner:

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message"
```

Enviar uma notificação de alerta persistente:

```bash
dialog --notification --style alert --title "Test Notification" --message "A test notification message"
```

![image](https://user-images.githubusercontent.com/3598965/201508706-be8fd3c5-5f06-434c-b97b-b773f6b96bdb.png)

Se a mensagem for mais longa do que o que a notificação pode exibir, a mensagem será truncada e serão exibidas elipses `...` para indicar isso. Além disso, um ícone de seta (chevron) deve aparecer no canto superior direito da notificação quando o usuário passar o cursor sobre ela, permitindo que o usuário expanda o conteúdo

[Imagem da captura de tela de 13 de novembro de 2022, às 23:26.](https://user-images.githubusercontent.com/3598965/201508943-f382a961-9a8e-4bc6-98a3-67925d367005.png)

![Captura de tela de 13 de novembro de 2022, às 17:26:15](https://user-images.githubusercontent.com/3598965/201509015-cc6591cc-5e66-4f9f-94bb-d9c0688460e9.png)

Adicionando uma legenda:

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message" --subtitle "Test Subtitle"
```

![image](https://user-images.githubusercontent.com/3598965/201508719-5f13f9fd-9507-4d6d-81c5-854d6ad4a79b.png)

Incluindo o título e o subtítulo, uma notificação pode ter até 5 linhas de texto. Um caractere `\n` dentro do corpo da mensagem criará uma quebra de linha na notificação.

Uma imagem pode ser adicionada usando `--icon` e aceita todos os formatos e fontes de imagem existentes.

![image](https://user-images.githubusercontent.com/3598965/201508767-b091140f-d040-4c86-b16b-d25bcfac8606.png)

Ao exibir uma imagem, o usuário pode expandir o conteúdo da notificação

![image](https://user-images.githubusercontent.com/3598965/201508803-29a1a02a-450f-4952-8991-9348dd754b38.png)

_Observação: Você __não pode__ substituir o ícone padrão que é exibido na notificação. As imagens adicionadas usando `--icon` aparecerão dentro da notificação._

## Definir uma ação

Você pode definir uma ação a ser executada quando o usuário clica na notificação. Essa ação pode ser um endereço URL ou um comando do sistema.

_OBSERVAÇÃO: As notificações são iniciadas pelo usuário e, consequentemente, as ações executadas pela notificação ocorrem no contexto do usuário._

O uso básico dessa funcionalidade é:

```bash
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "open -a Safari.app"
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "https://swiftdialog.app/"
```

Você pode especificar uma ação adicional e definir os rótulos dos botões:

```bash
dialog --notification --style banner --title "<text>" --message "<text>" \
    --button1text "Do Something" --button1action "/do/something" \
    --button2text "Do Something Else" --button2action "/do/something/else/"
```

`--button1action` é a ação padrão que ocorre quando o corpo da notificação ou o botão1 são clicados. `--button2action` só é acionada quando o botão2 é clicado.

## Identificadores de notificações e remoção

Você pode atribuir um identificador persistente a uma notificação usando `--identifier`. Isso permite que você remova uma notificação específica posteriormente:

```bash
# Send a notification with an identifier
dialog --notification --style banner --title "Update Available" --message "Version 2.0 is ready" --identifier "update-available"

# Remove it later
dialog --notification --style banner --remove --identifier "update-available"
```

Ligar `--remove` sem `--identifier` remove todas as notificações pendentes desse assistente.

Os identificadores também funcionam com notificações simuladas (veja abaixo).

## Habilitando os sons de notificação

Use `--enablenotificationsounds` para reproduzir o som de notificação padrão quando a notificação for exibida:

```bash
dialog --notification --style alert --title "Alert" --message "Action required" --enablenotificationsounds
```

## Notificações Falsas

As notificações "pseudo" são janelas com aparência de notificações, criadas diretamente pelo swiftDialog, e não são notificações do sistema macOS. Elas surgem deslizando a partir da borda direita da tela e imitam a aparência das notificações nativas, com um fundo translúcido.

### Por que usar notificações falsas?

- **Suporte para ícones personalizados** — O ícone exibido na notificação é totalmente personalizável usando `--icon`, incluindo símbolos SF, URLs, caminhos de arquivos e pacotes de aplicativos. Diferentemente das notificações do sistema, isso não exige a definição do ícone do pacote Dialog.app e a reinicialização do NotificationCenter.
- **Não é necessário um perfil MDM** — As notificações "falsas" não passam pelo centro de notificações do macOS, portanto, não é preciso configurar nenhum perfil mobileconfig nem conceder permissões de notificação.
- **Imagens incorporadas** — Utilize `--image` para exibir uma imagem dentro do corpo da notificação.
- **Marcação Markdown inline** — O conteúdo suporta formatação Markdown inline. `--message`

### O que as notificações falsas não são?

Notificações "pseudo" não são notificações do sistema. Elas desaparecem assim que são descartadas e não seguem as regras padrão das notificações do sistema macOS. Além disso, elas não se acumulam. É possível enviar várias notificações "pseudo", mas elas aparecerão umas sobre as outras até serem descartadas. Se isso for importante para você, utilize as notificações do sistema convencionais.



### Estilos de notificação simulados

| `--style` valor | Comportamento |
|---|---|
| `pseudo` | Igual a `pseudo-banner` |
| `pseudo-banner` | Desaparece automaticamente após 6 segundos (ou o valor de `--timer`). |
| `pseudo-alert` | Permanece na tela até que o usuário clique ou a feche |

### Uso básico

<img width="400" alt="image" src="/images/update-available.png" />

```bash
# Banner-style pseudo notification (auto-dismisses)
dialog --notification --style pseudo --title "Update Available" --message "Version 2.0 is ready to install"

# Alert-style pseudo notification (persistent)
dialog --notification --style pseudo-alert --title "Restart Required" --message "Please save your work and restart"
```

### Ícone e imagem personalizados

<img width="400" alt="image" src="/images/deployment-install-complete.png" />

```bash
dialog --notification --style pseudo --title "Deployment" --message "Software install complete" \
    --icon /System/Applications/App\ Store.app  \
    --image "/Applications/Keynote.app"
```

### Botões de ação

Quando `--button2text` ou `--button2action` é especificado, uma barra de ações aparece na parte inferior da notificação, com dois botões:

<img width="400" alt="image" src="/images/update-available-buttons.png" />

```bash
dialog --notification --style pseudo-alert --title "Update Available" \
    --message "macOS 26.4 is ready to install" \
    --button1text "Later" \
    --button2text "Install Now" --button2action "open 'x-apple.systempreferences:com.apple.Software-Update-Settings.extension'"
```

- Clicar no corpo da notificação ou no **Botão 1** executa `--button1action`.
- Clicar no **Botão 2** executa `--button2action`.
- Se nem `--button2text` nem `--button2action` forem especificados, a barra de ações é escondida e clicar em qualquer parte da notificação aciona `--button1action`.

### Temporizador de autoexclusão

Para o estilo `pseudo-banner`, a notificação desaparece automaticamente após 6 segundos, por padrão. Utilize `--timer` para definir uma duração personalizada em segundos:

```bash
# Auto-dismiss after 15 seconds
dialog --notification --style pseudo-banner --title "Reminder" --message "Meeting in 5 minutes" --timer 15
```

### Botão de fechar

<img width="400" alt="image" src="/images/restart-hover-button.png" />

Quando o usuário passa o cursor do mouse sobre uma notificação simulada, um botão de "fechar" (×) aparece no canto superior esquerdo. Ao clicar nesse botão, a notificação é removida, com o mesmo comportamento de um tempo limite (desaparece gradualmente, sai com o código 0, e nenhuma ação de botão é executada).

### Marcação de tempo em tempo real

As notificações "falsas" exibem um carimbo de data e hora ("agora") próximo ao título. Após 60 segundos, essa informação é atualizada para "há 1 minuto" e continua sendo atualizada a cada 60 segundos enquanto a notificação permanecer visível.

### Identificadores e remoção

Notificações simuladas oferecem suporte `--identifier` para remoção direcionada:

```bash
# Send a pseudo notification with an identifier
dialog --notification --style pseudo-alert --title "Updating" --message "Please wait..." --identifier "update-progress"

# Remove it when done
dialog --notification --style pseudo --remove --identifier "update-progress"

# Remove ALL visible pseudo notifications
dialog --notification --style pseudo --remove
```

Ao enviar uma nova notificação "pseudo", utilizando o mesmo identificador de uma notificação existente, a notificação antiga é automaticamente removida antes que a nova seja exibida.

### Sons de notificação

Use `--enablenotificationsounds` para reproduzir o som de alerta do sistema quando a notificação simulada aparecer:

```bash
dialog --notification --style pseudo --title "Alert" --message "Something happened" --enablenotificationsounds
```

## Aprovação e configuração do tipo de notificação por meio do MDM

Ao utilizar notificações pela primeira vez, é possível que você não receba nenhuma resposta ou que não seja solicitado a permitir o recebimento de notificações.

Para permitir notificações manualmente, você precisa acessar as configurações do sistema -> Notificações e ativar as notificações para o(s) aplicativo(s) desejado(s). Você também pode escolher entre os estilos "Nenhuma", "Notificação" ou "Alerta".

Ao implantar o swiftDialog por meio de um sistema MDM, é preferível utilizar um arquivo de configuração mobileconfig que pré-aprova as notificações e define o tipo de notificação.

### Identificadores de pacotes

| Versão | Identificador do pacote | Observações |
|---|---|---|
| Versões 2.2.1 e anteriores | `au.bartreardon.dialog` | Legado |
| v2.3 – v3.0 | `au.csiro.dialog` | Pacote principal do aplicativo |
| Versão 3.1+ (estilo de banner). | `au.csiro.dialog.notifier.banner` | `Dialog Banner` assistente |
| Versão 3.1 ou superior (estilo de alerta). | `au.csiro.dialog.notifier.alert` | `Dialog Alert` assistente |

> Para confirmar os identificadores exatos do pacote em uma versão instalada, execute o seguinte comando:
> ```
> defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Banner.app/Contents/Info.plist" CFBundleIdentifier
> `defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Alert.app/Contents/Info.plist" CFBundleIdentifier`
> ```

Se você possui uma instalação mista, pode incluir várias entradas de pacote no mesmo perfil. Um exemplo de carga útil para notificações no estilo de banner pode ser o seguinte:

```xml
<key>PayloadContent</key>
<array>
    <dict>
        <key>PayloadDisplayName</key>
        <string>Notifications Payload</string>
        <key>PayloadIdentifier</key>
        <string>449B1259-E631-4051-ADCE-9532B813ADDC</string>
        <key>PayloadOrganization</key>
        <string>Org Name</string>
        <key>PayloadType</key>
        <string>com.apple.notificationsettings</string>
        <key>PayloadUUID</key>
        <string>12EA8FDA-B204-4AD0-802C-C980615F0BA5</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>NotificationSettings</key>
        <array>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.bartreardon.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.banner</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>2</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.alert</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
        </array>
    </dict>
</array>
```

Observe que a chave `AlertType` controla o estilo de notificação de forma independente da chave `--style`:
- `1` = Banner (desaparece automaticamente).
- `2` = Alerta (permanece ativo até ser desativado).

Ao implementar com `--style alert`, defina `AlertType` como `2` na entrada `au.csiro.dialog.notifier.alert`, e o contrário para banners.

 > #### Uma observação sobre erros de notificação
 >
 > Se você receber o seguinte:
 >
 > ```
 > As notificações não estão disponíveis: Não foi possível estabelecer comunicação com um aplicativo auxiliar
 > ```
 >
 > Verifique se o aplicativo Dialog relevante possui as notificações habilitadas nas configurações do sistema, seja aplicando um dos arquivos de configuração mobileconfig mencionados acima por meio de um sistema de gerenciamento de dispositivos móveis (MDM) ou manualmente nas configurações do sistema.

## Atualizando o ícone padrão das notificações

As notificações utilizarão o ícone padrão do swiftDialog. Se você deseja personalizar a aparência e usar um ícone diferente, como um ícone que represente a identidade da sua empresa, você pode seguir os seguintes passos para alterar o ícone do aplicativo e utilizá-lo de forma mais adequada.

> #### Suporte a partir do macOS 26.4
>
> No macOS 26.4, a atualização do ícone do pacote de aplicativos e, consequentemente, do ícone de notificação, não funciona corretamente. Se a identidade visual é importante, utilize o novo recurso de "notificação simulada", que apresenta uma interface semelhante às notificações do sistema, mas não utiliza o sistema de notificações do macOS. Portanto, pode não ser adequado para todas as situações.

### Pré-requisitos

 - Pacote mais recente do swiftDialog
 - Uma imagem de substituição adequada, com pelo menos 512x512 pixels (preferencialmente 1024x1024).

 <img src="https://user-images.githubusercontent.com/3598965/201548460-042b057f-3174-407e-ae42-0916c0a57cee.png" width="500" />

 - #### Gerando uma imagem

   Você pode gerar uma imagem a partir do aplicativo de autoatendimento dos seus fornecedores de MDM usando o comando `sips`. Por exemplo:

    ##### Kandji

    ```bash
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sips -s format png /Applications/Kandji\ Self\ Service.app/Contents/Resources/AppIcon.icns --out /Library/Application\ Support/Dialog/Dialog.png
    ```

    ##### Jamf

    ```bash
    temp_file=$(/usr/bin/mktemp)
    /usr/bin/xxd -p -s 260 "$(defaults read /Library/Preferences/com.jamfsoftware.jamf self_service_app_path)"/Icon$'\r'/..namedfork/rsrc | /usr/bin/xxd -r -p > "$temp_file"
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sudo /usr/bin/sips -s format png "$temp_file" --out /Library/Application\ Support/Dialog/Dialog.png
    ```

### Etapas

  1. Copie a imagem do ícone de substituição para `/Library/Application Support/Dialog/Dialog.png` (sensível a maiúsculas e minúsculas).
  2. Instale o swiftDialog a partir do `.pkg` instalador.

Com a substituição `Dialog.png` implementada, o instalador substituirá o ícone padrão pela imagem especificada. As notificações usarão, então, a imagem personalizada como ícone.

 ![Captura de tela de 14 de novembro de 2022, às 9:55:20](https://user-images.githubusercontent.com/3598965/201548926-669bc9e0-8257-4bb1-ac1f-0e23ff82f378.png)
