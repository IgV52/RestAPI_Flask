from flask import Flask
from flask_migrate import Migrate
from webapp.quiz.app import api_bp
from webapp.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    app.register_blueprint(api_bp, url_prefix='/api')

    return app