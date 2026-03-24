---
title: Text Fields
description: Creating text input fields with various properties and validation
---

The `--textfield` option let you specify an area where the user can enter in some text before dismissing the dialog

It takes a parameter as text and uses that parameter as the textfield label both in the dialog UI and in reporting output

The results are sent to stdout when dialog exits in the following format:

`<textfield text> : <user input>`

or if using the `--json` option to enable json output:

```json
{
"<textfield text>" : "<user input>"
}
```

## Examples

If using the following dialog:

`dialog --textfield "Textfield 1"`

Will display the following dialog:

![image](https://user-images.githubusercontent.com/3598965/235908715-5f24a167-5ad1-4f81-aa7e-30faf5590b1c.png)

The user enters in a response:

![image](https://user-images.githubusercontent.com/3598965/235908865-40b37eac-874b-4ceb-a4e7-e8701ebdf790.png)

which will result in the following output:

`Textfield 1 : This is what the user entered`

or when using `--json`

```json
{
"Textfield 1" : "This is what the user entered"
}
```

## Additional Textfields

Multiple textfields can be specified by adding additional `--textfield` options when calling dialog

e.g. `dialog --textfield "Textfield 1" --textfield "Textfield 2"`

![image](https://user-images.githubusercontent.com/3598965/235909015-2c4f187b-a86d-4281-84ff-09afa6b87857.png)

You can specify as many textfialds as you need. Each textfield will output as a seperate field in the output.

**You may need to adjust the `--height` of your dialog window if you are adding multiple textfirlds so they fit**

Example:

`dialog --textfield "First Name" --textfield "Surname" --textfield "Age" --textfield "Favourite Colour"`

results in the following output:

```
First Name : Joe
Surname : Bloggs
Age : 32
Favourite Colour : Red
```

`--json`
```json
{
"First Name" : "Joe",
"Surname" : "Bloggs",
"Age" : "32",
"Favourite Colour" : "Red"
}
```

## Textfield Modifiers

Modifiers are appended to the textfield label as comma-separated values:

```sh
--textfield "<label>,<modifier>,<modifier>=<value>"
```

| Modifier | Description |
|---|---|
| `name=<text>` | Use this value as the output key instead of the label |
| `required` | Field must be filled before swiftDialog will exit |
| `secure` | Hide input as it is typed (password field) |
| `passwordfill` | Enable macOS password autofill on a `secure` field |
| `prompt="<text>"` | Placeholder text shown inside the field (not returned in output) |
| `value="<text>"` | Pre-populate the field with a default value (editable) |
| `regex=<pattern>` | Require field content to match the regular expression |
| `regexerror=<text>` | Custom error message shown when the regex is not satisfied |
| `editor` | Multi-line text editor instead of a single-line field |
| `isdate` | Replace the text field with a date picker. Output is formatted as a short date string. |
| `fileselect` | Add a Select button that opens a file picker |
| `filetype=<types>` | Restrict the file picker to the specified types (space-separated). Use file extensions (e.g. `png jpg`) or the type keywords `folder`, `image`, `movie`, `video`, `audio`. |
| `path=<path>` | Set the initial directory for the file picker |
| `confirm` | Add a confirmation field whose content must match the primary field |

### Name

`name=<text>` replaces the label as the key in output. Useful when you want a friendly label but a cleaner key name in the output.

### Secure

`secure` hides input as it is typed, and shows a lock icon. Content is still returned as plain text on stdout.

```sh
--textfield "Password,secure"
```

![image](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

### Password Fill

`passwordfill` enables the macOS password autofill feature. Must be combined with `secure`.

```sh
--textfield "Password,secure,passwordfill"
```

### Required

`required` prevents swiftDialog from exiting until the field has a value. Required fields are marked with an `*` and highlighted when the user attempts to dismiss without filling them in.

```sh
--textfield "Full Name,required"
```

![image](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)

### Prompt

`prompt="<text>"` shows placeholder text inside the field. The text disappears once the user starts typing and is not included in the output. Not supported on `secure` fields.

```sh
--textfield "Name,prompt="Enter your full name""
```

![image](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

### Value

`value="<text>"` pre-populates the field with a default value that the user can edit.

```sh
--textfield "Default Value Test",value="Some default value"
```

![image](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

### Regex and Regex Error

`regex=<pattern>` requires the field content to match the regular expression before swiftDialog will exit. `regexerror=<text>` sets the message shown when the pattern is not matched.

Unless the pattern explicitly allows it, a `regex` field cannot be empty.

```sh
--textfield "Product Code",prompt="Enter 5 digit code",regex="\d{5}",regexerror="Must be a five digit number"
```

![image](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

Use `--textfieldlivevalidation` to show a green/red overlay on the field as the user types, giving immediate feedback on whether the regex is satisfied.

### Editor

`editor` presents a larger, multi-line text area instead of a single-line field.

```sh
--textfield "Notes,editor"
```

![image](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

### Date Picker

`isdate` replaces the text field with a macOS date picker. The selected date is returned as a short date string (e.g. `3/24/2026`).

```sh
--textfield "Start Date,isdate"
```

### File Select

`fileselect` adds a **Select** button that opens a standard file picker. The chosen path is placed into the field and returned in the output.

```sh
--textfield "Config File,fileselect"
```

Use `filetype` to restrict what can be selected. Values are space-separated and can be file extensions or type keywords:

| Value | Selects |
|---|---|
| `folder` | Directories only |
| `image` | Any image type |
| `movie` / `video` | Any video type |
| `audio` | Any audio type |
| `<extension>` | Files matching that extension (e.g. `png`, `pdf`) |

```sh
--textfield "Select an image,fileselect,filetype=png jpg"
--textfield "Select a folder,fileselect,filetype=folder"
```

Use `path=<path>` to set the directory the file picker opens to:

```sh
--textfield "Log File,fileselect,path=/var/log"
```

![image](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

### Confirm

`confirm` adds a second field below the primary one. Both fields must contain the same value before swiftDialog will accept the input. Useful for password confirmation.

```sh
--textfield "Password,secure,required,confirm"
```

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### Combining Modifiers

Modifiers can be combined freely (where compatible):

```sh
--textfield "<label>,secure,required,prompt="<prompt_text>""
--textfield "<label>,required,regex="\d{5}",regexerror="Five digits required",prompt="00000""
--textfield "<label>,fileselect,filetype="jpeg jpg png",path=/Users/Shared"
```

### JSON Format

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "isdate" : true},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

## Keyboard Behaviour

Pressing **Return** in any single-line text field triggers the Button 1 action, equivalent to clicking the default button. This does not apply to `editor` fields.