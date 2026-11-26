---
title: Modificando o comportamento do atalho Command+Q
description: Personalizar atalhos de teclado para janelas de saída
translationSynced: 2026-11-25T11:51:26+00:00
---

Na versão 1.10.2 e posteriores do swiftDialog, o comando `--quitkey <char>` irá remapear `command+q` para `command +<char>`

Por exemplo, `--quitkey x` desativará o atalho Command+Q para fechar a caixa de diálogo, mas permitirá `command+x`.

Além disso, se um diálogo for encerrado usando uma ação de comando+<char>, o código de saída será `10`, permitindo que qualquer ação seja executada caso seja detectado.

Os atalhos `command+w`, `command+m` e "command+n" também estão desativados por padrão e não podem ser redefinidos.