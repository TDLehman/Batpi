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
   print "Right now I see: "+str(envmap)
   front = len(envmap)/2
   print "This is in front of me: " + str(envmap[front+1])+", "+str(envmap[front])+", "+str(envmap[front-1])
   
   stepcount = 0 # How far user has travelled thus far.
   command=raw_input("What should I do? (w,a,s,d,f,z,x,q)")
   while(command=="w" or command=="a" or command=="s" or command=="d" or command=="x" or command=="f" or command=="z"):
      if command=="w":
         print "w"
         motor.forward()
      elif command=="z":
         seconds=raw_input("for how many seconds?")
         motor.forwardx(int(seconds))
      elif command=="a":
         print "a"
         motor.turnLeft()
      elif command=="s":
         print "s"
         motor.backward()
      elif command=="d":
         print "d"
         motor.turnRight()
      elif command=="x":
         print "x"
         envmap=sensor.sweep()
         print "Here is everything I see:\n"+str(envmap)
         print "Here is what is in front of me: "+str(envmap[front-1])+", "+str(envmap[front])+", "+str(envmap[front+1])
      elif command=="f":
         print "This is in front of me: "+str(sensor.checkFront())
      elif command=="q":
         print "Quitting!"
      if command!="q":
         command=raw_input("What should I do? (w,a,s,d,x,f,z,q)")    
         stepcount=stepcount+1

   print "you are done!"
   print "I performed "+str(stepcount)+" actions!"

UserAI()
