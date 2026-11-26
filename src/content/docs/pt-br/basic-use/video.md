---
title: Exibindo vídeos
description: Aprenda como exibir vídeos e conteúdo de vídeo no swiftDialog, incluindo suporte para YouTube e Vimeo
translationSynced: 2026-11-25T11:07:46+00:00
---

## Exibindo vídeos

Os vídeos podem ser exibidos no lugar de uma mensagem. Quando especificado, o tamanho padrão da janela de diálogo será alterado para 900x600 para acomodar vídeos com proporção de 16:9. Tamanhos personalizados podem ser definidos usando os modificadores `--width` e `--height`.

```
--video  <file> | <url>
  Display a video instead of a message.
  Videos will be resized to fit the available display area (depending on video resolution, some letterboxing may occur)

    --videocaption <text>
    Text that will appear underneath the displayed video.

    --autoplay
    Video will start playing automatically on launch without requiring the user to press play
```

Qualquer formato de vídeo suportado pelo QuickTime deve ser reproduzível. Ao utilizar uma URL, é necessário fornecer o caminho completo para o recurso de vídeo.

`--title "Video Demo" --video /Users/Shared/Videos/day4session3.mp4`

![image](https://user-images.githubusercontent.com/3598965/138063195-19011cc7-840f-4701-9209-8405ffabcbeb.png)

### Suporte para YouTube e Vimeo (requer a versão 2.0 ou superior do swiftDialog).

Para incorporar um vídeo do YouTube ou Vimeo, você pode passar o ID do vídeo como um parâmetro para o comando `--video`, utilizando o prefixo `youtubeid=` ou `vimeoid=`.

Geralmente, o identificador pode ser encontrado na URL, seja no YouTube ou no Vimeo.

Exemplo do YouTube:

`dialog --video youtubeid=XXXXXXXXXX`

Exemplo do Vimeo:

`dialog --video vimeoid=XXXXXXXXXX`

_Observação: para os IDs de vídeos privados no Vimeo, pode ser necessário capturar informações adicionais na URL de incorporação. Isso será representado como informações adicionais `h=YYYYYYYY` – portanto, o comando completo para o swiftDialog seria `dialog --video "vimeoid=XXXXXXXXXX?h=YYYYYYYY"`._


## Atualizar uma caixa de diálogo em execução com novo conteúdo da web ou de vídeo

Envie os seguintes comandos para atualizar uma caixa de diálogo com novo conteúdo web ou de vídeo.

```bash
echo "webcontent: https://some.website.com" >> /var/tmp/dialog.log
echo "video: https://some.website.com/video.mov" >> /var/tmp/dialog.log
echo "video: /path/to/file.mov" >> /var/tmp/dialog.log
```

Atenção: No momento, não é possível atualizar o conteúdo de páginas web ou vídeos diretamente. Para acessar outro site, será necessário limpar o conteúdo atual e, em seguida, enviar o novo conteúdo.

```bash
echo "webcontent: none" >> /var/tmp/dialog.log
echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log
```

Você pode combiná-los, então `echo "webcontent: none" >> /var/tmp/dialog.log && echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log` também funciona.