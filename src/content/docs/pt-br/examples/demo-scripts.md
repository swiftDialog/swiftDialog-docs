---
title: Roteiros de demonstração
description: Roteiro completo para demonstração de como selecionar e instalar aplicativos
translationSynced: 2026-11-25T11:48:57+00:00
---

Uma completa coleção de demonstrações pode ser encontrada em https://github.com/swiftDialog/demo

## Suíte de demonstrações abrangente do swiftDialog

Uma coleção de scripts para o shell zsh que demonstra todas as principais funcionalidades do [swiftDialog](https://github.com/swiftDialog/swiftDialog), por meio de um tour interativo e autoguiado.

## Requisitos

- macOS 15 ou versões mais recentes
- [**swiftDialog versão 3 ou superior**](https://github.com/swiftDialog/swiftDialog/releases)

## Início rápido

```zsh
# clone this repo
git clone https://github.com/swiftDialog/demo.git swiftDialog-demo

# or download the zip
curl -sL "https://github.com/swiftDialog/demo/archive/refs/heads/main.zip" -o swiftDialog-demo.zip && unzip swiftDialog-demo.zip -d swiftDialog-demo

cd swiftDialog-demo
./run_demos.zsh
```

O controlador principal utiliza o próprio swiftDialog. Selecione as demonstrações que incluem caixas de seleção e, em seguida, avance por cada uma delas.

## Habilidades em Inteligência Artificial para a criação de conteúdo no swiftDialog

**Novo no swiftDialog?** Comece com a página oficial do [swiftDialog Builder](https://swiftdialog.app/builder/builder/)] para se familiarizar e criar protótipos visuais. Em seguida, utilize um dos conjuntos de ferramentas (skill packs) contidos no repositório para transformar esse conhecimento em scripts para o shell, no estilo do repositório. O Builder é útil, mas não é abrangente e não substitui as etapas finais de dimensionamento, limpeza e decisões relacionadas ao fluxo de trabalho.

### Habilidades disponíveis

**[`codex-swiftdialog-builder`](skills/codex-swiftdialog-builder/)** — Para GitHub Copilot / OpenAI Codex

- [`SKILL.md`](skills/codex-swiftdialog-builder/SKILL.md) — Fluxo de trabalho do Codex e seleção de níveis de serviço
- [`references/`](skills/codex-swiftdialog-builder/references/) — Orientações para criação de protótipos e desenvolvimento de conteúdo
- [`assets/templates/`](skills/codex-swiftdialog-builder/assets/templates/) — Scripts de inicialização básicos
- Inclui um processo do tipo Jamf/execução com privilégios de root `/var/tmp`, além de um mecanismo de transferência de propriedade para fluxos de trabalho de comandos e arquivos iniciados como `root`

**[`claude-swiftdialog-builder`](skills/claude-swiftdialog-builder/)** — Para Claude Sonnet

- [`CLAUDE.md`](skills/claude-swiftdialog-builder/CLAUDE.md) — Fluxo de trabalho e seleção de planos do Claude
- [`references/`](skills/claude-swiftdialog-builder/references/) — Orientações para criação de protótipos e desenvolvimento de conteúdo
- [`templates/`](skills/claude-swiftdialog-builder/templates/) — Scripts de inicialização básicos
- Inclui um processo do tipo Jamf/execução com privilégios de root `/var/tmp`, além de um mecanismo de transferência de propriedade para fluxos de trabalho de comandos e arquivos iniciados como `root`

Ambas as ferramentas seguem as mesmas convenções de repositório e produzem a mesma saída de script — escolha aquela que seja compatível com a sua plataforma de inteligência artificial. Consulte [`skills/README.md`](skills/README.md) para obter instruções detalhadas de uso.

Estes são pacotes de habilidades para assistentes de inteligência artificial, e não demonstrações funcionais que podem ser executadas diretamente no sistema.

## Ambiente de desenvolvimento com auxílio de inteligência artificial

Após explorar a demonstração e entender as funcionalidades do swiftDialog, utilize o diretório [`playground/`](playground/)] para criar seus próprios scripts personalizados com o auxílio da inteligência artificial. O ambiente de desenvolvimento inclui um guia completo e passo a passo que demonstra como:

- Utilize assistentes de inteligência artificial (como Claude e Copilot) aproveitando as funcionalidades integradas
- Escolha o nível adequado para o seu fluxo de trabalho (diálogos básicos → formulários → atualizações de progresso → modo de inspeção).
- Acompanhe cenários práticos detalhados, com instruções precisas e exemplos de interações esperadas com a inteligência artificial
- Crie scripts prontos para produção para tarefas de administração do Mac (configuração inicial, conformidade, implantação, monitoramento, confirmação de ações que podem causar perda de dados).

**Comece aqui:** [`playground/README.md`](playground/README.md) — Seu ambiente de trabalho para o desenvolvimento rápido de scripts swiftDialog com auxílio de inteligência artificial.

## Índice de demonstrações

- `01_basic_styles.zsh` — `--style` (alerta, aviso, precaução, centralizado), substituição de estilos
- `02_title_message.zsh` — `--title`, `--titlefont`, `--message`, `--messagefont`, `--messagealignment`, `--messageposition`, `--bannertitle`, título "nenhum"
- `03_icons.zsh` — `--icon` (Símbolos do sistema, aplicativos, recursos nativos, QR code, paleta de cores, cores automáticas, peso), `--iconsize`, `--iconalpha`, `--centreicon`, `--overlayicon`, `--hideicon`
- `04_buttons.zsh` — `--button1text`, `--button1symbol`, `--button1disabled`, `--button2text`, `--button2symbol`, `--infobuttontext`, `--infobuttonsymbol`, `--infobuttonaction`, `--buttonstyle` (centralizado, empilhado), `--buttonsize`, `--buttontextsize`, `--hidedefaultkeyboardaction`
- `05_images_banners.zsh` — `--image`, `--imagecaption`, `--bannerimage`, `--bannertitle`, `--bannertext`, `--background`, `--bgalpha`, `--bgposition`, `--bgfill`
- `06_progress_timer.zsh` — `--progress` (absoluto, incremento, reset, completo), `--progresstext`, `--progresstextalignment`, `--timer`, `--hidetimerbar`, atualizações de progresso do arquivo de comandos
- `07_text_fields.zsh` — `--textfield` (obrigatório, seguro, rápido, valor, expressão regular, erro de expressão regular, confirmar, seleção de arquivos, tipo de arquivo, caminho, nome), `--textfieldlivevalidation`
- `08_dropdowns.zsh` — `--selecttitle`, `--selectvalues`, `--selectdefault`, modificadores (obrigatórios, botão de opção, pesquisáveis, seleção múltipla, nome), separadores
- `09_checkboxes.zsh` — `--checkbox` (modificador de nome), `--checkboxstyle` (caixa de seleção, interruptor, tamanhos).
- `10_list_items.zsh` — `--listitem` (status, descrição do status, símbolos personalizados da plataforma), `--liststyle`, `--enablelistselect`, arquivo de comandos (list:, listitem:, adicionar, excluir, índice).
- `11_window_options.zsh` — `--width`, `--height`, `--big`, `--small`, `--position`, `--positionoffset`, `--moveable`, `--ontop`, `--resizable`, `--windowbuttons`, `--appearance`, `--showdockicon`, `--dockiconbadge`
- `12_command_file.zsh` — Descrição completa do arquivo de comandos: título:, fonte do título:, mensagem: (+adicionar), alinhamento:, ícone:, ícone de sobreposição:, transparência do ícone:, texto do botão 1:, botão 1:, texto informativo:, caixa de informações:, ícone: centralizado/esquerda
- `13_notifications.zsh` — `--notification`, `--subtitle`, `--identifier`, `--remove`
- `14_mini_presentation.zsh` — `--mini` (com barra de progresso), `--presentation` (com item de lista, caixa de informações, barra de progresso).
- `15_web_video.zsh` — `--webcontent`, `--video` (atalho do YouTube), `--videocaption`, `--autoplay`
- `16_json_input.zsh` — `--jsonstring`, `--jsonfile`, arrays JSON para caixas de seleção, opções de seleção, campos de texto e imagens
- `17_fullscreen_blur.zsh` — `--fullscreen`, `--blurscreen`, `--hideotherapps`
- `18_misc_features.zsh` — `--helpmessage`, `--infotext`, `--infobox`, `--vieworder`, `--quitkey`, `--sound`, `--showsoundcontrols`, `--displaylog`, `--loghistory`, `--debug`, `--eula`, `--alwaysreturninput`, explicação sobre a chave de autenticação/checksum
- `19_inspect_mode.zsh` — `--inspect-mode`, `--inspect-config`, `--published-sessions-dir`, `stepType: "cadence"`, `cadenceStyle: "carousel"`, frequência IPC (`cadence:satisfy`, `cadence:advance`, `cadence:goto`), redesenho da predefinição 3, logotipo no rodapé, força de ativação `appearance`, `cacheExtensions` com `aria2`
- `20_branched_workflows.zsh` — nível superior; `workflow` matriz; `branch.map`, `branch.default`, `branch.ifTrue`, `branch.ifFalse`, `nextpage`, `finalpage`, com histórico; Anterior

## Executando demonstrações individuais

Cada roteiro de demonstração é independente e completo.

```zsh
./demos/06_progress_timer.zsh
./demos/12_command_file.zsh
```

## Observações

- As demonstrações que utilizam `--blurscreen` ou `--fullscreen` irão, por um breve período, ocupar toda a tela
- As demonstrações de notificações exigem as permissões de notificação para o swiftDialog
- Alguns exemplos de imagens utilizam imagens de fundo do sistema, que podem variar dependendo da versão do macOS
- A demonstração 19 agora se concentra na atualização de inspeção da versão 3.1.0b4, incluindo o carrossel de ritmo, o redesenho compacto da predefinição 3, a publicação de sessões e um exemplo de arquivo JSON para preferências gerenciadas.
- As versões 19 e 20 exigem o **swiftDialog versão 3.1.0b4 ou superior** para suporte a fluxos de trabalho sequenciais e ramificados.
- Consulte as notas de lançamento da versão ](https://github.com/swiftDialog/swiftDialog/releases/tag/v3.1.0b4) swiftDialog v3.1.0b4 para obter informações detalhadas sobre os recursos abordados aqui.