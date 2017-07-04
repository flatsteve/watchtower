import picamera
import time

def take_picture():
    camera = picamera.PiCamera()
    print('Capturing picture')
    camera.capture("./static/camera-images/" + time.strftime("%y%m%d_%H-%M-%S") + ".jpg")
    camera.close()
