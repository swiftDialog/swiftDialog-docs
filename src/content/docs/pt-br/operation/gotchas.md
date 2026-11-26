---
title: Observações importantes
description: Problemas comuns e dicas de solução de problemas para o swiftDialog
translationSynced: 2026-11-25T11:53:48+00:00
---

# Problemas com arquivos de comando

## Permissões insuficientes

Se você iniciar o programa swiftDialog e o arquivo de comando não puder ser gravado, você receberá uma mensagem de erro:

```bash
ERROR: Existing file at /var/tmp/dialog.log but couldn't clean.
ERROR: Error info: Error Domain=NSCocoaErrorDomain Code=513 "You don't have permission to save the file "dialog.log" in the folder "tmp"." UserInfo={NSFilePath=/var/tmp/dialog.log, NSUnderlyingError=0x60000320f660 {Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied"}}
```

O arquivo de comando deve ser removido ou, alternativamente, as permissões devem ser alteradas para `-rw-rw-rw` (666).

---

# Mudanças no comportamento do swiftDialog versão 3.1.1

## `--alwaysreturninput` Retornos aplicáveis a todos os caminhos de saída

**O que mudou:** A partir da versão 3.1.1, `--alwaysreturninput` retorna resultados em formato de seleção, lista ou JSON em **todos** os caminhos de saída, e não apenas quando um botão é pressionado.

**Caminhos de saída afetados:**
- Arquivo de comando para sair
- Tempo limite do temporizador
- Tecla para sair
- Processo encerrado

**Migração:** Scripts que dependem do comportamento antigo (que só retornava ao pressionar um botão) podem apresentar novos resultados. Revise sua lógica de processamento se você utiliza `--alwaysreturninput`.

## `--ontop` Respeita a posição do cais

**O que mudou:** A opção `--ontop` agora respeita a posição da barra de aplicativos e posiciona a janela de diálogo dentro da área visível da tela (e não sobre a barra de aplicativos).

**Impacto:** As janelas de diálogo não cobrirão mais a barra de ancoragem quando `--ontop` for utilizado. Isso desfaz uma decisão intencional tomada em uma versão anterior.

## Modificadores para o Seletor de Datas

**O que mudou:** O modificador `isdate` foi **descontinuado** em favor de `date` e `time`.

**Migração:** Atualize seus scripts:

```bash
# Old (deprecated)
dialog --textfield "Start Date,isdate"

# New
dialog --textfield "Start Date,date"
```

---

# Problemas Comuns

## Opções repetíveis como argumento final

**Problema:** As opções repetíveis (`--selectvalues`, `--selecttitle`, `--textfield`, `--checkbox`, `--image`, `--listitem`, `--icon`, `--imagecaption`) utilizadas como o último argumento poderiam causar uma falha no sistema.

**Status:** Corrigido na versão 3.1.1

## O seletor de datas não retorna nenhum valor

**Problema:** O uso de `--textfield ...,isdate` não retornava nenhum valor porque era uma estrutura de suporte que nunca retornava valores.

**Status:** Corrigido na versão 3.1.1. Utilize os modificadores `date` ou `time` em vez disso.

## Legenda da imagem não está funcionando

**Problema:** O arquivo de comando `imagecaption:` não teve efeito porque ele apenas escrevia em `appvars.imageCaptionArray` (consumido uma vez na inicialização) em vez de `observedData.imageArray` (fonte reativa).

**Status:** Corrigido na versão 3.1.1

## Os cabeçalhos de grupo predefinidos estão sendo exibidos incorretamente

**Problema:** Os títulos dos grupos de implantação ("Concluído", "Instalação pendente") estão sendo exibidos na posição incorreta ou duplicados.

**Status:** Corrigido na versão 3.1.1

## A barra de botões do teclado não está funcionando

**Problema:** `--hidedefaultkeyboardaction` não estava funcionando devido a uma regressão na reescrita da barra de botões.

**Status:** Corrigido na versão 3.1.1