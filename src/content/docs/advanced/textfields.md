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

Use the `date` or `time` modifier to replace the text field with a macOS date/time picker. The selected value is returned as a formatted string.

```sh
--textfield "Start Date,date"
--textfield "Start Time,time"
--textfield "Start Date and Time,date,time"
```

**Note:** The `isdate` modifier has been deprecated in favour of `date` and `time`.

#### Date Bounds

Use `mindate=` and `maxdate=` to restrict the selectable date range:

```sh
--textfield "Pick a day,date,mindate=20260901,maxdate=20260930"
--textfield "No earlier than today,date,mindate=20260928"
--textfield "Before end of year,date,maxdate=20261231"
```

**Format:** Dates must be in `YYYYMMDD` format (region-proof). Separators are accepted and stripped (e.g., `2026-09-30` → `20260930`). Invalid dates are ignored and the bound is not applied.

#### Date Format

Use `format=` to specify the return format using strftime syntax:

```sh
--textfield "Select date,date,format=+%Y-%m-%d"
--textfield "Get epoch,date,value=20260901,format=+%s"
```

Common format strings:
- `+%Y-%m-%d` - ISO 8601 format (e.g., `2026-09-29`)
- `+%s` - Unix timestamp (seconds since epoch)
- `+%x` - Locale's date representation
- `+%D` - US format (e.g., `09/29/26`)

#### Seeding the Date Picker

Use `value=` to set the initial date. The picker accepts multiple formats:

```sh
--textfield "Start date,date,value=2026-09-30"
--textfield "Start date,date,value=September 30, 2026"
--textfield "Start date,date,value=1759132800"
```

Supported formats: ISO 8601, locale-specific, 12/24-hour, epoch timestamps, and natural language.

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

Text fields can be specified as JSON in two ways:

#### Whole-Config JSON

When using a JSON configuration file or `--jsonstring`/`--jsonfile`, specify text fields as an array:

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "date" : true, "mindate" : "20260901", "maxdate" : "20260930", "format" : "+%Y-%m-%d"},
    {"title" : "<label>", "time" : true, "value" : "14:30"},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

#### Per-Argument JSON Configuration

From 3.1.1, text fields can also be specified as JSON objects via `--textfield` (instead of using comma-separated modifiers). This provides more direct control and is especially useful for complex configurations.

**Syntax:**
```bash
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'
```

**Properties:**
- `title` - The field label text
- `name` - Alternative output key name
- `required` - Field must be filled (true/false)
- `secure` - Hide input as it is typed (password field)
- `passwordfill` - Enable macOS password autofill (requires `secure`)
- `prompt` - Placeholder text shown inside the field
- `value` - Pre-populate the field with a default value
- `regex` - Require field content to match the regular expression
- `regexerror` - Custom error message shown when regex is not satisfied
- `editor` - Multi-line text editor instead of single-line field
- `date` - Replace field with date picker (true)
- `time` - Replace field with time picker (true)
- `mindate` - Minimum selectable date (YYYYMMDD format)
- `maxdate` - Maximum selectable date (YYYYMMDD format)
- `format` - Return format using strftime syntax (e.g., `+%Y-%m-%d`, `+%s`)
- `fileselect` - Add a Select button that opens a file picker
- `filetype` - Restrict file picker to specific types (space-separated extensions or keywords)
- `path` - Initial directory for file picker
- `confirm` - Add confirmation field that must match primary field

**Examples:**

```bash
# Basic required field with prompt
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'

# Secure field with password fill
dialog --textfield '{"title":"Password","secure":true,"passwordfill":true,"prompt":"Enter password"}'

# Date picker with bounds
dialog --textfield '{"title":"Select Date","date":true,"mindate":"20260901","maxdate":"20260930","format":"+%Y-%m-%d"}'

# Time picker with default value
dialog --textfield '{"title":"Select Time","time":true,"value":"14:30"}'

# File picker with restrictions
dialog --textfield '{"title":"Select Config","fileselect":true,"filetype":"json plist","path":"/Library/Preferences"}'

# Multi-line editor
dialog --textfield '{"title":"Notes","editor":true}'

# Regex validation
dialog --textfield '{"title":"Product Code","prompt":"Enter 5 digit code","regex":"\\d{5}","regexerror":"Must be a five digit number"}'

# Confirmation field
dialog --textfield '{"title":"Password","secure":true,"required":true,"confirm":true}'
```

**Date picker fields:**
- Use `"date": true` or `"time": true` (or both) to create a picker
- `"mindate"` and `"maxdate"` accept dates in `YYYYMMDD` format (separators are stripped)
- `"format"` sets the return format using strftime syntax
- `"value"` seeds the initial date/time in multiple formats (ISO, locale, epoch, natural language)

**All modifiers supported:** Every modifier available in CSV form is also available as a JSON key.

**Multiple text fields:**

```bash
dialog --textfield '{"title":"First Name","required":true}' \
       --textfield '{"title":"Last Name","required":true}' \
       --textfield '{"title":"Email","regex":".+@.+\\..+","prompt":"user@example.com"}'
```

**Note:** When using per-argument JSON, each `--textfield` is independent. The whole-config JSON form is still supported for batch initialization.

## Keyboard Behaviour

Pressing **Return** in any single-line text field triggers the Button 1 action, equivalent to clicking the default button. This does not apply to `editor` fields.