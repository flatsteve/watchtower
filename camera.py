import picamera
import time
import os
from utils import get_images

def take_picture():
    camera = picamera.PiCamera()
    images = get_images()
    
    if len(images) >= 5:
        os.remove(images[-1])
   
    print('Capturing picture')
    camera.capture("./static/camera-images/" + str(int(time.time())) + ".jpg")
    camera.close()
