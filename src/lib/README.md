# Tylor Lehman
# BatPi
# README
Senior Project. Make a Raspberry Pi use a sonic distance sensor to map its surroundings, and then navigate a certain distance from its starting location.




Pin assignments (GPIO.BCM):
name - assignment - physical pin - file

power-  3.3V 	(Physical pin 2)  - Power rail
Ground- 	(Physical pin 6)  - Ground rail
trig -  GPIO 23 (physical pin 16) - Echolocate.py
echo -  GPIO 24 (physical pin 18) - Echolocate.py
Servo - GPIO 4  (physical pin 7 ) - ServoDrive.py (only used as example)
Motor1A-GPIO 17 (physical pin 11) - PiPilot.py
Motor1B-GPIO 27 (physical pin 13) - PiPilot.py
Motor1E-GPIO 22 (physical pin 15) - PiPilot.py
Motor2A-GPIO 5  (physical pin 29) - PiPilot.py
Motor2B-GPIO 6  (physical pin 31) - PiPilot.py
Motor2E-GPIO 13 (physical pin 33) - PiPilot.py