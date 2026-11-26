---
title: Exemplos de scripts Jamf
description: Modelo básico de script para o Jamf Pro para exibir caixas de diálogo com parâmetros
translationSynced: 2026-11-25T11:47:33+00:00
---

## Roteiro básico

Este script pode ser adicionado à sua instância do Jamf Pro e usado como um script genérico para exibir caixas de diálogo básicas

### Parâmetros

 - Parâmetro 4: Título
 - Parâmetro 5: Mensagem
 - Parâmetro 6: Ícone
 - Parâmetro 7: Sobreposição
 - Parâmetro 8: Texto do Botão 1
 - Parâmetro 9: Texto do Botão 2
 - Parâmetro 10: Texto do botão "Informações"
 - Parâmetro 11: Adicional. Pode ser **um** dos seguintes:
    - `--moveable`
    - `--ontop`
    - `--big`
    - `--small`
    - `--ignorednd`


```bash
#!/bin/zsh

dialog="/usr/local/bin/dialog"

if [[ -n ${4} ]]; then titleoption="--title"; title="${4}"; fi
if [[ -n ${5} ]]; then messageoption="--message"; message="${5}"; fi
if [[ -n ${6} ]]; then iconoption="--icon"; icon="${6}"; fi
if [[ -n ${7} ]]; then overlayoption="--overlayicon"; overlayicon="${7}"; fi
if [[ -n ${8} ]]; then button1option="--button1text"; button1text="${8}"; fi
if [[ -n ${9} ]]; then button2option="--button2text"; button2text="${9}"; fi
if [[ -n ${10} ]]; then infobuttonoption="--infobuttontext"; infobuttontext="${10}"; fi
extraflag=${11}

${dialog} \
    ${titleoption} "${title}" \
    ${messageoption} "${message}" \
    ${iconoption} "${icon}" \
    ${overlayoption} "${overlayicon}" \
    ${button1option} "${button1text}" \
    ${button2option} "${button2text}" \
    ${infobuttonoption} "${infobuttontext}" \
    ${extraflag}

returncode=$?

case ${returncode} in
    0)  echo "Pressed Button 1"
        ## Process exit code 0 scenario here
        ;;

    2)  echo "Pressed Button 2"
        ## Process exit code 2 scenario here
        ;;

    3)  echo "Pressed Button 3"
        ## Process exit code 3 scenario here
        ;;

    *)  echo "Something else happened. exit code ${returncode}"
        ## Catch all processing
        ;;
esac

# make sure script exits cleanly otherwise Self Service will complain if it's anything other than 0
exit 0
```