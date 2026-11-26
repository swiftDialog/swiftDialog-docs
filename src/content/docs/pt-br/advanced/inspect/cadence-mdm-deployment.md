---
title: Ritmo de execução controlado em uma implementação de MDM
description: Utilizando o tipo de etapa "cadência com gatilho" para criar uma tela de implantação orientada por atributos, que avança com base no estado real do sistema, sendo adequada para implantações de gerenciamento de dispositivos móveis (MDM) com ferramentas como Fleet, Jamf, Intune e outras.
translationSynced: 2026-11-25T11:41:24+00:00
---

O recurso de "passo com ritmo controlado" transforma uma tela de implantação em uma sequência orientada por **atributos**: cada mensagem é exibida até que uma **condição real** seja satisfeita, momento em que avança. As condições são lidas do estado real do sistema, portanto, a tela nunca indica que a operação foi concluída antes que realmente esteja.

Este sistema é **independente de soluções MDM**. Os dados que ele lê — aplicativos instalados, recibos de pacotes e **preferências gerenciadas via mobileconfig, conforme indicado em `/Library/Managed Preferences/`** — são gerados da mesma forma por **Fleet, Jamf, Intune, Mosyle, Kandji, Munki, Installomator** e outros. Os exemplos abaixo utilizam o **Fleet** como caso de uso, mas nada é específico para o Fleet.

## Como isso se encaixa em um plano de implementação

O MDM realiza as tarefas (instala softwares, configura perfis); o swiftDialog **monitora** esse processo:

| Tarefa de implantação | Atributo Cadence | O que ele diz |
|---|---|---|
| Aplicativo instalado | `app` (`bundleId`) | `NSWorkspace.urlForApplication(withBundleIdentifier:)` |
| Pacote instalado | `file` | recibo em `/var/db/receipts/<pkgid>.bom` |
| **Perfil / arquivo de configuração para dispositivos móveis implementado.** | **`managedpref`** (`domain`+`key`) | `/Library/Managed Preferences/<domain>.plist` (dispositivo) ou `…/<user>/<domain>.plist` |
| Configuração baseada em scripts | `file` | um arquivo de marcador que o script modifica |
| Verificação não observável | `source:"ipc"` | Um script de MDM utiliza `cadence:satisfy:<id>` (osquery, Installomator log, MDM API). |

**Unidade híbrida:** a maioria das entradas faz consulta nativamente (sem orquestrador, funciona off-line / na janela de login); algumas entradas `source:"ipc"` são avançadas por um script MDM para coisas que não podem ser observadas diretamente. O verbo IPC é `cadence:satisfy:<id>` (também `advance` / `goto`).

`timeout` Em caso de falha em uma tarefa, o sistema automaticamente avança para a próxima etapa, garantindo que uma política com problemas não cause o travamento da interface do usuário.

## Duas fases

Como a fase de login/assistente de configuração não possui uma sessão de usuário (sem aplicativos do usuário, apenas configurações gerenciadas no nível do dispositivo), utilize duas configurações, selecionadas por sessão pelo aplicativo de inicialização.

### Fase A – Janela de login / Assistente de configuração (apenas no nível do dispositivo).
```json
{
  "preset": "5", "stepType-note": "device phase",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Setting up your Mac",
    "cadenceInterval": 1.0, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "mdm",      "message": "Confirming management…", "sfSymbol": "checkmark.shield.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.mdm", "key": "AccessRights", "evaluation": "exists", "scope": "device" }, "timeout": 600 },
      { "id": "filevault","message": "Enabling disk encryption…", "sfSymbol": "lock.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.MCX.FileVault2", "key": "Enable", "evaluation": "equals", "expectedValue": "On", "scope": "device" }, "timeout": 900 },
      { "id": "rosetta",  "message": "Installing base packages…", "sfSymbol": "shippingbox.fill",
        "attribute": { "type": "file", "path": "/var/db/receipts/com.company.baseline.bom" }, "timeout": 900 }
    ]
  }]
}
```

