from flask import Flask, request, render_template
from candidates import *

app = Flask(__name__)

candidate = Candidates(load_candidates_from_json('candidates.json'))                                # создание объекта класса


@app.route('/')
def page_all_candidates():
    """Вывод списка всех кандидатов в заданном формате """

    new_dict = candidate.get_candidate_names()                                                      # получение словаря ид:имя

    return render_template('list.html', key=new_dict.keys(), candidates=new_dict)                   # возвращаем через шаблон ссылку и список имен кандидатов


@app.route('/candidates/<int:id>')
def page_candidates_by_id(id):
    """Вывод данных о кандидате через ид """
    name, position, image, skills = candidate.get_candidate_by_id(id)                               # получение даных через get_candidate_by_id
    return render_template('card.html', name=name, position=position, image=image, skills=skills)   # шаблонизация


@app.route('/search/<candidate_name>')
def get_candidates_by_name(candidate_name):
    """Вывод данных о кандидате по имени """
    count, result_dict = candidate.get_candidates_by_name(candidate_name)
    return render_template('search.html', count=count, key=result_dict.keys(), candidates=result_dict)


@app.route('/skill/<skill_name>')
def get_candidates_by_skill(skill_name):
    """Вывод данных о кандидате по навыку """
    count, result_dict = candidate.get_candidates_by_skill(skill_name)
    return render_template('skill.html', count=count, key=result_dict.keys(), candidates=result_dict)


