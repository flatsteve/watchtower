import glob
import os
from datetime import datetime
from flask import Flask
from flask import render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from camera import take_picture

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///watchtower'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'

db = SQLAlchemy(app)

def get_images():
    images = glob.glob('./static/camera-images/*.jpg')
    return sorted(images)

@app.route('/', methods=['GET', 'POST'])
def index():
    images = get_images()

    return render_template('index.html', 
		    images=images
		    )

@app.route('/picture', methods=['POST'])
def picture():
    take_picture()
    images = get_images()
    
    if len(images) >= 7:
        os.remove(images[0])

    return redirect(url_for('index'))

@app.route('/toggle-sensor', methods=['POST'])
def toggle_sensor():
    #toggle()
    return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
