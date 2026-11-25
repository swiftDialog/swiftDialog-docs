---
title: 示例 Jamf 脚本
description: Jamf Pro 脚本的基本模板，用于显示带有参数的对话框
translationSynced: 2026-11-25T05:43:37+00:00
---

## 基础脚本

此脚本可以添加到您的 Jamf Pro 环境中，并用作一个通用脚本，用于调用基本的对话框。

### 参数

 - 参数 4：标题。
 - 参数 5：消息。
 - 参数 6：图标。
 - 参数 7：叠加。
 - 参数 8：按钮 1 的文本。
 - 参数 9：按钮 2 的文本。
 - 参数 10：信息按钮的文本。
 - 参数 11：附加信息。 可以是以下选项中的**任何一个**：
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