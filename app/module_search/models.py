from app import db

# Define a User model
class User(db.Model):

    __tablename__ = 'users'

    # User Name
    id = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(45),  nullable=False)
    email    = db.Column(db.String(45),  nullable=True)
    password = db.Column(db.String(45),  nullable=False)
    first_name = db.Column(db.String(45), nullable=True)
    last_name = db.Column(db.String(45), nullable=True)

    # Authorisation Data: role & status
    #role     = db.Column(db.SmallInteger, nullable=False)
    #status   = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, username, email, password, first_name, last_name):

        self.username     = username
        self.email    = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User %r>' % (self.username)   
