---
title: Variáveis internas
description: Utilização de variáveis dinâmicas para informações do sistema em diálogos
translationSynced: 2026-11-25T11:53:04+00:00
---

## Variáveis internas

O swiftDialog agora contém variáveis internas que serão preenchidas com informações específicas do servidor. Inclua-as em suas strings de texto como `{variablename}`

As variáveis incluídas são:

    {computername}  - nome do host do computador {computermodel} - modelo do computador, ex. "Mac mini (2023)" {serialnumber}  - número de série {username}      - nome de usuário atual, ex. `johndoe` {userfullname}  - nome completo, ex. `John Doe` {osversion}     - versão do macOS, ex. `14.4.1` {osname}        - nome do macOS, ex. `Sonoma`

Quaisquer variáveis de ambiente também podem ser acessadas dessa maneira

    diálogo --ícone computador --título "{computermodel}" --mensagem "Executando {osname} {osversion}" --estilo centralizado

<img width="350" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/84c41296-8571-4a7b-b9a0-54359465561f">