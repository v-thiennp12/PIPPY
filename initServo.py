#!/usr/bin/python3

import time
import PCA9685

pwm     = PCA9685.PCA9685(address=0x60)
pwm.setPWMFreq(50)
count   = 0

min_pul = 110
max_pul = 450

mid_pulse       = int((min_pul + max_pul)/2)
vertical_pulse  = int(195.0)

# pwm.setServoPulse(0, mid_pulse)
# pwm.setServoPulse(1, mid_pulse) #*
# pwm.setServoPulse(2, mid_pulse)
# pwm.setServoPulse(3, mid_pulse) #*
# pwm.setServoPulse(4, mid_pulse)
# pwm.setServoPulse(5, mid_pulse)
# pwm.setServoPulse(6, mid_pulse)
# pwm.setServoPulse(7, mid_pulse)

pwm.setServoPulse(0, vertical_pulse)
pwm.setServoPulse(1, vertical_pulse) #*
pwm.setServoPulse(2, vertical_pulse)
pwm.setServoPulse(3, vertical_pulse) #*
pwm.setServoPulse(4, vertical_pulse)
pwm.setServoPulse(5, vertical_pulse)
pwm.setServoPulse(6, vertical_pulse)
pwm.setServoPulse(7, vertical_pulse)