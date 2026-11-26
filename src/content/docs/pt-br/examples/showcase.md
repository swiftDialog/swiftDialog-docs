---
title: Vitrine
description: Projetos comunitários, scripts e exemplos que utilizam o swiftDialog
translationSynced: 2026-11-25T11:49:19+00:00
---

## O que se segue é uma demonstração das diferentes maneiras pelas quais o swiftDialog pode ser utilizado.

[Demonstrações de scripts do swiftDialog](https://github.com/swiftdialog/demo)

## Oficinas e vídeos

Estes são vídeos gravados em diferentes conferências.

Bart Reardon

 - [JNUC 2022](https://www.youtube.com/watch?v=HXwUeBWh20I)

 - Oficina SwiftDialog [MacDevOpsYVR 2024](https://www.youtube.com/watch?v=dZgmmQbTTdg)

Jon Crain

 - PSU MacAdmins 2023: [Diálogos personalizáveis para macOS: Utilizando o SwiftDialog para uma melhor experiência do usuário.](https://www.youtube.com/watch?v=QtWNBn76LQM)

Trevor Sysock

 - PSU MacAdmins 2024 [Você encontrou o seu "Installomator" no meu swiftDialog! ](https://www.youtube.com/watch?v=WU6o3iJNQM4)

## Blogs

Como exibir notificações personalizadas com swiftDialog e SimpleMDM](https://simplemdm.com/blog/how-to-display-custom-notifications-with-swiftdialog-and-simplemdm/)

[Conheça o Bart - Jamf](https://www.jamf.com/blog/bart-reardon-swiftdialog/)


## Projetos que se integram com o swiftDialog

Esses projetos não exigem que o swiftDialog esteja em funcionamento, mas integrações opcionais estão disponíveis

### [Scripting para o macOS](https://scriptingosx.com) - Installomator]

![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/Installomator/Installomator/main)

Um único script de instalação para resolver todos os problemas. https://github.com/Installomator/Installomator

 - Exiba o progresso do Installomator usando o SwiftDialog no Jamf. ](https://github.com/Installomator/Installomator/tree/main/MDM/Jamf)

### [Mac Nerd](https://github.com/Mac-Nerd/) - Patchomator]

![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/Mac-Nerd/patchomator/1.1)

Um script de gerenciamento para o Installomator. https://github.com/Mac-Nerd/patchomator

 - [Exibir o progresso e outras mensagens através do swiftDialog, se estiver instalado. ](https://github.com/Mac-Nerd/patchomator#swift-dialog)

### [Atualização Automática do Aplicativo](https://github.com/App-Auto-Patch/App-Auto-Patch)

![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/App-Auto-Patch/App-Auto-Patch)

O App Auto-Patch combina a descoberta automática de aplicativos instalados, a integração com o Installomator e prompts intuitivos do swiftDialog para automatizar o gerenciamento de atualizações de aplicativos em computadores Mac.

O App Auto-Patch foi desenvolvido com base em um conceito semelhante ao projeto Patchomator, e uma parte significativa do seu código foi adaptada desse projeto.

## Projetos adicionais que são baseados em ou que utilizam o swiftDialog de alguma forma

### [Scott Kendall](https://github.com/ScottEKendall/)

 - [Scripts do Jamf Pro ](https://github.com/ScottEKendall/JAMF-Pro-Scripts)

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/ScottEKendall/JAMF-Pro-Scripts/main)

### [Richard Purves](https://github.com/franton/)

 - [Implantação Rápida ](https://github.com/franton/SwiftDeploy) Método de implantação automatizada para Jamf Pro e SwiftDialog

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/franton/SwiftDeploy/main)

### [Graham Pugh](https://github.com/grahampugh/)

 - Apague a instalação – Reinstale o macOS diretamente do volume do sistema usando ](https://github.com/grahampugh/erase-install) `startosinstall`

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/grahampugh/erase-install/main)

### [Dan Snelson](https://github.com/dan-snelson/dialog-scripts)

 - [Exibir Mensagem](https://github.com/dan-snelson/dialog-scripts/tree/main/Display%20Message) - Utilize os parâmetros do script de política do switftDialog e do Jamf Pro para exibir facilmente mensagens envolventes para os usuários finais.

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/dan-snelson/dialog-scripts/main)

 - [Configuração do seu Mac](https://github.com/setup-your-mac/Setup-Your-Mac): Simplifique a configuração inicial do dispositivo utilizando o swiftDialog e os eventos de política personalizados do Jamf Pro

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/setup-your-mac/Setup-Your-Mac/main)


### [Adam Codega](https://github.com/acodega/dialog-scripts)

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/acodega/dialog-scripts/main)

 - [MDM Apps Deploy](https://github.com/acodega/dialog-scripts/blob/main/MDMAppsDeploy.sh) - Exibe uma caixa de diálogo com uma lista de aplicativos e indica quando foram instalados

 - [Nome do Computador (obtido pela entrada do usuário)](https://github.com/acodega/dialog-scripts/blob/main/computerNameFromInput.sh)

 - [Verificação e instalação do swiftDialog](https://github.com/acodega/dialog-scripts/blob/main/dialogCheckFunction.sh): Verifica a versão atual do swiftDialog instalada e instala os componentes necessários

### [Jon Crain](https://github.com/joncrain/)

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/joncrain/swiftDialog-scripts/main)

 - [swiftDialog scripts](https://github.com/joncrain/swiftDialog-scripts) - Scripts que utilizam o [swiftDialog](https://github.com/bartreardon/swiftDialog) para diversas tarefas.

 - [Fluxo de trabalho DEP/ADE ](https://github.com/joncrain/swiftDialog-scripts/tree/main/depnotify-swiftdialog) - Fluxo de trabalho do tipo DEPnotify com seleção de software opcional.

 - [Alerta do FileVault](https://github.com/joncrain/swiftDialog-scripts/tree/main/fv_alert-swiftdialog) - Alerta que será acionado quando o Crypt detectar um problema com o armazenamento de chaves.

 - [Aviso do Assistente de Migração](https://github.com/joncrain/swiftDialog-scripts/tree/main/ma_alert-swiftdialog) - exibir uma notificação para o usuário final quando o Assistente de Migração for iniciado

 - [Software Update](https://github.com/joncrain/swiftDialog-scripts/tree/main/nudge-swiftdialog) - Nudge SwiftDialog. Baseado livremente no [Nudge](https://github.com/macadmins/nudge)

 - [Alerta de inscrição no MDM ](https://github.com/joncrain/swiftDialog-scripts/tree/main/umad-swiftdialog) - Conceitualmente baseado em [umad](https://github.com/macadmins/umad) de Erik Gomez.

### [James Smith](https://github.com/smithjw/)

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/smithjw/speedy-prestage-pkg/main)

 - [swiftDialog speedy-prestage](https://github.com/smithjw/speedy-prestage-pkg/tree/feature/swiftDialog) - Script de Inscrição da Jamf]

### [Thijs Xhaflaire](https://github.com/txhaflaire/)

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/txhaflaire/DiskEncrypter/main)

 - Criptografar dispositivos de armazenamento removíveis não criptografados. ](https://github.com/txhaflaire/DiskEncrypter) Criptografar dispositivos de armazenamento removíveis não criptografados

### [Second Son Consulting](https://www.secondsonconsulting.com/)

 - [Configuração Inicial](https://github.com/SecondSonConsulting/Baseline) - Uma solução de configuração automática e independente de plataformas de gerenciamento de dispositivos móveis (MDM) para macOS

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/SecondSonConsulting/Baseline/main)

 - [Renew](https://github.com/SecondSonConsulting/Renew) - Um script para macOS que incentiva os usuários a reiniciar seus computadores.]

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/SecondSonConsulting/Renew/main)

 - [Exemplos do swiftDialog](https://github.com/SecondSonConsulting/swiftDialogExamples)

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/SecondSonConsulting/swiftDialogExamples/main) - exemplos de scripts para demonstrar os diversos recursos do [SwiftDialog](https://github.com/bartreardon/swiftDialog)

### [Martin Piron](https://github.com/ooftee)

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/ooftee/dialog-starterkit/main)

 - [Kit de Inicialização](https://github.com/ooftee/dialog-starterkit) - uma forma simples e intuitiva de selecionar e instalar um conjunto de aplicativos

### [PezzaD84](https://github.com/PezzaD84)

 - [Assemble](https://github.com/PezzaD84/Assemble) - Script para configurar dispositivos utilizando o swiftDialog]

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/PezzaD84/Assemble/main)

 - [JAMF-LAPS-UI](https://github.com/PezzaD84/JAMF-LAPS-UI) - Uma interface de usuário para o recurso JAMF LAPS integrado.]

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-UI/main)

 - [JAMF-LAPS-Configurator](https://github.com/PezzaD84/JAMF-LAPS-Configurator) - Um script Bash para auxiliar na configuração do JAMF LAPS

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-Configurator/main)

 - [Informações do Dispositivo](https://github.com/PezzaD84/Device-Information) - Um script Bash para exibir informações do dispositivo em uma interface amigável.]

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/PezzaD84/Device-Information/main)

### [Andrew Barnett](https://github.com/AndrewMBarnett)

 - [Reinscrição](https://github.com/AndrewMBarnett/ReEnroll) - Automatize o processo de reinscrição de dispositivos no Jamf Pro

   ![Último commit do GitHub (ramo)](https://img.shields.io/github/last-commit/AndrewMBarnett/ReEnroll/main)

### [Microsoft](https://github.com/microsoft)

 - [Implementando uma tela de apresentação de integração com Swift Dialog e Intune. ](https://github.com/microsoft/shell-intune-samples/tree/03b181ca16c8a8f677a19a3a45f5943fb36e69b9/macOS/Config/Swift%20Dialog)

   ![Último commit do GitHub (branch)](https://img.shields.io/github/last-commit/microsoft/shell-intune-samples/master) - Tela de apresentação para a integração do Intune