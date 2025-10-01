---
title: Displaying Images
description: Learn how to display images, image captions, and image carousels in swiftDialog
---

## Displaying Images

Images can be displayed and by default will replace the message area.

`--imagecaption` is available for a short one line description of each image. If a `--message` is also present then it will be displayed underneath any images and captions.

```
-g, --image  <file> | <url>
  Display an image instead of a message.
  Images will be resized to fit the available display area

    --imagecaption <text>
    Text that will appear underneath the displayed image.
```

Any supported image format can be passed in either as a `<file>` or `<url>`

Example:

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/129476046-5b0cdef0-346b-4af6-a0eb-e8e72c72715d.png">

### Images in base64 format

Wherever an image can be used, they can now be specified in base64. using the `base64=` prefix
e.g. `--icon base64=<base64_text>`

### Multiple Images

Specifying more than one `--image` will display the images in a carousel with next/previous chevrons and indication of which image in the sequence is being displayed.

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/148642555-96247bff-8d95-414d-bf96-1fe28e27ed9c.png">

In addition to displaying the images statically, you can use `--autoplay <sec>` to have the next image display after the specified number of seconds (default is 10). A progress indicator will show beneath the image display to indicate when the next transition will occur. After the last image is shown the display will reset and start from the first image.