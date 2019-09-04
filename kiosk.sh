#!/bin/bash

# Run this script in display 0 - the monitor
export DISPLAY=:0
 
# Hide the mouse from the display
unclutter &
 
# If Chrome crashes (usually due to rebooting), clear the crash flag so we don't have the annoying warning bar
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences
sleep 8
ip=$(
    ifconfig wlan0 |
    perl -ne 'print $1 if /inet\s.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b/'
)
 
# Run Chromium and open tabs
/usr/bin/chromium-browser --window-size=480,320 --incognito --disable-pinch --overscroll-history-navigation=0 --kiosk --window-position=0,0 "http://"$ip":7836"

 
# Start the kiosk loop. This keystroke changes the Chromium tab
# To have just anti-idle, use this line instead:
# xdotool keydown ctrl; xdotool keyup ctrl;
# Otherwise, the ctrl+Tab is designed to switch tabs in Chrome

while (true)
 do
  xdotool keydown ctrl+Tab; xdotool keyup ctrl+Tab;
  sleep 15
done