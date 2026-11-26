---
title: Temporizador e barra de progresso
description: Criando diálogos com temporizadores de contagem regressiva e barras de progresso interativas
translationSynced: 2026-11-25T11:29:29+00:00
---

Uma caixa de diálogo pode ser iniciada com um temporizador que será desativado quando o número de segundos especificado tiver se esgotado

`--timer (<seconds>)`


Substitui o botão padrão por um temporizador de contagem regressiva, após o qual a caixa de diálogo será fechada com o código de saída `4`. O valor padrão do temporizador é `10` segundos. Um valor opcional `<seconds>` pode ser especificado para definir o valor desejado. Se `<seconds>` for maior que 60, a contagem regressiva será exibida no formato `HH:MM:SS`, por exemplo, 280 segundos serão exibidos como `4:40` na contagem inicial.

Se usado em conjunto com `--button1text`, o botão padrão será exibido, mas estará desativado durante os primeiros 3 segundos do temporizador. Após esse período, ele se torna ativo e pode ser usado para fechar a janela de diálogo, retornando o código de saída padrão de 0

<img width="727" alt="image" src="https://user-images.githubusercontent.com/3598965/129475759-9ba50127-8366-46a3-8288-780298142f09.png">


`--hidetimerbar` irá ocultar a barra de progresso e o contador regressivo.

Isso garante que o botão padrão seja visível, evitando que apareçam diálogos que não podem ser fechados, sem qualquer indicação de quando o temporizador expira.

---

## Barra de progresso

O Dialog pode exibir uma barra de progresso interativa que pode ser atualizada dinamicamente através do [arquivo de comandos](/pt-br/advanced/command-file).

`--progress [<int>]`

Exibe uma barra de progresso com o número de etapas especificado. Se nenhum valor for fornecido, o padrão é 10 etapas.

Para avançar a barra de progresso, envie um comando para o arquivo de comandos da janela de diálogo:

```sh
echo "progress: <int>" >> /var/tmp/dialog.log
```

`--progresstext <text>`

Define o texto inicial que é exibido abaixo da barra de progresso. O texto pode ser atualizado a qualquer momento:

```sh
echo "progresstext: Installing software..." >> /var/tmp/dialog.log
```

### Alinhamento do texto de progresso

`--progresstextalignment [left | right]`

Define o alinhamento horizontal do texto de progresso exibido abaixo da barra de progresso. O valor padrão é centralizado.