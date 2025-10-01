---
title: Help Messages
description: Adding contextual help messages to dialogs
---

## Help Messages

Help messages can be a way to provide extra detail if needed without taking up additional dialog space

`--helpmessage <text>`

`<text>` will accept markdown for message formatting

When present, an extra help button will appear next to the default button.


![image](https://user-images.githubusercontent.com/3598965/216032093-2aede3aa-4cda-402c-9cd7-fa4edb506cfc.png)

Clicking it will present the help message in a popover sheet

![image](https://user-images.githubusercontent.com/3598965/216032203-35960f72-24f5-491e-8d75-b6b43e4a123c.png)

The height of the sheet displayed will adjust to the size of the message.

### `--helpimage`

Add an image with `--helpimage /path/to/image.png`.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/d4c4504f-2e6f-4e83-882f-be0e799c9ffc" />

Supports standard icon arguments, including qr code:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/1c4c99bc-8548-4547-b16b-0dd02cc2c02d" />