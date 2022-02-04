#!/usr/bin/env python3

import rospy
# import turtlesim/Pose to read the turtle position
from turtlesim.msg import Pose

def pose_callback(data):
	# get turtle x and y positions
	turt_x = data.x
	turt_y = data.y
