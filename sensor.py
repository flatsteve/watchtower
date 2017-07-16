#!/usr/bin/python

import config
from gpiozero import MotionSensor, Button
from utils import flash, alert, toggle, shutdown

sensor = MotionSensor(4)
#button = Button(13)

try:
	while True:
        #button.when_pressed = toggle
		
		#if config.system_active:
		sensor.wait_for_motion()
		sensor.when_motion = alert()
			
except KeyboardInterrupt:
    shutdown()
