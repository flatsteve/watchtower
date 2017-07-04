import time
import datetime
import sys
import config
from gpiozero import MotionSensor, Buzzer, LED, Button
from instapush import Instapush, App
from camera import take_picture

device = App(appid=config.appid, secret=config.secret)
sensor = MotionSensor(4)
buzzer = Buzzer(17)
led = LED(18)
button = Button(13)
system_active = False

config.alerts_triggered = 0

def flash():
	print('Motion detected')
	led.blink()
	buzzer.beep()
	time.sleep(config.delay_between_alerts)
	led.off()
	buzzer.off()

def startup():
	print('Starting Watchtower in')
	for i in range(config.startup_delay, 0, -1):
                print(i)
		led.on()
		time.sleep(1)
		led.off()
		time.sleep(1)

def toggle():
	print('Button pressed')
	if not system_active:
		startup()
		system_active = True
	else: 
		system_active = False
		config.alerts_triggered = 0

def alert():
	if config.alerts_triggered >= config.max_alerts:
		return sys.exit()

	device.notify(
			event_name='alert', 
			trackers={ 'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
			)
	take_picture()
	flash()	
	config.alerts_triggered += 1

try:
	while True:
		button.when_pressed = toggle
		
		if system_active:
			sensor.wait_for_motion()
			sensor.when_motion = alert()
			
except KeyboardInterrupt:
	print 'Sensor shutting down...'
	led.off()
	buzzer.off()	
	sys.exit()
