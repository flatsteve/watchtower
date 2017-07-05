import glob

def get_images():
    images = glob.glob('./static/camera-images/*.jpg')
    return sorted(images)
