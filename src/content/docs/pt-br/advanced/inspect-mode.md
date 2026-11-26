---
title: Modo de Inspeção
description: "Guia introdutório do modo de inspeção do swiftDialog: monitoramento de instalações e conformidade do sistema"
translationSynced: 2026-11-25T11:37:27+00:00
---


# Modo de Inspeção do swiftDialog

O modo de inspeção do SwiftDialog é um novo recurso integrado que permite o monitoramento em tempo real dentro do sistema de arquivos do macOS. Ele acompanha o status do sistema de arquivos (utilizando a API FSEvents da Apple) enquanto monitora a instalação de aplicativos e examina pastas, arquivos e o conteúdo de arquivos plist, permitindo visualizar verificações de conformidade. Este recurso foi projetado especificamente para uso durante o processo de inscrição de dispositivos, implantação de software e auditoria de conformidade, fornecendo aos usuários finais uma visibilidade clara do seu status de conformidade.

## Visão geral

O modo "Inspeção" monitora continuamente os caminhos de arquivo e diretórios de cache especificados, permitindo acompanhar o status de aplicativos ou componentes do sistema. Ele oferece feedback visual por meio de diversos layouts pré-definidos, cada um otimizado para diferentes casos de uso.


### Características principais
- Monitoramento em tempo real do sistema de arquivos
- Detecção do progresso do download por meio do monitoramento do cache
- Várias opções de configurações visuais para diferentes cenários
- Validação simples baseada em listas (booleano, string e existência).
- Temas e personalização da marca (com limitações).
- Botões que são ativados automaticamente após a conclusão

## Primeiros passos

### Uso básico

1. Crie um arquivo de configuração no formato JSON:
```json
{
  "title": "Application Installation",
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}

```
:::tip[order of items]
Importante: o atributo "guiIndex" deve ser único e define a ordem dos elementos na interface gráfica. Números menores são exibidos primeiro.
:::

2. Inicie o swiftDialog com a opção de inspeção habilitada:
```bash
/usr/local/bin/dialog --inspect-mode --inspect-config /path/to/config.json
```

3. Opcionalmente, defina a variável de ambiente que especifica o caminho para o arquivo de configuração:
```bash
export DIALOG_INSPECT_CONFIG="/path/to/config.json"
/usr/local/bin/dialog --inspect-mode
```

## Referência de Configuração JSON

### Opções gerais de diálogo

O modo de inspeção suporta um novo objeto `options` na configuração JSON para controlar o comportamento geral do diálogo. Isso permite que você defina as propriedades da janela diretamente na configuração de inspeção, sem a necessidade de passar argumentos pela linha de comando.

```json
{
  "options": {
    "moveable": true,
    "ontop": true,
    "resizable": true,
    "windowbuttons": "min,max,close"
  }
}
```

**Opções disponíveis:**
- `moveable` (booleano) - Permite arrastar a janela
- `ontop` (booleano) - Manter a janela sempre visível, acima de todas as outras janelas
- `resizable` (booleano) - Permitir que a janela seja redimensionada (implica `moveable`).
- `windowbuttons` (string) - Habilitar botões da janela: `close`, `min`, `max` (separados por vírgula).

**Prioridade:** As opções fornecidas pela linha de comando têm precedência sobre as opções definidas em formato JSON.

**Opções não suportadas:** Qualquer opção que não esteja na lista de opções permitidas será ignorada, e uma mensagem será registrada.

**Exemplo:**
```json
{
  "title": "Application Installation",
  "options": {
    "moveable": true,
    "ontop": true
  },
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}
```

### Chaves de nível raiz

| Chave | Tipo | Obrigatório | Padrão | Descrição |
|-----|------|----------|---------|-------------|
| `preset` | String | Não | "predefinição1" | Layout visual pré-definido (preset1-7). |
| `title` | String | Não | "Inspeção do sistema" | Título da janela |
| `message` | String | Não | - | Texto principal da mensagem |
| `icon` | String | Não | - | Caminho do ícone ou símbolo SF (por exemplo, "sf=escudo_preenchido"). |
| `size` | String | Não | "padrão" | Tamanho da janela: "compacto", "padrão", "grande" |
| `width` | Inteiro | Não | - | Largura da janela personalizada (substitui o tamanho definido). |
| `height` | Inteiro | Não | - | Altura da janela personalizada (substitui o tamanho definido). |
| `cachePaths` | Matriz | Não | - | Diretórios a serem monitorados para downloads |
| `scanInterval` | Inteiro | Não | 2 | Intervalo de varredura do sistema de arquivos em segundos |
| `button1text` | String | Não | "OK" | Texto do botão principal |
| `button1disabled` | Booleano | Não | falso | Desative o botão principal inicialmente |
| `button2text` | String | Não | "Cancelar" | Texto do botão secundário |
| `button2visible` | Booleano | Não | verdadeiro | Mostrar botão secundário |
| `autoEnableButton` | Booleano | Não | verdadeiro | Botão de ativação automática ao ser concluído |
| `autoEnableButtonText` | String | Não | "OK" | Texto do botão quando a função está habilitada automaticamente |
| `items` | Matriz | Sim | - | Conjunto de itens a serem inspecionados |

