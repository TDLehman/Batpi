# Tylor Lehman
# BatPi
# ServoDrive.py

# set: The first argument to this is the file to be written to (property) and the second argument the value to write to it.

# the program starts with a few file writes to turn the delay mode off, set the mode to be 'servo', set the maximum servo value to be 180 and finally to make the output pin active.

# A variable (delay_period) is used to contain the time in seconds between each step of the servo.

# The while loop will just continue forever. Within the loop there are two near identical 'for' loops. The first counts the angle up from 0 to 180 and the second sets the servo angle to 180 – angle, moving the servo arm back from 180 to 0 degrees.

#----------------------------------------------------------------------

import time
def set(property, value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
		f.write(value)
		f.close()	
	except:
		print("Error writing to: " + property + " value: " + value)
     
def setServo(angle):
	set("servo", str(angle))
	
	
set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")
     
delay_period = 0.01
     
while True:
	for angle in range(0, 180):
		setServo(angle)
		time.sleep(delay_period)
	for angle in range(0, 180):
		setServo(180 - angle)
		time.sleep(delay_period)
