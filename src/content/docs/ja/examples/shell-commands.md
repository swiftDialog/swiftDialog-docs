---
title: シェルコマンド
description: ボタンの操作からシェルコマンドを実行するための実験的な機能。
translationSynced: 2026-11-23T23:39:10+00:00
---

v1.1.2では、`button1shellaction`コマンドを通じて、実験的な機能が導入されています。


```
--button1shellaction <command>
                << EXPERIMENTAL >>
                Runs the specified shell command using zsh
                Command input and output is not sanitised or checked.
                If your command fails, Dialog still exits 0
```

この関数は、単一の文字列パラメータを受け取り、それをシェルに渡して実行します。例えば、以下のようなケースが考えられます。

` --button1shellaction "say thank you for running dialog"`

現在、入力のサニタイズや出力のサニタイズは行われません。指定されたコマンドがエラーで終了した場合でも、Dialogはボタン1の終了コードとして`0`を返します。コマンドのステータスは、コマンドの終了コードを含めて画面に出力されます。例：

```
.../Dialog.app/Contents/MacOS/Dialog --button1shellaction "bad command here"
zsh:1: command not found: bad
```

コマンドの実行結果は直接標準出力に送られるため、必要に応じて結果を確認したり、解析したりすることができます。

## 他のボタンに対するシェルアクションの設定。

ボタン2（キャンセル）とボタン3（情報）を押すと、それぞれコード2と3でダイアログが終了します。これらの終了コードを検出・解析することで、システム管理者がシェル上で特定の操作を実行できるようになります。そのため、ダイアログの終了ステータスを記録し、それに応じて処理を行うことをお勧めします。

## 考慮事項。

このコマンドはバックグラウンドで実行されないため、コマンドの実行中はDialogが表示されたままですが、操作不能になります。コマンドの実行が完了すると、Dialogは自動的に終了します。時間がかかる可能性のあるコマンドを実行する場合は、この点にご注意ください。

シェルコマンドは、それを呼び出したプロセスの権限も引き継ぎます。もしDialogをrootユーザーから実行した場合、シェルコマンドもroot権限を持つことになります。