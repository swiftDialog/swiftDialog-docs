---
title: Fluxo de trabalho do swiftDialog
description: Fluxos de diálogo com múltiplas etapas no swiftDialog
translationSynced: 2026-11-25T11:37:50+00:00
---

> **OBSERVAÇÃO**: O recurso de "Fluxo de Trabalho" (Workflow) foi introduzido na versão 3.1 do swiftDialog.

# Documentação do recurso de fluxo de trabalho do swiftDialog

## Visão geral

A funcionalidade **Fluxo de Trabalho** permite criar fluxos de diálogo com várias etapas no swiftDialog, possibilitando a criação de interfaces de usuário semelhantes a assistentes, que guiam os usuários por meio de várias telas de entrada e informações. Cada cartão representa uma tela separada, com sua própria configuração, e os usuários podem navegar para frente e para trás dentro do fluxo de trabalho.

Os fluxos de trabalho são definidos usando arquivos de configuração em formato JSON, o que facilita a criação de diálogos complexos e com várias etapas, sem a necessidade de escrever código.

## Características principais

- **Fluxos de trabalho em várias etapas:** Divida diálogos complexos em etapas gerenciáveis
- **Controles de navegação:** Botões "Próximo", "Anterior" e "Concluir" com funcionamento automático
- **Ramificação condicional:** Direcione o fluxo para diferentes etapas de trabalho com base na seleção de um menu suspenso ou no estado de uma caixa de seleção, sem a necessidade de scripts de retorno
- **Persistência de dados:** As informações inseridas pelo usuário são mantidas ao navegar entre os diferentes painéis de fluxo de trabalho
- **Configurações globais:** Defina configurações padrão uma única vez e personalize-as individualmente para cada cartão
- Substituição de variáveis: Valores de referência de etapas anteriores do fluxo de trabalho, utilizando a sintaxe `{fieldname}`
- **Validação:** Validação obrigatória dos campos antes de prosseguir
- **Configuração dinâmica:** Cada cartão pode ter elementos de interface do usuário e configurações exclusivas
- **Chamadas de retorno (Callbacks)**: Execute scripts do shell ao navegar entre os painéis do fluxo de trabalho

## Conceitos básicos

### Estrutura do fluxo de trabalho

Um diálogo baseado em fluxo de trabalho é definido em um arquivo de configuração JSON com a seguinte estrutura:

```json
{
  "workflow": [
    { "title": "Step 1", "message": "First screen..." },
    { "title": "Step 2", "message": "Second screen..." },
    { "title": "Step 3", "message": "Final screen..." }
  ]
}
```

### Configuração Global

As propriedades definidas no nível raiz (fora do `workflow` array) servem como valores padrão para todos os cards de fluxo de trabalho. Os cards de fluxo de trabalho individuais podem substituir esses valores padrão:

```json
{
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertNoteIcon.icns",
  "button1text": "Continue",
  "workflow": [
    { "title": "Step 1", "message": "Uses default icon" },
    { "title": "Step 2", "icon": "SF=checkmark.circle", "message": "Custom icon" }
  ]
}
```

### Identificação por cartão

Os cartões são automaticamente ordenados de acordo com sua posição no array. Você pode, opcionalmente, especificar um critério de ordenação explícito `id` para uma organização personalizada:

```json
{
  "workflow": [
    { "id": 0, "title": "First" },
    { "id": 10, "title": "Second" },
    { "id": 5, "title": "Third (will be displayed second)" }
  ]
}
```

## Navegação

### Comportamento do botão

No modo de fluxo de trabalho, o comportamento do botão é alterado automaticamente:

- **Botão 1** (lado direito):
  - Exibe a palavra "Próximo" nos cartões de fluxo de trabalho de 1 a n-1
  - Exibe a palavra "Finalizar" no último cartão (ou texto personalizado através de `button1text`).
  - Valida os campos obrigatórios antes de prosseguir
  
- **Botão 2** (lado esquerdo):
  - Escondido no primeiro cartão
  - Exibe o botão "Anterior" nos cartões de fluxo de trabalho do 2 ao n
  - Não há validação ao navegar para trás

### Personalização do texto dos botões

