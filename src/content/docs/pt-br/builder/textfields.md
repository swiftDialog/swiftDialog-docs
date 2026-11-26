---
title: Modo Construtor - Campos de Texto
description: Edite as propriedades e a aparência de uma janela de diálogo e exporte os resultados como um arquivo de configuração JSON
translationSynced: 2026-11-25T11:46:39+00:00
---

Configure as entradas `--textfield`

<img width="500" alt="image" src="/builder/builder_textfields.png" />

Clique no botão `[+]` para adicionar uma nova entrada

Clique no ícone de lixeira para remover uma entrada

Arraste a barra (☰) localizada à esquerda de uma linha para reorganizar as entradas


<img width="500" alt="image" src="/builder/builder_textfields_popualated.png" />


## Propriedades

As seguintes propriedades podem ser configuradas

#### Formate a saída como JSON

Define o formato de saída. Essa propriedade é compartilhada com [caixas de seleção](/pt-br/builder/checkboxes/)

#### Obrigatório

Define a flag `required`.

#### Confirmar

Define a `confirm` flag. Ao ativar essa opção, um campo de texto duplicado será exibido para a entrada configurada

#### Selecionar arquivo

Habilita o botão `fileselect`

##### Tipo de arquivo

Utilize com `fileselect`. Insira o tipo de arquivo desejado (ou tipos, em formato CSV), por exemplo: `"png,jpg"`

##### Caminho inicial

Utilizado com `fileselect`. Define o caminho inicial a ser utilizado ao exibir a caixa de diálogo de seleção de arquivos

#### Título

Define o título/rótulo do campo de texto

#### Nome

Define o nome do campo de texto. Se utilizado, este valor representará esta entrada na saída, em vez do rótulo

#### Valor padrão

Defina o valor padrão a ser exibido no campo de texto. Esse conteúdo será exibido na saída

#### Prompt

Define um texto de instrução que será exibido no campo de texto. Esse conteúdo não aparecerá no resultado final

#### Expressões regulares

Defina uma expressão regular que o conteúdo do campo de texto deve corresponder

#### Erro de expressão regular

Defina a mensagem de erro que será exibida quando o conteúdo do campo de texto não corresponder à expressão regular fornecida

[Voltar](/pt-br/builder/builder/)