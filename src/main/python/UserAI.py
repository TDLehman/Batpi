# Tylor Lehman
# BatPi
# UserAI.py


# Initial AI for BatPi. Will try to go forward until there is something 
# 500 units in front of it.

from PiDrive import PiDrive
from fullsweep import fullsweep
def UserAI():
   motor = PiDrive()
   sensor= fullsweep()
   envmap= sensor.sweep()
   front = len(envmap)/2
   stepcount = 0 # How far user has travelled thus far.
   command=raw_input("What should I do? (w,a,s,d,x,q)")
   while(command=="w" or command=="a" or command=="s" or command=="d" or command=="x"):
      if command=="w":
         print "w"
         motor.forward()
      elif command=="a":
         print "a"
         motor.turnLeft()
      elif command=="s":
         print "s"
         motor.reverse()
      elif command=="d":
         print "d"
         motor.turnRight()
      elif command=="x":
         print "x"
         envmap=sensor.sweep()
      command=raw_input("What should I do? (w,a,s,d,x,q)")    
      stepcount=stepcount+1

   print "either that was an invalid command, or you are done!"
   print "I performed "+str(stepcount)+" actions!"

UserAI()
