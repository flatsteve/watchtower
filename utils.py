import sys
import glob
import time
import datetime
import config
from instapush import Instapush, App
from gpiozero import Buzzer, LED

device = App(appid=config.appid, secret=config.secret)
buzzer = Buzzer(17)
led = LED(26)

def reset():
    led.off()
    buzzer.off()

def get_images():
    images = glob.glob('./static/camera-images/*.jpg')
    return sorted(images, reverse=True)

def startup():
    reset()
    print('Starting Watchtower in...')

    for i in range(config.startup_delay, 0, -1):
        print(i)
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

def toggle():
    print('Toggling system')
    if not config.system_active:
        startup()
        config.system_active = True
    else:
        config.system_active = False
        config.alerts_triggered = 0
        reset()

def flash():
    led.blink()
    buzzer.beep()
    time.sleep(config.delay_between_alerts)
    led.off()
    buzzer.off()

def alert():
    if config.alerts_triggered >= config.max_alerts:
        return
    try:
        device.notify(
            event_name='alert',
            trackers={ 'time': datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S") }
            )
    except Exception:
        pass
    
    # Avoid circular dependancy 
    from camera import take_picture
    take_picture()
    flash()
    config.alerts_triggered += 1

def shutdown():
    print 'Sensor shutting down...'
    reset()
    sys.exit()
