---
title: Data Entry - Textfields
description: Edit the properties and appearance of a dialog window and output the results as a json config
---

Configure `--textfield` entries

<img width="500" alt="image" src="/src/content/docs/builder/assets/builder_textfields.png" />

Click the `[+]` button to add an new entry

Click the trash icon to remove an entry


<img width="500" alt="image" src="/src/content/docs/builder/assets/builder_textfields_popualated.png" />


## Properties

The following properties can be set

#### Format output as JSON

Sets the output format. This property is shared with [checkboxes](/builder/checkboxes/)

#### Required

Sets the `required` flag. 

#### Confirm

Sets the `confirm` flag. Enabling this will show a duplicate textfield for the configured entry

#### File Select

Enables the `fileselect` button

##### File Type

Used with `fileselect`. Enter in the desired filetype (or types as a csv) e.g. `"png,jpg"`

##### Initial Path

Used with `fileselect`. Sets the initial path to use with displaying the file select dialog

#### Title

Sets the textfield title/label

#### Name

Sets the textfield name. If used, this value will represent this entry in the output instead of the label

#### Default Value

Set the default value to display in the textfield. This content will appear in output

#### Prompt

Sets a prompt to display in the textfield. This content will not appear in output

#### Regex

Set a regex that the content of the textfield must match 

#### Regex Error

Set the error to display when textfield content does not match the provided regex

[Back](/builder/builder/)