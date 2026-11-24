---
title: 承認
description: swiftDialogへのアクセスを制御するための認証キーの設定。
translationSynced: 2026-11-23T23:29:55+00:00
---

## 認証（認可）🔐

バージョン2.3以降のswiftDialogでは、認証キーを検索する機能が追加されており、もし認証キーが存在する場合、プログラムの実行にはそのキーが必要になります。

認証キーは、swiftDialogの不正利用を防止するための仕組みです。この文字列の値はSHA256でハッシュ化され、保存されている値と比較されます。

****

### 【免責事項】

 > 「認証キーの使用方法およびそのセキュリティ確保については、swiftDialogの責任範囲外です。ワークフロー全体を考慮し、認証キーがいつ、どこで使用されるかを確認する必要があります。なぜなら、認証キーはある時点で平文で表示される可能性があり、悪意のある攻撃者がそれを発見する可能性があるからです。」
 >
 >この機能はバージョン2.3で新たに追加されたものであり、swiftDialogの不正利用を抑制することを目的としています。これは、包括的な予防策を提供するものではありません。

****

### 仕組みについて。

swiftDialogは、`au.csiro.dialog`ドメインのキー名`AuthorisationKey`を確認します。キーの値は、秘密のキーフレーズのSHA256ハッシュである必要があります。この値が存在する場合、一致しなければならず、一致しないとswiftDialogは起動しません。

例えば、使用する秘密のフレーズが`password`である場合、このフレーズのSHA256ハッシュ値を`au.csiro.dialog`のドメインに保存します。

      "AuthorisationKey" = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

起動ダイアログを表示し、秘密のフレーズを指定します。

      ダイアログ：キーは "password" です。

または、環境変数`DIALOG_AUTH_KEY`を、環境設定またはスクリプトの冒頭で設定し、処理が完了したらそれを削除するようにします。毎回、値を引数として渡す代わりに、この方法がより効率的です。

    export DIALOG_AUTH_KEY="password"

    ... ここでスクリプトによる処理が行われます ...

    DIALOG_AUTH_KEY の設定を解除します。

正しいキーを指定しない場合、ダイアログはエラーコード`30`で終了します。

認証が成功すると、swiftDialogが起動し、画面の右上に小さな鍵のアイコンが表示され、認証されたダイアログセッションであることを示します。

<img src="https://github.com/bartreardon/swiftDialog/assets/3598965/4026888f-0183-4c5e-be8c-9fb137b0faf2" width="500">


この`--checksum <YourSecretString>`引数は、特定の文字列に必要なハッシュ値を生成するための便利な方法です。同様のことは、以下の方法でも実現できます。

    echo -n "私の秘密のパスフレーズ" | shasum -a 256

この方法を使用する際は、必ず`echo -n`を使用してください。 `echo`を使用すると、出力に改行が含まれ、チェックサムの値が期待される値と異なる場合があります。

鍵を便利に使えるように保管する方法はいくつかあります。まずは、ある場所に鍵を置いておくことから始めるのが良いかもしれません。https://scriptingosx.com/2021/04/get-password-from-keychain-in-shell-scripts/

## 使用例

スクリプトにパスワードを組み込む方法はいくつかあります。以下はその一例です。

ランダムな秘密鍵とチェックサムを生成します。
```bash
secret=$(uuidgen); checksum=$(echo -n "$secret" | shasum -a 256 | awk '{print $1}'); echo "secret = ${secret}"  && echo "checksum = ${checksum}"
```

出力される内容は、おおよそ以下のようになるはずです。

```bash
secret = 85F1C8B0-406E-4F8C-8B76-0C9C4AC6A42D
checksum = 557fce8c82dcf62cf04b233a2534912c083900b7ba84364b5991ff6111181cb8
```

SwiftDialogに対するチェックサムを検証する。

```bash
if [[ "${checksum}" == "$(dialog --checksum ${secret})" ]]; then echo "Success"; else echo "checksum failed"; fi
```

これは、生成されたチェックサムがswiftDialogによって検証されることを確認するものです。問題がなければ、`au.csiro.dialog`に対して、`AuthorisationKey = ${checksum}`の設定プロファイルを作成し、展開してください。

スクリプトのロジックにおいて、引数として渡された値から変数を作成します（[Installomator](https://github.com/Installomator/Installomator/blob/471f8b44170ef32699c6bffe587a29b89c5f7e8c/fragments/main.sh#L9)]の提供による）。

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

スクリプトを実行する際に、環境変数をスクリプト内に直接記述するのではなく、引数として渡すようにしてください。

```bash
dialog_script.sh DIALOG_AUTH_KEY="<secret-here>"
```

その後、スクリプト内で必要に応じて`swiftDialog`を何度でも呼び出すことができます。`swiftDialog`は、呼び出しごとに指定された条件（`DIALOG_AUTH_KEY`）に基づいて検証を行います。