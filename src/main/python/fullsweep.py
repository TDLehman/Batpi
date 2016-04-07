# Tylor Lehman
# BatPi
# fullsweep.py




# fullsweep currently takes 10 average samples and stores them in array li
# and then prints array li. It should probably be returned to something later
#
# Gets stuck in echolocate sometimes _____________________________________________________________________________ 
from Echolocate import Echolocate
from time import sleep


class fullsweep(object):
   def __init__(self):
      self.step_size = 10 # change pulse width 10*10us = 100us or 0.1ms in each step
      self.dont_buffer = 0 # don't buffer writes to avoid flushes
      self.samparray = [0 for i in range(200/self.step_size)]
      self.locator = Echolocate()
      
   def sweep(self):
      li = 0 # Loop counter
      with open('/dev/servoblaster', "w", self.dont_buffer ) as servo_blaster_device:
         for pulse_width in range(50,250,self.step_size):
            cmd = "0=" + str(pulse_width) + "\n"
            print cmd
            servo_blaster_device.write(cmd)
            self.samparray[li] = self.locator.getSample()
            #sleep(.25) # This might be way too big of a sleep

if __name__ == "__main__":
   x=fullsweep()
   x.sweep()
