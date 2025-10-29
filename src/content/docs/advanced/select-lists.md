---
title: Select Lists and Radio Buttons
description: Creating dropdown lists and radio button groups for user selection
---

Dialog has the ability to take a list of values and display them as a dropdown with optional default selection.

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)

## How to Use


### Select List title

`--selecttitle <text>(,radio|required|searchable|name=\"<text>\")`

Set the label can be given to the list with the `--selecttitle` command line option.
e.g. `--selecttitle "Select an Option"`

![image](https://user-images.githubusercontent.com/3598965/122635336-9ee98a80-d126-11eb-8839-f859eb19688e.png)


This name will appear in swiftDialog output on STDOUT with the value of the selected item.
For a single select list, standard output format will be:
```
    "SelectedOption" : "<value>"
    "SelectedIndex" : <index>
    "<name>" : "<value>"
    "<name>" index : "<index>"
```

Multiple `--selecttitle` arguments may be specified. Related `--selectvalues` and `--selectdefault` arguments can be specified and are associated to a select list in the order they are presented

If multiple select lists are used, "SelectedOption" and "SelectedIndex" are not represented.

Output of select items is only shown if swiftDialog's exit code is 0

### Select List Values

`--selectvalues <text><csv>`

Values are specified in CSV format and passed in using the `--selectvalues` command line option
e.g. `--selectvalues "Option 1,Option 2,Option 3,Option 4, Option 5"`

![image](https://user-images.githubusercontent.com/3598965/122635303-6053d000-d126-11eb-94f1-6950f0e3d43e.png)

### Select List Default

`--selectdefault <text>`

The default option cen be set using the `--selectdefault` command line option
e.g. `--selectdefault "Option 4"`

![image](https://user-images.githubusercontent.com/3598965/122635358-c2143a00-d126-11eb-80b2-475a62b6ed9a.png)

If a default value is _not_ specified, and the user does not select an item from the list, no output is given.


example output:
```
    SelectedOption: Option 1
    SelectedIndex: 0
```

Output of select items is only shown if Dialog's exit code is 0

## JSON Schema

The configuration can be specified using JSON for more direct control.

```json
{
  "selectitems" : [
    {
      "title" : "Select Item",
      "name" : "altname",
      "values" : ["red","green","blue"],
      "default" : "red",
      "required" : false,
      "style" : "default"
    }
  ]
}
```

### Examples:

```json
"selectitems" : [
  {"title" : "Select 1", "values" : ["one","two","three"]},
  {"title" : "Select 2", "values" : ["red","green","blue"], "default" : "red"}
]
```

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)


```json
"selectitems" : [
  {"title" : "Pick One", "values" : ["One","Two","Three"], "style" : "radio"}
]
```

![image](https://github.com/bartreardon/swiftDialog/assets/3598965/1d2659c6-9048-440b-9246-2756ec097a24)


## Modifiers

### Name

Causes the output to be recorded with the specified `name` instead of using the title

```bash
% dialog --selecttitle "Alternate Name",name=alt --selectvalues "Option One, Option Two, Option Three"

"SelectedOption" : "Option One"
"SelectedIndex" : 0
"alt" : "Option One"
"alt" index : "0"
```

### Searchable

The `searchable` modifier adds a search field to the list. Typing in the text box will filter the list.

<img width="550" alt="image" src="/images/select_1.png" />

<img width="550" alt="image" src="/images/select_2.png" />

### Radio

The `radio` modifier will change the select list to display a group with radio buttons. When using `radio` with no default item specified, the first entry in the list will become the default selected item. As such, using radio buttons _always_ forces one of the values to be selected and modifiers like `required` are ignored.

`--selecttitle "Radio buttons",radio --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235897669-c08fdd79-aa14-4fec-8c6d-a930861a122f.png)

### Required

The `required` modifier will make that particular list a required item that must have a value before swiftDialog will exit

`--selecttitle "Required item",required --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235898090-5f7e9fac-2913-413f-ae85-c850ae86ee6b.png)

![image](https://user-images.githubusercontent.com/3598965/235898473-6fb9749f-3406-4f8d-b112-b214e95dccd4.png)

## Adding sections to the list

Add three or more hyphens `---` into your list wherever you need a divider in your list

`--selectvalues "Option One, Option Two, ---, Option Three, Option Four, ---, Option Five"`

![image](https://user-images.githubusercontent.com/3598965/235900591-96ace495-5205-459c-9b2e-4bcd3ede00ee.png)

**NOTE: each `---` will count in the index even though the divider itself is not selectable. In the above example there will be 7 items in the list array even though only 5 are displayed in the menu. Please take this into account when constructing your select lists**

## Output

Dialog will output the user selected value (or default value if given and the user selects no value) to `stdout` on exit. This output can be parsed by a script and acted on accordingly.

There are two lines in the output.
* The first line is the text of the list item and will be output as `SelectedOption: <text of item>`
* The second line is the index of the item selected and will be in the format `SelectedIndex: <index of item>`

The index starts at `0` so if the third item in the list is selected, the output of `SelectedIndex` will be `SelectedIndex: 2`

## Example reading output

given the following output:
```
 SelectedOption: Option 4
 SelectedIndex: 3
```

pass through grep and awk to obtain the value you want to process

` | grep "SelectedOption" | awk -F ": " '{print $NF}'`

or

` | grep "SelectedIndex" | awk -F ": " '{print $NF}'`

## Adding multiple select lists

To add multiple select lists, simply specify multiple instances of `--selectvalues` `--selecttitle` and `--selectdefault`. The title and default will be assigned in the order they are given.


### multi select output

when using multiple select lists the output is modified to allow parsing the various named lists. for example, if using the json above and selecting "two" and "red" will result in the following output:

```
Select 1 : two
Select 1 index : 1
Select 2 : red
Select 2 index : 0
```

if sending output in json format it would result in the following:

```json
{
  "Select 1" : {
    "selectedIndex" : 1,
    "selectedValue" : "two"
  },
  "Select 2" : {
    "selectedIndex" : 0,
    "selectedValue" : "red"
  }
}
```