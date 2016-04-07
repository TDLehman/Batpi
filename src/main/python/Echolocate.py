# Tylor Lehman
# BatPi

# Imports from Python library. Setmode automatically sets up pin numbering
import RPi.GPIO as GPIO
import time


# Setmode might have to go inside of function. idk.
class Echolocate(object):
   def __init__(self):
      GPIO.setmode(GPIO.BCM) # Set easy pin numbering system
      GPIO.setwarnings(False) # Ignore stupid warnings
      self.trig = 23 # GPIO 23 (Pin 16), Connects to Sonar Sensor trigger
      self.echo = 24 # GPIO 24 (pin 18), connects to Sonar Sensor Echo
      GPIO.setup(self.trig, GPIO.OUT) # set GPIO ports as either output or input
      GPIO.setup(self.echo, GPIO.IN)

   def getSample(self):
      x = self.takeSample(self.trig, self.echo)
      y = self.takeSample(self.trig, self.echo)
      z = self.takeSample(self.trig, self.echo)

      while max(x,y,z) > 2*min(x,y,z):
         print ("Outlier Detected. Retaking Samples")
         x = self.takeSample(self.trig, self.echo)
         y = self.takeSample(self.trig, self.echo)
         z = self.takeSample(self.trig, self.echo)

      avDistance = (x+y+z)/float(3)
      return avDistance


   def takeSample(self, trig, echo):
      # Uncomment for error checking
      #print "Once"
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(trig, GPIO.OUT) # set GPIO ports as either output or input
      GPIO.setup(echo, GPIO.IN)
      GPIO.output(trig,  False) # set trigger pin to low,
      time.sleep(.10) # wait for it to settle
      GPIO.output(trig, True)
      time.sleep(0.00001) # HC - SR04 documentation, set trig high 10uS.
      GPIO.output(trig, False)
      while GPIO.input(echo) == 0: # trigger sets echo pin to high
        start = time.time() # Keeps getting stuck here! 
      while GPIO.input(echo) == 1: # echo goes low when signal is returned
        end = time.time() # Python returns last time echo was high 
      duration = end - start # measure the time the pin stayed high
      soundSpeed = 34300 # Speed of soundwave
      distance = duration*34300/2 # account for return trip
      # reset pins, return distance to nearest object
      return distance

if __name__ == "__main__":
   x = Echolocate()
   print x.getSample()
   print x.getSample()
