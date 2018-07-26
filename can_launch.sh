#!/bin/bash

echo "Initialising CAN Interface to USBtin device"

slcan_attach -f -s8 -o $1
slcand $1 $2
sudo ifconfig $2 up
