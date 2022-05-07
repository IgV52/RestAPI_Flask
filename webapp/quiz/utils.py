from webapp.db import db
from webapp.quiz.models import Post, Question

import requests

def check_dicts(dicts: dict):
    quality_value = len(dicts)
    data_value = len([key for key in dicts if dicts[key]])
    if quality_value == data_value:
        return True
    return False

def get_db(data: list):
    db.session.bulk_insert_mappings(Question, data)
    db.session.commit()
    info_base(data[0]['post_id'])

def get_or_create_data(data: list):
    uniq_quest = []
    
    for dicts in data:
        quest=Question.query.filter(Question.id == dicts['id']).first()
        
        if not quest and dicts not in uniq_quest and check_dicts(dicts):
            uniq_quest.append(dicts)
    get_db(uniq_quest) 

def format_data(data: list, post_id: int):
    del_key = ['category','airdate','updated_at','game_id','invalid_count','category_id']
    new_data = []
    for dicts in data:
        for key in del_key:
            del dicts[key]
        dicts['post_id'] = post_id
        new_data.append(dicts)
    return new_data

def info_base(post_id: int):
    question = Question.query.filter(Question.post_id==post_id).all()
    count = Post.query.order_by(Post.id.desc()).first()
    quality_quest = len(question)
    num = count.count - quality_quest
    if quality_quest == count.count:
        return 'Good'
    else:
        questions_quiz(num, post_id)

def questions_quiz(num_questions: int, post_id: int):
    url = f'http://jservice.io/api/random?count={num_questions}'
    result = requests.get(url)
    data = result.json()
    data = format_data(data, post_id)
    get_or_create_data(data)



    




