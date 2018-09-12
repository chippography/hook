#!/usr/bin/env python

# ROS Publisher Node talker.py from:
#    https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
#
# Raspberry PI Button code from:
#    https://gpiozero.readthedocs.io/en/stable/recipes.html

import rospy

from hook.msg import Handset

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

def hook_faker():
    # Set-up Publisher
    global pub
    pub = rospy.Publisher('hook', Handset, queue_size=10)
    rospy.init_node('hook_faker', anonymous=True)

    # keyboard input toggles
    is_picked_up = False
    while(raw_input("Toggle Handset, (q) to quit.") != 'q'):
        is_picked_up = not is_picked_up
        if is_picked_up:
            picked_up()
        else:
            hung_up()

if __name__ == '__main__':
    try:
        hook_faker()
    except rospy.ROSInterruptException:
        pass
