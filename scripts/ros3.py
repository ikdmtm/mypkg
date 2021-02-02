#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

i = 0
j = 0
k = 1
n3 = 0

def cb(message):
    global i
    i = message.data
    #rospy.loginfo(message.data)

rospy.init_node('ros3')
sub = rospy.Subscriber('ros2', Int32, cb)
pub = rospy.Publisher('ros3', Int32, queue_size=1)
rate = rospy.Rate(100)

while not rospy.is_shutdown():
    j = i + 1
    if j%60 == 0:
        k += 1
    if k%100 == 0:
        n3 += 1
    if n3%60 == 0:
        n3 = 0
    pub.publish(n3)
    rate.sleep()