Por padrão, os botões de navegação exibem as opções "Próximo", "Anterior" e "Finalizar". Para alterar essas opções:

- `--nextbuttontext "<text>"` — Texto para o botão "Próximo" (padrão: `Next`).
- `--previousbuttontext "<text>"` — Texto para o botão "Anterior" (padrão: `Previous`).
- `button1text` (nível superior ou por cartão) — texto para o botão de **Finalizar**

```bash
dialog --jsonfile config.json --nextbuttontext "Continue" --previousbuttontext "Back"
```

### Fluxo de navegação

<img width="650" alt="image" src="/images/navigation-flow.png" />


## Navegação por ramificação

Por padrão, os cards de fluxo de trabalho são exibidos na ordem do array. Você pode alterar essa ordem usando três propriedades opcionais, configuráveis individualmente para cada card:

| Propriedade | Tipo | Objetivo |
|---|---|---|
| `branch` | objeto | Escolha a próxima carta com base em um valor específico presente na carta atual |
| `nextpage` | inteiro | Substituição estática — vá para este cartão `id` após o próximo |
| `finalpage` | booleano | Este cartão encerra o fluxo de trabalho; o próximo passo se torna "Finalizar" |

Quando o usuário clica em "Avançar", o componente swiftDialog resolve o destino na seguinte ordem:

1. `branch` (se definido e uma regra correspondente for encontrada).
2. `nextpage` (se definido).
3. A próxima carta na sequência
4. Fim do fluxo de trabalho (se não existir uma próxima etapa, ou se `finalpage` for verdadeiro).

O botão "Anterior" é inteligente e leva o usuário de volta à tela de onde ele realmente veio, e não simplesmente à tela anterior na ordem sequencial. Isso funciona corretamente, mesmo em diferentes seções do aplicativo.

> O swiftDialog não verifica a existência de loops ou elementos que não podem ser acessados. Se o seu fluxo de trabalho puder retornar a etapas anteriores, o usuário simplesmente revisitará esses elementos. Se isso não for intencional, revise a lógica do fluxo de trabalho para corrigir o problema.

### Derivando de um menu suspenso

O valor `branch.field` corresponde ao valor do campo `name` (preferencialmente) ou ao seu `title`/`label`. Para um menu suspenso, o valor selecionado é comparado com as chaves em `branch.map`:

```json
{
  "workflow": [
    {
      "id": 1,
      "title": "Choose your path",
      "message": "Pick an option to control which card appears next.",
      "selectitems": [
        {
          "name": "userType",
          "title": "Account type",
          "values": ["Admin", "Standard", "Guest"],
          "default": "Standard"
        }
      ],
      "branch": {
        "field": "userType",
        "map": {
          "Admin":    10,
          "Standard": 20,
          "Guest":    30
        },
        "default": 99
      }
    },
    { "id": 10, "title": "Admin setup", "nextpage": 99 },
    { "id": 20, "title": "Standard setup", "nextpage": 99 },
    { "id": 30, "title": "Guest setup", "nextpage": 99 },
    { "id": 99, "title": "Summary", "finalpage": true }
  ]
}
```

`branch.default` é opcional. Se definido, e o valor selecionado não estiver presente em `map`, o fluxo de trabalho avança para o cartão de fallback especificado.

### Derivando de uma caixa de seleção

Para um campo booleano, utilize a forma abreviada `ifTrue` / `ifFalse` em vez de `map`:

```json
{
  "id": 5,
  "checkbox": [
    { "name": "wantsExtras", "label": "Show advanced options" }
  ],
  "branch": {
    "field": "wantsExtras",
    "ifTrue":  6,
    "ifFalse": 99
  }
}
```

Você também pode usar `map` com as teclas `"true"` e `"false"`, se preferir, mas `ifTrue`/`ifFalse` é mais fácil de entender.

### Substituição Estática `nextpage`

Se você não precisa de roteamento dinâmico, mas deseja que um cartão avance para a próxima etapa, defina `nextpage`:

```json
{ "id": 3, "title": "Optional details", "nextpage": 10 }
```

### Finalizando o fluxo de trabalho antecipadamente

Marque qualquer cartão como "final" para interromper o fluxo de trabalho naquele ponto:

```json
{ "id": 99, "title": "Summary", "finalpage": true }
```

