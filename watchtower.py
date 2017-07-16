import config
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes import api
from utils import get_images

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///watchtower'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
app.register_blueprint(api, url_prefix='/api')

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    images = get_images()

    return render_template('index.html', 
            images=images,
            active=config.system_active
		    )

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
