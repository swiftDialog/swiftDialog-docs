---
title: 授权
description: 设置授权密钥以控制 swiftDialog 的访问权限
translationSynced: 2026-11-25T05:45:42+00:00
---

## 授权 🔐

在版本 2.3 及更高版本中，swiftDialog 可以查找授权密钥，如果找到该密钥，则需要使用该密钥才能运行。

授权密钥是一种防止未经授权使用 swiftDialog 的方法。该字符串值将使用 SHA256 算法进行哈希处理，并与存储的值进行比较。

****

### 🚨 声明

 > 授权密钥的使用方式以及如何确保其安全性，不属于 swiftDialog 的责任范围。在使用授权密钥时，应仔细考虑工作流程，以及授权密钥何时何地会被使用，因为很可能在某个环节，授权密钥会以明文形式出现，而有决心的人可能会发现它。
 >
 >_此功能是 2.3 版本的全新特性，旨在防止滥用 swiftDialog，而不是作为一种全面的预防措施。_

****

### 工作原理

swiftDialog 会检查 `au.csiro.dialog` 域中的键名 `AuthorisationKey`。键值应为密钥短语的 SHA256 哈希值。如果存在此值，则它必须匹配，否则 swiftDialog 将无法启动。

例如，如果需要使用的密钥短语是`password`，那么将该短语的SHA256哈希值存储在`au.csiro.dialog`域中。

      "授权密钥" = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

启动对话框，并指定秘密短语：

      对话框，键名："密码"。

或者，您可以在您的环境设置中或脚本的开头设置一个环境变量 `DIALOG_AUTH_KEY`，然后在脚本执行完毕后将其取消设置，而不是每次都将该值作为参数传递。

    export DIALOG_AUTH_KEY="password"

    ... 在此处进行脚本化处理 ...

    取消设置 DIALOG_AUTH_KEY 变量。

如果未指定正确的密钥，对话框将以退出码 `30` 结束。

当授权成功后，swiftDialog 将会运行，并且在右上角会显示一个小锁图标，表示已建立授权的对话会话。

<img src="https://github.com/bartreardon/swiftDialog/assets/3598965/4026888f-0183-4c5e-be8c-9fb137b0faf2" width="500">


这个方法 `--checksum <YourSecretString>` 是一种方便的方式，可以用来生成特定字符串所需的哈希值。 你也可以使用以下方法实现相同的功能：

    echo -n "我的秘密密码" | shasum -a 256

请务必使用`echo -n`，如果采用此方法。使用`echo`会导致输出包含换行符，并且校验和结果可能与您期望的不同。

有很多方法可以存放钥匙，以便方便使用。一个不错的起点可能是 https://scriptingosx.com/2021/04/get-password-from-keychain-in-shell-scripts/。

## 使用示例

有很多方法可以确保你的脚本通过审核。以下是一个例子：

生成一个随机的密钥和校验和。
```bash
secret=$(uuidgen); checksum=$(echo -n "$secret" | shasum -a 256 | awk '{print $1}'); echo "secret = ${secret}"  && echo "checksum = ${checksum}"
```

输出结果应该类似于...

```bash
secret = 85F1C8B0-406E-4F8C-8B76-0C9C4AC6A42D
checksum = 557fce8c82dcf62cf04b233a2534912c083900b7ba84364b5991ff6111181cb8
```

验证校验和与 swiftDialog 的结果是否一致。

```bash
if [[ "${checksum}" == "$(dialog --checksum ${secret})" ]]; then echo "Success"; else echo "checksum failed"; fi
```

这验证了生成的校验和将由 swiftDialog 进行验证。如果一切正常，则为 `au.csiro.dialog` 创建一个配置文件，其中包含 `AuthorisationKey = ${checksum}`，然后进行部署。

对于您的脚本逻辑，创建一个变量，该变量的值来自传入的参数（感谢[Installomator⟧）。](https://github.com/Installomator/Installomator/blob/471f8b44170ef32699c6bffe587a29b89c5f7e8c/fragments/main.sh#L9)

```bash
# read script arguments:
while [[ -n $1 ]]; do
    if [[ $1 =~ ".*\=.*" ]]; then
        # if an argument contains an = character, send it to eval
        eval $1
    fi
    # shift to next argument
    shift 1
done
```

在调用脚本时，应将环境变量作为参数传递，而不是将值直接以明文形式存储在脚本中。

```bash
dialog_script.sh DIALOG_AUTH_KEY="<secret-here>"
```

然后，您可以在脚本中多次调用 `swiftDialog` 函数，它将根据 `DIALOG_AUTH_KEY` 进行验证。