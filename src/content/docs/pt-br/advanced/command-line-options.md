---
title: Opções da Linha de Comando
description: Referência completa de todas as opções e argumentos da linha de comando do swiftDialog
translationSynced: 2026-11-25T11:28:09+00:00
---

O diálogo pode ser configurado por meio de opções na linha de comando. Todas as opções também podem ser especificadas usando um arquivo de configuração JSON](/pt-br/advanced/json-configuration).

```sh
dialog --title "Hello" --message "World"
```

Use `--help <option>` para obter informações detalhadas sobre um argumento específico.

---

## Conteúdo

| Argumento | Curto | Descrição |
|---|---|---|
| `--title <text>` | `-t` | Defina o título da caixa de diálogo. Utilize `none` para ocultar. |
| `--subtitle <text>` | | Uma linha de texto secundária exibida abaixo do título. Também utilizada como texto de subtítulo para [notificações](/pt-br/advanced/notifications). |
| `--message <text>` | `-m` | Defina a mensagem do diálogo. Suporta [Markdown](/pt-br/basic-use/markdown). |
| `--messagealignment [left\|centre\|right]` | | Alinhamento horizontal da mensagem |
| `--messageposition [top\|centre\|bottom]` | | Posição vertical do bloco de conteúdo da mensagem |
| `--titlefont <params\|json>` | | Modifique a fonte do título. Aceita pares separados por vírgula ou um objeto JSON: `key=value`, `colour`, `size`, `weight`, `name`, `alignment`, `offset`, `shadow` |
| `--messagefont <params\|json>` | | Modifique a fonte da mensagem. Aceita pares separados por vírgula `key=value` ou um objeto JSON |

Consulte [Título](/pt-br/basic-use/title) e [Mensagem](/pt-br/basic-use/message) para mais detalhes.

---

## Ícone

| Argumento | Curto | Descrição |
|---|---|---|
| `--icon <file\|url\|json>` | `-i` | Defina o ícone do diálogo. Aceita o caminho do arquivo, URL, símbolo SF (`SF=name`), recursos internos ou um objeto JSON |
| `--iconsize <num>` | | Tamanho do ícone em pontos (padrão: 150). |
| `--iconalpha <num>` | | Opacidade do ícone, variando de 0.0 (transparente) a 1.0 (totalmente opaco). |
| `--iconalttext <text>` | | Rótulo de acessibilidade para o ícone |
| `--overlayicon <file\|url\|json>` | `-y` | A imagem sobreposta é exibida no canto inferior direito do ícone. Aceita os mesmos formatos que `--icon` |
| `--hideicon` | `-h` | Ocultar o ícone para aumentar a área da mensagem |
| `--centreicon` / `--centericon` | | Reposicione o ícone para que fique centralizado entre o título e a mensagem |

Consulte o [Ícone](/pt-br/basic-use/icon)] para obter mais detalhes.

---

## Banner e fundo

| Argumento | Curto | Descrição |
|---|---|---|
| `--bannerimage <file\|url>` | `-n` | Exiba uma imagem de banner no topo da janela de diálogo |
| `--bannertitle <text>` | | Exibir o texto do título sobreposto à imagem do banner |
| `--bannertext <text>` | | Equivalente a definir `--bannertitle` e `--title` |
| `--bannerheight <num>` | | Defina a altura do banner |
| `--background <file>` | `-bg` | Defina uma imagem de fundo/marca d'água |
| `--bgalpha <num>` | `-ba` | Opacidade da imagem de fundo (padrão: 0,5). |
| `--bgposition <position>` | `-bp` | Posição da imagem de fundo (por exemplo, `center`, `topleft`). |
| `--bgfill [fill\|fit]` | `-bf` | Modo de preenchimento da imagem de fundo |
| `--bgscale [fill\|fit]` | `-bs` | Modo de escala da imagem de fundo |
| `--screenbackground <file\|url>` | | Exibir uma imagem em tela cheia, atrás da janela de diálogo |

