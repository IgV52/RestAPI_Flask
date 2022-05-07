from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from webapp.db import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    question = relationship('Question', backref='posts')

class Question(db.Model):
    __tablename__ = 'questions'

    my_id = Column(Integer, primary_key=True)
    id = Column(Integer)
    answer = Column(String)
    question = Column(String)
    value = Column(Integer)
    created_at = Column(Date)
    post_id = Column(Integer, ForeignKey('posts.id'))

    def __repr__(self):
        return self.question
