#!/bin/bash

echo "Initialising CAN Interface to USBtin device"

slcan_attach -f -s8 -o $1
slcand $1 slcan0
sudo ifconfig slcan0 up