### Fase B – área de trabalho após o login (sinais completos).
```json
{
  "preset": "5",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Installing your apps",
    "cadenceInterval": 0.5, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "edge",    "message": "Installing Microsoft Edge…", "sfSymbol": "globe",
        "attribute": { "type": "app", "bundleId": "com.microsoft.edgemac" }, "timeout": 600 },
      { "id": "office",  "message": "Installing Office…", "sfSymbol": "doc.fill",
        "attribute": { "type": "app", "bundleId": "com.microsoft.Word" }, "timeout": 1200 },
      { "id": "vpn",     "message": "Applying VPN profile…", "sfSymbol": "network",
        "attribute": { "type": "managedpref", "domain": "com.company.vpn", "key": "Enabled", "evaluation": "boolean", "expectedValue": "true", "scope": "device" }, "timeout": 600 },
      { "id": "compliance","message": "Running compliance check…", "sfSymbol": "checkmark.seal.fill",
        "attribute": { "source": "ipc" }, "timeout": 600 }
    ]
  }]
}
```
A entrada `compliance` é `source:"ipc"`: um script de MDM executa a verificação (usando osquery ou uma API do fornecedor) e, em seguida, `… ipc send "cadence:satisfy:compliance"`.

## A implementação (exemplo do Fleet: a mesma estrutura se aplica a qualquer solução MDM).
1. **Pacote:** swiftDialog + o programa de inicialização + ambos os arquivos JSON do Cadence.
2. **Perfil (mobileconfig):** Configuração do lançador: quais configurações são aplicadas por sessão e quais flags são usadas na tela de login.
   (O aplicativo de inicialização lê suas próprias preferências gerenciadas da mesma forma — sob `/Library/Managed Preferences/`.)
3. **LaunchAgents** (dispositivo + janela de login) para iniciar o swiftDialog na sessão correta.
4. **GitOps / políticas:** Os perfis e o software que os "gates" do Cadence controlam, além do pequeno script que...
   emite `cadence:satisfy` para qualquer `source:"ipc"` registro.

Gere os arquivos de configuração para dispositivos móveis (mobileconfig) e os artefatos do GitOps utilizando as ferramentas `contour`/`fleet-gitops`, que validam o perfil de acordo com o esquema da Apple.

## Branding e informações personalizadas para cada usuário, com base nas preferências gerenciadas

Para implantações em ambientes multi-inquilinos, as informações sobre as **configurações de faturamento** e a **cor da marca/tonalidade** podem ser lidas a partir de uma configuração gerenciada, em vez de serem codificadas diretamente, permitindo que cada perfil MDM de cada inquilino forneça seus próprios valores, sem alterar a configuração padrão. Ambos utilizam um `ManagedValueRef`:

| Chave | Tipo | Descrição |
|---|---|---|
| `domain` | String | Domínio de preferências gerenciadas, por exemplo: `nl.root3.support` |
| `key` | String | Um parâmetro fundamental dentro desse domínio é o valor de luminosidade das cores. |
| `darkKey` | String | Tecla opcional para ativar o modo escuro (apenas cores). |

- `cadenceRef` — lê o conjunto de configurações de cadência (os `CadenceEntry` dicionários) a partir de uma preferência gerenciada, em vez de um `cadence` array inline.
- `brandColorRef` — lê a cor da marca/tinta (clara, com a opção de escura) a partir de uma configuração pré-definida.

```json
{
  "cadenceRef":    { "domain": "nl.root3.support", "key": "claims" },
  "brandColorRef": { "domain": "nl.root3.support", "key": "brandColor", "darkKey": "brandColorDark" }
}
```

Como os valores são obtidos a partir de `/Library/Managed Preferences/<domain>.plist`, eles seguem o mesmo comportamento de "atualização imediata assim que o perfil é carregado" que os atributos `managedpref` mencionados acima.

<!-- REVIEW: cadenceRef / brandColorRef are documented as top-level keys (alongside the inline `cadence` array). Confirm this matches how they're consumed for all presets. -->

## Observações
- `managedpref` Ele lê o arquivo diretamente, então avança assim que o perfil é carregado (sem atraso)
  Latência do cache de preferências do sistema. `evaluation:"exists"` = "perfil presente"; `equals`/`boolean` = "um valor específico está sendo aplicado".
- Na fase da janela de login, apenas o escopo do dispositivo é aplicável; as preferências gerenciadas no escopo do usuário e as `app` verificações não são aplicadas
  Pertence à Fase B.
- Retornando a uma sequência finalizada (Voltar), as **reproduções rápidas** em `cadenceMinDwell` começam e são interrompidas
  Não tente prender ou pendurar.
