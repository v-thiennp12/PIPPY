#!/usr/bin/python3

import time
import PCA9685
import sys
#import curses

def keycontrol(argv):
    # inputfile = str(sys.argv[1])
    # print('inputfile ', inputfile)
    channel     = int(sys.argv[1])
    round       = int(sys.argv[2])
    #keycontrol  = bool(sys.argv[2])
    
    if (channel >= 0) & (channel < 16):
        # screen  = curses.initscr()
        count = 0
        pwm   = PCA9685.PCA9685(0x60, debug=False)
        pwm.setPWMFreq(50)
        while count < round:
            for i in range(500,2500,1):
                pwm.setServoPulse(channel,i)
            time.sleep(0.02)

            for i in range(2500,500,-1):
                pwm.setServoPulse(channel,i)
            time.sleep(0.02)
            count += 1

if __name__ == '__main__':
    keycontrol(sys.argv)

#value = input("Please enter an integer:\n")
#print(f'You entered {value}')