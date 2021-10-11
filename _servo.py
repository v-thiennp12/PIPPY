#!/usr/bin/python3

import time
import PCA9685
import sys
import curses

def keycontrol(argv):
    


    channel     = int(sys.argv[1])
    round       = int(sys.argv[2])
    #pulse       = int(sys.argv[2])
    
    if (channel >= 0) & (channel < 16):
        
        pwm   = PCA9685.PCA9685(0x60, debug=False)
        pwm.setPWMFreq(50)
        pulse = 110
        pwm.setServoPulse(channel, pulse)
        time.sleep(0.5)
        screen    = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)

        count = 0
        try:
            while count < round:
                char = screen.getch()
                if char == curses.KEY_LEFT:
                    pulse -= 5
                    if pulse < 110:
                        pulse = 110                
                    # pwm.setServoPulse(channel, pulse)

                    pwm.setServoPulse(0, pulse)
                    pwm.setServoPulse(1, pulse) #*
                    pwm.setServoPulse(2, pulse)
                    pwm.setServoPulse(3, pulse) #*
                    pwm.setServoPulse(4, pulse)
                    pwm.setServoPulse(5, pulse)
                    pwm.setServoPulse(6, pulse)
                    pwm.setServoPulse(7, pulse)

                    time.sleep(0.02)
                    count += 1

                elif char == curses.KEY_RIGHT:
                    pulse += 5
                    if pulse > 450:
                        pulse = 450                
                    # pwm.setServoPulse(channel, pulse)

                    pwm.setServoPulse(0, pulse)
                    pwm.setServoPulse(1, pulse) #*
                    pwm.setServoPulse(2, pulse)
                    pwm.setServoPulse(3, pulse) #*
                    pwm.setServoPulse(4, pulse)
                    pwm.setServoPulse(5, pulse)
                    pwm.setServoPulse(6, pulse)
                    pwm.setServoPulse(7, pulse)

                    time.sleep(0.02)
                    count += 1

            # shut down cleanly
            curses.nocbreak()
            screen.keypad(False)
            curses.echo()
            curses.endwin()

            print('maximum playing reached : %d  ' %(count))
            # time.sleep(2)

        finally:
            # print('maximum playing reached : %d  ' %(count))
            time.sleep(0.001)
        # # shut down cleanly
        #     curses.nocbreak()
        #     screen.keypad(0)
        #     curses.echo()
        #     curses.endwin()

if __name__ == '__main__':
    keycontrol(sys.argv)

#value = input("Please enter an integer:\n")
#print(f'You entered {value}')