Em um último cartão, o botão 1 exibe a palavra "Concluir" e fecha a janela de diálogo quando clicado, independentemente de quantos outros cartões de fluxo de trabalho existam no conjunto.

## Exemplos de uso

### Exemplo 1: Assistente simples com três etapas

```json
{
  "title": "Setup Wizard",
  "icon": "SF=gearshape.2",
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to the setup wizard. Click Continue to begin."
    },
    {
      "title": "Enter Information",
      "message": "Please provide your details:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email Address", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Setup is complete! Click Finish to close this wizard.",
      "button1text": "Finish"
    }
  ]
}
```

Execute-o:
```bash
dialog --jsonfile /path/to/config.json
```

### Exemplo 2: Utilizando substituição de variáveis

A substituição de variáveis permite que você faça referência a valores de etapas anteriores do fluxo de trabalho, utilizando a sintaxe `{fieldname}`:

```json
{
  "title": "User Registration",
  "workflow": [
    {
      "title": "Personal Information",
      "message": "Step 1: Enter your details",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true }
      ]
    },
    {
      "title": "Confirmation",
      "message": "Hello {First Name} {Last Name}! Please confirm your information is correct.",
      "infobox": "**Name:** {First Name} {Last Name}"
    }
  ]
}
```

Os espaços reservados `{First Name}` e `{Last Name}` no Cartão 2 serão substituídos pelos valores inseridos no Cartão 1.

### Exemplo 3: Configurações Globais com Substituições

```json
{
  "icon": "SF=info.circle",
  "width": 600,
  "height": 400,
  "workflow": [
    {
      "title": "Introduction",
      "message": "This card uses the default icon and size."
    },
    {
      "title": "Custom Layout",
      "icon": "SF=wrench.and.screwdriver",
      "width": 800,
      "height": 500,
      "message": "This card has a custom icon and larger size."
    },
    {
      "title": "Back to Normal",
      "message": "This card reverts to default icon and size."
    }
  ]
}
```

### Exemplo 4: Coleta de dados em várias etapas

```json
{
  "title": "System Configuration",
  "icon": "/System/Library/PreferencePanes/Appearance.prefPane/Contents/Resources/AppIcon.icns",
  "workflow": [
    {
      "title": "Network Settings",
      "message": "Configure network preferences:",
      "selectitems": [
        {
          "title": "Network Type",
          "values": ["WiFi", "Ethernet", "VPN"],
          "default": "WiFi"
        }
      ]
    },
    {
      "title": "User Preferences",
      "message": "Set user preferences:",
      "checkbox": [
        { "label": "Enable notifications", "checked": true },
        { "label": "Auto-update", "checked": true },
        { "label": "Send analytics", "checked": false }
      ]
    },
    {
      "title": "Summary",
      "message": "Review your settings:",
      "infobox": "**Network:** {Network Type}\\n\\n**Notifications:** {Enable notifications}\\n**Auto-update:** {Auto-update}\\n**Analytics:** {Send analytics}"
    }
  ]
}
```

### Exemplo 5: Indicador de progresso com cartões

```json
{
  "title": "Installation Wizard",
  "workflow": [
    {
      "title": "Preparing (1 of 3)",
      "message": "Preparing installation...",
      "progress": 100,
      "progresstext": "Checking system requirements"
    },
    {
      "title": "Installing (2 of 3)",
      "message": "Installing software...",
      "progress": 100,
      "progresstext": "Copying files"
    },
    {
      "title": "Complete (3 of 3)",
      "message": "Installation complete!",
      "icon": "SF=checkmark.circle.fill",
      "progress": 100,
      "progresstext": "Finished"
    }
  ]
}
```

### Exemplo 6: Validação de campos obrigatórios

```json
{
  "title": "Registration Form",
  "workflow": [
    {
      "title": "Account Details",
      "message": "All fields marked with * are required",
      "textfield": [
        { "title": "Username", "required": true, "prompt": "Enter username" },
        { "title": "Password", "required": true, "secure": true },
        { "title": "Confirm Password", "required": true, "secure": true }
      ]
    },
    {
      "title": "Contact Information",
      "message": "Please provide at least one contact method",
      "textfield": [
        { "title": "Email", "required": true },
        { "title": "Phone", "required": false }
      ]
    }
  ]
}
```

