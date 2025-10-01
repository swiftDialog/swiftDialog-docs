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

## Textfields Properties

Textfields can have one or more of the following properties:

 - `name`
 - `secure`
 - `required`
 - `prompt` (only available in macOS 12+)
 - `regex`
 - `regexerror`
 - `editor`
 - `fileselect`
 - `filetype`
 - `confirm`

#### Name

`name=<text>` will use the name value in output as the key instead of the title.

#### Secure

`secure` creates a field that hides the input as it is being typed. A lock icon indicates a field has this property.

_as a note of caution, if using a secure field to accept passwords, be aware that the entered string will still appear in cleartext when returned to stdout_

![image](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

#### Required

`required` creates a field that must be filled in before swiftDialog will exit. If a field is not filled, a highlight will appear indicating which field(s) require input. The title will be appended with an `*` character and the text `Required fields` will appear as a subtext to the list of text fields.

![image](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)


![image](https://user-images.githubusercontent.com/3598965/159698462-a9199a76-4bcf-4825-908c-48845a6c6cb2.png)

#### Prompt

`prompt="<prompt_text>` will inset some prompt text into the textfield. This text is not returned to stdout and disappears once you start typing in the text field area

![image](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

** Prompt text is macOS 12 only and is not supported on secure fields.

#### Value

`value="<default text>"` will pre-populate the textfield with the specified value.

This differs from `prompt` in that the text can be edited

`--textfield "Default Value Test",value="Some default value"`

![image](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

#### Regex and Regex Error

`regex=<regular_expression>` will require that the textfeld match the expression.

`regexerror=<text>` is the error message that will be presented if the text entered does not meet the regular expression requirements

Example:

`--textfield "Regex Test",prompt="Enter 5 digit product code",regex="\d{5}",regexerror="Code must be a five digit number"`

![image](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

![image](https://user-images.githubusercontent.com/3598965/171410903-6355bd92-17ea-47ea-be5e-d229d96ae837.png)

**NOTE:** Unless the regex allows it, using `regex` implies that the field cannot be empty and the error prompt will be displayed if and entry is not made.

#### Editor

`editor` will present a text field that is larger and can accept multiple lines of text if detailed responses are required.

`--textfield "Editor Demo:,editor"`

![image](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

#### Fileselect and Filetype

`fileselect` will add a "Select" button to the textfield to allow selection of a file using the standard file selection sheet. The path of the selected file will be placed into the contents of the textfield. No other action is taken on the file.

Optionally `filetype=<file_extension>` can limit the selection to only allowable filetypes. e.g. `filetype=png` would only allow files with the `.png` extension to be selected in the file selection sheet.

Multiple filetypes can be specified as space separated list, e.g. `filetype="jpeg jpg png"`

`--textfield "Select a file,fileselect"`

`filetype=folder` will allow selection of a folder

![image](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

#### Confirm

`confirm` will add a secondary textfield whose contents need to match the primary one for validation to succeed.

This can be combined with one or more other modifiers like `secure`, `required` and `regex`

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### Use

The added properties are optional and can be invoked on the command line by separating the properties with a comma (no spaces). For example:

`--textfield <field_label>,secure,required,prompt="<promt_text>"`

or in json with:

```json
{
  "textfield" : [
    {"title" : "<field_label>", "secure" : true, "required" : true, "prompt" : "<prompt_text>" },
    {"title" : "<field_label>", "editor" : true },
    {"title" : "<field_label>", "fileselect" : true, "filetype" : "<file_extension>" }
  ]
}
```