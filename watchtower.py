from flask import Flask
from flask import render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///watchtower'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(60))

    def __init__(self, name):
	    self.name = name

@app.route('/', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Title is required', 'error')
        else:
            user = User(request.form['name'])
            db.session.add(user)
            db.session.commit()
            flash(u'Todo item was successfully created')
    return render_template('users.html', 
		    users=User.query.all()
		    )

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
