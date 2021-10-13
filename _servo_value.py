#!/usr/bin/python3

import time
import PCA9685
import sys
#import curses

def keycontrol(argv):   
    channel     = int(sys.argv[1])
    pulse       = int(sys.argv[2])
    
    if (channel >= 0) & (channel < 16):        
        pwm   = PCA9685.PCA9685(address=0x60, debug=False)
        pwm.setPWMFreq(50)
        time.sleep(0.02)
        pwm.setServoPulse(channel, pulse)
        time.sleep(0.02)
        # pwm.exit()

if __name__ == '__main__':
    keycontrol(sys.argv)

#value = input("Please enter an integer:\n")
#print(f'You entered {value}')