#!/bin/bash

echo "Drive Joints: Stop Driving"

echo "front_left_drive_joint commanded to stop"
cansend slcan0 233#00072710

echo "front_right_drive_joint commanded to stop"
cansend slcan0 202#00072710

echo "mid_left_drive_joint commanded to stop"
cansend slcan0 207#00072710

echo "mid_right_drive joint commanded to stop"
cansend slcan0 232#00072710

echo "rear_left_drive_joint commanded to stop"
cansend slcan0 21A#00072710

echo "rear_right_drive_joint commanded to stop"
cansend slcan0 20A#00072710
