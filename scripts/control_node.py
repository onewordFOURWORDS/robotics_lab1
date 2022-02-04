#!/usr/bin/env python3

import rospy
# import turtlesim/Pose to read the turtle position
from turtlesim.msg import Pose
# import geometry_msgs/Twist for turtle control
from geometry_msgs.msg import Twist
# import the message we created in this package
from robotics_lab1.msg import Turtlecontrol


# variables to be used in proportional control
kp = 0
xd = 0
xt = 0

def pose_callback(data):
	global xt
	# get xt (x position of turtle)
	xt = data.x
	
def turtlecontrol_callback(data):
	global kp
	global xd
	# get kp (control gain)
	kp = data.kp
	# get xd (desired turtle position)
	xd = data.xd
	
	
def main():
	# initilize the ROS node
	rospy.init_node('control_node' , anonymous = True)
	
	
	# add first subscriber to read turtle position info
	rospy.Subscriber('turtle1/pose', Pose, pose_callback)
	# add second subscriber to read turtle control position
	rospy.Subscriber('robotics_lab1/msg', Turtlecontrol, turtlecontrol_callback)
	
	
	# declare a publisher to publish turtle velocity commands
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size = 10)
	
	
	# define a loop rate and set the frequency to 10 Hz
	loop_rate = rospy.Rate(10)
	
	# declare a variable of type Twist (just an empty message)
	vel_cmd = Twist()

	
	
	
	
	
	# run a control loop on a regular basis (every 0.1 seconds)
	while not rospy.is_shutdown():

		# Calculate the proportional velocity
		vel_cmd.linear.x = kp*(xd - xt)
	
		# publish the calculated velocity to the turtle
		cmd_pub.publish(vel_cmd)
		
		loop_rate.sleep()

if __name__ == '__main__':
	main()
