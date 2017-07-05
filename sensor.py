from config import system_active
from gpiozero import MotionSensor, Button
from utils import flash, alert, toggle, shutdown

sensor = MotionSensor(4)
button = Button(13)

try:
	while True:
		button.when_pressed = toggle
		
		if system_active:
			sensor.wait_for_motion()
			sensor.when_motion = alert()
			
except KeyboardInterrupt:
    shutdown()
