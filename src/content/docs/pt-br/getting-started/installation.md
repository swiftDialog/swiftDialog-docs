---
title: Instalação
description: Como instalar o swiftDialog no macOS
translationSynced: 2026-11-25T10:40:24+00:00
---

## Métodos de instalação

### Instalador de Pacotes (Recomendado)

A maneira mais fácil de instalar o swiftDialog é utilizando o instalador **.pkg** disponível na página de [lançamentos](https://github.com/swiftDialog/swiftDialog/releases).

O instalador irá colocar o swiftDialog em `/usr/local/bin/dialog`, que deve estar localizado no diretório padrão `$PATH` no macOS.

### Instalação manual

Se você preferir realizar a instalação manualmente:

1. Baixe a versão mais recente na [página de lançamentos](https://github.com/swiftDialog/swiftDialog/releases)
2. Extraia o arquivo binário
3. Copie para `/usr/local/bin/dialog` ou para outro local no seu `$PATH`
4. Certifique-se de que o arquivo binário tenha permissões de execução: `chmod +x /usr/local/bin/dialog`

### Instalação via Homebrew

Em breve – A fórmula do Homebrew está em desenvolvimento.

## Verificação

Após a instalação, verifique se o swiftDialog está funcionando corretamente:

```bash
dialog --version
```

Ou teste com um diálogo simples:

```bash
dialog --title "Test" --message "swiftDialog is installed!"
```

## Atualização do swiftDialog

Para atualizar o swiftDialog, basta baixar e instalar a versão mais recente. O instalador substituirá a versão existente.

É possível verificar se há atualizações de forma programática utilizando:

```bash
dialog --checkupdates
```

## Desinstalação

Para remover o swiftDialog:

```bash
sudo rm /usr/local/bin/dialog
```

## Implantação via MDM (Gerenciamento de Dispositivos Móveis)

O swiftDialog pode ser implementado por meio de soluções de gerenciamento de dispositivos móveis (MDM), como Jamf Pro, Mosyle ou Iru. Basta instalar o pacote .pkg nos dispositivos gerenciados.

### Exemplo de Política Jamf

1. Faça o upload do arquivo .pkg do swiftDialog para o Jamf Pro
2. Crie uma política para implementar o pacote
3. Adapte o dispositivo às suas necessidades
4. Definir gatilho (check-in, recorrente, autoatendimento, etc.)