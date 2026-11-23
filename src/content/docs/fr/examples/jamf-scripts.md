---
title: Exemples de scripts Jamf
description: Modèle de script Jamf Pro de base pour afficher des boîtes de dialogue avec des paramètres
translationSynced: 2026-11-23T05:32:32+00:00
---

## Script de base

Ce script peut être ajouté à votre instance Jamf Pro et utilisé comme un script générique pour afficher des boîtes de dialogue de base

### Paramètres

 - Paramètre 4 : Titre
 - Paramètre 5 : Message
 - Paramètre 6 : Icône
 - Paramètre 7 : Superposition
 - Paramètre 8 : Texte du bouton 1
 - Paramètre 9 : Texte du bouton 2
 - Paramètre 10 : Texte du bouton "Informations"
 - Paramètre 11 : Informations complémentaires. Peut être **l'un** des éléments suivants :
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