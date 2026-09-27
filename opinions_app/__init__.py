from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'SECRET KEY'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from . import views, models, forms, error_handlers, cli_commands
