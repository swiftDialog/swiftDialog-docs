---
title: Jamf スクリプトのサンプル例。
description: Jamf Proの基本的なスクリプトテンプレート。パラメータ付きのダイアログを表示する機能を提供します。
translationSynced: 2026-11-23T23:39:11+00:00
---

## 基本的なスクリプト。

このスクリプトは、Jamf Pro 環境に追加して使用でき、基本的なダイアログを表示するための汎用的なスクリプトとして活用できます。

### パラメータ。

 - パラメータ4：タイトル。
 - パラメータ5：メッセージ。
 - パラメータ6: アイコン。
 - パラメータ7：オーバーレイ。
 - パラメータ8：ボタン1のテキスト。
 - パラメータ9：ボタン2のテキスト。
 - パラメータ10：情報ボタンのテキスト。
 - パラメータ11: 追加情報。以下のいずれか**一つ**を指定できます。
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