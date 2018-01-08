import sys, glob, time, datetime, os
import config

from db import db, Settings
from instapush import Instapush, App
from gpiozero import Buzzer, LED

device = App(appid=config.appid, secret=config.secret)
buzzer = Buzzer(17)
led = LED(26)

def reset():
    try:
        led.off()
        buzzer.off()
    except: 
        pass

def get_images():
    images = glob.glob('./static/camera-images/*.jpg')
    return sorted(images, reverse=True)

def get_settings():
    return Settings.query.get(1)

def save_settings(settings):
    current_settings = Settings.query.get(1)
    current_settings.iso = settings.get('iso', 0)
    current_settings.shutter_speed = settings.get('shutter_speed', 0)
    db.session.commit()

def remove_image(url):
    try:
        os.remove(url)
    except OSError:
        print('Failed to remove image')

def startup():
    reset()
    print('Starting Watchtower in...')

    for i in range(config.startup_delay, 0, -1):
        print(i)
        try:
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
        except: 
            print('Problem with pins')
            pass

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
    try:
        led.blink()
        buzzer.beep()
        time.sleep(config.delay_between_alerts)
        led.off()
        buzzer.off()
    except:
        print('Problem with pins')
        pass

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
