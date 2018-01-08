import picamera, time, os

from utils import get_images
from db import Settings

def take_picture():
    images = get_images()
    if len(images) >= 5:
        os.remove(images[-1])
 
    current_settings = None
    
    try: 
        current_settings = Settings.query.get(1)
    except: 
        pass

    if current_settings is not None:
        camera = picamera.PiCamera()
        camera.iso = current_settings.iso
        camera.shutter_speed = current_settings.shutter_speed
    else:
        camera = picamera.PiCamera()

    print('Capturing picture')
    camera.capture("./static/camera-images/" + str(int(time.time())) + ".jpg")
    camera.close()
