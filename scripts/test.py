#!/usr/bin/env python3

import rospy
# read turtlesim/Pose message
from turtlesim.msg import Pose
# import math module to convert radians to degree
import math
# import geometry_msgs/Twist for turtle control
from geometry_msgs.msg import Twist

# declare constant for the angular position scales
ROTATION_SCALE = 180.0/math.pi

def pose_callback(data):

	# convert x to cm
	x_in_cm = data.x * 100
	# show the results on screen
	rospy.loginfo("x is %0.2f cm", x_in_cm)


if __name__ == '__main__':
	# intialize the node
	rospy.init_node('test', anonymous = True)
	# add subscriber to read pos info from turtle1/pos
	rospy.Subscriber('/turtle1/pos', Pose, pose_callback)

	# declare a publisher to publish turtle velocity commands
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size = 10)
	# declare a variable of type Twist (just an empty message)
	vel_cmd = Twist()
	
	loop_rate = rospy.Rate(10)

	# run a control loop on a regular basis (every 0.1 seconds)
	while not rospy.is_shutdown():
		vel_cmd.linear.x = .2
		
		# publish the calculated velocity to the turtle
		cmd_pub.publish(vel_cmd)
		
		loop_rate.sleep()
