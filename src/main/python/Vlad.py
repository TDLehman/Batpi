# Tylor Lehman
# BatPi
# Vlad.py


# Initial AI for BatPi. Will try to go forward until there is something 
# 500 units in front of it.

from PiDrive import PiDrive

def Vlad():
   motor = PiDrive()
   sensor= fullsweep()
   
   envmap=sensor.sweep()
   front = len(envmap)/2
   stepcount = 0 # How far vlad has travelled thus far.
   print "I'm going to try to go forward."
   while(envmap(front)>500 & envmap(front+1)>500 & envmap(front-1)>500):
      motor.forward()
      envmap=sensor.sweep()
      stepcount=stepcount+1
   
   print "There's something in front of me. I'm done."
   print "I performed "+stepcount+" actions!"
Vlad()
