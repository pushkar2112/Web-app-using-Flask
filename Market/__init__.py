from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '29c4ae51f26e6eb11f88d2cb'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from Market import routes