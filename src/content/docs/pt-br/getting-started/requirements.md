---
title: Requisitos do sistema
description: Requisitos de versão do macOS e compatibilidade para o swiftDialog
translationSynced: 2026-11-25T10:40:18+00:00
---

## Requisitos do macOS

swiftDialog é um aplicativo binário universal desenvolvido utilizando o SwiftUI.

### 3.0+
- **Versão mínima do macOS:** macOS 15 (Sonoma).
- **Arquitetura**: Binário Universal (Intel e Apple Silicon).
- **Framework:** SwiftUI

### 2.3+
- **Versão mínima do macOS:** macOS 12 (Monterey).

### Versões Antigas
- A última versão que oferece suporte ao **macOS 11 (Big Sur)** é a [v2.2.1](https://github.com/swiftDialog/swiftDialog/releases/tag/v2.2.1)


## Dependências

O swiftDialog é um aplicativo independente que não possui dependências externas. Ele inclui todos os frameworks necessários dentro do pacote do aplicativo.

## Permissões

O swiftDialog pode exigir determinadas permissões, dependendo do uso.

### Operação básica
- Não são necessárias permissões especiais para exibir diálogos básicos

### Recursos avançados
- **Notificações**: O usuário deve conceder permissão para que o sistema envie notificações
- **Acesso Completo ao Disco:** Pode ser necessário se for preciso ler ou gravar dados em áreas protegidas

## Requisitos de rede

- **Funcionamento offline:** O swiftDialog funciona completamente offline
- **Operações Online:**
  - Verificando se há atualizações
  - Exibição de conteúdo web
  - Download de imagens remotas

