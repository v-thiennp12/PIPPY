#!/usr/bin/python3

import time
import PCA9685

pwm     = PCA9685.PCA9685(address=0x60)
pwm.setPWMFreq(50)
count   = 0

# calibrated in average across all servos
# first calibration, roughly
min_pul = 110
max_pul = 450
mid_pulse       = int((min_pul + max_pul)/2)
vertical_pulse  = int(195.0) #or 365 #average for all servo, before fine-tune

# before fine-tune : pwm at 280 in average for all rods
# at middle position [90deg], servo goes from 0 to 180 deg
# # min_pul = 110
# # max_pul = 450
pwm.setServoPulse(0, mid_pulse)
pwm.setServoPulse(1, mid_pulse) #*
pwm.setServoPulse(2, mid_pulse)
pwm.setServoPulse(3, mid_pulse) #*
pwm.setServoPulse(4, mid_pulse)
pwm.setServoPulse(5, mid_pulse)
pwm.setServoPulse(6, mid_pulse)
pwm.setServoPulse(7, mid_pulse)

# before fine-tune : pwm at 195 in average for all rods
# at vertical position [45deg], servo goes from 0 to 180 deg
# pwm.setServoPulse(0, vertical_pulse)
# pwm.setServoPulse(1, vertical_pulse) #*
# pwm.setServoPulse(2, vertical_pulse)
# pwm.setServoPulse(3, vertical_pulse) #*
# pwm.setServoPulse(4, vertical_pulse)
# pwm.setServoPulse(5, vertical_pulse)
# pwm.setServoPulse(6, vertical_pulse)
# pwm.setServoPulse(7, vertical_pulse)

# **************************************************************
# after fine-tune (calibration for each rod)
#servo/channel | mid pulse [vertical position of each rod]
#init position pwm [vertical position of each rod]
# **************************************************************
# top-view

# ______head________

# 4                1
#  >______________<
# 5                0
#         |
#         |
# 6                3
#  >______________<
# 7                2

# 0 |init_pwm0 = 190
# 1 |init_pwm1 = 173
# 2 |init_pwm2 = 205
# 3 |init_pwm3 = 200

# 4 |init_pwm4 = 187
# 5 |init_pwm5 = 173
# 6 |init_pwm6 = 175
# 7 |init_pwm7 = 187

# pwm.setServoPulse(0, 190)
# pwm.setServoPulse(1, 173) #*
# pwm.setServoPulse(2, 205)
# pwm.setServoPulse(3, 200) #*
# pwm.setServoPulse(4, 187)
# pwm.setServoPulse(5, 173)
# pwm.setServoPulse(6, 175)
# pwm.setServoPulse(7, 187)

#save last values to PCA9685 register
pwm.exit()