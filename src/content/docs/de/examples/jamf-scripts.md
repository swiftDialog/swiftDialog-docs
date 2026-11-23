---
title: Beispielhafte Jamf-Skripte
description: Grundlegende Jamf Pro-Skriptvorlage zum Anzeigen von Dialogfenstern mit Parametern
translationSynced: 2026-11-23T00:09:00+00:00
---

## Grundlegendes Skript

Dieses Skript kann in Ihre Jamf Pro-Instanz integriert und als generisches Skript verwendet werden, um grundlegende Dialogfenster aufzurufen

### Parameter

 - Parameter 4: Titel
 - Parameter 5: Nachricht
 - Parameter 6: Symbol
 - Parameter 7: Überlagerung
 - Parameter 8: Text für Schaltfläche 1
 - Parameter 9: Text für Schaltfläche 2
 - Parameter 10: Text für den Info-Button
 - Parameter 11: Zusätzliche Informationen. Kann einer der folgenden Werte sein:
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