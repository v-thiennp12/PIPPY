#!/usr/bin/python3

import time
import PCA9685
import sys
#import curses

def keycontrol(argv):   
    # channel     = int(sys.argv[1])
    # pulse       = int(sys.argv[2])
    # pulse       = input("Please enter an integer for pulse or 'q' to exit :\n")
    
    # if (channel >= 0) & (channel < 16):        
    pwm   = PCA9685.PCA9685(address=0x60, debug=False)
    pwm.setPWMFreq(50)
    time.sleep(0.02)
    pulse = 0
    while True:       
        try:
            pulse       = int(input("Please enter an integer for pulse or 'q' to exit : "))
        except ValueError:
            print("Not an integer! \n")
            break
            # if pulse == 'q':
            #     break            
            # continue
        else:
            # print("Yes an integer!")
            pwm.setServoPulse(0, int(pulse))
            pwm.setServoPulse(1, int(pulse))
            pwm.setServoPulse(2, int(pulse))
            pwm.setServoPulse(3, int(pulse))
            pwm.setServoPulse(4, int(pulse))
            pwm.setServoPulse(5, int(pulse))
            pwm.setServoPulse(6, int(pulse))
            pwm.setServoPulse(7, int(pulse))           
            time.sleep(0.02)
        # elif:
        #     break
        pwm.exit()

if __name__ == '__main__':
    keycontrol(sys.argv)

#value = input("Please enter an integer:\n")
#print(f'You entered {value}')