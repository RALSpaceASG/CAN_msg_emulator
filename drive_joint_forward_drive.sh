#!/bin/bash

echo "Drive Joints: Drive Forward"

echo "front_left_drive_joint commanded to drive forward"
cansend slcan0 233#000F2710

echo "front_right_drive_joint commanded to drive forward"
cansend slcan0 202#000F2710

echo "mid_left_drive_joint commanded to drive forward"
cansend slcan0 207#000F2710

echo "mid_right_drive joint commanded to drive forward"
cansend slcan0 232#000F2710

echo "rear_left_drive_joint commanded to drive forward"
cansend slcan0 21A#000F2710

echo "rear_right_drive_joint commanded to drive forward"
cansend slcan0 20A#000F2710
