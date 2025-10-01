---
title: Nudge-style Update Script
description: Basic macOS update prompt script using swiftDialog
---

If you want a comprehensive way to nudge people to update their version of macOS 11+ then you should use [Nudge](https://github.com/macadmins/nudge).

If your needs are less stringent though this is a basic script that will issue a prompt to get the user to run software update.

```bash
#!/bin/zsh

# gheto nudge like script using dialog with jamfjelper has a backup
#
#  Created by Bart Reardon on 15/9/21.
#
# TODO: move a bunch of these variables into parameters that can be called from jamf
#

dialogcli="/usr/local/bin/dialog"
jamfhelper="/Library/Application Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper"

OSVer=$(sw_vers | grep "ProductVersion" | awk '{print $NF}')
buildVer=$(sw_vers | grep "BuildVersion" | awk '{print $NF}')
#requiredOSVer="10.15.7 Security Update 2021-005"
#requiredBuildVer="19H1417" # 10.15.7 Security Update
requiredOSVer="11.6.0"
requiredBuildVer="20G165" # 11.6.0

if [[ "${buildVer}" == "${requiredBuildVer}" ]] || [[ "${requiredOSVer}" == "${OSVer}"* ]]; then
    # catch if we're already on the build we want
    # is explicit but should catch deployments that haven't checked in to the MDM with the updated OS version
    #exit 0
fi

updateselected=0
persistant=0 # set this to 1 and the popup will persist until the update is performed

title="Important Security Update Required"
titlefont="colour=red"
message="### ⚠️You are running macOS version ${OSVer}

It is important that you update to **macOS ${requiredOSVer}** at your earliest convenience

macOS ${requiredOSVer} contains important security updates and fixes a critical vulnerability

**Your swift attention to applying this update is appreciated**"
infotext="More Information"
infolink="https://support.apple.com/en-us/HT212804" # 11.6.0
#infolink="https://support.apple.com/en-au/HT212600" # 10.15.7 Security Update
icon="/System/Library/PreferencePanes/SoftwareUpdate.prefPane"
#icon="/Applications/Self Service.app"
overlay="caution"
button1text="Open Software Update"
buttona1ction="open -b com.apple.systempreferences /System/Library/PreferencePanes/SoftwareUpdate.prefPane"
button2text="Contact the Service Centre"
button2action="https://link.to/servicecentre.html"

runDialog () {
    ${dialogcli} -p -o -d --title "${title}" \
                         --titlefont ${titlefont} \
                         --overlayicon "${overlay}" \
                         --icon "${icon}" \
                         --message "${message}" \
                         --infobuttontext "${infotext}" \
                         --infobuttonaction "${infolink}" \
                         --button1text "${button1text}" \
                         --button2text "${button2text}"

    processExitCode $?
}

runJamfHelper () {
    # Need to change the logo and button text for use with jamfHelper
    logoimage="/Library/Security/PolicyBanner.rtfd/logo_colour_100x100.png"
    if [[ -e "${logoimage}" ]]; then
        icon="${logoimage}"
    else
        # system help icon in case
        icon="/System/Library/CoreServices/HelpViewer.app/Contents/Resources/AppIcon.icns"
    fi
    button1text="Open Update"
    button2text="More Info"

    "${jamfhelper}" -windowType utility \
                    -title "${title}" \
                    -description "${message}" \
                    -icon "${icon}" \
                    -button1 "${button1text}" \
                    -button2 "${button2text}" \
                    -defaultButton 1
    processExitCode $?
}

processExitCode () {
    exitcode=$1
    if [[ $exitcode == 0 ]]; then
        updateselected=1
        open -b com.apple.systempreferences /System/Library/PreferencePanes/SoftwareUpdate.prefPane
    elif [[ $exitcode == 2 ]]; then
        currentUser=$(echo "show State:/Users/ConsoleUser" | scutil | awk '/Name :/ { print $3 }' )
        uid=$(id -u "$currentUser")
        launchctl asuser $uid open "${button2action}"
  	elif [[ $exitcode == 3 ]]; then
  		updateselected=1
    fi
}

while [[ ${persistant} -eq 1 ]] || [[ ${updateselected} -eq 0 ]]
do
    if [[ -e "${dialogcli}" ]]; then
        runDialog
    elif [[ -e "${jamfhelper}" ]]; then
        runJamfHelper
    else
        # well something is up if dialog and jamfHelper are both missing - force an exit
        updateselected=1
    fi
done

exit 0
```