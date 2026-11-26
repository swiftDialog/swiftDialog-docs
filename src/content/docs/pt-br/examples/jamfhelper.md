---
title: Suporte da jamfHelper
description: Utilizando o swiftDialog como uma substituição direta para o jamfHelper
translationSynced: 2026-11-25T11:50:42+00:00
---

O Dialog agora tem a capacidade de aceitar um conjunto básico de opções de linha de comando no formato jamfHelper, com a nova flag `--jh`.

Isso facilita a implementação em fluxos de trabalho e scripts existentes, substituindo a chamada para `/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper` por `/usr/local/bin/dialog --jh`

Ao utilizar a flag, o sistema de diálogo será instruído a converter as opções do `jamfHelper` em opções equivalentes no diálogo. Nem todas as opções são suportadas. As opções padrão do diálogo que não possuem equivalente no `jamfHelper` ainda estão disponíveis, por exemplo, `--width`, `--height` e `--image`.

<br/>

## Características e comportamento

***
### Implementado

#### `-windowType [hud | utility | fs]`

`hud` e `utility` são ignorados. `fs` é convertido em diálogo `--fullscreen` e será exibido em tela cheia nas janelas de diálogo

#### `-windowPosition [ul | ll | ur | lr]`

A janela de posicionamento pode ser exibida no canto superior direito, superior esquerdo, inferior direito ou inferior esquerdo da tela do usuário. Essa é a única funcionalidade que atualmente não faz parte das opções padrão das janelas de diálogo, mas foi implementada para garantir a compatibilidade com o jamfHelper.

#### `-title "string"`
Convertido para `--title`

Define o título da janela para a string especificada

#### `-heading "string"` e `-description "string"`
Convertido para `--message`

Tanto `-heading` quanto `-description` são incorporados na opção de diálogo `--message`. `-heading` é convertido em um título de nível 4 em Markdown `####`, seguido por uma linha em branco e, em seguida, por `-description`

#### `-icon path`
Convertido para `--icon`

Se não estiver presente, a opção "forces dialogs" `--hideicon` fará com que o comportamento seja semelhante ao do jamfHelpers, exibindo o diálogo mesmo que um identificador (ID) não seja especificado

#### `-button1 "string"`
Convertido para `--button1text`

**_Comportamento alterado:_** O diálogo sempre exibe o botão padrão, o que difere do funcionamento do jamfHelper. O texto do botão padrão é `OK`

#### `-button2 "string"`
Convertido para `--button2text`

#### `-alignDescription [right | left | center | justified | natural]`
Convertido para `--alignment`

As únicas opções implementadas são `right`, `centre` e `left`

#### `-timeout int` e `-countdown`
Convertido para `--timer`.

`-countdown` é sempre implícito, pois o indicador de tempo sempre mostra o tempo limite, e a barra de tempo não é implementada na janela de diálogo.

<br/>

***
### Não implementado

#### `-defaultButton [1 | 2]`
O botão padrão é sempre o botão número 1

#### `-cancelButton [1 | 2]`
O botão "Cancelar" é sempre o botão número 2 (se estiver visível).

#### `-showDelayOptions "int, int, int,..."`

#### `-alignHeading [right | left | center | justified | natural]`

#### `-alignCountdown [right | left | center | justified | natural]`

#### `-iconSize pixels`

#### `-lockHUD`

#### `-fullScreenIcon`