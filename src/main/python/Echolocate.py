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


      # Check for outliers
      while max(x,y,z) > 2*min(x,y,z) or min(x,y,z)==-1:
         #print ("Outlier Detected. Retaking Samples")
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
      time.sleep(.05) # wait for it to settle
      # Instead, just wait for echo pin to be low.
      while GPIO.input(echo) == 1:
         print "waiting for this thing to cool off"
      GPIO.output(trig, True)
      time.sleep(0.00001) # HC - SR04 documentation, set trig high 10uS.
      GPIO.output(trig, False)
      loopbreaker=0
      start=time.time() # added this to prevent crash from undefined start
      while GPIO.input(echo) == 0: # trigger sets echo pin to high
        start = time.time() # Keeps getting stuck here!
        loopbreaker=loopbreaker+1
        if loopbreaker>1000:  # This would indicate that Echo didn't trigger
          #print "Echo didn't trigger. Returning"
          return -1
          
        #print time.time()-start
      end=start # prevent crash from undefined end hopefully!
      while GPIO.input(echo) == 1: # echo goes low when signal is returned
        end = time.time() # Python returns last time echo was high 
      duration = end - start # measure the time the pin stayed high
      distance = duration*17150 # Will return Distance in CM
      # reset pins, return distance to nearest object
      return distance

if __name__ == "__main__":
   y = Echolocate()
   print y.getSample()
   # Try 100 Times
   #x = 0
   #while x<100:
     #if y.getSample()>150:
       #print "Something went wrong at "+x
     #x=x+1
   #print "done. did something go wrong? ^ "+x  
   
