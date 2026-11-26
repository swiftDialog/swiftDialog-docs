---
title: Modo construtor
description: Edite as propriedades e a aparência de uma janela de diálogo e exiba os resultados em um arquivo de configuração JSON
translationSynced: 2026-11-25T11:40:31+00:00
---


## Kit de construção swiftDialog

Para ativar, execute `dialog --builder`. Ao ser chamado, uma janela adicional é exibida, permitindo que você atualize o conteúdo e as propriedades do diálogo e veja os resultados em tempo real.

Você pode então exportar o resultado como **JSON** ou como um comando de linha de comando `dialog` pronto para ser executado, permitindo recriar o diálogo exatamente como você o projetou.

**OBSERVAÇÃO: Este recurso não cobre 100% de todas as funcionalidades do swiftDialog, e algumas configurações podem não estar disponíveis ou não aparecer no resultado gerado. O desenvolvimento está em andamento.**

<img width="500" alt="image" src="/builder/builder_main.png" />

<div className="not-content" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin: 2rem 0; align-items: flex-start;">

<div style="align-self: flex-start;">

### Básico
 - [Título](/pt-br/builder/title/)
 - [Mensagem](/pt-br/builder/message/)
 - [Ícone](/pt-br/builder/icon/)
 - [Barra lateral](/pt-br/builder/sidebar/)
 - [Janela](/pt-br/builder/window/)
 - [Botões](/pt-br/builder/buttons/)

</div>

<div style="align-self: flex-start;">

### Avançado
 - [Caixas de seleção](/pt-br/builder/checkboxes/)
 - [Imagens](/pt-br/builder/images/)
 - [Itens da lista](/pt-br/builder/listitems/)
 - [Mídia](/pt-br/builder/media/)
 - [Campos de Texto](/pt-br/builder/textfields/)

</div>

</div>

### Saída

A visualização de **Saída** mostra o design atual, seja no formato **JSON** ou como um comando de **linha de comando** – alterne entre eles usando a aba. A partir daí, você pode **copiar para a área de transferência** ou **salvar o arquivo**. O botão **Comando de Exportação**, localizado no rodapé, copia o comando de linha de comando de qualquer parte do editor.