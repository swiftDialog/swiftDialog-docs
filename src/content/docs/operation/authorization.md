---
title: Authorization
description: Setting up authorization keys to control swiftDialog access
---

## Authoris(z)ation 🔐

In v2.3 and newer, swiftDialog can look for a authorisation key and if present will require it to run

The authorisation key is a way to prevent unauthorised use of swiftDialog. The string value will be hashed with SHA256 and compared against the stored value

****

### 🚨 Disclaimer

 > _The use of the authorisation key and how it is secured is not the responsibility of swiftDialog. Consideration should be given to the workflow and when and where the authorisation key is used as it will most likely appear in cleartext at some point and a determined attacker could discover it._
 >
 >_This feature is new for v2.3 and is intended as a deterrant to misuse of swiftDialog, not as a comprehensive preventative solution._

****

### How it works

swiftDialog will check the `au.csiro.dialog` domain for the key name `AuthorisationKey`. The key value should be a SHA256 hash of a secret keyphrase. If this value is present, then it must match or swiftDialog will not launch.

e.g. if the secret phrase to be used is `password` then the store the SHA256 hash of this phrase in the `au.csiro.dialog` domain:

      "AuthorisationKey" = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

launch dialog and specify the secret phrase:

      dialog --key "password"

Alternately, set an environment variable `DIALOG_AUTH_KEY` in your environment or at the start of your script and then unset it after you finish rather than pass in the value as an argument every time:

    export DIALOG_AUTH_KEY="password"

    ... scripted processing here ...

    unset DIALOG_AUTH_KEY

Failure to specify the correct key will casue dialog to quit with exit code `30`

When authorisation is successful, swiftDialog will run and a small lock icon will appear in the top right indicating an authorised dialog session.

<img src="https://github.com/bartreardon/swiftDialog/assets/3598965/4026888f-0183-4c5e-be8c-9fb137b0faf2" width="500">


The `--checksum <YourSecretString>` argument is a convenient way to generate the required hash of a specific string. You can do the same with:

    echo -n "My Secret Passphrase" | shasum -a 256

_be sure to use `echo -n` if using this method. Using `echo` will include a newline in the output and the checksum will be different to what you expect_

There are a number of ways to store a key for convenient use. A good place to start might be https://scriptingosx.com/2021/04/get-password-from-keychain-in-shell-scripts/

## Example Use

There are multiple ways to acheive passing in your secret to your scripts. This is but one example:

Generate a random secret and checksum
```bash
secret=$(uuidgen); checksum=$(echo -n "$secret" | shasum -a 256 | awk '{print $1}'); echo "secret = ${secret}"  && echo "checksum = ${checksum}"
```

The output should look something like...

```bash
secret = 85F1C8B0-406E-4F8C-8B76-0C9C4AC6A42D
checksum = 557fce8c82dcf62cf04b233a2534912c083900b7ba84364b5991ff6111181cb8
```

Validate the checksum against swiftdialog

```bash
if [[ "${checksum}" == "$(dialog --checksum ${secret})" ]]; then echo "Success"; else echo "checksum failed"; fi
```

This verifies the checksum generated will be validated by swiftDialog. If all is well, create a config profile for `au.csiro.dialog` with `AuthorisationKey = ${checksum}` and deploy.

For your script logic, create a variable from a passed in argument (courtesy of [Installomator](https://github.com/Installomator/Installomator/blob/471f8b44170ef32699c6bffe587a29b89c5f7e8c/fragments/main.sh#L9))

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

When calling the script, create the environment variable as an argument rather than store the value in cleartext within the script

```bash
dialog_script.sh DIALOG_AUTH_KEY="<secret-here>"
```

You can then call swiftDialog as many times as needed within your script and it will validate against `DIALOG_AUTH_KEY`