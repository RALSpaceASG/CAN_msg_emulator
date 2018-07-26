#!/bin/bash

echo "Steer Joints: Go To HOME_POSITION"

echo "front_left_steer_joint commanded to HOME_POSITON"
cansend slcan0 30F#000F00000000

echo "front_right_steer_joint commanded to HOME_POSITION"
cansend slcan0 312#000F00000000

echo "mid_left_steer_joint commanded to HOME_POSITION"
cansend slcan0 31F#000F00000000

echo "mid_right_steer joint commanded to HOME_POSITION"
cansend slcan0 326#000F00000000

echo "rear_left_steer_joint commanded to HOME_POSITION"
cansend slcan0 303#000F00000000

echo "rear_right_steer_joint commanded to HOME_POSITION"
cansend slcan0 319#000F00000000
