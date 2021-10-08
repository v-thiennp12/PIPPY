#!/usr/bin/python3

import time
import PCA9685

pwm = PCA9685.PCA9685(address=0x60)
pwm.setPWMFreq(50)
count = 0

while count < 2 :
    for i in range(0,16):
        pwm.setPWM(i, 0, 300)
        #pwm.setServoPulse(i, 1500)
        time.sleep(0.02)
    count += 1
    time.sleep(0.1) ##
