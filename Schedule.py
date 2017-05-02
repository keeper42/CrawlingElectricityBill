# Author: LJF
# Coding: UTF-8
# The version of python: 3.5
# Created time: 2017/05/02
# This is a function that runs the program periodically

import os
import sched
import time
    
# Set schedule
schedule = sched.scheduler(time.time, time.sleep) 
    
def perform_command(cmd, inc): 
    # Arrange inc second to run itself again, that is, run the cycle
    schedule.enter(inc, 0, perform_command, (cmd, inc)) 
    os.system(cmd)
        
def timming_exe(cmd, inc = 60): 
    # Enter is used to schedule the occurrence of an event, starting from the first n seconds
    schedule.enter(inc, 0, perform_command, (cmd, inc)) 
    # Continue running until the scheduled time queue becomes empty
    schedule.run()
    
# timming_exe("python ThreadTest.py", 10)
print("The main function is executed once a day: ") 
timming_exe("python Main.py", 86400)

#
#
# End Schedule
#
#