Se os usuários tentarem clicar em "Avançar" sem preencher os campos obrigatórios, uma mensagem de erro será exibida.

## Recursos avançados

### Propriedades específicas do fluxo de trabalho

Qualquer propriedade padrão do swiftDialog pode ser utilizada em um fluxo de trabalho. As propriedades mais comuns incluem:

- **Layout**: `width`, `height`, `position`
- **Conteúdo:** `title`, `message`, `icon`, `iconsize`
- **Entrada:** `textfield`, `selectitems`, `checkbox`, `radio`
- **Exibição**: `image`, `video`, `webcontent`, `listitem`
- **Progresso**: `progress`, `progresstext`
- **Informações**: `infobox`, `helpmessage`
- **Estilo**: `messagefont`, `alignment`, `bannerimage`
- **Navegação**: `branch`, `nextpage`, `finalpage` (veja [Navegação Hierárquica](#navegação-por-ramificação)]).

### Nomenclatura dos campos de entrada

Para que a substituição de variáveis funcione corretamente, os campos de entrada devem ter nomes consistentes:

```json
{
  "textfield": [
    { "title": "First Name" }  // Referenced as {First Name}
  ],
  "selectitems": [
    { "title": "Department", "values": ["IT", "HR", "Sales"] }  // Referenced as {Department}
  ]
}
```

Se um campo não tiver uma especificação explícita `title`, você pode usar uma propriedade `name`:

```json
{
  "textfield": [
    { "title": "Your Name", "name": "username" }  // Referenced as {username}
  ]
}
```

### Persistência de dados

As entradas do usuário são salvas automaticamente quando:
- Clique em "Próximo" para avançar para o próximo cartão
- Clique em "Anterior" para voltar

Quando os usuários retornam a um cartão anterior, os dados que eles inseriram são restaurados.

### Acesso aos dados do cartão

Quando o usuário clica em "Concluir" no último cartão, todos os dados coletados são exibidos na saída padrão (stdout) em formato JSON:

```json
{
  "First Name": "John",
  "Last Name": "Doe",
  "Email Address": "john.doe@example.com",
  "Department": "IT",
  "Enable notifications": true
}
```

### Chamadas de retorno sobre pagamentos antecipados

Use a opção `--onadvance` para executar um comando de shell ao navegar entre os painéis de fluxo de trabalho:

```bash
dialog --jsonfile config.json --onadvance "/path/to/script.sh"
```

O script recebe:
- Índice de cartão (baseado em zero).
- Identificação do cartão (se aplicável).
- Recebimento de dados do cartão no formato JSON através da entrada padrão (stdin)

O script deve ser encerrado com:
- **Código de saída 0:** Permite a progressão
- **Código de saída diferente de zero:** Interrompe o processo e exibe uma mensagem de erro

Exemplo de script de callback:
```bash
#!/bin/bash
# script.sh - Validate email format before advancing

input=$(cat)
email=$(echo "$input" | jq -r '.["Email Address"]')

if [[ ! "$email" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$ ]]; then
    echo "Invalid email address format"
    exit 1
fi

exit 0
```

## Melhores práticas

### 1. Mantenha os fluxos de trabalho focados
Cada cartão deve ter um único e claro objetivo. Não sobrecarregue os usuários com muitos campos em um único cartão.

### 2. Utilize títulos descritivos
Os títulos dos cards devem indicar claramente em qual etapa o usuário está.
```json
{ "title": "Step 1: Personal Information" }
{ "title": "Step 2: Contact Details" }
{ "title": "Step 3: Review & Confirm" }
```

### 3. Fornecer o contexto
Utilize o campo de mensagem para explicar o que o usuário precisa fazer:
```json
{
  "title": "Account Setup",
  "message": "Create your account by choosing a username and password. Your username must be at least 6 characters."
}
```

### 4. Utilize a validação de campos obrigatórios
Marque os campos obrigatórios para garantir a integridade dos dados:
```json
{ "title": "Email", "required": true }
```

### 5. Fornecer cartões de resumo
Inclua um cartão de revisão final que mostre todas as informações coletadas:
```json
{
  "title": "Review Your Information",
  "message": "Please verify everything is correct before proceeding.",
  "infobox": "**Name:** {Full Name}\\n**Email:** {Email}\\n**Department:** {Department}"
}
```

### 6. Considere o fluxo de navegação
- Não faça com que o primeiro cartão exija muitas informações – facilite a experiência dos usuários
- Coloque a coleta dos dados mais importantes no início
- Salve a confirmação/visualização para a tela final do cartão

### 7. Utilize uma formatação consistente
Defina configurações padrão globais para garantir uma aparência consistente.
```json
{
  "icon": "SF=person.crop.circle",
  "width": 700,
  "height": 450,
  "messagefont": "size=13",
  "workflow": [ /* ... */ ]
}
```

## Limitações e Observações

1. **Atualizações de Arquivos de Comando:** Ao utilizar o modo de fluxo de trabalho com um arquivo de comando, algumas atualizações dinâmicas podem não funcionar como esperado. O modo de fluxo de trabalho é projetado para a coleta de informações, e não para atualizações dinâmicas de status.

2. **Personalização de Botões:** O comportamento dos botões 1 e 2 é controlado pelo modo de fluxo de trabalho e não pode ser totalmente personalizado enquanto estiver nesse modo.

3. **Códigos de Saída:** No modo de fluxo de trabalho, a caixa de diálogo só é fechada quando:
   - O usuário clica em "Concluir" no último cartão (código de saída 0).
   - Usuário cancelou (o código de saída varia).
   - A validação falha e o usuário opta por cancelar a operação

4. **Escopo das Variáveis**: As variáveis de cartões de fluxo de trabalho anteriores estão disponíveis apenas em cartões subsequentes, e não em cartões anteriores. A substituição de variáveis é unidirecional.

5. **Nome dos Campos:** Para uma substituição correta das variáveis, utilize caracteres alfanuméricos e espaços nos títulos dos campos. Caracteres especiais podem causar problemas.

## Solução de problemas

### Cartões não aparecendo
- Verifique a sintaxe do JSON com `jsonlint` ou uma ferramenta similar
- Certifique-se de que o `workflow` array esteja no nível raiz
- Verifique se pelo menos um cartão está definido

### Variáveis que não foram substituídas
- Certifique-se de que os nomes dos campos correspondam exatamente (distinguindo entre letras maiúsculas e minúsculas).
- Verifique se as referências a variáveis utilizam chaves: `{fieldname}`
- Verifique se o campo referenciado estava presente em um cartão anterior, e não no cartão atual ou em um cartão futuro

### Validação não está funcionando
- Verifique se os campos estão configurados corretamente. `"required": true`
- Verifique se o campo possui uma propriedade com valor `title` ou `name`
- Analise os logs de depuração com a flag `--debug`

### Botão "Anterior" não está sendo exibido
- Verifique se você não está no primeiro cartão do fluxo de trabalho (o botão "Anterior" fica oculto no primeiro cartão).
- Verifique se o modo de fluxo de trabalho está realmente habilitado (se o array de fluxo de trabalho existe).

### A transação foi direcionada para o cartão incorreto
- Confira se `branch.field` corresponde ao `name` do campo (ou ao seu `title`/`label` se nenhum nome estiver definido)
- Para menus suspensos, as chaves utilizadas para a correspondência são comparadas com o valor selecionado pelo usuário, levando em consideração a capitalização e os espaços em branco
- Para caixas de seleção, prefira as chaves de mapeamento `ifTrue`/`ifFalse` em vez de `"true"`/`"false"`
- Verifique o registro do swiftDialog — alvos inválidos `nextpage` / `branch` são reportados durante a inicialização

## Exemplo completo: Assistente de integração de novos funcionários

```json
{
  "title": "Employee Onboarding",
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/UserIcon.icns",
  "width": 750,
  "height": 500,
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome to the Company!",
      "message": "## Welcome Aboard!\\n\\nThis wizard will guide you through the onboarding process.\\n\\nClick Continue to get started.",
      "icon": "SF=hands.clap.fill",
      "iconsize": 120
    },
    {
      "title": "Personal Information",
      "message": "Please provide your personal details (all fields required):",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true },
        { "title": "Employee ID", "required": true },
        { "title": "Work Email", "required": true, "prompt": "name@company.com" }
      ]
    },
    {
      "title": "Department Assignment",
      "message": "Select your department and role:",
      "selectitems": [
        {
          "title": "Department",
          "values": ["Engineering", "Marketing", "Sales", "HR", "Finance"],
          "default": "Engineering"
        },
        {
          "title": "Role",
          "values": ["Manager", "Senior", "Mid-level", "Junior"],
          "default": "Mid-level"
        }
      ]
    },
    {
      "title": "System Preferences",
      "message": "Configure your system preferences:",
      "checkbox": [
        { "label": "Enable email notifications", "checked": true },
        { "label": "Join company Slack", "checked": true },
        { "label": "Subscribe to company newsletter", "checked": true },
        { "label": "Opt-in to mentorship program", "checked": false }
      ]
    },
    {
      "title": "Review & Confirm",
      "message": "Please review your information before completing the onboarding process:",
      "icon": "SF=checkmark.circle",
      "infobox": "**Name:** {First Name} {Last Name}\\n**Employee ID:** {Employee ID}\\n**Email:** {Work Email}\\n\\n**Department:** {Department}\\n**Role:** {Role}\\n\\n**Email Notifications:** {Enable email notifications}\\n**Slack:** {Join company Slack}\\n**Newsletter:** {Subscribe to company newsletter}\\n**Mentorship:** {Opt-in to mentorship program}",
      "button1text": "Complete Onboarding"
    }
  ]
}
```

Salve isto como `onboarding.json` e execute.
```bash
dialog --jsonfile onboarding.json
```

## Exemplo de integração: Script Shell

Aqui está um exemplo completo de um script de shell que utiliza o modo de fluxo de trabalho e processa a saída:

```bash
#!/bin/bash

# onboarding.sh - Employee onboarding with swiftDialog workflow

DIALOG="/usr/local/bin/dialog"
CONFIG="/tmp/onboarding_config.json"

# Create the JSON configuration
cat > "$CONFIG" << 'EOF'
{
  "title": "Employee Onboarding",
  "icon": "SF=person.crop.circle.badge.checkmark",
  "width": 700,
  "height": 450,
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to Company XYZ! This wizard will set up your account."
    },
    {
      "title": "Enter Details",
      "message": "Please provide your information:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Onboarding complete for {Full Name}!",
      "infobox": "We'll send a confirmation to {Email}"
    }
  ]
}
EOF

# Run dialog and capture output
if output=$("$DIALOG" --jsonfile "$CONFIG" 2>&1); then
    echo "Onboarding completed successfully!"
    echo "Collected data:"
    echo "$output" | jq .
    
    # Extract specific fields
    full_name=$(echo "$output" | jq -r '.["Full Name"]')
    email=$(echo "$output" | jq -r '.Email')
    
    echo "Processing onboarding for $full_name ($email)..."
    
    # Add your custom logic here
    # - Create user account
    # - Send welcome email
    # - Configure systems
    
else
    echo "Onboarding was cancelled or failed"
    exit 1
fi

# Cleanup
rm -f "$CONFIG"
```

## Resumo

A funcionalidade "Fluxo de Trabalho" (Workflow) no swiftDialog oferece uma forma poderosa de criar interfaces com múltiplos passos, semelhantes a assistentes, utilizando uma configuração simples em JSON. Os principais benefícios incluem:

- **Simplificação de fluxos de trabalho complexos:** Divida processos complicados em etapas gerenciáveis
- **Navegação integrada** - Botões "Próximo", "Anterior" e "Concluir" automáticos
- **Coleta de dados** – Colete e valide facilmente as informações fornecidas pelos usuários em diversas telas
- **Configuração flexível** - Utilize configurações padrão globais e opções de personalização específicas para cada fluxo de trabalho
- **Substituição de variáveis** - Utilize valores de etapas anteriores do fluxo de trabalho em etapas subsequentes
- **Não é necessário conhecimento de programação** – Configure tudo em formato JSON

Para obter mais informações sobre as opções e parâmetros individuais do swiftDialog, consulte a documentação principal do swiftDialog ou utilize `dialog --help`.
