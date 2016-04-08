# Tylor Lehman
# BatPi
# Vlad.py


# Initial AI for BatPi. Will try to go forward until there is something 
# 500 units in front of it.


def Vlad():
   motor = PiDrive()
   sensor= fullsweep()
   
   envmap=sensor.sweep()
   front = len(envmap)/2
   print "I'm going to try to go forward."
   while(envmap(front)>500&&envmap(front+1)>500&envmap(front-1)>500):
      motor.forward()
      envmap=sensor.sweep()
   
   print "There's something in front of me. I'm done."
