---
title: Modo Construtor - Botões
description: Edite as propriedades e a aparência de uma janela de diálogo e exporte os resultados como um arquivo de configuração JSON
translationSynced: 2026-11-25T11:44:51+00:00
---

Permite definir as propriedades da área do botão

<img width="500" alt="image" src="/builder/builder buttons.png" />

#### Tamanho do botão

Defina um dos quatro tamanhos de botão (afeta todos os botões).

 - miniatura
 - pequeno(a)
 - padrão (normal)
 - grande

#### Botão 1

Define o texto a ser exibido no Botão 1, também conhecido como botão padrão

Padrão `"OK"`

A configuração "Desabilitado" define o estado do botão 1 como desativado (e pode ser reativado por meio de um comando no arquivo de configuração `button1: enable`).

#### Botão 2

Defina o texto que será exibido no Botão 2

Padrão `"Cancel"`

#### Botão de Informação

Defina o texto que será exibido no botão de informações

Ative a opção "Sair ao clicar em 'Informações'" para que a janela de diálogo se feche quando o botão de informações for clicado

Defina a ação do botão "Informações" para que ele abra um URL específico quando for clicado.

#### Símbolo

Os botões 1, Botão 2 e o botão "Informações" podem exibir um símbolo SF ao lado de seus respectivos rótulos. O editor de símbolos expõe as propriedades do símbolo como controles individuais:

 - Nome do símbolo SF
 - **Posição** — líder, vice-líder, primeiro ou último lugar
 - **Modo de renderização:** hierárquico, monocromático, multicolorido ou com paleta de cores
 - **Cor:** Uma única cor, ou 2 a 3 cores da paleta, quando o modo de renderização da paleta é selecionado
 - Tamanho personalizado

Uma visualização em tempo real do símbolo criado é exibida, e o botão na visualização da caixa de diálogo é atualizado à medida que você edita.

[Voltar](/pt-br/builder/builder/)