Consulte as [imagens para banners](/pt-br/advanced/banner-images) e as [imagens de fundo](/pt-br/advanced/background-images) para mais detalhes.

---

## Botões

| Argumento | Curto | Descrição |
|---|---|---|
| `--button1text <text>` | | Rótulo para o Botão 1 (associado à tecla "Voltar" ↵, padrão: `OK`). |
| `--button1action <url>` | | URL a ser aberta quando o Botão 1 for clicado |
| `--button1shellaction <cmd>` | | Comando do shell a ser executado quando o Botão 1 for clicado |
| `--button1symbol <sf symbol\|json>` | | Símbolo SF ou objeto JSON para o Botão 1 |
| `--button1disabled` | | Iniciar com o Botão 1 desativado |
| `--button2` | `-2` | Botão "Mostrar 2" |
| `--button2text <text>` | | Rótulo para o Botão 2 (associado à tecla Esc ⎋, padrão: `Cancel`). |
| `--button2symbol <sf symbol\|json>` | | Símbolo SF ou objeto JSON para o Botão 2 |
| `--button2disabled` | | Iniciar com o botão 2 desativado |
| `--infobutton` | `-3` | Mostrar o botão de informações |
| `--infobuttontext <text>` | | Rótulo para o botão de informações |
| `--infobuttonaction <url>` | | URL a ser aberta quando o botão de informações for clicado |
| `--infobuttonsymbol <sf symbol\|json>` | | Símbolo SF ou objeto JSON para o botão de informações |
| `--buttonstyle [center\|stack]` | | Layout de botões |
| `--buttonsize [mini\|small\|regular\|large]` | | Tamanho do botão |
| `--buttontextsize <num>` | | Tamanho da fonte do rótulo do botão |
| `--quitoninfo` | | Interromper a caixa de diálogo quando o botão de informações for selecionado |

Consulte [Botões](/pt-br/basic-use/buttons)] para mais informações.

---

## Fluxo de trabalho

| Argumento | Curto | Descrição |
|---|---|---|
| `--nextbuttontext <text>` | | Rótulo para o botão "Próximo" no fluxo de trabalho (padrão: `Next`). |
| `--previousbuttontext <text>` | | Rótulo para o botão "Anterior" do fluxo de trabalho (padrão: `Previous`). |
| `--onadvance <command>` | | Comando do Shell a ser executado ao avançar entre as páginas do fluxo de trabalho <br> (a entrada é fornecida via stdin; um código de saída diferente de zero impede o avanço). |

Consulte [Fluxo de Trabalho](/pt-br/advanced/workflows)] para obter mais detalhes.

---

## Mensagem de Ajuda

| Argumento | Curto | Descrição |
|---|---|---|
| `--helpmessage <text>` | | Exiba um botão de ajuda com conteúdo em uma janela pop-up. Suporta formatação Markdown. |
| `--helpimage <file\|url>` | | Adicione uma imagem à janela de ajuda |
| `--helpsheetbuttontext <text>` | | Rótulo do botão para fechar a página de ajuda (padrão: `OK`). |
| `--helpalignment [left\|centre\|right]` | | Alinhamento do conteúdo das mensagens de ajuda |

Consulte a [mensagem de ajuda](/pt-br/operation/help-message) para obter mais detalhes.

---

## Imagens, vídeos e conteúdo para a web

| Argumento | Curto | Descrição |
|---|---|---|
| `--image <file\|url>` | `-g` | Exibe uma imagem. Várias instâncias criam um carrossel. |
| `--imagecaption <text>` | | Legenda exibida abaixo da imagem |
| `--video <file\|url>` | | Exibe um vídeo. Compatível com atalhos `youtube=<id>` e `vimeo=<id>`. |
| `--videocaption <text>` | | Legenda exibida abaixo do vídeo |
| `--autoplay` | | Reproduzir vídeo automaticamente ao abrir |
| `--webcontent <url>` | | Exibir uma página da web na área de mensagens |

