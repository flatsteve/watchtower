import os, subprocess
import config
from flask import Blueprint, url_for, redirect, request
from camera import take_picture
from utils import get_images, remove_image, toggle, startup, reset, save_settings

api = Blueprint('api', __name__)

@api.route('/picture', methods=['POST', 'DELETE'])
def picture():
    url = request.args.get('url', None)

    if request.method == 'POST' and url is None:
        take_picture()
    else:
        remove_image(url)

    return redirect(url_for('index'))

@api.route('/toggle-active', methods=['POST'])
def toggle_active():
    if not config.system_active:
        startup()
        config.process = subprocess.Popen('./sensor.py')
        config.system_active = True
    else:
        reset()
        config.process.kill()
        config.system_active = False
        config.alerts_triggered = 0

    return redirect(url_for('index'))

@api.route('/camera-settings', methods=['POST'])
def camera_settings():
    settings = request.form
   
    if settings is not None:
        save_settings(settings)

    return redirect(url_for('settings'))
