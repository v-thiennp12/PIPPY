#!/usr/bin/python3

import time
import PCA9685
import sys
import curses

def keycontrol(argv):
    channel     = int(sys.argv[1])
    
    if (channel >= 0) & (channel < 16):        
        pwm         = PCA9685.PCA9685(0x60, debug=False)
        pwm.setPWMFreq(50)

        #init pulse PWM
        #servos rotate in anti-clockwise direction
        min_pul     = 140 #100
        max_pul     = 440 #450
        mid_pulse   = 290

        pwm.setServoPulse(0, mid_pulse)
        pwm.setServoPulse(1, mid_pulse)
        pwm.setServoPulse(2, mid_pulse)
        pwm.setServoPulse(3, mid_pulse)
        pwm.setServoPulse(4, mid_pulse)
        pwm.setServoPulse(5, mid_pulse)
        pwm.setServoPulse(6, mid_pulse)
        pwm.setServoPulse(7, mid_pulse)
        time.sleep(0.5)

        screen      = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)
        pwm_step    = 5
        pulse       = mid_pulse        

        try:
            while True:
                char = screen.getch()

                if char == ord('q'):
                    #if q is pressed quit
                    break

                elif char == curses.KEY_LEFT:
                    pulse -= pwm_step
                    if pulse < min_pul:
                        pulse = min_pul

                    pwm.setServoPulse(0, pulse)
                    pwm.setServoPulse(1, pulse)
                    pwm.setServoPulse(2, pulse)
                    pwm.setServoPulse(3, pulse)
                    pwm.setServoPulse(4, pulse)
                    pwm.setServoPulse(5, pulse)
                    pwm.setServoPulse(6, pulse)
                    pwm.setServoPulse(7, pulse)
                    time.sleep(0.02)

                elif char == curses.KEY_RIGHT:
                    pulse += pwm_step
                    if pulse > max_pul:
                        pulse = max_pul

                    pwm.setServoPulse(0, pulse)
                    pwm.setServoPulse(1, pulse)
                    pwm.setServoPulse(2, pulse)
                    pwm.setServoPulse(3, pulse)
                    pwm.setServoPulse(4, pulse)
                    pwm.setServoPulse(5, pulse)
                    pwm.setServoPulse(6, pulse)
                    pwm.setServoPulse(7, pulse)
                    time.sleep(0.02)

            # shut down cleanly
            curses.nocbreak()
            screen.keypad(False)
            curses.echo()
            curses.endwin()

            #save last values to PCA9685 register
            # pwm.exit()

        finally:
            time.sleep(0.02)

if __name__ == '__main__':
    keycontrol(sys.argv)
    #value = input("Please enter an integer in [0..15] to select channel :\n")
    #print(f'You entered {value}')