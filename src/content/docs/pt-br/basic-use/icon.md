---
title: Personalizando o ícone
description: Aprenda como configurar e personalizar ícones, imagens e sobreposições no swiftDialog
translationSynced: 2026-11-25T10:52:11+00:00
---

##### Índice
 - [Uso básico](#uso-basico)
 - [Uso um pouco mais avançado](#uso-um-pouco-mais-avancado)
 - [Ícones integrados](#construido-com-icones)
 - [Utilizando os símbolos SF](#utilizando-os-simbolos-sf)
 - [Sobreposições de ícones](#sobreposicoes-de-icones)
 - [Tamanho do Ícone](#tamanho-do-icone)
 - [Ocultando o Ícone](#ocultando-o-icone)
 - [Definir ícones com cores escuras ou claras](#definir-icones-com-cores-escuras-ou-claras)

***


Utilize a opção de linha de comando `-i` ou `--icon` para especificar qual ícone ou imagem você deseja exibir na área do título do ícone.

### Uso:

`--icon <file | url | text= >`


## Uso básico

O swiftDialog aceita imagens nos formatos `png` e `jpg` e exibe a imagem especificada na área de exibição do ícone.

As imagens serão redimensionadas para se ajustarem à área de exibição, que possui 170 pontos de largura por 260 pontos de altura.

`png` é a opção preferida; no entanto, se `jpg` for especificado, as imagens serão exibidas com cantos ligeiramente arredondados, proporcionando uma aparência mais suave.

<img src="https://user-images.githubusercontent.com/3598965/111853793-912e3880-8970-11eb-852f-3d5f7e5d2119.png" width=450>

## Uso um pouco mais avançado
O swiftDialog aceitará o caminho para um aplicativo e utilizará o ícone desse aplicativo como imagem.

e.g. `--icon /Applications/Safari.app`

<img src="https://user-images.githubusercontent.com/3598965/111853901-e36f5980-8970-11eb-80e2-c3fca298627d.png" width=450>

O swiftDialog também aceita uma URL que aponta para um recurso de imagem.

e.g. `--icon "https://user-images.githubusercontent.com/3598965/111854068-84f6ab00-8971-11eb-935b-487f1a15b91f.png"`

<img src="https://user-images.githubusercontent.com/3598965/111854089-a5bf0080-8971-11eb-95fe-a720206bb10a.png" width=450>

## Configuração de transparência do ícone

Use `--iconalpha` para definir um valor de transparência.

A escala varia de `0.0` (totalmente transparente) a `1.0` (totalmente opaco).

## Ícone alternativo (modo escuro).

Use `:dark=` e especifique um ícone alternativo ou um caminho a ser utilizado caso a interface do usuário esteja no modo escuro.

e.g. `--icon /path/to/light.png:dark=/path/to/dark.png`

## Construído com ícones

O swiftDialog possui vários ícones integrados que podem ser utilizados com a opção `--icon`

`--icon info`

![Ícone de Informação](https://user-images.githubusercontent.com/3598965/111854259-5e853f80-8972-11eb-9476-e2c5ceed3da9.png)

`--icon caution`

![Ícone de Atenção](https://user-images.githubusercontent.com/3598965/111854239-46adbb80-8972-11eb-9708-e864a71e3e0a.png)

`--icon warning`

![Ícone de aviso](https://user-images.githubusercontent.com/3598965/111854248-52997d80-8972-11eb-9f11-52a0b8a8d650.png)

`--icon computer`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/2ee4c788-bc9a-4328-ac1b-1537bf30dcb7">

## Utilizando `text=`

Você também pode usar o `text=` prefixo para exibir texto na área do ícone. Isso é útil para exibir um único caractere ou emoji.

e.g. `--icon text=👍`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/931fa9f5-0f96-4b32-bf6e-cffa28c26e31">


## Utilizando os Símbolos SF

O swiftDialog também pode exibir qualquer símbolo do SF Symbols. https://developer.apple.com/sf-symbols/

### Sintaxe dos Símbolos SF (formato CSV)

Ao especificar símbolos SF para ícones ou ícones de sobreposição, parâmetros adicionais para cor e espessura estão disponíveis:

  `"SF=sf.symbol.name,colour=<text><hex>,weight=<text>"`

  `color,colour=<text><hex>` Especificado em formato hexadecimal, por exemplo, #00A4C7. Também aceita qualquer uma das cores padrão da Apple: `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Se a opção for inválida, a cor padrão será a cor do sistema `primary`

Cor especial. `"auto"`

Quando utilizado com um símbolo SF multicolorido, o esquema de cores padrão do símbolo será aplicado. Se utilizado com um símbolo SF monocromático, a cor padrão será preto e o modo escuro não será respeitado.

e.g. `dialog -s -i SF=airplane.circle.fill,colour=auto`

![image](https://user-images.githubusercontent.com/3598965/126090330-8dc612a9-40f9-99e2-caf41d07903e.png)

Os gradientes de cores podem ser definidos adicionando o argumento adicional `colour2` ou `color2`, por exemplo: `SF=applelogo,colour=pink,colour2=purple`

![image](https://user-images.githubusercontent.com/3598965/170815055-e943c2a4-e846-44d5-b323-bb8be1333438.png)

Os símbolos SF multicoloridos podem ser coloridos usando o argumento `palette`, por exemplo: `SF=person.3.sequence.fill,palette=red,green,blue`

![image](https://user-images.githubusercontent.com/3598965/171398294-0a74dcad-b5b2-4dd0-b5b2-4dd0-b320-c65d5d5e8d22.png)

O peso do símbolo SF pode ser definido com o argumento `weight`

   `weight=<text>` aceita qualquer um dos seguintes valores:
    * `thin` (padrão)
    * `light`
    * `regular`
    * `medium`
    * `heavy`
    * `bold`

### Símbolos SF animados

O suporte para símbolos SF animados está disponível no macOS 14 ou versões mais recentes.

Exemplo de uso:

`--icon sf=rainbow,colour=auto,animation=variable`

No momento, o suporte é limitado para os seguintes tipos de animação:
 - `variable`
 - `variable.reversing`
 - `variable.iterative`
 - `variable.iterative.reversing`
 - `variable.cumulative`
 - `pulse`
 - `pulse.bylayer`

### Objetos de ícones JSON

Os ícones também podem ser especificados como objetos JSON para um controle mais preciso. Isso é especialmente útil para configurações de ícones complexas, que envolvem múltiplas propriedades.

**Sintaxe:**
```bash
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'
```

**Chaves suportadas:**
- `sf` / `name` / `symbol` - Nome do símbolo SF
- `path` / `icon` / `value` - Caminho do arquivo para a imagem ou aplicativo
- `weight` - Peso do símbolo (`thin`, `light`, `regular`, `medium`, `heavy`, `bold`).
- `colour` / `color` - Cor primária (código hexadecimal ou nome).
- `colour2` / `color2` - Cor secundária para gradientes
- `palette` - Conjunto de cores para símbolos multicoloridos
- `animation` - Tipo de animação para símbolos animados (macOS 14 ou superior).
- `bgcolour` / `bgcolor` - Cor de fundo para os ícones sobrepostos
- `auto` - Valor especial para o esquema de cores automático
- `light` / `dark` - Variações de modo claro/escuro (objeto de ícone aninhado).

**Exemplos:**

```bash
# Basic symbol with colour and weight
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'

# Gradient
dialog --icon '{"sf":"applelogo","colour":"pink","colour2":"purple"}'

# Multicolor palette
dialog --icon '{"sf":"person.3.sequence.fill","palette":["red","green","blue"]}'

# Application icon
dialog --icon '{"path":"/Applications/Chess.app"}'

# Light/dark variants
dialog --icon '{"light":{"sf":"sun.max"},"dark":{"sf":"moon"}}'

# Animated symbol (macOS 14+)
dialog --icon '{"sf":"rainbow","colour":"auto","animation":"variable"}'

# Overlay icon with background
dialog --overlayicon '{"sf":"exclamationmark","colour":"yellow","bgcolour":"none"}'
```

Funciona em: `--icon`, `--overlayicon`, `--listitem` (campo de ícone), `--checkbox` (campo de ícone)

**Observação:** Quando usado nos campos `--listitem` ou `--checkbox`, o campo "ícone" aceita objetos JSON aninhados:

```bash
dialog --listitem '{"title":"Download","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}'
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}'
```



## Sobreposições de ícones

Utilize a opção de linha de comando `-y` ou `--overlayicon ` para especificar qual ícone ou imagem você deseja usar como sobreposição para o ícone principal.

As sobreposições são exibidas com metade da resolução normal e deslocadas para o canto inferior direito da área de exibição dos ícones principais. Ao usar essa opção, você pode combinar imagens para visualização

Os ícones sobrepostos utilizam os mesmos tipos de imagem e as mesmas localizações que o parâmetro `--icon`, incluindo os ícones padrão e os símbolos da SF


Exemplo:

`--icon caution --overlayicon /Applications/Safari.app`

`-i caution -y /Applications/Safari.app`

![ícone de aviso com sobreposição do ícone do Safari](https://user-images.githubusercontent.com/3598965/111854381-16b2e800-8973-11eb-9cf9-c2b1d8d8b6b7.png)

Exemplo 2:

`--icon /Applications/Google\ Chrome.app --overlayicon warning`

`-i /Applications/Google\ Chrome.app -y warning`

![Ícone do Chrome com uma sobreposição de aviso](https://user-images.githubusercontent.com/3598965/111888622-2e9d7100-8a32-11eb-9693-e53bb2f42692.png)

### Aplique um fundo transparente ao usar os símbolos SF

Ao usar os símbolos SF, um quadrado arredondado ligeiramente transparente é adicionado para destacar o símbolo em relação ao ícone principal, pois muitos símbolos contêm elementos que não funcionam bem como uma sobreposição.

![image](https://user-images.githubusercontent.com/3598965/173157681-0dd05429-35db-4872-89a1-8a8e42bf44a4.png)

A aparência do fundo pode ser ajustada com um modificador `bgcolor=` e utiliza a mesma sintaxe em todos os lugares onde `color` pode ser definido. Também é possível especificar uma cor especial `bgcolor=none` caso não seja desejado o fundo sobreposto.

![image](https://user-images.githubusercontent.com/3598965/173157715-46fda24b-2cfb-417b-835a-ed452888546d.png)

## Tamanho do ícone

`--iconsize <float>` Redimensionará o ícone para a largura especificada. A largura padrão é `170`

Exemplo 1:

`--icon caution --overlayicon /Applications/Safari.app --iconsize 300`

![image](https://user-images.githubusercontent.com/3598965/137573508-a2eb2dfc-cf46-4009-8783-66d8e2040724.png)


Exemplo 2:

`--icon /Applications/Firefox.app --iconsize 100 -s`

![image](https://user-images.githubusercontent.com/3598965/137573587-0e11823b-dc12-4756-ab4c-8442c4d5f050.png)

## Posição do ícone

`--centreicon` ou `--centericon`

Altera a posição do ícone para que fique centralizado

![image](https://user-images.githubusercontent.com/3598965/159693524-551b863d-33db-4af0-b971-a9a08161d525.png)

Também é possível alterar essa configuração utilizando um arquivo de comandos enquanto o swiftDialog está em execução

`echo "icon: centre" >> /var/tmp/dialog.log`

## Ocultar o ícone

O ícone pode ser removido completamente usando um dos seguintes comandos:

`--hideicon`

ou

`--icon none`

## Definir ícones com cores escuras ou claras, dependendo se a interface do usuário está no modo escuro ou no modo claro

Exceto para alguns símbolos da biblioteca SF Symbols, o swiftDialog não possui nenhuma funcionalidade integrada para alternar entre ícones do modo claro e do modo escuro.

É possível definir o ícone com base nas configurações da interface do usuário, embora isso possa ser feito no script que faz a chamada.

**zsh / bash** (obrigado a [mm2270](https://github.com/mm2270)).

```bash
#!/bin/zsh

icon_path_dark="/path/to/icondark.png"
icon_path_lite="/path/to/iconlite.png"

logged_in_user=$(/usr/sbin/scutil <<< "show State:/Users/ConsoleUser" | /usr/bin/awk '/Name :/ && ! /loginwindow/ {print $3}')

os_color_mode=$(/usr/bin/defaults read /Users/$logged_in_user/Library/Preferences/.GlobalPreferences.plist AppleInterfaceStyle)

if [ "$os_color_mode" = "Dark" ]; then
	icon_path=$icon_path_dark
else
	icon_path=$icon_path_lite
fi
```

ou em Python (obrigado a [joncrain](https://github.com/joncrain)).

```python
from Foundation import NSBundle

def is_dark_mode():
    appearanceBundle = NSBundle.bundleWithPath_(
        "/System/Library/PreferencePanes/Appearance.prefPane"
    )
    appearanceShared = appearanceBundle.classNamed_("AppearanceShared")
    app = appearanceShared.sharedAppearanceAccess()
    if app.theme() == 1:
        return False
    else:
        return True

if is_dark_mode():
    content["icon"] = "dark_icon.png"
else:
    content["icon"] = "light_icon.png"
```