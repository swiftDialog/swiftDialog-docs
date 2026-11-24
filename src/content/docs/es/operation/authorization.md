---
title: Autorización
description: Configuración de las claves de autorización para controlar el acceso a swiftDialog
translationSynced: 2026-11-24T22:58:23+00:00
---

## Autorización 🔐

En la versión 2.3 y posteriores, swiftDialog puede buscar una clave de autorización y, si la encuentra, requerirá que se proporcione para poder ejecutarse

La clave de autorización es un mecanismo para evitar el uso no autorizado de swiftDialog. El valor de la cadena se codificará mediante el algoritmo SHA256 y se comparará con el valor almacenado

****

### 🚨 Advertencia

 > _El uso de la clave de autorización y cómo se protege no son responsabilidad de swiftDialog. Se debe prestar atención al flujo de trabajo y a cuándo y dónde se utiliza la clave de autorización, ya que es probable que aparezca en texto plano en algún momento, y un atacante determinado podría descubrirla._
 >
 >_Esta función es nueva en la versión 2.3 y tiene como objetivo disuadir el uso indebido de swiftDialog, no ofrecer una solución preventiva exhaustiva._

****

### Cómo funciona

swiftDialog verificará el `au.csiro.dialog` dominio en busca del nombre de la clave `AuthorisationKey`. El valor de la clave debe ser un hash SHA256 de una frase secreta. Si este valor está presente, debe coincidir; de lo contrario, swiftDialog no se iniciará.

Por ejemplo, si la frase secreta a utilizar es `password`, entonces almacene el hash SHA256 de esta frase en el dominio `au.csiro.dialog`:

      "AuthorisationKey" = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

Inicie el diálogo y especifique la frase secreta:

      diálogo --clave "contraseña"

Alternativamente, puede establecer una variable de entorno `DIALOG_AUTH_KEY` en su entorno o al principio de su script, y luego eliminarla una vez que haya terminado, en lugar de pasar el valor como un argumento cada vez.

    export DIALOG_AUTH_KEY="password"

    ... procesamiento programado aquí...

    deshabilite DIALOG_AUTH_KEY

La falta de especificación de la clave correcta provocará que el diálogo se cierre con el código de salida `30`

Cuando la autorización se completa con éxito, swiftDialog se ejecutará y aparecerá un pequeño icono de candado en la esquina superior derecha, indicando que se ha iniciado una sesión de diálogo autorizada.

<img src="https://github.com/bartreardon/swiftDialog/assets/3598965/4026888f-0183-4c5e-be8c-9fb137b0faf2" width="500">


El argumento `--checksum <YourSecretString>` es una forma práctica de generar el hash requerido de una cadena de texto específica. Puede lograr lo mismo de la siguiente manera:

    echo -n "Mi frase secreta" | shasum -a 256

Asegúrese de utilizar `echo -n` si utiliza este método. El uso de `echo` incluirá un salto de línea en la salida, y la suma de verificación será diferente a la que espera

Existen varias formas de guardar una llave para facilitar su uso. Un buen punto de partida podría ser https://scriptingosx.com/2021/04/get-password-from-keychain-in-shell-scripts/

## Ejemplo de uso

Existen diversas formas de lograr que un texto pase desapercibido, integrándose de manera sutil en otros contenidos. Este es solo un ejemplo:

Generar un código secreto aleatorio y un valor de suma de verificación
```bash
secret=$(uuidgen); checksum=$(echo -n "$secret" | shasum -a 256 | awk '{print $1}'); echo "secret = ${secret}"  && echo "checksum = ${checksum}"
```

Debe resultar algo así...

```bash
secret = 85F1C8B0-406E-4F8C-8B76-0C9C4AC6A42D
checksum = 557fce8c82dcf62cf04b233a2534912c083900b7ba84364b5991ff6111181cb8
```

Verificar el valor de suma de verificación (checksum) con swiftdialog

```bash
if [[ "${checksum}" == "$(dialog --checksum ${secret})" ]]; then echo "Success"; else echo "checksum failed"; fi
```

Esto verifica que la suma de comprobación generada será validada por swiftDialog. Si todo está correcto, cree un perfil de configuración para `au.csiro.dialog` con `AuthorisationKey = ${checksum}` y despliéguelo.

Para la lógica de su script, cree una variable a partir de un argumento que se le pasa (gracias a [Installomator](https://github.com/Installomator/Installomator/blob/471f8b44170ef32699c6bffe587a29b89c5f7e8c/fragments/main.sh#L9)]).

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

Al ejecutar el script, cree la variable de entorno como un argumento, en lugar de almacenar el valor directamente en el script en texto plano

```bash
dialog_script.sh DIALOG_AUTH_KEY="<secret-here>"
```

Luego, puede llamar a la función `swiftDialog` tantas veces como sea necesario dentro de su script, y esta validará la información según `DIALOG_AUTH_KEY`