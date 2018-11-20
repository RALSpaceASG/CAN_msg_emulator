#!/bin/bash

echo "===================================================="
echo "       MARVIN Motion Control - Test Scripts         "
echo "       ------------------------------------         "
echo ""
echo ""
echo "Steer Joints: Go To POSITIVE_LIMIT (HOME_POSITION + 62 deg)"
echo ""
echo "Note this will EXCEED the imposed ROS Positive Joint Limit (+60 deg)"
echo ""
echo "62 deg = 1082104 urad = HOME_POSITION + 0x001082F8"
echo ""
echo "===================================================="
echo ""

echo "front_left_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 62 deg)"
cansend slcan0 30F#000F001082F8

echo "front_right_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 62 deg)"
cansend slcan0 312#000F001082F8

echo "mid_left_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 62 deg)"
cansend slcan0 31F#000F001082F8

echo "mid_right_steer joint commanded to POSITIVE_LIMIT (HOME_POSITION + 62 deg)"
cansend slcan0 326#000F001082F8

echo "rear_left_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 62 deg)"
cansend slcan0 303#000F001082F8

echo "rear_right_steer_joint commanded to POSITIVE_LIMIT (HOME_POSITION + 62 deg)"
cansend slcan0 319#000F001082F8
