import sys, glob, time, datetime, os
import config
import requests

from db import db, Settings
from gpiozero import Buzzer, LED


buzzer = Buzzer(17)
led = LED(26)


def reset():
    config.alerts_triggered = 0

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
        reset()


def flash():
    try:
        print("Flash")
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
        r = requests.post(config.zap_url, data={'time': datetime.datetime.now().strftime("%H:%M")})
        print(r.status_code, r.reason)
    except Exception:
        print("Somthing went wrong...")
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

