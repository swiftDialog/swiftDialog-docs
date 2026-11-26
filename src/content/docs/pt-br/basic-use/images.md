---
title: Exibindo imagens
description: Aprenda como exibir imagens, legendas de imagens e carrosséis de imagens no swiftDialog
translationSynced: 2026-11-25T10:48:49+00:00
---

## Exibindo imagens

As imagens podem ser exibidas e, por padrão, substituirão a área de mensagens.

`--imagecaption` está disponível para uma breve descrição de uma linha para cada imagem. Se um `--message` também estiver presente, ele será exibido abaixo de quaisquer imagens e legendas.

```
-g, --image  <file> | <url>
  Display an image instead of a message.
  Images will be resized to fit the available display area

    --imagecaption <text>
    Text that will appear underneath the displayed image.
```

Qualquer formato de imagem suportado pode ser utilizado, seja como entrada `<file>` ou como entrada `<url>`

Exemplo:

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/129476046-5b0cdef0-346b-4af6-a0eb-e8e72c72715d.png">

### Imagens no formato base64

Sempre que uma imagem puder ser utilizada, ela agora pode ser especificada em base64, utilizando o prefixo `base64=`, por exemplo: `--icon base64=<base64_text>`

### Múltiplas imagens

Especificar mais de uma `--image` exibirá as imagens em um carrossel, com setas de "próximo" e "anterior", e uma indicação de qual imagem da sequência está sendo exibida.

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/148642555-96247bff-8d95-414d-bf96-1fe28e27ed9c.png">

Além de exibir as imagens de forma estática, você pode usar `--autoplay <sec>` para que a próxima imagem seja exibida após o número especificado de segundos (o padrão é 10). Um indicador de progresso será exibido abaixo da imagem para indicar quando a próxima transição ocorrerá. Após a exibição da última imagem, a exibição será reiniciada e começará pela primeira imagem.

Use `--hidetimer` para ocultar o indicador de contagem regressiva que é exibido durante as transições automáticas.