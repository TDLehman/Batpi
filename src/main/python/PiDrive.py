# Tylor Lehman
# BatPi
# PiDrive.py


# Controls the DC motors for movement of the Raspberry Pi 
import RPi.GPIO as GPIO
from time import sleep



class PiDrive(object):
   def __init__(self):
      GPIO.setwarnings(False)
      print "Don't forget, warnings are turned off for PiDrive"
      GPIO.setmode(GPIO.BCM) 
      self.Motor1A = 17 # GPIO 17 (pin 11)
      self.Motor1B = 27 # GPIO 27 (pin 13) 
      self.Motor1E = 22 # GPIO 22 (Pin 15)
       
      self.Motor2A = 5 # GPIO 5 (Pin 29)
      self.Motor2B = 6 # GPIO 6 (Pin 31)
      self.Motor2E = 13 # GPIO 13 (Pin 33)

      GPIO.setup(self.Motor1A,GPIO.OUT)
      GPIO.setup(self.Motor1B,GPIO.OUT)
      GPIO.setup(self.Motor1E,GPIO.OUT)
       
      GPIO.setup(self.Motor2A,GPIO.OUT)
      GPIO.setup(self.Motor2B,GPIO.OUT)
      GPIO.setup(self.Motor2E,GPIO.OUT)

#________________________________________________________

   def forward(self):
      print "Going forward 1"
      GPIO.output(self.Motor2A,GPIO.HIGH)
      GPIO.output(self.Motor2B,GPIO.LOW)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(.05) 
      
      
      GPIO.output(self.Motor1A,GPIO.HIGH)
      GPIO.output(self.Motor1B,GPIO.LOW)
      GPIO.output(self.Motor1E,GPIO.HIGH)
#      sleep(1) #try to correct for turning. :(     
      sleep(.5)
      self.stop() 

   def forwardx(self, distance):
      print "Going forward "+str(distance)
      GPIO.output(self.Motor1A,GPIO.HIGH)
      GPIO.output(self.Motor1B,GPIO.LOW)
      GPIO.output(self.Motor1E,GPIO.HIGH)
      
      GPIO.output(self.Motor2A,GPIO.HIGH)
      GPIO.output(self.Motor2B,GPIO.LOW)
      GPIO.output(self.Motor2E,GPIO.HIGH)

      sleep(distance)
      self.stop()


      
   def backward(self): 
      print "Going backward 1"
      GPIO.output(self.Motor1A,GPIO.LOW)
      GPIO.output(self.Motor1B,GPIO.HIGH)
      GPIO.output(self.Motor1E,GPIO.HIGH)
       
      GPIO.output(self.Motor2A,GPIO.LOW)
      GPIO.output(self.Motor2B,GPIO.HIGH)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(.5)
      self.stop()



   # Turns approximately 45 degrees 
   def turnLeft(self):
      print "Turning Left"
      # Comments are backward.
      #Turn left wheel forward
      GPIO.output(self.Motor1A,GPIO.HIGH)
      GPIO.output(self.Motor1B,GPIO.LOW)
      GPIO.output(self.Motor1E,GPIO.HIGH)   
      #Turn right wheel backward
      GPIO.output(self.Motor2A,GPIO.LOW)
      GPIO.output(self.Motor2B,GPIO.HIGH)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(.5)
      self.stop()

   def turnRight(self):
      print "Turning Right"
      # Comments are still backward
      # Turn left wheel backward
      GPIO.output(self.Motor1A,GPIO.LOW)
      GPIO.output(self.Motor1B,GPIO.HIGH)
      GPIO.output(self.Motor1E,GPIO.HIGH)
      # Turn right wheel forward
      GPIO.output(self.Motor2A,GPIO.HIGH)
      GPIO.output(self.Motor2B,GPIO.LOW)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(.5)
      self.stop()

   def stop(self): 
      print "Stopping"
      GPIO.output(self.Motor1E,GPIO.LOW)
      GPIO.output(self.Motor2E,GPIO.LOW)
      #GPIO.cleanup()



if __name__ == "__main__":
   x=PiDrive()
   x.forward()
   x.forward()
#   x.backward()
#   x.turnLeft()
#   x.turnRight()

