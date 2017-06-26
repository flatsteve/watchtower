class User(db.Model):
	__tablename__ = 'users'
 	id = db.Column('id', db.Integer, primary_key=True)
 	name = db.Column(db.String(60))

 	def __init__(self, name):
 		self.name = name
