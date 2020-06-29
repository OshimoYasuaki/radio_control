#!/usr/bin/env python 
import rospy
from sensor_msgs.msg import Joy

def joy_control(joy_msg):
    forward = joy_msg.buttons[13]
    back = joy_msg.buttons[14]
    left = joy_msg.buttons[15]
    right = joy_msg.buttons[16]

    if forward == 1:

    elif back == 1:

    elif right == 1:

    elif left == 1:

if __name__ == '__main__':
    rospy.init_node('control')
    rospy.Subscriber('Joy',joy_control,queue =1)
    rospy.spin()