### Chaves de personalização visual

| Chave | Tipo | Padrão | Descrição |
|-----|------|---------|-------------|
| `banner` | String | - | Caminho da imagem do banner (substitui o ícone). |
| `bannerHeight` | Inteiro | 100 | Altura do banner em pixels |
| `bannerTitle` | String | - | Título sobreposto na faixa |
| `highlightColor` | String | "#808080" | Cor de destaque (código hexadecimal). |
| `backgroundColor` | String | - | Cor de fundo (código hexadecimal). |
| `backgroundImage` | String | - | Caminho da imagem de fundo |
| `backgroundOpacity` | Duplo | 1.0 | Opacidade do fundo (0-1). |
| `textOverlayColor` | String | - | Cor da sobreposição de texto para fundos |
| `gradientColors` | Matriz | - | Conjunto de códigos de cores hexadecimais para gradiente |
| `iconBasePath` | String | - | Caminho base para os caminhos relativos dos ícones |
| `appearance` | String | "automóvel" | Forçar a exibição da janela de inspeção: `"dark"`, `"light"` ou `"auto"` (seguir as configurações do sistema operacional). Substitui a configuração do sistema operacional em ambos os sentidos. |

### Configuração de itens

Cada item no `items` array requer:

| Chave | Tipo | Obrigatório | Descrição |
|-----|------|----------|-------------|
| `id` | String | Sim | Identificador único |
| `displayName` | String | Sim | Nome de exibição na interface do usuário |
| `guiIndex` | Inteiro | Sim | Ordem de classificação (baseada em zero). |
| `paths` | Matriz | Sim | Caminhos de arquivo a serem verificados para confirmar a existência |
| `icon` | String | Não | Ícone específico do produto |
| `plistKey` | String | Não | Chave PLIST para validação |
| `expectedValue` | String | Não | Valor esperado no arquivo plist |
| `evaluation` | String | Não | Tipo de avaliação: "igual", "booleano", "existe", "contém", "intervalo" |
| `description` | String | Não | Uma descrição opcional é exibida abaixo do título do item (renderizada pelas configurações 1, 2, 3, 5 e 6). |
<!-- | `subtitle` | String | No | Subtitle text (preset6) | --> <!-- | `category` | String | Não | Agrupamento de categorias (predefinição 5) |
| `categoryIcon` | String | Não | Ícone de categoria (predefinição 5). | -->


## Recursos avançados

### Monitoramento de cache

Monitore as pastas de download para detectar instalações em andamento.

```json
{
  "cachePaths": [
    "/Library/Managed Installs/Cache",
    "/Library/Application Support/Installomator/Downloads",
    "/Library/Application Support/JAMF/Downloads", 
    "/Library/Application Support/AirWatch/Data/Munki/Managed Installs/Cache"
  ],
  "scanInterval": 5,
  "cacheExtensions": ["download", "pkg", "dmg", "aria2"]
}
```

