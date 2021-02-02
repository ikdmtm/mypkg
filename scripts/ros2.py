#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

i = 0
j = 0
n2 = 0

def cb(message):
    global i
    i = message.data
    #rospy.loginfo(message.data)

rospy.init_node('ros2')
sub = rospy.Subscriber('ros1', Int32, cb)
pub = rospy.Publisher('ros2', Int32, queue_size=1)
rate = rospy.Rate(100)

while not rospy.is_shutdown():
    j = i + 1
    if j%100 == 0:
        n2 += 1
    if n2%60 == 0:
        n2 = 0
    pub.publish(n2)
    rate.sleep()