Consulte as [imagens](/pt-br/basic-use/images), o [vídeo](/pt-br/basic-use/video) e o [conteúdo da web](/pt-br/basic-use/web-content) para obter mais detalhes.

---

## Área de Informações

| Argumento | Curto | Descrição |
|---|---|---|
| `--infotext <text>` | | Substitua o botão de informações por um texto estático |
| `--infobox <text>` | | Exibir o texto (com suporte a Markdown) abaixo do ícone |
| `--infoboxwidth <num>` | | Defina a largura da caixa de informações de forma independente do tamanho do ícone |

Consulte a [caixa de informações](/pt-br/advanced/info-box)] para obter mais detalhes.

---

## Entrada do usuário

| Argumento | Curto | Descrição |
|---|---|---|
| `--textfield <text\|json>[,options]` | | Adicione um campo de entrada de texto. Suporta `required`, `secure`, `prompt`, `regex`, `fileselect`, `date`, `time`, `mindate`, `maxdate` e mais. Também pode ser especificado como um objeto JSON |
| `--textfieldlivevalidation` | | Exibir feedback instantâneo da validação de expressões regulares nos campos de texto |
| `--checkbox <text\|json>` | | Adicione uma caixa de seleção com o rótulo especificado. Também pode ser especificada como um objeto JSON |
| `--checkboxstyle [checkbox\|switch][,size]` | | Alterar a aparência da caixa de seleção |
| `--selecttitle <text>[,options]` | | Adicione uma lista suspensa com o nome especificado |
| `--selectvalues <csv>` | | Valores separados por vírgula para a lista de seleção |
| `--selectdefault <text>` | | Valor padrão selecionado para a lista de opções |
| `--selectstyle` | | Estilo para a lista de opções |
| `--selectitem <json>` | | Defina um item de lista selecionável usando a sintaxe de objeto JSON |

Consulte [Campos de Texto](/pt-br/advanced/textfields), [Caixas de Seleção](/pt-br/advanced/checkboxes) e [Listas de Seleção](/pt-br/advanced/select-lists) para obter mais detalhes.

### Configuração JSON para argumentos

Muitos argumentos que aceitam valores separados por vírgula também podem ser especificados como objetos JSON. Isso oferece um controle mais preciso e é especialmente útil para configurações complexas.

**Detecção:** Se um valor for interpretado como um objeto JSON, o construtor JSON é utilizado; caso contrário, a análise CSV é aplicada.

**Argumentos suportados:**
- `--textfield` - Configuração completa do campo, com todos os modificadores
- `--checkbox` - Caixa de seleção com ícone e ativação de botão
- `--listitem` - Item de lista com objetos de ícone aninhados
- `--selecttitle` - Tratado da mesma forma que `--selectitem`
- `--selectitem` - Itens de lista de seleção definidos em JSON
- `--titlefont` / `--messagefont` - Configuração da fonte, incluindo cor, tamanho, espessura e sombra
- `--icon` / `--overlayicon` - Objetos de ícones com símbolos, cores, paletas e animações
- `--button1symbol` / `--button2symbol` / `--infobuttonsymbol` - Símbolos de botões com posicionamento

Consulte as páginas de documentação individuais para obter os esquemas JSON detalhados e exemplos.

---

## Listas de itens

| Argumento | Curto | Descrição |
|---|---|---|
| `--listitem <text\|json>` | | Adicione um item à lista. Suporta ícones de status e ações ao clicar. Também pode ser especificado como um objeto JSON, com suporte para ícones aninhados |
| `--liststyle [expanded\|compact]` | | Espaçamento vertical entre as linhas de uma lista |
| `--enablelistselect` | | Permitir a seleção de itens da lista; a seleção será retornada ao final da operação |

Consulte as [listas de itens](/pt-br/advanced/item-lists)] para obter mais detalhes.

---

## Temporizador e barra de progresso

