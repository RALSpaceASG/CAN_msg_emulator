#!/bin/bash

echo "===================================================="
echo "       MARVIN Motion Control - Test Scripts         "
echo "       ------------------------------------         "
echo ""
echo "Steer Joints: Go To HOME_POSITION + 10 deg"
echo "10 deg = 174533 urad = HOME_POSITION + 0x0002A9C5"
echo ""
echo "===================================================="
echo ""

echo "front_left_steer_joint commanded to HOME_POSITON + 10 deg"
cansend slcan0 30F#000F0002A9C5

echo "front_right_steer_joint commanded to HOME_POSITION + 10 deg"
cansend slcan0 312#000F0002A9C5

echo "mid_left_steer_joint commanded to HOME_POSITION + 10 deg"
cansend slcan0 31F#000F0002A9C5

echo "mid_right_steer joint commanded to HOME_POSITION + 10 deg"
cansend slcan0 326#000F0002A9C5

echo "rear_left_steer_joint commanded to HOME_POSITION + 10 deg"
cansend slcan0 303#000F00029AC5

echo "rear_right_steer_joint commanded to HOME_POSITION + 10 deg"
cansend slcan0 319#000F00029AC5
