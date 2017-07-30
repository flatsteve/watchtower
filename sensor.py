#!/usr/bin/python

import config
from gpiozero import MotionSensor, Button
from utils import flash, alert, toggle, shutdown

sensor = MotionSensor(4)

try:
	while True:
		sensor.wait_for_motion()
		sensor.when_motion = alert()
			
except KeyboardInterrupt:
    shutdown()
