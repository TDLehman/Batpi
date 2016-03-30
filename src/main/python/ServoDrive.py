# Tylor Lehman
# BatPi
# ServoDrive.py

# the servod daemon from ./servoblaster/PiBits/servoblaster/
# It sets up a named pipe device named /dev/servoblaster.
# Writing pulse width to /dev/servoblaster actuates the servo.
#
# Example: echo 0=150 > /dev/servoblaster
# The example means send pulse width of 150 steps (each step is 10us, so pulse width is 1500us or 1.5ms)
# to servo #0 (which by default should be connected to pin 7, unless the defaults are overridden from servod command line).
# Note that 'sudo' is not required because all users have write permission on /dev/servoblaster
#
# The list of default pins and servo numbers are shown below. What this means is if you connect
# servo to board pin 7, that servo can be addresses as '0'.
#      Servo number    GPIO number   Pin in P1 header
#          0               4             P1-7
#          1              17             P1-11
#          2              18             P1-12
#          3             21/27           P1-13
#          4              22             P1-15
#          5              23             P1-16
#          6              24             P1-18
#          7              25             P1-22

from time import sleep

hold_position_time = 0.1 # secs
step_size = 10 # ie, change pulse width by 10*10us = 100us or 0.1ms in each step

# Dont buffer the writes to the device file, to avoid explicit flush()es.
dont_buffer = 0

with open('/dev/servoblaster', "w", dont_buffer ) as servo_blaster_device:
    while True:
        for pulse_width in range(100,200,step_size):
            # The \n is required. Without it, it doesn't work.
            cmd = "0=" + str(pulse_width) + "\n"
            print cmd
            servo_blaster_device.write(cmd)
            # flush() is required if buffering is enabled, which by default is.
            #servo_blaster_device.flush()
            sleep(hold_position_time)

        for pulse_width in range(200,100,-step_size):
            cmd = "0=" + str(pulse_width) + "\n"
            print cmd
            servo_blaster_device.write(cmd)
            #servo_blaster_device.flush()
            sleep(hold_position_time)
share i
