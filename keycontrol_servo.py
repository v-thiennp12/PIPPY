#!/usr/bin/python3

import time
import PCA9685
import sys
#import curses

def keycontrol(argv):
    # screen    = curses.initscr()
    
    channel     = int(sys.argv[1])
    # round       = int(sys.argv[2])
    pulse       = int(sys.argv[2])
    
    if (channel >= 0) & (channel < 16):
        
        
        pwm   = PCA9685.PCA9685(address=0x60, debug=False)
        pwm.setPWMFreq(50)

        # pwm.setServoPulse(0, pulse)
        # pwm.setServoPulse(1, pulse) #*
        # pwm.setServoPulse(2, pulse)
        # pwm.setServoPulse(3, pulse) #*
        pwm.setServoPulse(4, pulse)
        pwm.setServoPulse(5, pulse)
        pwm.setServoPulse(6, pulse)
        pwm.setServoPulse(7, pulse)

        time.sleep(0.5)

        # pwm.setServoPulse(channel, pulse)
        time.sleep(0.02)

        # count = 0
        # while count < round:
        #     # for i in range(250,3000,1):
        #     for i in range(50,500,1):
        #         pwm.setServoPulse(channel,i)
        #         time.sleep(0.02)

        #     for i in range(500,50,-1):
        #         pwm.setServoPulse(channel,i)
        #         time.sleep(0.02)
        #     count += 1

if __name__ == '__main__':
    keycontrol(sys.argv)

#value = input("Please enter an integer:\n")
#print(f'You entered {value}')