#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def joy_cb(joy_msg):
    lmoter = "/dev/rtmotor_raw_l0"
    rmoter = "/dev/rtmotor_raw_r0"
    onoff_motor = open("/dev/rtmotoren0",'w')
    if joy_msg.buttons[9] == 1:
        print("on")
        onoff_motor.write('1/n')
        onoff_motor.close()

    elif joy_msg.buttons[10] == 1:
        print("off")
        onoff_motor.write('0/n')
        onoff_motor.close()

    elif joy_msg.buttons[13] == 1 :
        print("up")
        l_file = open(lmoter,'w')
        r_file = open(rmoter,'w')
        l_file.write('300\n')
        r_file.write('300\n')
        l_file.close()
        r_file.close()

    elif joy_msg.buttons[14] == 1:
        print("down")
        l_file = open(lmoter,'w')
        r_file = open(rmoter,'w')
        l_file.write('-300\n')
        r_file.write('-300\n')
        l_file.close()
        r_file.close()

    elif joy_msg.buttons[15] == 1:
        print("left")
        r_file = open(rmoter,'w')
        r_file.write('300\n')
        r_file.close()

    elif joy_msg.buttons[16] == 1:
        print("right")
        l_file = open(lmoter,'w')
        l_file.write('300\n')
        l_file.close()

    elif joy_msg.buttons[6] == 1:
        print("turn_l")
        l_file = open(lmoter,'w')
        r_file = open(rmoter,'w')
        l_file.write('-300\n')
        r_file.write('300\n')
        l_file.close()
        r_file.close()

    elif joy_msg.buttons[7] == 1:
        print("turn_r")
        l_file = open(lmoter,'w')
        r_file = open(rmoter,'w')
        l_file.write('300\n')
        r_file.write('-300\n')
        l_file.close()
        r_file.close()

    else:
        print("stop")
        l_file = open(lmoter,'w')
        r_file = open(rmoter,'w')
        l_file.write('0\n')
        r_file.write('0\n')
        l_file.close()
        r_file.close()

if __name__ == '__main__':
    rospy.init_node('joy_motor')
    sub = rospy.Subscriber('joy',Joy,joy_cb,queue_size = 1)
    rospy.spin()
