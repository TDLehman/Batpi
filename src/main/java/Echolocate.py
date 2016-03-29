# Tylor Lehman
# BatPi

# Imports from Python library. Setmode automatically sets up pin numbering
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM) # Set easy pin numbering system
GPIO.setwarnings(False) # Ignore stupid warnings

trig = 23 #GPIO 23 (Pin 16), Connects to Sonar Sensor trigger
echo = 24 # GPIO 24 (pin 18), connects to Sonar Sensor Echo
GPIO.setup(trig, GPIO.OUT) # sets GPIO ports as either outputs or inputs
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig,  False) # set trigger pin to low,
time.sleep(.5) # wait for it to settle
GPIO.output(trig, True)
time.sleep(0.00001) # As per HC - SR04 documentation, set trig high for 10uS.
GPIO.output(trig, False)
while GPIO.input(echo) == 0: # trigger sets echo pin to high
  start = time.time()
while GPIO.input(echo) == 1: # echo goes low when signal is returned
  end = time.time() # Python returns last time echo was high 
duration = end - start # measure the time the pin stayed high
soundSpeed = 34300 # Speed of soundwave
distance = duration*34300/2 # account for return trip
# reset pins, return distance to nearest object
GPIO.cleanup()
print distance
