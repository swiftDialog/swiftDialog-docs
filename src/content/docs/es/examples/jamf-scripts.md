---
title: Ejemplos de scripts de Jamf
description: Plantilla básica de script de Jamf Pro para mostrar cuadros de diálogo con parámetros
translationSynced: 2026-11-24T23:01:50+00:00
---

## Guión básico

Este script se puede añadir a su instancia de Jamf Pro y utilizar como un script genérico para mostrar cuadros de diálogo básicos

### Parámetros

 - Parámetro 4: Título
 - Parámetro 5: Mensaje
 - Parámetro 6: Icono
 - Parámetro 7: Superposición
 - Parámetro 8: Texto del botón 1
 - Parámetro 9: Texto del botón 2
 - Parámetro 10: Texto del botón de información
 - Parámetro 11: Adicional. Puede ser **uno** de los siguientes:
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