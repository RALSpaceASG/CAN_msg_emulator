#!/bin/bash

echo "===================================================="
echo "       MARVIN Motion Control - Test Scripts         "
echo "       ------------------------------------         "
echo ""
echo "Steer Joints: Go To HOME_POSITION + 50 deg"
echo "50 deg = 872665 urad = HOME_POSITION + 0x000D50D9"
echo ""
echo "===================================================="
echo ""

echo "front_left_steer_joint commanded to HOME_POSITON + 50 deg"
cansend slcan0 30F#000F000D50D9

echo "front_right_steer_joint commanded to HOME_POSITION + 50 deg"
cansend slcan0 312#000F000D50D9

echo "mid_left_steer_joint commanded to HOME_POSITION + 50 deg"
cansend slcan0 31F#000F000D50D9

echo "mid_right_steer joint commanded to HOME_POSITION + 50 deg"
cansend slcan0 326#000F000D50D9

echo "rear_left_steer_joint commanded to HOME_POSITION + 50 deg"
cansend slcan0 303#000F000D50D9

echo "rear_right_steer_joint commanded to HOME_POSITION + 50 deg"
cansend slcan0 319#000F000D50D9
