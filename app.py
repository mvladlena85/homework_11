from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route("/part1/")
def first_part_of_the_homework():
    return render_template('homework_part1.html')


@app.route("/candidate/<int:uid>/")
def candidate_card(uid):
    candidate = get_candidate(uid)
    return render_template('card.html', candidate_card=candidate)


@app.route("/candidate/<candidate_name>/")
def search_candidates_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    candidates_quantity = len(candidates)
    return render_template('search.html', candidates=candidates, candidates_quantity=candidates_quantity)


@app.route("/skill/<skill>/")
def search_candidates_by_skill(skill):
    candidates = get_candidates_by_skill(skill)
    candidates_quantity = len(candidates)
    return render_template('skill.html', skill=skill, candidates=candidates, candidates_quantity=candidates_quantity)


app.run()