| Argumento | Curto | Descrição |
|---|---|---|
| `--timer [<seconds>]` | | Exibe um temporizador de contagem regressiva (padrão: 10 segundos). Sai com o código 4 caso o tempo expire. |
| `--hidetimerbar` | | Oculte a barra de temporizador, mas continue a contagem regressiva |
| `--hidetimer` | | Oculte completamente o temporizador |
| `--progress [<int>]` | | Exibir uma barra de progresso com o número de etapas especificado |
| `--progresstext <text>` | | Texto inicial exibido abaixo da barra de progresso |

Consulte [Temporizador e Barra de Progresso](/pt-br/advanced/timer-progress) para obter mais detalhes.

---

## Tamanho e posição da janela

| Argumento | Curto | Descrição |
|---|---|---|
| `--width <num>` | | Largura da janela de diálogo, em pontos |
| `--height <num>` | | Altura da janela de diálogo, em pontos |
| `--small` | `-s` | Reduza o tamanho padrão da janela em 25% |
| `--big` | `-b` | Aumente o tamanho padrão da janela em 25% |
| `--position <position>` | | Posição da janela (por exemplo, `center`, `topright` ou `x,y`). |
| `--positionoffset <int>` | | Deslocamento da borda ao usar `--position` (padrão: 16). |
| `--moveable` | `-o` | Permitir que a janela seja arrastada |
| `--resizable` | | Permitir que a janela seja redimensionada (implica `--moveable`). |
| `--ontop` | `-p` | Mantenha a janela sempre visível, acima de todas as outras janelas |
| `--windowbuttons [close,min,max]` | | Habilitar os botões de fechar, minimizar e maximizar a janela |
| `--showonallscreens` | | Exibir a janela em todas as telas conectadas |
| `--appearance [dark\|light]` | | Substituir a aparência da janela |

Consulte as seções "Tamanho da Janela" e "Layout" para obter mais detalhes. ](/pt-br/advanced/window-size) ](/pt-br/advanced/layout)

---

## Configurações predefinidas de estilo de janela

| Argumento | Curto | Descrição |
|---|---|---|
| `--style <preset>` | | Aplicar um estilo predefinido: `presentation`, `mini`, `centered`, `alert`, `caution`, `warning` |
| `--mini` | | Uma janela compacta que exibe o título, o ícone e uma mensagem de duas linhas |
| `--fullscreen` | `-f` | Modo de tela cheia (sem botões; os comandos do teclado continuam funcionando). |
| `--presentation` | | Modo de apresentação com barra de progresso e layout estruturado |
| `--eula` | | Exibir na tela de aceitação do Termo de Uso |
| `--blurscreen` | | Desfoque todo o conteúdo da tela que estiver por trás da janela de diálogo |
| `--hideotherapps` | | Ocultar todos os outros aplicativos ao iniciar |

Veja [Tela Cheia](/pt-br/advanced/full-screen) e [Apresentação](/pt-br/advanced/presentation) para mais detalhes.

---

## Notificações

| Argumento | Curto | Descrição |
|---|---|---|
| `--notification` | | Enviar uma notificação do sistema para o macOS |
| `--identifier <text>` | `-id` | Identificador único para a notificação |
| `--remove` | | Remova a notificação correspondente. `--identifier` |
| `--enablenotificationsounds` | | Ativar sons de notificação |

Consulte [Notificações](/pt-br/advanced/notifications)] para obter mais detalhes.

---

## Som

| Argumento | Curto | Descrição |
|---|---|---|
| `--sound <file\|url>` | | Reproduzir um arquivo de áudio ao iniciar |
| `--showsoundcontrols` | | Mostrar controles de reprodução (reproduzir/pausar, silenciar, barra de tempo). |

---

## Ícone da barra de tarefas

| Argumento | Curto | Descrição |
|---|---|---|
| `--showdockicon` | | Exibir o ícone do Dialog na barra de aplicativos (Dock) do macOS |
| `--dockicon <file\|url>` | | Exibir uma imagem personalizada como o ícone da barra de aplicativos (implica `--showdockicon`). |
| `--dockiconbadge <text>` | | Exibir um indicador no ícone da Barra de Tarefas visível |

