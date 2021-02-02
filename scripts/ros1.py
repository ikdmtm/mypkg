#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('ros1')
pub = rospy.Publisher('ros1', Int32, queue_size=1)
rate = rospy.Rate(100)

n = 0

while not rospy.is_shutdown():
    n += 1
    if n%100==0:
        n = 0
    pub.publish(n)
    rate.sleep()
