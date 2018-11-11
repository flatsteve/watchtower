import picamera, time, os

from utils import get_images
from db import Settings
from time import sleep

def take_picture():
    images = get_images()

    if len(images) >= 5:
        os.remove(images[-1])
 
    current_settings = None
    
    try: 
        current_settings = Settings.query.get(1)
    except: 
        pass
    
    print("ISO:", current_settings.iso)
    print('Shutter speed', current_settings.shutter_speed)

    if current_settings is not None:
        camera = picamera.PiCamera()
        camera.iso = current_settings.iso
        camera.shutter_speed = current_settings.shutter_speed
        sleep(3)
    else:
        camera = picamera.PiCamera()

    print('Capturing image')
    camera.capture('./static/camera-images/' + str(int(time.time())) + '.jpg')

    camera.close()