---

## Arquivo de comandos

| Argumento | Curto | Descrição |
|---|---|---|
| `--commandfile [<file>]` | | Caminho para o arquivo de comando para atualizações em tempo real da interface (padrão: `/var/tmp/dialog.log`). |
| `--displaylog <file>` | | Exibir o conteúdo de um arquivo exatamente como ele está escrito |
| `--loghistory [<int>]` | | Pré-preencher `--displaylog` com as últimas N linhas (padrão: 100). |

Consulte o [arquivo de comando](/pt-br/advanced/command-file) para obter mais detalhes.

---

## Entrada e saída em formato JSON

| Argumento | Curto | Descrição |
|---|---|---|
| `--jsonfile <file>` | | Carregar a configuração do diálogo a partir de um arquivo JSON |
| `--jsonstring <text>` | | Carregar a configuração do diálogo a partir de uma string JSON |
| `--json` | `-j` | Os resultados serão apresentados no formato JSON |

Consulte a [configuração em JSON](/pt-br/advanced/json-configuration)] para obter mais detalhes.

---

## Teclado e interação

| Argumento | Curto | Descrição |
|---|---|---|
| `--quitkey <char>` | | Tecla personalizada para sair (usada como `⌘ + <key>`, padrão: `q`). |
| `--hidedefaultkeyboardaction` | | Exigir `⌘ + ⇧` para ativar as ações de teclado "Voltar" / "Esc" |
| `--alwaysreturninput` | | Sempre retorne a entrada do usuário ao sair, independentemente do código de saída |
| `--ignorednd` | `-d` | Exibir a janela de diálogo mesmo quando o modo "Não Perturbe" estiver ativado |
| `--vieworder <csv>` | | Substituir a ordem de exibição dos tipos de elementos de entrada |

---

## Autorização

| Argumento | Curto | Descrição |
|---|---|---|
| `--key <string>` | `-k` | Chave de autenticação necessária para iniciar a caixa de diálogo |
| `--checksum <string>` | | Gere um hash SHA256 (para uso com `--key`). |

Consulte [Autorização](/pt-br/operation/authorization)] para obter mais detalhes.

---

## Tela de login

| Argumento | Curto | Descrição |
|---|---|---|
| `--loginwindow` | | Exibir a janela de diálogo na tela de login (requer um LaunchAgent apropriado). |

Consulte a seção "[Janela de Login](/pt-br/operation/login-window)]" para obter mais detalhes.

---

## Modo de Inspeção

| Argumento | Curto | Descrição |
|---|---|---|
| `--inspect-mode` | | Iniciar no modo de inspeção |
| `--inspect-config <file>` | | Especifique a configuração para o modo de inspeção |
| `--inspect-schema <file>` | | Especifique o esquema para o modo de inspeção |
| `--schema-validate <file>` | | Validar uma configuração em relação a um esquema |

Consulte [Modo de Inspeção](/pt-br/advanced/inspect-mode)] para obter mais detalhes.

---

## Utilitários e Depuração

| Argumento | Curto | Descrição |
|---|---|---|
| `--version` | `-v` | Imprima a string de versão |
| `--help [<argument>]` | | Imprimir a ajuda, ou obter ajuda detalhada para um argumento específico |
| `--licence` | `-l` | Imprimir a licença |
| `--debug [<colour>]` | | Ative o modo de depuração, com a opção de destacar os limites do conteúdo |
| `--verbose` | `-vvv` | Habilitar a saída detalhada dos logs |
| `--listfonts` | | Imprimir os nomes das fontes disponíveis |
| `--demo` | | Iniciar no modo de demonstração |
| `--builder` | | Iniciar a interface do kit de construção |
| `--jh` | `-jh` | Ativar o modo de compatibilidade do jamfHelper |

Consulte [Builder](/pt-br/reference/builder)] para obter mais detalhes.
