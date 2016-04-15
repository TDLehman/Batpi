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
   direction = 0  #keep track of direction faced.
   envmap=sensor.sweep()
   front = len(envmap)/2
   fdistance = 0 # How far will I go per forward called?
   stepcount = 0 # How far vlad has travelled thus far.
   print "I'm going to try to go forward."
   print "This is what I see: "+str(envmap[front-1])+", "+str(envmap[front])+", "+str(envmap[front+1])
   #print "Here is everything I see:"+str(envmap)
   prevmap=envmap

   # This block calibrates forward distance
   if(envmap[front]>10 and envmap[front+1]>10 and envmap[front-1]>10):
      print "Calibrating"
      sample=sensor.checkFront()
      motor.forward()
      fdistance=sample-sensor.checkFront()
      envmap=sensor.sweep()


      
   while(stepcount<10):   
      while(envmap[front]>20 and envmap[front+1]>20 and envmap[front-1]>20):
         motor.forward()
         motor.forward()
         envmap=sensor.sweep()
         
      if(envmap[front-3]>envmap[front+3] and envmap[0]>20):
         motor.turnRight()
         motor.turnRight()
         motor.forward()
         motor.forward()
         motor.turnLeft()
         motor.turnLeft()
         
      elif(envmap[10]>20):
         motor.turnLeft()
         motor.turnLeft()
         motor.forward()
         motor.forward()
         motor.turnRight()
         motor.turnRight()
      stepcount=stepcount+1
   print "I think I'm pretty stuck. I'm done."
   print "I performed "+str(stepcount)+" actions!"

   
Vlad()
