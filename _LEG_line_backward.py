#!/usr/bin/python3

import time
import PCA9685
import sys
import curses
import numpy

def keycontrol(argv):       
        pwm             = PCA9685.PCA9685(0x60, debug=False)
        pwm.setPWMFreq(50)

        #init pulse PWM
        #in anti-clockwise order
        min_pulse           = 100 #good 190 #200 #50
        max_pulse           = 450 #good 310 #300 #450
        mid_pulse           = 250 # (max + min)/2

        #front-left LEG
        pwm.setServoPulse(4, mid_pulse)
        pwm.setServoPulse(5, mid_pulse)
        
        # #front-right LEG
        # pwm.setServoPulse(0, mid_pulse)
        # pwm.setServoPulse(1, mid_pulse)

        # # rear-left LEG
        # pwm.setServoPulse(6, mid_pulse)
        # pwm.setServoPulse(7, mid_pulse)

        # #rear-right LEG
        # pwm.setServoPulse(2, mid_pulse)
        # pwm.setServoPulse(3, mid_pulse)        

        time.sleep(0.02)
        #init pulse

        key_get         = curses.initscr()        
        curses.noecho()
        curses.cbreak()
        key_get.keypad(True)
        
        pwm_step        = 10
        count_updown    = 0

        try:
            while True:
                char = key_get.getch()

                if char == ord('q'):
                    #if q is pressed quit
                    break

                if char == curses.KEY_UP:
                    count_updown += 1
                    if ((mid_pulse + abs(count_updown*pwm_step)) > max_pulse) \
                       | ((mid_pulse - abs(count_updown*pwm_step)) < min_pulse) :
                        count_updown -= 1                    

                elif char == curses.KEY_DOWN:
                    count_updown -= 1
                    if ((mid_pulse + abs(count_updown*pwm_step)) > max_pulse) \
                       | ((mid_pulse - abs(count_updown*pwm_step)) < min_pulse) :
                        count_updown += 1

                #front-left LEG
                # pwm.setServoPulse(4, int(mid_pulse + count_updown*pwm_step)) 
                # pwm.setServoPulse(5, int(mid_pulse + count_updown*(pwm_step +20))
                # print('count_updown ', count_updown)

                # pwm.setServoPulse(4, int(mid_pulse + count_updown*pwm_step))                
                # pwm.setServoPulse(5, int(mid_pulse + count_updown*pwm_step - numpy.sign(count_updown)*10))
                # print('count_updown ', count_updown)

                pwm.setServoPulse(4, int(mid_pulse + count_updown*pwm_step))                
                # pwm.setServoPulse(5, int(mid_pulse + count_updown*pwm_step + numpy.sign(count_updown)*(abs(count_updown)*2 + 10)))
                pwm.setServoPulse(5, int(mid_pulse + count_updown*pwm_step - (abs(count_updown)*5 + 30)))
                print('count_updown ', count_updown)

                # pwm.setServoPulse(4, int(mid_pulse - count_updown*pwm_step))
                # pwm.setServoPulse(5, int(mid_pulse + count_updown*pwm_step))
                
                # #front-right LEG
                # pwm.setServoPulse(0, mid_pulse - count_updown*pwm_step)
                # pwm.setServoPulse(1, mid_pulse + count_updown*pwm_step)

                # #rear-left LEG
                # pwm.setServoPulse(6, mid_pulse - count_updown*pwm_step)
                # pwm.setServoPulse(7, mid_pulse + count_updown*pwm_step)

                # #rear-right LEG
                # pwm.setServoPulse(2, mid_pulse - count_updown*pwm_step)
                # pwm.setServoPulse(3, mid_pulse + count_updown*pwm_step) 

                time.sleep(0.02) 

            # shut down cleanly
            curses.nocbreak()
            key_get.keypad(False)
            curses.echo()
            curses.endwin()

            #save last values to PCA9685 register
            # pwm.exit()

        finally:
        # print('maximum playing reached : %d  ' %(count))
            time.sleep(0.001)

if __name__ == '__main__':
    keycontrol(sys.argv)