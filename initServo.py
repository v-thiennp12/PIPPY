#!/usr/bin/python3

import time
import PCA9685

pwm     = PCA9685.PCA9685(address=0x60)
pwm.setPWMFreq(50)
count   = 0

def angle2pulse(angle):
    min_pul = 500
    max_pul = 2500

    return int(angle/180*(max_pul-min_pul) + min_pul)

while count < 2 :
    for channel in range(0,16):
        pwm.setServoPulse(channel, angle2pulse(50))
    time.sleep(0.02)
    count += 1
#pwm.exit_PCA9685()