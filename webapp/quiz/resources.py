from flask_restful import Resource, reqparse
from webapp.quiz.utils import questions_quiz
from webapp.db import db
from webapp.quiz.models import Post, Question

parser = reqparse.RequestParser()

class Quest(Resource):
    def post(self):
        parser.add_argument('num_questions', type=int, help=0)
        args = parser.parse_args()
        post = Post(count=args['num_questions'])
        db.session.add(post)
        db.session.commit()
        post_id = db.session.query(Post).order_by(Post.id.desc()).first()
        last_quest = db.session.query(Question).order_by(Question.question.desc()).first()
        error = questions_quiz(args['num_questions'], post_id.id)
        last_quest = {'last_question' : str(last_quest)}
        if error:
            last_quest = error
        return last_quest, 201


