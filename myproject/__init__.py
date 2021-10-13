import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# Often people will also separate these into a separate config.py file 
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#These imports need to come after you've defined db (avoid errors in models.py files).
## Grab the blueprints from the other views.py files for each "app"
from myproject.books.views import books_blueprint
from myproject.library_books.views import librarybooks_blueprint
from myproject.users.views import users_blueprint
from myproject.libraries.views import libraries_blueprint
from myproject.library_activities.views import libraryactivities_blueprint


app.register_blueprint(books_blueprint, url_prefix='/books')
app.register_blueprint(librarybooks_blueprint, url_prefix="/library_books")
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(libraries_blueprint, url_prefix='/libraries')
app.register_blueprint(libraryactivities_blueprint, url_prefix='/library_activities')