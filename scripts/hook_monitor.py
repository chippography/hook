#!/usr/bin/env python

# ROS Publisher Node talker.py from:
#    https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#
# Raspberry PI Button code from:
#    https://gpiozero.readthedocs.io/en/stable/recipes.html

import rospy

from hook.msg import Handset

from gpiozero import Button

# def talker():
#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()
#         rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         rate.sleep()

def picked_up():
    global pub
    pub_str = "PICKED UP %s" % rospy.get_time()
    rospy.loginfo(pub_str)
    pub.publish(Handset(stamp=rospy.Time.now(), picked_up=True))

def hung_up():
    global pub
    pub_str = "HUNG UP %s" % rospy.get_time()
    rospy.loginfo(pub_str)
    pub.publish(Handset(stamp=rospy.Time.now(), picked_up=False))

def hook_monitor():
    # Set-up Publisher
    global pub
    pub = rospy.Publisher('hook', Handset, queue_size=10)
    rospy.init_node('hook_monitor', anonymous=True)

    # Set-up Button
    button = Button(4) # PIN 7 is GPIO4, API uses GPIO_ pin numberings
    button.when_pressed = picked_up
    button.when_released = hung_up

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        hook_monitor()
    except rospy.ROSInterruptException:
        pass
