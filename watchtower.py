import config, re, datetime
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

@app.route('/', methods=['GET'])
def index():
    images = get_images()
    image_list = []

    for imageUrl in images:
        image_list.append({ 
            'url': imageUrl, 
            'date': datetime.datetime.fromtimestamp(
                int(re.findall(r'[0-9]+', imageUrl)[0])).strftime('%a, %d %b %Y at %H:%M%p')
            })

    return render_template('index.html', 
            images=image_list,
            active=config.system_active
		    )

@app.route('/settings', methods=['GET'])
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
