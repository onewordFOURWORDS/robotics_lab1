#!/usr/bin/env python3

import rospy
#import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist
# import turtlesim/Pose to read the turtle position
from turtlesim.msg import Pose
# import the message from this package
from robotics_lab1 import Turtlecontrol

def get_turt_pos(data):
	# get turtle x and y position
	turt_x = data.x
	turt_y = data.y




if __name__ == '__main__':
	# declare a publisher to publish turtle velocity commands
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size = 10)
	# initilize the ROS node
	rospy.init_node('control_publisher' , anonymous = True)
	# define a loop rate and set the frequency to 10 Hz
	loop_rate = rospy.Rate(10)
	# declare a variable of type Twist (just an empty message)
	vel_cmd = Twist()
	
	
	
	
	# run a control loop on a regular basis (every 0.1 seconds)
	while not rospy.is_shutdown():
		# set the linear velocity command
		vel_cmd.linear.x = 0.5
		# publish the velocity command
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 second and go to next step
		loop_rate.sleep()
