#!/bin/bash

echo "===================================================="
echo "       MARVIN Motion Control - Test Scripts         "
echo "       ------------------------------------         "
echo ""
echo "Steer Joints: Go To HOME_POSITION - 50 deg"
echo "50 deg = 872665 urad => HOME_POSITION + 0xFFF2AF27 (2'sC)"
echo ""
echo "===================================================="
echo ""

echo "front_left_steer_joint commanded to HOME_POSITON - 50 deg"
cansend slcan0 30F#000FFFF2AF27

echo "front_right_steer_joint commanded to HOME_POSITION - 50 deg"
cansend slcan0 312#000FFFF2AF27

echo "mid_left_steer_joint commanded to HOME_POSITION - 50 deg"
cansend slcan0 31F#000FFFF2AF27

echo "mid_right_steer joint commanded to HOME_POSITION - 50 deg"
cansend slcan0 326#000FFFF2AF27

echo "rear_left_steer_joint commanded to HOME_POSITION - 50 deg"
cansend slcan0 303#000FFFF2AF27

echo "rear_right_steer_joint commanded to HOME_POSITION - 50 deg"
cansend slcan0 319#000FFFF2AF27
