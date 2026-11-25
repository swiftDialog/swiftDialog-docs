---
title: 捕获对话输出
description: 用户输入捕获方法以及对话结果处理方法
translationSynced: 2026-11-25T05:46:14+00:00
---

您可以通过多种方式获取Dialog的输出结果，了解用户执行的操作，或者获取用户输入的数据。

## 返回码

最简单的对话框始终会至少有一个按钮，当用户点击该按钮时，对话框会关闭，并返回一个值为 `0` 的退出码。

这些可选按钮，可以通过`--button2`、`--infobutton`（或其衍生物）触发。当点击这些按钮时，会返回不同的代码：`2`或`3`，具体取决于点击的是哪个按钮。

以下是每次操作完成后返回的错误代码。您可以忽略这些代码，也可以在调用脚本中使用它们，以执行进一步的操作。

| 行动。      | 可选的。 | 快捷键。 | 返回码。 |
| ----------- | -------- | ------ | ----------- |
| `button1`   | 不。       | 进入。  | 0           |
| `button2`   | 是的。      | 退出。    | 2           |
| `infobutton` | 是的。      |        | 3           |
| \<timer\>   | 是的。      |        | 4           |
| 命令文件 `quit:` | 是的。 |    | 5           |
| `--quitkey` | 是的。      | 命令 + Q 键。  | 10          |
| 密钥验证失败。 | 是的。  |        | 30          |
| 图片资源未找到。 | |    | 201         |
| 文件未找到。 |       |        | 202         |


要在您的脚本中处理返回值，只需在 bash 中或通过您选择的脚本语言，捕获来自 `$?` 的结果即可。

例如，在处理返回值代码时：`zsh`

```zsh
#!/bin/zsh
dialog ...<options_here>
case $? in
  0)
  echo "Pressed OK"
  # Button 1 processing here
  ;;
  2)
  echo "Pressed Cancel Button (button 2)"
  # Button 2 processing here
  ;;
  3)
  echo "Pressed Info Button (button 3)"
  # Button 3 processing here
  ;;
  4)
  echo "Timer Expired"
  # Timer ran out code here
  ;;
  5)
  echo "quit: command used"
  # post quit: command code here
  ;;
  10)
  echo "User quit with cmd+q"
  # User quit code here
  ;;
  30)
  echo "Key Authorisation Failed"
  # Key auth failure code here
  ;;
  201)
  echo "Image resource not found"
  ;;
  202)
  echo "Image for icon not found"
  ;;
  *)
  echo "Something else happened"
  ;;
esac
```


## 标准输出

除了返回码之外，如果提供了一个或多个 `--textfield` 或 `--selectvalues`，输出将发送到 `sdtout`。默认输出为非格式化，仅用 `:` 字符分隔标签和输出。

以下是对话和用户输入：

`dialog --textfield "text 1" --textfield "text 2" --selecttitle "make selection" --selectvalues "one,two,three,four"`

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/127793083-b07b4b46-8da6-46ee-a4ce-fcca84949a31.png">

输出结果如下所示：

```
 SelectedOption : three
 SelectedIndex : 2
text 1 : one
text 2 : two
```

`SelectedOption` 是被选中的下拉选项的文本。 `SelectedIndex` 是被选中的选项的索引（索引从 0 开始，因此索引 2 表示选择了列表中第三个选项）。

文本字段的显示方式是，使用在对话框中传入的标签作为输出中的标签。例如，对于上述情况：

`text 1` 显示用户在名为“文本 1”的文本框中输入的文本，而 `text 2` 也是如此。

你可以使用 `awk` 来处理你感兴趣的每一行输出，例如：
```bash
/usr/local/bin/dialog <...> | grep "SelectedOption" | awk -F " : " '{print $NF}'
```

为了进行更高级的处理，您可以传递一个 `--json` 参数，它会将输出格式化为 JSON 格式，以便使用 JSON 解析器（例如，在 Python 中）进行处理。

对于上述示例，JSON 输出结果会如下所示：
```json
{
"SelectedOption" : "three",
"SelectedIndex" : 2,
"text 1" : "one",
"text 2" : "two"
}
```

## 更多示例

使用 Python 捕获输出和返回码。
```python
import subprocess

result = subprocess.Popen("/usr/local/bin/dialog <...>")
text = result.communicate()[0]   # contents of stdout
return_code = result.returncode  # return code
```