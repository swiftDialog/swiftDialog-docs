---
title: Displaying Videos
description: Learn how to display videos and video content in swiftDialog, including YouTube and Vimeo support
---

## Displaying Videos

Videos can be displayed in place of a message. When specified, the default Dialog size will switch to 900x600 to accomodate a 16:9 ratio video. Custom sizes can be specified using the `--width` and `--height` modifiers.

```
--video  <file> | <url>
  Display a video instead of a message.
  Videos will be resized to fit the available display area (depending on video resolution, some letterboxing may occur)

    --videocaption <text>
    Text that will appear underneath the displayed video.

    --autoplay
    Video will start playing automatically on launch without requiring the user to press play
```

Any video format supported by Quicktime should be viewable. If using a URL, the full path to the video resource must be used.

Example: `--title "Video Demo" --video /Users/Shared/Videos/day4session3.mp4`

![image](https://user-images.githubusercontent.com/3598965/138063195-19011cc7-840f-4701-9209-8405ffabcbeb.png)

### YouTube and Vimeo support (requires swiftDialog v2.0 or newer)

To embed a YouTube or Vimeo video, you can pass in the video ID as a parameter to the `--video` command using the `youtubeid=` or `vimeoid=` prefix

The ID can usually be found in the URL on either YouTube or Vimeo

YouTube Example:

`dialog --video youtubeid=XXXXXXXXXX`

Vimeo example:

`dialog --video vimeoid=XXXXXXXXXX`

_Note: for ID's of private Vimeo videos, you may also need to capture the additional information in the embed URL. This will be represented as additional `h=YYYYYYYY` - the full embed command for swiftDialog would therefore be `dialog --video "vimeoid=XXXXXXXXXX?h=YYYYYYYY"`._


## Updating a running dialog with new web or video content

Send the following commands to update a dialog with new web or video content

```bash
echo "webcontent: https://some.website.com" >> /var/tmp/dialog.log
echo "video: https://some.website.com/video.mov" >> /var/tmp/dialog.log
echo "video: /path/to/file.mov" >> /var/tmp/dialog.log
```

Some caveats though:
Currently you can't update web or video content in place. To switch to another website you will need to clear the contents and then send the new content.

```bash
echo "webcontent: none" >> /var/tmp/dialog.log
echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log
```

you can string those together though so `echo "webcontent: none" >> /var/tmp/dialog.log && echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log` also works.