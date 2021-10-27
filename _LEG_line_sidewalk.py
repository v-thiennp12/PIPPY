#!/usr/bin/python3

import time
import PCA9685
import sys
import curses
import numpy

def keycontrol(argv):       
        pwm             = PCA9685.PCA9685(0x60, debug=False)
        pwm.setPWMFreq(50)

        pwm_step        = 20

        #init pulse PWM
        #in anti-clockwise order
        min_pulse           = 100 #good 190 #200 #50
        max_pulse           = 450 #good 310 #300 #450
        mid_pulse           = 275 # (max + min)/2

        pulse_0             = mid_pulse - 1*(pwm_step) - 1*(pwm_step)
        pulse_1             = mid_pulse - 1*(pwm_step) - 1*(pwm_step)
        pulse_2             = mid_pulse
        pulse_3             = mid_pulse
        pulse_4             = mid_pulse
        pulse_5             = mid_pulse
        pulse_6             = mid_pulse + 1*(pwm_step) + 1*(pwm_step)
        pulse_7             = mid_pulse + 1*(pwm_step) + 1*(pwm_step)
        
        #front-left LEG
        pwm.setServoPulse(4, pulse_4)
        pwm.setServoPulse(5, pulse_5)        
        #front-right LEG
        pwm.setServoPulse(0, pulse_0)
        pwm.setServoPulse(1, pulse_1)
        # rear-left LEG
        pwm.setServoPulse(6, pulse_6)
        pwm.setServoPulse(7, pulse_7)
        # #rear-right LEG
        pwm.setServoPulse(2, pulse_2)
        pwm.setServoPulse(3, pulse_3)        

        time.sleep(0.02)
        #init pulse

        key_get         = curses.initscr()
        key_get.keypad(True) 
        curses.noecho()
        curses.cbreak()
        # curses.nl()
        # curses.def_prog_mode()
        # curses.def_shell_mode()                
        
        count_updown    = 0

        try:
            while True:
                char = key_get.getch()

                if char == ord('q'):
                    #if q is pressed quit
                    break
                else:
                    # cycle 1
                    #front-right LEG up
                    pulse_0 += -2*pwm_step
                    pulse_1 += +pwm_step
                    pwm.setServoPulse(0, int(pulse_0))
                    pwm.setServoPulse(1, int(pulse_1))
                    #rear-left LEG up
                    pulse_6 += -2*pwm_step
                    pulse_7 += +1*pwm_step              
                    pwm.setServoPulse(6, int(pulse_6))
                    pwm.setServoPulse(7, int(pulse_7))
                    
                    # front-left LEG back
                    pulse_4 += 1*(pwm_step)
                    pulse_5 += 1*(pwm_step)
                    pwm.setServoPulse(4, int(pulse_4))                
                    pwm.setServoPulse(5, int(pulse_5))
                    # rear-right LEG back
                    pulse_2 += -1*(pwm_step)
                    pulse_3 += -1*(pwm_step)
                    pwm.setServoPulse(2, int(pulse_2))                
                    pwm.setServoPulse(3, int(pulse_3))                

                    time.sleep(0.02)
                    # -----
                    
                    # # cycle 2
                    # #front-right LEG up
                    # pulse_0 += -pwm_step/3
                    # pulse_1 += +pwm_step/3
                    # pwm.setServoPulse(0, int(pulse_0))
                    # pwm.setServoPulse(1, int(pulse_1))
                    # #rear-left LEG up
                    # pulse_6 += -pwm_step/3
                    # pulse_7 += +pwm_step/3                
                    # pwm.setServoPulse(6, int(pulse_6))
                    # pwm.setServoPulse(7, int(pulse_7))
                    
                    # # front-left LEG back
                    # pulse_4 += 1*(10)
                    # pulse_5 += 1*(10)
                    # pwm.setServoPulse(4, int(pulse_4))                
                    # pwm.setServoPulse(5, int(pulse_5))    
                    # # rear-right LEG back
                    # pulse_2 += -1*(10)
                    # pulse_3 += -1*(10)
                    # pwm.setServoPulse(2, int(pulse_2))                
                    # pwm.setServoPulse(3, int(pulse_3))

                    # time.sleep(0.02)
                    # # -----    

                    # # cycle 3
                    # #front-right LEG up
                    # pulse_0 += -pwm_step/3
                    # pulse_1 += +pwm_step/3
                    # pwm.setServoPulse(0, int(pulse_0))
                    # pwm.setServoPulse(1, int(pulse_1))
                    # #rear-left LEG up
                    # pulse_6 += -pwm_step/3
                    # pulse_7 += +pwm_step/3                
                    # pwm.setServoPulse(6, int(pulse_6))
                    # pwm.setServoPulse(7, int(pulse_7))

                    # # front-left LEG back
                    # pulse_4 += 1*(10)
                    # pulse_5 += 1*(10)
                    # pwm.setServoPulse(4, int(pulse_4))                
                    # pwm.setServoPulse(5, int(pulse_5))    
                    # # rear-right LEG back
                    # pulse_2 += -1*(10)
                    # pulse_3 += -1*(10)
                    # pwm.setServoPulse(2, int(pulse_2))                
                    # pwm.setServoPulse(3, int(pulse_3))

                    # time.sleep(0.02)
                    # # ---

                    # ---
                    time.sleep(0.04)
                    # ---

                    #front-right LEG down
                    pwm.setServoPulse(0, mid_pulse + 1*pwm_step)
                    pwm.setServoPulse(1, mid_pulse - 1*pwm_step)
                    #rear-left LEG down
                    pwm.setServoPulse(6, mid_pulse + 1*pwm_step)
                    pwm.setServoPulse(7, mid_pulse - 1*pwm_step)

                    # time.sleep(0.02)

                    # front-left LEG forward-up
                    pulse_4 = mid_pulse - 2*pwm_step
                    pulse_5 = mid_pulse + 1*pwm_step
                    pwm.setServoPulse(4, int(pulse_4))                
                    pwm.setServoPulse(5, int(pulse_5))
                    # rear-right LEG forward-up
                    pulse_2 = mid_pulse - 1*pwm_step
                    pulse_3 = mid_pulse + 2*pwm_step
                    pwm.setServoPulse(2, int(pulse_2))                
                    pwm.setServoPulse(3, int(pulse_3))
                    
                    time.sleep(0.02)

                    # front-left LEG normal
                    pulse_4 = mid_pulse
                    pulse_5 = mid_pulse
                    pwm.setServoPulse(4, int(pulse_4))                
                    pwm.setServoPulse(5, int(pulse_5))
                    # rear-right LEG normal
                    pulse_2 = mid_pulse
                    pulse_3 = mid_pulse
                    pwm.setServoPulse(2, int(pulse_2))                
                    pwm.setServoPulse(3, int(pulse_3))

                    # time.sleep(0.02)

                    #front-right LEG normal
                    pulse_0 = mid_pulse
                    pulse_1 = mid_pulse
                    pwm.setServoPulse(0, pulse_0)
                    pwm.setServoPulse(1, pulse_1)
                    #rear-left LEG normal
                    pulse_6 = mid_pulse
                    pulse_7 = mid_pulse
                    pwm.setServoPulse(6, pulse_6)
                    pwm.setServoPulse(7, pulse_7)       

                    time.sleep(0.02)

                    # --------------------------
                    time.sleep(0.1)         

            # shut down cleanly
            curses.nocbreak()
            key_get.keypad(False)
            curses.echo()
            # curses.reset_prog_mode()
            # curses.reset_shell_mode()
            # curses.nonl()         
            curses.endwin()

            #save last values to PCA9685 register
            pwm.exit()

        finally:
        # print('maximum playing reached : %d  ' %(count))
            time.sleep(0.02)

if __name__ == '__main__':
    keycontrol(sys.argv)


# if char == curses.KEY_UP:
#     count_updown += 1
#     if ((mid_pulse + abs(count_updown*pwm_step)) > max_pulse) \
#        | ((mid_pulse - abs(count_updown*pwm_step)) < min_pulse) :
#         count_updown -= 1                    

# elif char == curses.KEY_DOWN:
#     count_updown -= 1
#     if ((mid_pulse + abs(count_updown*pwm_step)) > max_pulse) \
#        | ((mid_pulse - abs(count_updown*pwm_step)) < min_pulse) :
#         count_updown += 1    