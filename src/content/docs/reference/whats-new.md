---
title: What's New
description: Recent features and updates in swiftDialog
---

## swiftDialog 2.2

### What's New

- Select lists (aka drop down lists) can now be tagged as required via a property on `--selecttitle` #240
   - `--selecttitle "This one is required",required --selecttitle "This one is not"`

    <img width="350" alt="image" src="https://user-images.githubusercontent.com/3598965/234566934-052803e6-5a40-402c-9e38-770a88d17bca.png">
- New option `--checkboxstyle` option, arguments are `checkbox` or `switch`. Sets the checkbox style to use switch style or checkbox style
   - `switch` style has additional options, large, regular, small, mini.
   - `switch` style also allows for display of icons
   - All options are available via command line arguments or json
   -  `--checkboxstyle "<style>"`
    <img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-60c3-46aa-9a11-041aeeca8ffc.png" width="350">
 - Select lists can now be displayed as radio buttons using the `radio` modifier on `--selecttitle`
   - e.g. `--selecttitle "Test list",radio --selectvalues "Item One, Item Two, Item Three"`
   <img src="https://user-images.githubusercontent.com/3598965/235853959-8b3c9899-8fc5-4e8f-ae90-e8a950ed7eed.png" width="350">
 - Select lists can have dividers within the list by adding `---` as a value wherever one is required
   - <img src="https://user-images.githubusercontent.com/3598965/235856053-f9f20959-f5a5-4d14-8069-b3defd2e115c.png" width="350">
 - Labels on input fields such as textfields, select lists and checkboxes are no longer bold. All user input areas have a subtle background
   <img src="https://user-images.githubusercontent.com/3598965/235856540-5f7c965b-6fe8-4466-99b0-a84f6b254ca5.png" width="350">

### More New Stuff

 - New `helpmessage` command to update help message text from the command file #248
   - `echo "helpmessage: Updated message to be displayed in the help sheet" >> /var/tmp/dialog.log`
 - New `activate` command to bring swiftDialog to the front #221
   - `echo "activate:" >> /var/tmp/dialog.log`
 - New option `--iconalpha` can set an alpha value for `--icon`. Values are from 0.0 (transparent) to 1.0 (opaque)
   - `--iconalpha 0.5`
   - `echo "iconalpha: 0.5" >> /var/tmp/dialog.log`
 - Progress bar can be shown while displaying a video or image or pretty much any time

### Other Changes

 - Label and input font size will change proportionally with `--messagefont`
 - Simplified overlay icon view. It now uses the same view as icon with the only addition of the background layer for SF symbols
 - Fixed an issue when resetting required field alert state
 - Fixed an issue where multiple required fields were not represented in the error sheet
 - Added some additional logic to notification authorisation detection to print more useful authorisation state
 - Updated - Added ability to specify multiple files for on textfields #260
 - Updated log function (more logging will be added over time)
 - Cleaned up a bunch of old commented out code and other boring code stuff
 - Fixed - fallback error image for banners #239 #217
 - Fixed - `--quitkey` not functioning in --mini mode is fixed #253
 - Updated `--help`. With no arguments help lists all options and a brief note. `--help <option>` will give detailed information on that option
   - `--help checkboxstyle`
 - Updated - `--messageposition` now works for top centre and bottom to position the message elements vertically.
 - Updated - `--blurscreen` blurs all spaces as well as all screens on multi monitor setups
 - Updated - Main dialog window is movable (when enabled) by clicking anywhere on the window instead of clicking the non-visible title bar

The pkg for this release is now distribution style ( #250 ) so can be deployed as a pre-stage package without modification. This makes it easier to deploy and run at the setup assistant - how to do that reliably at the time you want it to run is an exercise left to the reader