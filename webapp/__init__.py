from flask import Flask
from webapp.quiz.api import api_bp
from webapp.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.before_first_request
    def create_table():
        db.create_all()
    
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
