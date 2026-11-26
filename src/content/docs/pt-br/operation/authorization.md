---
title: Autorização
description: Configuração de chaves de autorização para controlar o acesso ao swiftDialog
translationSynced: 2026-11-25T11:52:11+00:00
---

## Autorização 🔐

Na versão 2.3 e posteriores, o swiftDialog pode procurar uma chave de autorização. Se essa chave estiver presente, ela será necessária para que o programa seja executado

A chave de autorização é um mecanismo para impedir o uso não autorizado do swiftDialog. O valor da string será convertido em um hash utilizando o algoritmo SHA256 e comparado com o valor armazenado

****

### 🚨 Isenção de responsabilidade

 > _O uso da chave de autorização e a forma como ela é protegida não são responsabilidade da swiftDialog. É importante considerar o fluxo de trabalho e quando e onde a chave de autorização é utilizada, pois ela provavelmente aparecerá em texto simples em algum momento, e um invasor determinado poderia descobri-la._
 >
 >_Este recurso é novo na versão 2.3 e tem como objetivo dissuadir o uso indevido do swiftDialog, e não se trata de uma solução preventiva abrangente._

****

### Como funciona

O swiftDialog verificará o domínio `au.csiro.dialog` em busca do nome da chave `AuthorisationKey`. O valor da chave deve ser um hash SHA256 de uma frase-chave secreta. Se esse valor estiver presente, ele deve corresponder ao valor esperado, caso contrário, o swiftDialog não será iniciado.

Por exemplo, se a frase secreta a ser utilizada for `password`, então armazene o hash SHA256 dessa frase no domínio `au.csiro.dialog`:

      "AuthorisationKey" = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

Inicie o diálogo e especifique a frase secreta:

      diálogo --chave "senha"

Alternativamente, defina uma variável de ambiente `DIALOG_AUTH_KEY` no seu ambiente ou no início do seu script, e então remova-a após concluir a tarefa, em vez de passar o valor como um argumento a cada vez:

    export DIALOG_AUTH_KEY="password"

    ... processamento automatizado aqui ...

    Desconfigurar a variável DIALOG_AUTH_KEY

A falha em especificar a chave correta fará com que a janela de diálogo seja fechada com o código de saída `30`

Quando a autorização é bem-sucedida, o swiftDialog será executado e um pequeno ícone de cadeado aparecerá no canto superior direito, indicando uma sessão de diálogo autorizada.

<img src="https://github.com/bartreardon/swiftDialog/assets/3598965/4026888f-0183-4c5e-be8c-9fb137b0faf2" width="500">


O `--checksum <YourSecretString>` argumento é uma forma prática de gerar o hash necessário de uma string específica. Você pode fazer o mesmo com:

    echo -n "Minha Senha Secreta" | shasum -a 256

Certifique-se de usar `echo -n` se estiver utilizando este método. O uso de `echo` incluirá uma quebra de linha no resultado, e o valor da soma de verificação será diferente do que você espera

Existem diversas maneiras de guardar uma chave para facilitar o seu uso. Um bom ponto de partida pode ser https://scriptingosx.com/2021/04/get-password-from-keychain-in-shell-scripts/

## Exemplo de uso

Existem várias maneiras de garantir que seus scripts passem nos testes. Este é apenas um exemplo:

Gere um código secreto aleatório e um valor de soma de verificação
```bash
secret=$(uuidgen); checksum=$(echo -n "$secret" | shasum -a 256 | awk '{print $1}'); echo "secret = ${secret}"  && echo "checksum = ${checksum}"
```

A saída deve ter uma aparência semelhante a...

```bash
secret = 85F1C8B0-406E-4F8C-8B76-0C9C4AC6A42D
checksum = 557fce8c82dcf62cf04b233a2534912c083900b7ba84364b5991ff6111181cb8
```

Verifique o checksum em relação ao SwiftDialog

```bash
if [[ "${checksum}" == "$(dialog --checksum ${secret})" ]]; then echo "Success"; else echo "checksum failed"; fi
```

Isso verifica se o checksum gerado será validado pelo swiftDialog. Se tudo estiver correto, crie um perfil de configuração para `au.csiro.dialog` com `AuthorisationKey = ${checksum}` e faça a implantação.

Para a lógica do seu script, crie uma variável a partir de um argumento passado (cortesia de [Installomator](https://github.com/Installomator/Installomator/blob/471f8b44170ef32699c6bffe587a29b89c5f7e8c/fragments/main.sh#L9)]).

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

Ao executar o script, crie a variável de ambiente como um argumento, em vez de armazenar o valor diretamente no script em texto simples

```bash
dialog_script.sh DIALOG_AUTH_KEY="<secret-here>"
```

Você pode então chamar a função `swiftDialog` quantas vezes forem necessárias dentro do seu script, e ela validará os dados de acordo com `DIALOG_AUTH_KEY`