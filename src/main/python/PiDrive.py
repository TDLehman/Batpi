# Tylor Lehman
# BatPi
# PiDrive.py


# Controls the DC motors for movement of the Raspberry Pi 
import RPi.GPIO as GPIO
from time import sleep



class PiDrive(object):
   def __init__(self):
      GPIO.setmode(GPIO.BCM) 
      Motor1A = 17 # GPIO 17 (pin 11)
      Motor1B = 27 # GPIO 27 (pin 13) 
      Motor1E = 22 # GPIO 22 (Pin 15)
       
      Motor2A = 5 # GPIO 5 (Pin 29)
      Motor2B = 6 # GPIO 6 (Pin 31)
      Motor2E = 13 # GPIO 13 (Pin 33)

      GPIO.setup(Motor1A,GPIO.OUT)
      GPIO.setup(Motor1B,GPIO.OUT)
      GPIO.setup(Motor1E,GPIO.OUT)
       
      GPIO.setup(Motor2A,GPIO.OUT)
      GPIO.setup(Motor2B,GPIO.OUT)
      GPIO.setup(Motor2E,GPIO.OUT)


   def forward() 
      print "Going forward 1"
      GPIO.output(Motor1A,GPIO.HIGH)
      GPIO.output(Motor1B,GPIO.LOW)
      GPIO.output(Motor1E,GPIO.HIGH)
      
      GPIO.output(Motor2A,GPIO.HIGH)
      GPIO.output(Motor2B,GPIO.LOW)
      GPIO.output(Motor2E,GPIO.HIGH)
      sleep(1)
      stop() 
      
   def backward() 
      print "Going backward 1"
      GPIO.output(Motor1A,GPIO.LOW)
      GPIO.output(Motor1B,GPIO.HIGH)
      GPIO.output(Motor1E,GPIO.HIGH)
       
      GPIO.output(Motor2A,GPIO.LOW)
      GPIO.output(Motor2B,GPIO.HIGH)
      GPIO.output(Motor2E,GPIO.HIGH)
      sleep(1)
      stop()

   def stop() 
      print "Stopping"
      GPIO.output(Motor1E,GPIO.LOW)
      GPIO.output(Motor2E,GPIO.LOW)
      GPIO.cleanup()
    
   def turnRight()
      print "Turning Right"
      #Turn left wheel forward
      GPIO.output(Motor1A,GPIO.HIGH)
      GPIO.output(Motor1B,GPIO.LOW)
      GPIO.output(Motor1E,GPIO.HIGH)   
      #Turn right wheel backward
      GPIO.output(Motor2A,GPIO.LOW)
      GPIO.output(Motor2B,GPIO.HIGH)
      GPIO.output(Motor2E,GPIO.HIGH)
      sleep(.25)
      stop()

   def turnLeft()
      print "Turning Left"
      # Turn left wheel backward
      GPIO.output(Motor1A,GPIO.LOW)
      GPIO.output(Motor1B,GPIO.HIGH)
      GPIO.output(Motor1E,GPIO.HIGH)
      # Turn right wheel forward
      GPIO.output(Motor2A,GPIO.HIGH)
      GPIO.output(Motor2B,GPIO.LOW)
      GPIO.output(Motor2E,GPIO.HIGH)
      sleep(.25)
      stop()

if __name__ == "__main__":
   forward()
   backward()
   turnLeft()
   turnRight()

