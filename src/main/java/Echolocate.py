# Tylor Lehman
# BatPi

# Imports from Python library. Setmode automatically sets up pin numbering
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Specify input and output pins
# GPIO 23 (Pin 16), connects to the trigger of the sonar sensor
trig = 23
# GPIO 24 (pin 18), connects to the echo of the sonar sensor
echo = 24
# sets GPIO ports as either outputs or inputs
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
# make sure trigger pin is set to low, then wait for it to settle
GPIO.output(trig, false)
time.sleep(.5)
# As per HC - SR04 documentation, set trig to high for 10uS.
GPIO.output(trig, TRUE)
time.sleep(0.00001)
GPIO.output(trig, FALSE)
# echo pin stays high from the time the trigger happens until a signal is returned
# So, measure the time the pin stayed high
while GPIO.input(echo) == 0:
  start = time.time()
while GPIO.input(echo) == 1:
  end = time.time()
duration = end - start
#Calculate distance to object. divided by 2 to account for return trip of sound wave
soundSpeed = 34300
distance = duration*34300/2
# reset pins, return distance to nearest object
GPIO.cleanup()
return distance
