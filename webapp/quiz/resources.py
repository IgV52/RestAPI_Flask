from flask_restful import Resource, reqparse
from webapp.db import db
from webapp.quiz.models import Post, Question
from webapp.quiz.utils import questions_quiz

parser = reqparse.RequestParser()

class Quest(Resource):
    def post(self):
        
        parser.add_argument('num_questions', type=int, help=0)
        
        args = parser.parse_args()
        post = Post(count=args['num_questions'])
        
        last_quest = {"answer": "Error input"}

        if post.count:
            db.session.add(post)
            db.session.commit()
        
            post_id = Post.query.order_by(Post.id.desc()).first()
            last_quest = {"Question": str(Question.query.order_by(Question.my_id.desc()).first())}
            questions_quiz(args['num_questions'], post_id.id)
    
        return last_quest, 201


