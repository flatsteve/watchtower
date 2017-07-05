import os
from flask import Blueprint, url_for, redirect
from camera import take_picture
from utils import get_images

api = Blueprint('api', __name__)

@api.route('/picture', methods=['POST'])
def picture():
    take_picture()
    images = get_images()

    if len(images) >= 7:
        os.remove(images[0])

    return redirect(url_for('index'))

@api.route('/toggle-sensor', methods=['POST'])
def toggle_sensor():
    #toggle()
    return redirect(url_for('index'))


