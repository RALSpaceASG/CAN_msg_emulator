#!/bin/bash

echo "===================================================="
echo "       MARVIN Motion Control - Test Scripts         "
echo "       ------------------------------------         "
echo ""
echo "Steer Joints: Go To HOME_POSITION - 10 deg"
echo "10 deg = 174533 urad => HOME_POSITION + 0xFFFD563B (2'sC)"
echo ""
echo "===================================================="
echo ""

echo "front_left_steer_joint commanded to HOME_POSITON - 10 deg"
cansend slcan0 30F#000FFFFD563B

echo "front_right_steer_joint commanded to HOME_POSITION - 10 deg"
cansend slcan0 312#000FFFFD563B

echo "mid_left_steer_joint commanded to HOME_POSITION - 10 deg"
cansend slcan0 31F#000FFFFD563B

echo "mid_right_steer joint commanded to HOME_POSITION - 10 deg"
cansend slcan0 326#000FFFFD563B

echo "rear_left_steer_joint commanded to HOME_POSITION - 10 deg"
cansend slcan0 303#000FFFFD563B

echo "rear_right_steer_joint commanded to HOME_POSITION - 10 deg"
cansend slcan0 319#000FFFFD563B
