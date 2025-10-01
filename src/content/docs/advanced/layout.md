---
title: Layout
description: Customizing the order and arrangement of dialog elements
---

## Custom View Ordering

`--vieworder <csv>`

With the exception of Images and message content, window elements can be re-ordered.

The default order is:
 > textfile
 > webcontent
 > listitem
 > checkbox
 > textfield
 > radiobutton
 > dropdown

 These elements can be re-arranged to suit display needs by specifying the desired order as a csv list of items, e.g. `--vieworder "dropdown, textfield, checkbox"`

 <img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/1b69abc7-4367-4eac-9e2d-a208ea47a60f" width="750px">