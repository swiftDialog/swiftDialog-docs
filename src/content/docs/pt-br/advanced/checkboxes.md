---
title: Caixas de seleção
description: Criando caixas de seleção e botões de alternância interativos no swiftDialog
translationSynced: 2026-11-25T11:18:55+00:00
---

Caixas de seleção podem ser utilizadas para oferecer diversas opções que podem ser selecionadas ou não, e então processadas.

## Uso básico

Especifique um ou mais parâmetros `--checkbox <text>` e a janela de diálogo exibirá uma caixa de seleção com `<text>` como rótulo.

### Estilo

As caixas de seleção também podem ser exibidas como um botão de alternância, em vez de uma caixa de seleção tradicional.

Por padrão, a opção aparece como uma caixa de seleção ao lado do rótulo:

![image](https://user-images.githubusercontent.com/3598965/235893894-1d4c26ba-1afc-4e9f-a58d-16a36c27787f.png)

Use a opção `--checkboxstyle switch` para alterar o estilo do interruptor:

![image](https://user-images.githubusercontent.com/3598965/235894156-c8cf82e7-d627-43a4-b11e-3acfc296a3e2.png)

Se você preferir um estilo de interruptor maior, pode especificar isso como uma propriedade no estilo do interruptor:

As opções são `mini`, `small`, `regular` ou `large`

`--checkboxstyle switch,large`

![image](https://user-images.githubusercontent.com/3598965/235894351-71200445-5871-4e27-b792-2a983a34514c.png)
## Uso avançado

Ao usar a configuração [JSON](/pt-br/advanced/json-configuration) para definir as opções do diálogo, parâmetros de caixas de seleção opcionais ficam disponíveis.

O formato do arquivo JSON é o seguinte:

```json
{
  "checkbox" : [
	  {"label" : "<label>", "checked" : false, "disabled" : false, "icon" : "<file|url>" }
	],
 "checkboxstyle" : {
    "style" : "switch",
    "size"  : "regular"
	}
}
```

`"checked" : [true|false]` - Inicializará a caixa de seleção no estado "marcado" se estiver definida como `true`. O padrão é "desmarcada".

`"disabled" : [true|false]` - desabilitará a caixa de seleção, independentemente de seu estado (marcada ou desmarcada), caso seja definida para `true`

`"icon" : "<file|url>"` - Está disponível como um parâmetro JSON quando `checkboxstyle` é definido como `switch`; caso contrário, será ignorado

<img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-16aa041aeeca8ffc.png" width=400>

### Configuração JSON para argumentos

A partir da versão 3.1.1, as caixas de seleção também podem ser especificadas como objetos JSON através de `--checkbox` (em vez de usar o JSON de configuração completo). Isso oferece um controle mais direto e é especialmente útil para configurações complexas.

**Sintaxe:**
```bash
dialog --checkbox '{"label":"Enable telemetry","checked":true,"enableButton1":true}'
```

**Características:**
- `label` - O texto do rótulo da caixa de seleção
- `checked` - Estado inicial (verdadeiro/falso, padrão: falso).
- `disabled` - Indica se a caixa de seleção está desabilitada (verdadeiro/falso, padrão: falso).
- `enableButton1` - Ativar o Botão 1 quando esta caixa de seleção estiver marcada (verdadeiro/falso).
- `icon` - Caminho para o ícone ou objeto de ícone no formato JSON (utilizado apenas com o estilo `switch`).

**Exemplos:**

```bash
# Basic checkbox
dialog --checkbox '{"label":"I agree to terms"}'

# Checked by default
dialog --checkbox '{"label":"Enable notifications","checked":true}'

# Checkbox that enables Button 1
dialog --checkbox '{"label":"I understand","enableButton1":true}' --button1disabled

# Checkbox with icon (switch style)
dialog --checkbox '{"label":"Enable feature","checked":true,"icon":"/System/Library/CoreServices/Software Update.app"}' --checkboxstyle switch

# Checkbox with JSON icon object
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}' --checkboxstyle switch
```

**Observação:** Ao utilizar `enableButton1`, também defina `--button1disabled` para impedir que o usuário clique no botão antes de marcar a caixa.

### Configuração JSON completa

A forma JSON de configuração completa ainda é suportada:

```json
{
  "checkbox" : [
    {"label" : "Option 1", "checked" : true, "disabled" : true },
    {"label" : "Option 2", "checked" : true, "disabled" : false },
    {"label" : "Option 3", "checked" : false }
  ],
  "checkboxstyle" : {
    "style" : "switch",
    "size" : "large"
  }
}
```

### exemplo

O seguinte exemplo em formato JSON e a captura de tela do diálogo ilustram como essas configurações funcionam:

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true, "disabled" : false },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5" },
	  {"label" : "Option 6", "disabled" : true }
	]
}
```

![image](https://user-images.githubusercontent.com/3598965/150663608-6ee03207-0558-4769-a016-44fe5822fccb.png)

## Utilizando uma caixa de seleção para controlar o estado do botão1

Você pode usar uma caixa de seleção para controlar o estado do botão padrão. Isso é útil se você quiser garantir que o usuário tenha selecionado uma opção obrigatória antes de prosseguir.

Exemplo:

`dialog --checkbox "I Agree",enableButton1 --button1disabled`

<img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/5a4d2ce4-ea37-447d-86d1-a12ca9d4807e"> <img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/ec12eb71-b6f9-466e-ad32-cb8812bc759c">

Isso também pode ser configurado usando JSON:

```json
{
  "checkbox" : [
    {"label" : "I Agree", "enableButton1" : true }
  ],
  "button1disabled" : true
}
```

 > É importante definir o botão1 como desabilitado inicialmente, caso contrário, o usuário poderá clicar no botão antes que a caixa de seleção seja marcada. Isso não é definido por padrão. Também é importante ressaltar que definir a propriedade `disabled` e `enablebutton1` em uma caixa de seleção não é recomendado, pois isso tornará a caixa de seleção inacessível

## Saída

Os resultados são enviados para a saída padrão (stdout) e, por padrão, aparecem da seguinte forma:
```
Option 1 : true
Option 2 : true
Option 3 : false
Option 4 : true
Option 5 : false
Option 6 : false
```

Opcionalmente, você pode especificar o parâmetro `--json` e obter os resultados em formato JSON:

```json
{
  "Option 2" : true,
  "Option 4" : true,
  "Option 5" : false,
  "Option 6" : true,
  "Option 1" : true,
  "Option 3" : false
}
```