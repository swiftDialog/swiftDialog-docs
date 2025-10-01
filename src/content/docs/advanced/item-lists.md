---
title: Item Lists
description: Creating dynamic ordered lists with status indicators and icons
---

Item lists let you display a reasonable number of items in an ordered list. If the list extends beyond the visible area, the list becomes scrollable.

Lists can be present on a dialog with any of the existing customisation options except for images which use the entire message display.

<hr />
There are three ways to create an Item list:

### 1) Command line

Specify one or more `--listitem <text>` entries as a command line argument. The list will be constructed in the order given.

List item icons can be set using command line arguments `--listitem "<text>,icon=<image>"` however, if you require more advanced options you must use JSON.

### 2) JSON

When using JSON as a configuration source, specify items as a one dimensional array.

#### Basic

The basic method is an easy way to initiate a list of items with no status set.

```json
{
  "listitem" : ["Item 1", "Item 2", "Item 3"]
}
```

#### Advanced

Advanced lets you initialise a list and optionally set an icon, status and status text

```json
{
  "listitem" : [
    {"title" : "Item One", "icon" : "/path/to/image", "status" : "pending", "statustext" : "Pending"},
    {"title" : "Item Two", "icon" : "/path/to/SomeApp.app", "status" : "wait", "statustext" : "Waiting"},
    {"title" : "Item Three", "icon" : "https://some.url/image", "status" : "success", "statustext" : "Winning"}
  ]
}
```

##### Status options

The list items status can be one of `wait`, `success`, `fail`, `error`, `pending` or `progress` and will display an apropriate icon in the status area.

When using `progress` as a status, a circular progress counter will be displayed as the status icon. Appending a number, e.g.  `progress: 20` will animate the indicator to the appropriate position representing the percentage to be filled. The progress indicator accepts any values between `0` and `100`

<img width="599" alt="image" src="https://user-images.githubusercontent.com/3598965/182604151-3eabe9b5-3f77-4949-9b88-c522676e3314.png">


### 3) As a command sent to the command file

Send items as coma separated values

`echo "list: Item 1, Item 2, Item 3" >> /var/tmp/dialog.log`


## Updating an existing list

Entries in an already displayed list can be updated with a status by sending commands to the command file.


#### Basic

The basic syntax required is:

`echo listitem: <list item title>: <status text> >> /var/tmp/dialog.log`

 - `<list item title>` must match the list item name/title and is case sensitive
 - `<status text>` can be any unicode text string
   - If sent one of the supported status keywords then a matching indicator will be shown instead of text

#### Advanced

The advanced syntax lets you update the status text and status indicator as well as reference the list item by index. Keywords are separated in a comma separated list (this does mean that the `title` and `statustext` entries cannot contain text with a comma present):

`listitem: [title: <title>|index: <index>], status: <status>, statustext: <text>`

`<index>` starts at 0

e.g.

`listitem: index: 0, status: complete, statustext: Item 1 on the list has completed`

New items can be appended to the end og an existing list with the `add:` command and items can be removed with the `delete:` command. When adding a row, status and statustext are optional.

Examples:

`echo "listitem: add, title: <title>, statustext: <text>, status: <status>" >> /var/tmp/dialog.log`

delete by index: `echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log`

delete by title reference `echo "listitem: title: Some Row Title, delete:" >> /var/tmp/dialog.log`

It is possible to add or delete items in a list with no list currently visible.

## Showing or hiding a list

List can be commanded to hide or show without affecting the contents of the list.

show `echo "list: show`

hide `echo "list: hide`

## Removing a list

An existing list can be removed by sending the command `list: clear` to the command file.

Clearing a list removes all entries and statuses associated with it.

## Examples


`echo "list: Test item 1, Test item 2, Test item 3" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151488006-ba027af7-0736-47b2-abdd-ba847491f086.png)

Then sending the following commands will update the list status

`echo "listitem: Test item 1: Complete ✅" >> /var/tmp/dialog.log`

`echo "listitem: Test item 2: There was an error processing this item ❌" >> /var/tmp/dialog.log`

`echo "listitem: Test item 3: wait" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151486051-967e760e-f164-467f-8bd6-dcccba3c7504.png)

#### Advanced JSON format

![image](https://user-images.githubusercontent.com/3598965/163742836-22fd32e8-8010-467f-a518-b4d348619698.png)