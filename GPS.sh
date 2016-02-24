#! /bin/bash
# Start GPS

echo DO NOT CLOSE THIS WINDOW WHILE WARDRIVING!!! Just minimise it...
service gpsd stop
killall gpsd
gpsd -D 5 -N /dev/ttyUSB0

