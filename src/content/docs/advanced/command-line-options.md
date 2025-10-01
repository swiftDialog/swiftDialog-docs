---
title: Command Line Options
description: Complete reference for all swiftDialog command line options and arguments
---

Dialog is pretty boring by itself. Use the following commandline options to spruce it up a bit.

you can also optionally configure dialog using [JSON](/advanced/json-configuration)


## Arguments

    swiftDialog v2.5.1.4775
    ©2024 Bart Reardon


    use --help <option> for more details

    -t,  --title <text>

        Set the Dialog title

    --subtitle <text>

        Text to use as subtitle when sending a system notification

    -m,  --message <text>

        Set the dialog message

    --style presentation | mini | centered | alert | caution | warning

        Configure a pre-set window style

    --messagealignment [left | centre | center | right]

        Set the message alignment

    --messageposition [top | centre | center | bottom]

        Set the message position

    --helpmessage <text>

        Enable help button with content <text>

    -i,  --icon <file> | <url>

        Set the dialog icon

    --iconsize <num>

        Set the dialog icon size

    --iconalpha <num>

        Set the dialog icon transparancy

    -y,  --overlayicon <file> | <url>

        Set an image to display as an overlay to --icon

    -n,  --bannerimage <file> | <url>

        Enable banner image

    --bannertitle <text>

        Enable title within banner area

    --bannertext <text>

        Set text to display in banner area

    --button1text <text>

        Set the label for Button1

    --button1action <url>

        Set the Button1 action

    --button2text <text>

        Displays Button2 with <text>

    --button2action <text>

        Custom Actions For Button 2 Is Not Implemented

    --infobuttontext <text>

        Displays info button with <text>

    --infobuttonaction <url>

        Set the info button action

    --buttonstyle center|centre|stack

        Configure how the button area is displayed

    --selecttitle <text>(,radio|required,name="<text>")

        Select list name

    --selectvalues <csv>

        Select list values

    --selectdefault <text>

        Default select list value

    --titlefont <text>

        Lets you modify the title text of the dialog

    --messagefont <text>

        Set the message font of the dialog

    --textfield <text>[,required,secure,prompt="<text>",name="<text>"]

        Enable a textfield with the specified label

    --checkbox <text>

        Enable a checkbox with the specified label

    --checkboxstyle default|checkbox|switch[,<size>]

        Change the appearance of checkboxes

    --timer [<seconds>]

        Enable countdown timer (with <seconds>)

    --progress [<int>]

        Enable interactive progress bar

    --progresstext <text>

        Enable the progress text with <text>

    -g,  --image <file> | <url>

        Display an image

    --imagecaption <text>

        Display a caption underneath an image

    --width <number>

        Set dialog window width

    --height <number>

        Set dialog window height

    -bg,  --background <file>

        Set a dialog background image

    -ba,  --bgalpha <number>

        Set background image transparancy

    -bp,  --bgposition [topleft | left | bottomleft | top | center/cetre | bottom | topright | right | bottomright]

        Set background image position

    -bf,  --bgfill [fill | fit]

        Set background image fill type

    -bs,  --bgscale [fill | fit]

        Enable background image scaling

    --position [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]

        Set dialog window position

    --positionoffset <int>

        Set dialog window position offset

    --video <file> | <url>

        Display a video

    --videocaption <text>

        Display a caption underneath a video

    --debug (<colour>)

        Enable debug mode

    --jsonfile <file>

        Read dialog settings from JSON formatted <file>

    --jsonstring <text>

        Read dialog settings from JSON formatted <string>

    --commandfile [<file>]

        Set command file path

    --listitem <text>

        Enable a list item with the specified label

    --liststyle <text>

        Set list style [expanded|compact]

    --infotext <text>

        Display <text> in place of info button

    --infobox <text>

        Display <text> in info box

    --quitkey <char>

        Set dialog quit key

    --webcontent <url>

        Display a web page

    -k,  --key <string>

        Use the specified authentication key to allow dialog to launch

    --checksum <string>

        Generate a SHA256 value

    --displaylog <file>

        Open a file and display the contents as it is being written

    --vieworder <csv>

        Change the order in which some items are displayed

    --appearance [dark|light]

        Set the preferred window appearance

    --button1disabled <text>

        Disable Button1

    --button2disabled <text>

        Disable Button2

    -2,  --button2

        Displays Button2

    -3,  --infobutton

        Displays info button

    -v,  --version

        Print version string

    -h,  --hideicon <text>

        Hides the icon from view

    --centreicon <text>

        Set icon to be in the centre

    --help [<argument>]

        Print help

    -l,  --licence

        Print license

    --hidetimerbar <text>

        Hide countdown timer if enabled

    --autoplay <text>

        Enable video autoplay

    --blurscreen

        Blur screen content behind dialog window

    --notification <text>

        Send a system notification

    -o,  --moveable

        Enable dialog to be moveable

    -p,  --ontop

        Enable dialog to be always positioned on top of other windows

    -s,  --small

        Enable 25% decrease in default window size

    -b,  --big

        Enable 25% increase in default window size

    -f,  --fullscreen

        Enable full screen view

    --quitoninfo

        Quit when info button is selected

    -j,  --json

        Enable JSON output

    -jh,  --jh

        Enable jamfHelper mode

    --mini

        Enable mini mode

    --presentation

        Enable presentation mode

    --windowbuttons [close,min,max]

        Enables window buttons

    --resizable

        Enable the dialog window to be resizable

    --showonallscreens

        Enable the dialog window to appear on all screens

    --loginwindow

        Enable the dialog window to be shown at login

    --hidedefaultkeyboardaction

        Hides the default behaviour of Return ↵ and Esc ⎋ keys