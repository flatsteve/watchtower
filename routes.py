import os
import config
import subprocess
from flask import Blueprint, url_for, redirect
from camera import take_picture
from utils import get_images, toggle

api = Blueprint('api', __name__)

@api.route('/picture', methods=['POST'])
def picture():
    take_picture()

    return redirect(url_for('index'))

@api.route('/toggle-active', methods=['POST'])
def toggle_active():
    if not config.system_active:
        config.process = subprocess.Popen('./sensor.py')
        config.system_active = True
    else:
        config.process.kill()
        config.system_active = False
        config.alerts_triggered = 0

    return redirect(url_for('index'))

