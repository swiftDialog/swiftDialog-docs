---
title: Checkboxes
description: Creating interactive checkboxes and switches in swiftDialog
---

Checkboxes can be used to offer a number of options that can be selected or not and then processed.

## Basic use

Specify one or more `--checkbox <text>` parameters and dialog will display a checkbox with `<text>` as the label.

### Style

Checkboxes can also be displayed as a switch instead of a checkbox.

The default is as a checkbox next to the label:

![image](https://user-images.githubusercontent.com/3598965/235893894-1d4c26ba-1afc-4e9f-a58d-16a36c27787f.png)

Use the `--checkboxstyle switch` option to change to the switch style:

![image](https://user-images.githubusercontent.com/3598965/235894156-c8cf82e7-d627-43a4-b11e-3acfc296a3e2.png)

If you prefer a larger switch style, you can specify this as a property on the switch style:

The options are `mini`, `small`, `regular` or `large`

`--checkboxstyle switch,large`

![image](https://user-images.githubusercontent.com/3598965/235894351-71200445-5871-4e27-b792-2a983a34514c.png)

## Advanced use

When using [JSON configuration](/advanced/json-configuration) to set Dialog options, optional checkbox parameters become available.

The json takes the form:

```json
{
  "checkbox" : [
	  {"label" : "<label>", "checked" : false, "disabled" : false, "icon" : "<file|url>" }
	],
 "checkboxstyle" : {
    "style" : "switch",
    "size"  : "regular"
	}
}
```
`"checked" : [true|false]` - will initialise the checkbox in the checked state if set to `true`. The default is unchecked.

`"disabled" : [true|false]` - will disable the checkbox if set to `true` regardless of checked state

`"icon" : "<file|url>"` - is available as json paramater when `checkboxstyle` is set to `switch`, otherwise it will be ignored

<img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-60c3-46aa-9a11-041aeeca8ffc.png" width=400>

### example

The following JSON and resulting dialog screenshot illustrate how these settings behave:

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true, "disabled" : false },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5" },
	  {"label" : "Option 6", "disabled" : true }
	]
}
```

![image](https://user-images.githubusercontent.com/3598965/150663608-6ee03207-0558-4769-a016-44fe5822fccb.png)

## Using a checkbox to control button1 state

You can use a checkbox to control the state of the default button. This is useful if you want to ensure that the user has selected a required option before proceeding.

Example:

`dialog --checkbox "I Agree",enableButton1 --button1disabled`

<img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/5a4d2ce4-ea37-447d-86d1-a12ca9d4807e"> <img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/ec12eb71-b6f9-466e-ad32-cb8812bc759c">

This can also be set using json:

```json
{
  "checkbox" : [
    {"label" : "I Agree", "enableButton1" : true }
  ],
  "button1disabled" : true
}
```

 > **It's important to set button1 to disabled initially, otherwise the user can click the button before the checkbox is checked. This is not set by default. It should also be stated that setting the `disabled` property as well as `enablebutton1` on a checkbox is not advised as it will make the checkbox not accessible.**

## Output

Results are sent to sdtout and by default look as follows:
```
Option 1 : true
Option 2 : true
Option 3 : false
Option 4 : true
Option 5 : false
Option 6 : false
```

Optionally you can specify the `--json` parameter and get the results in json format:

```json
{
  "Option 2" : true,
  "Option 4" : true,
  "Option 5" : false,
  "Option 6" : true,
  "Option 1" : true,
  "Option 3" : false
}
```