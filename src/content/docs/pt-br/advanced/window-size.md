---
title: Tamanho e comportamento da janela
description: Controlando o posicionamento, o tamanho e a aparência visual da janela de diálogo
translationSynced: 2026-11-25T11:31:48+00:00
---

O comportamento padrão da janela de diálogo é ser posicionada no centro da tela e não pode ser movida. Outras janelas podem ser colocadas sobre ela. É possível alterar esse comportamento utilizando as seguintes opções de linha de comando.

Ambas as opções podem ser utilizadas de forma independente, sem depender uma da outra.

## Visibilidade da janela

`-p` ou `--ontop`

Use esta opção para forçar a janela de diálogo a permanecer sempre no topo.

## Posição da janela

`-o` ou `--moveable`

Use esta opção para permitir que a janela seja arrastada pela tela.

`--position [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]`

Posiciona a janela de diálogo na localização especificada na tela

`--positionoffset <num>`

Define o deslocamento da borda da janela (a distância entre as bordas da tela e a janela).

`--position <x>,<y>`

Posiciona a janela de diálogo nas coordenadas x,y fornecidas, por exemplo: `--position 100,200`

**Observações:**
 - A posição 0,0 corresponde ao canto superior esquerdo da área visível da tela
 - A área visível da tela não inclui a área ocupada pela barra de aplicativos ou pela barra de menu. Por exemplo, se a barra de aplicativos estiver posicionada no lado esquerdo da tela, o ponto de origem será deslocado para dentro.


## Tamanho da janela

Você pode alterar o tamanho para que ele seja maior ou menor do que o padrão, dependendo da quantidade de informações que você deseja incluir na sua mensagem, ou para exibir tamanhos diferentes em telas de diferentes dimensões. As imagens são redimensionadas de acordo. O tamanho da fonte do texto permanece o mesmo.

`-b` ou `--big`

Isso faz com que a janela pareça cerca de 25% maior do que o normal, aumentando a área visível onde os ícones são exibidos

![image](https://user-images.githubusercontent.com/3598965/184131775-9ec40570-8e70-47ba-aecd-5561f6b6f54d.png)

`-s` ou `--small`

Isso faz com que a janela pareça cerca de 25% menor do que o normal

![image](https://user-images.githubusercontent.com/3598965/184131853-94255fc7-b040-4b64-812b-bbe7e9bf412b.png)

## Aparência da janela

É possível forçar o uso do modo claro ou do modo escuro, e o sistema utilizará essa configuração, independentemente da preferência atual do usuário

`--appearance dark` ou `--appearance light`

## Modo compacto

O modo "mini" é ativado passando o argumento `--mini`.

O modo mini força a exibição em uma janela pequena, com um layout modificado e opções limitadas para a exibição de conteúdo. `--title` é menor e centralizado na parte superior da janela, ou pode ser desativado com `--title none`. `--message` pode ter até quatro linhas de texto (qualquer texto mais longo será truncado). `--icon`, quando visível, ocupa a parte esquerda da janela, e todo o outro conteúdo é exibido à direita. `--hideicon` e `--icon none` são respeitados. `--button1text` e `--button2text` estão disponíveis, mas o botão de informações não.

![image](https://user-images.githubusercontent.com/3598965/184130942-8e0461e3-744d-4e69-89bc-6754cbd92abf.png)

Se o argumento `--progress` for usado, a área do botão é removida e substituída por uma barra de progresso e uma única linha de texto de progresso. Para fechar a janela de diálogo, o comando `quit:` deve ser passado para o arquivo de comandos.

![image](https://user-images.githubusercontent.com/3598965/184131293-efe2e2a3-2a33-42cf-b397-941d053b2693.png)

## `--style` - Configure o estilo de janela predefinido

Altera os valores padrão para modificar a forma como uma janela de diálogo é exibida.

Estilos diferentes de `--mini` não possuem atributos especiais, e a aparência visual pode ser obtida utilizando os diversos parâmetros para definir as propriedades da janela.

`centered`, `alert` e `caution` utilizarão o valor de `--title` e o adicionarão como um título à área de mensagem, e então desabilitarão o título. Isso posiciona o título abaixo do ícone central exibido.

    "mini" é funcionalmente equivalente a "--mini". "centered" define todas as opções para conteúdo centralizado. "alert" cria uma janela de diálogo pré-configurada de 300x300 pixels, com o conteúdo centralizado. "caution" e "warning" são equivalentes a "alert", com o ícone configurado

Exemplo de `dialog --style alert`:

<img width="412" alt="image" src="https://github.com/bartreardon/swiftDialog/assets/3598965/53add8af-3407-4152-b374-486db664b8e9">

Isso é equivalente a digitar:

```bash
dialog --title none --iconsize 80 --message "### An Important Message  \n\nThis contains important message content\n\nPlease read" --messagealignment centre --buttonstyle centre --centreicon --width 300 --height 300
```

## Tamanhos de janelas personalizados

O tamanho da caixa de diálogo pode ser ajustado de acordo com a sua preferência, em vez das opções padrão. `--small` ou `--big`.

`--width` e `--height` podem ser usados para definir o tamanho da janela de diálogo desejado. O conteúdo será redimensionado para se ajustar.

O swiftDialog suporta o uso de `%` como uma função do tamanho atual da tela, por exemplo, `--width 50%` definirá a largura da janela para 50% da resolução atual da tela.

![image](https://user-images.githubusercontent.com/3598965/129476080-a708fe71-c566-4caf-8323-899e5dbdcc2b.png)

## `--blurscreen`

`--blurscreen` irá sobrepor todas as telas com um fundo desfocado e posicionar a janela de diálogo acima de todas as outras janelas. Isso permite tanto uma comunicação mais direcionada quanto fluxos de trabalho nos quais você não deseja que o usuário interaja com outros aplicativos ou com a área de trabalho (por exemplo, durante o processo de integração).


<img src="https://user-images.githubusercontent.com/8291873/229149297-ab060e52-120a-42bc-8a4c-1150b7d80ca2.png" width="500">


### Comportamento do `--ontop` com `--blurscreen` e janelas de diálogo existentes

Se um diálogo existente estiver ativo `--blurscreen`, o uso de `--ontop` fará com que diálogos subsequentes apareçam acima da camada de desfoque. Isso permite executar um diálogo em segundo plano e abrir diálogos adicionais, mantendo-os visíveis. É importante observar que, se você pretende interagir com esses diálogos por meio de programação, certifique-se de usar arquivos de comando exclusivos para cada um.

## `--showonallscreens`

Quando utilizado, a janela de diálogo será exibida em todas as áreas de trabalho virtuais

Se vários monitores estiverem em uso, a janela de diálogo aparecerá em todas as áreas de trabalho virtuais associadas ao monitor em que foi iniciada.