# Tylor Lehman
# BatPi
# Vlad.py


# Initial AI for BatPi. Will try to go forward until there is something 
# 50 units in front of it.

from PiDrive import PiDrive
from fullsweep import fullsweep
def Vlad():
   motor = PiDrive()
   sensor= fullsweep()
   
   envmap=sensor.sweep()
   front = len(envmap)/2
   
   stepcount = 0 # How far vlad has travelled thus far.
   print "I'm going to try to go forward."
   print "This is what I see: "+str(envmap[front-1])+", "+str(envmap[front])+", "+str(envmap[front+1])
   print "Here is everything I see:"+str(envmap)
   while(envmap[front]>20 and envmap[front+1]>20 and envmap[front-1]>20):
      motor.forward(min(envmap[front],envmap[front+1],envmap[front-1])/10)
      envmap=sensor.sweep()
      stepcount=stepcount+1
      
   
   print "There's something in front of me. I'm done."
   print "I performed "+str(stepcount)+" actions!"
   
Vlad()
