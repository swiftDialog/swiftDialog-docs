---
title: Timer and Progress Bar
description: Creating dialogs with countdown timers and interactive progress bars
---

Dialog can be initiated with a timer that will close when the number of seconds has expired

`--timer (<seconds>)`


Replaces default button with a timer countdown after which dialog will close with exit code `4`, Default timer value is `10` seconds. Optional value `<seconds>` can be specified to the desired value. If `<seconds>` is > 60 the countdown will be rendered in `HH:MM:SS` format, e.g. 280 seconds will display `4:40` for the initial countdown.

If used in conjuction with `--button1text` the default button will be displayed but will be disabled for the first 3 seconds of the timer, after which it becomes active and can be used to dismiss dialog with the standard button 1 exit code of 0

<img width="727" alt="image" src="https://user-images.githubusercontent.com/3598965/129475759-9ba50127-8366-46a3-8288-780298142f09.png">


`--hidetimerbar` will hide the progress bar and countdown display.

Doing so forces default button to be visible to prevent un-dismissable dialogs with no indication of when the timer expires.