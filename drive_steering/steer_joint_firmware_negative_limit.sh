#!/bin/bash

echo "===================================================="
echo "       MARVIN Motion Control - Test Scripts         "
echo "       ------------------------------------         "
echo ""
echo ""
echo "Steer Joints: Go To POSITIVE_LIMIT (HOME_POSITION + 30 deg)"
echo "30 deg = 523599 urad = HOME_POSITION + 0x0007FD4F"
echo ""
echo "===================================================="
echo ""

echo "front_left_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 30 deg)"
cansend slcan0 30F#000FFFF00563

echo "front_right_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 30 deg)"
cansend slcan0 312#000FFFF00563

echo "mid_left_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 30 deg)"
cansend slcan0 31F#000FFFF00563

echo "mid_right_steer joint commanded to POSITIVE_LIMIT (HOME_POSITION + 30 deg)"
cansend slcan0 326#000FFFF00563

echo "rear_left_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 30 deg)"
cansend slcan0 303#000FFFF00563

echo "rear_right_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 30 deg)"
cansend slcan0 319#000FFFF00563
