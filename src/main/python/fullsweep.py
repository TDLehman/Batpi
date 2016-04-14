# Tylor Lehman
# BatPi
# fullsweep.py




# fullsweep currently takes 10 average samples and stores them in array li
# and then prints array li. It should probably be returned to something later
#
# Gets stuck in echolocate sometimes _____________________________________________________________________________ 
from Echolocate import Echolocate
from time import sleep
from subprocess import call

class fullsweep(object):
   def __init__(self):
      #Initialize servoblaster to only use pin 7 
      call(["sudo /home/pi/PiBits/ServoBlaster/user/servod --p1pins=7"], shell=True)
      self.step_size = 200/10 # Divisor = number of samples
      self.dont_buffer = 0 # don't buffer writes to avoid flushes
      self.samparray = [0 for i in range(200/self.step_size)]
      self.locator = Echolocate()
      
   def sweep(self):
      li = 0 # Loop counter
      with open('/dev/servoblaster', "w", self.dont_buffer ) as servo_blaster_device:
         servo_blaster_device.write("0=50\n")
         sleep(.2) # Give the servo time to catch up.
         for pulse_width in range(50,250,self.step_size):
            cmd = "0=" + str(pulse_width) + "\n"
            print cmd  #Uncomment to print each servo location
            servo_blaster_device.write(cmd)
            sleep(.1) # let the servo settle before taking samples
            self.samparray[li] = self.locator.getSample()
            print str(self.samparray[li])
            li=li+1
      return self.samparray      


      
   def checkFront(self):
      with open('/dev/servoblaster', "w", self.dont_buffer ) as servo_blaster_device:
         servo_blaster_device.write("0=150\n")
         sleep(.2) #Give time to face forward
         sample1 = self.locator.getSample()
         return sample1
      


   
if __name__ == "__main__":
   x=fullsweep()
   x.sweep()
