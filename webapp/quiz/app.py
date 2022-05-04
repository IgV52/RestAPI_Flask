from flask import Blueprint
from flask_restful import Api
from webapp.quiz.resources import Quest

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Quest, '/')