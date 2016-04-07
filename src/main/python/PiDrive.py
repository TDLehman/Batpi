# Tylor Lehman
# BatPi
# PiDrive.py


# Controls the DC motors for movement of the Raspberry Pi 
import RPi.GPIO as GPIO
from time import sleep



class PiDrive(object):
   def __init__(self):
      GPIO.setwarnings(False)
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


   def forward(self):
      print "Going forward 1"
      GPIO.output(self.Motor1A,GPIO.HIGH)
      GPIO.output(self.Motor1B,GPIO.LOW)
      GPIO.output(self.Motor1E,GPIO.HIGH)
      
      GPIO.output(self.Motor2A,GPIO.HIGH)
      GPIO.output(self.Motor2B,GPIO.LOW)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(1)
      self.stop() 
      
   def backward(self): 
      print "Going backward 1"
      GPIO.output(self.Motor1A,GPIO.LOW)
      GPIO.output(self.Motor1B,GPIO.HIGH)
      GPIO.output(self.Motor1E,GPIO.HIGH)
       
      GPIO.output(self.Motor2A,GPIO.LOW)
      GPIO.output(self.Motor2B,GPIO.HIGH)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(1)
      self.stop()

    
   def turnRight(self):
      print "Turning Right"
      #Turn left wheel forward
      GPIO.output(self.Motor1A,GPIO.HIGH)
      GPIO.output(self.Motor1B,GPIO.LOW)
      GPIO.output(self.Motor1E,GPIO.HIGH)   
      #Turn right wheel backward
      GPIO.output(self.Motor2A,GPIO.LOW)
      GPIO.output(self.Motor2B,GPIO.HIGH)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(.50)
      self.stop()

   def turnLeft(self):
      print "Turning Left"
      # Turn left wheel backward
      GPIO.output(self.Motor1A,GPIO.LOW)
      GPIO.output(self.Motor1B,GPIO.HIGH)
      GPIO.output(self.Motor1E,GPIO.HIGH)
      # Turn right wheel forward
      GPIO.output(self.Motor2A,GPIO.HIGH)
      GPIO.output(self.Motor2B,GPIO.LOW)
      GPIO.output(self.Motor2E,GPIO.HIGH)
      sleep(.50)
      self.stop()

   def stop(self): 
      print "Stopping"
      GPIO.output(self.Motor1E,GPIO.LOW)
      GPIO.output(self.Motor2E,GPIO.LOW)
      #GPIO.cleanup()



if __name__ == "__main__":
   x=PiDrive()
   x.forward()
   x.backward()
   x.turnLeft()
   x.turnRight()

