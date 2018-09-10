# Hook (this is the mollusc)

Headset hook monitor for pick-up and use.

ROS package.

## TODO
- custom message to publish on /hook
   header
   picked_up BOOL (True - headset is picked up, False - headset is hung up)
- test the pull-up, pull-down state for the hook
- make the pull-up / pull-down state customisable?
  (Or just switch btw. 3.3V and GND for other...)
- make the GPIO pin for the hook customisable (4)