Por padrão, arquivos que terminam com `.pkg`, `.dmg` e `.download`, localizados em `cachePaths`, marcam um item correspondente como "*baixando*". Defina `cacheExtensions` para alterar essa lista — por exemplo, adicione `aria2` para que os arquivos parciais `<name>.aria2` do aria2c sejam detectados (problema #617). O ponto no início é opcional.

### Validação de Conformidade com a Lista de Verificação (Plist)

Valide a configuração do sistema utilizando verificações em arquivos plist:

```json
{
  "preset": "preset5",
  "items": [{
    "id": "findmymac",
    "displayName": "Find My Mac Status",
    "guiIndex": 0,
    "paths": ["/Library/Preferences/com.apple.FindMyMac.plist"],
    "plistKey": "FMMEnabled",
    "expectedValue": "true",
    "evaluation": "boolean"
  }]
}
```

### Limiares de cor personalizados

Defina os níveis de conformidade personalizados e as cores correspondentes.

```json
{
  "colorThresholds": {
    "excellent": 0.95,
    "good": 0.80,
    "warning": 0.60,
    "excellentColor": "#00C853",
    "goodColor": "#2196F3",
    "warningColor": "#FF9800",
    "criticalColor": "#F44336"
  }
}
```


### Painéis de Conformidade

Para relatórios de conformidade baseados em arquivos plist, adicione um array de nível superior `plistSources`. O swiftDialog agrega os arquivos plist referenciados em categorias, com contagens de "aprovado/total" e uma pontuação geral, e os exibe através dos blocos de conteúdo `compliance-summary` e `findings-list` (e quaisquer células do tipo "bento"), atualizando-os em intervalos regulares.

```json
{
  "plistSources": [
    {
      "path": "/Library/Preferences/com.company.compliance.plist",
      "type": "compliance",
      "healthyLabel": "Compliant",
      "attentionLabel": "Action Required"
    }
  ],
  "guidance": [
    { "type": "compliance-summary" },
    { "type": "findings-list" }
  ]
}
```

**`plistSources[]` propriedades:**

| Chave | Tipo | Padrão | Descrição |
|-----|------|---------|-------------|
| `path` | String | - | Caminho para o arquivo plist |
| `type` | String | - | Tipo de fonte: `compliance`, `health`, `licenses`, `preferences` ou `custom` |
| `healthyLabel` | String | "Saudável" | Rótulo para uma verificação aprovada<br> (aparece em cartões de resumo, linhas de resultados e subtítulos). |
| `attentionLabel` | String | "Requer atenção" | Etiqueta para um teste com falha |
| `successValues` | Matriz | - | Valores que indicam sucesso |
| `expectedValue` | String | - | Valor esperado para conformidade |
| `findingKey` | String | "encontrar" | Chave de acesso para ler os detalhes do resultado |
| `timestampKey` | String | automóvel; carro | Chave que armazena a data e hora da última verificação (tentativas automáticas `lastComplianceCheck`, `LastUpdateCheck`, `lastCheck`, `timestamp`). |
| `includePattern` | String | - | Expressão regular para definir as chaves a serem incluídas na descoberta automática |
| `excludeKeys` | Matriz | - | Chaves a serem excluídas da descoberta automática |
| `keyMappings` | Matriz | - | Como interpretar chaves específicas em arquivos plist |
| `maxCheckDetails` | Inteiro | 15 | Máximo de itens exibidos por categoria |
| `icon` | String | - | Símbolo SF para a categoria |

**Blocos de conteúdo que exibem os dados agregados:**

- `compliance-summary` — um banner com o status geral, além de cartões estatísticos para cada categoria.
- `findings-list` — Uma lista detalhada de verificações individuais, organizada por categorias e com informações disponíveis.

As células do Bento também se conectam automaticamente aos mesmos dados: o subtítulo e a cor do ícone de uma célula são atualizados em tempo real, sem a necessidade de campos de esquema adicionais. <br>

## Exemplos completos

### Instalador básico de aplicativos

```json
{
  "title": "Installing Office Suite",
  "message": "Please wait while we install your applications",
  "preset": "preset1",
  "icon": "sf=apps.iphone.badge.plus",
  "iconBasePath":"/Users/Shared/icons/",
  "cachePaths": ["/Users/Shared/Downloads"],
  "button1text": "Please Wait...",
  "button1disabled": true,
  "autoEnableButton": true,
  "autoEnableButtonText": "Continue",
  "items": [
    {
      "id": "microsoft_word",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"],
      "icon": "Microsoft Word.png"
    },
    {
      "id": "microsoft_excel",
      "displayName": "Microsoft Excel",
      "guiIndex": 1,
      "paths": ["/Applications/Microsoft Excel.app"],
      "icon": "Microsoft Excel.png"
    },
    {
      "id": "microsoft_powerpoint",
      "displayName": "Microsoft PowerPoint",
      "guiIndex": 2,
      "paths": ["/Applications/Microsoft PowerPoint.app"],
      "icon": "Microsoft PowerPoint.png"
    }
  ]
}
```
:::tip[iconBasePath]
Defina um caminho base para os ícones dos itens, a fim de simplificar a configuração. Os nomes das imagens são carregados a partir de `iconBasePath`, quando disponíveis. Caso contrário, especifique o caminho completo para cada item.
:::


## Solução de problemas

### Configuração não carregada
- Verifique a sintaxe do JSON usando `jq` ou validadores online
- Verifique as permissões do arquivo (deve ser legível).
- Certifique-se de que a variável de ambiente seja devidamente exportada

### Itens não detectados
- Verifique os caminhos exatos dos arquivos (sensíveis a maiúsculas e minúsculas).
- Verifique se os caminhos exigem privilégios de administrador
- Use `cachePaths` para detecção de downloads
- Aumente `scanInterval` para sistemas mais lentos

### Modo de depuração
Ativar a saída de depuração:
```bash
/usr/local/bin/dialog --inspect-mode --debug
```

```bash
export DIALOG_DEBUG=1
/usr/local/bin/dialog --inspect-mode
```

### Variáveis de ambiente comuns
- `DIALOG_INSPECT_CONFIG`: Caminho para o arquivo JSON de configuração
- `DIALOG_DEBUG`: Ativar o registro de informações de depuração
- `DIALOG_COMMAND_FILE`: Caminho para o arquivo de comandos personalizado

## Melhores práticas

1. **Comece pelo básico:** Utilize a configuração padrão e mantenha a configuração o mais simples possível
2. **Caminhos de Teste:** Verificar se todos os caminhos de arquivo existem ou existirão
3. **Utilize o monitoramento de cache**: Adicione `cachePaths` para detecção de downloads
4. **Gerenciamento de Ícones**: Armazene os ícones em um local centralizado, com `iconBasePath`
5. **Estados do Botão:** Utilize `autoEnableButton` para uma melhor experiência do usuário
6. **Predefinições Adequadas**: Escolha as predefinições com base no caso de uso:
   - Rastreamento da instalação: Presquisa 1 ou 2 ou 3
   - Display de conformidade: Presquisa 4


