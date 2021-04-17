import os

from flask import Flask, make_response
from flask_migrate import Migrate, MigrateCommand
from config import Config
from flask_script import Manager
from flask import render_template, redirect, url_for, request
import random
import logging
import sys
from logging import Formatter
from flask import send_file, abort

def log_to_stderr(app):
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    handler.setLevel(logging.WARNING)
    app.logger.addHandler(handler)


app = Flask(__name__)
app.config.from_object(Config)

from models import *

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


def generate_code(codes):
    al = list("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM")
    random.shuffle(al)
    n = random.randint(5, 10)
    res = "".join(al[:n])
    if res in codes:
        res = generate_code(codes)
    return res


def generate_text(ideas):
    text = ""
    for idea in ideas:
        text += str(idea.text) + "\n\n\n" + "-" * 10 + "\n"
    return text


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/storm/create', methods=["GET", "POST"])
def create_storm():
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('desc')
        codes = Storm.query.all()
        code = generate_code(codes)
        try:
            storm = Storm(name=name, description=description, code=code)
            ss = db.session
            ss.add(storm)
            ss.commit()
            return redirect(url_for('created_code', code=code))
        except Exception as e:
            print(e)
            return render_template('index.html')

    return render_template('create_storm.html')


@app.route('/storm/created/<code>')
def created_code(code):
    storm = Storm.query.filter(Storm.code == code).first_or_404()
    return render_template("created_code.html", storm=storm)


@app.route('/enter-to', methods=["GET", "POST"])
def enter_to_storm():
    if request.method == "POST":
        code = request.form.get('code')
        return redirect(url_for('stormif', code=code))
    return render_template('enter_to_storm.html')


@app.route('/storm/<code>', methods=["GET", "POST"])
def stormif(code):
    if request.method == "POST":
        text = request.form.get('text')
        color = request.form.get('color')
        print(request.form)
        try:
            storm_id = Storm.query.filter(Storm.code == code).first().id
            idea = Idea(text=text, color=color, storm_id=storm_id)
            ss = db.session
            ss.add(idea)
            ss.commit()
        except Exception:
            return redirect(url_for('page_not_found'))

    storm = Storm.query.filter(Storm.code == code).first_or_404()
    ideas = storm.ideas.order_by(Idea.created.desc())
    if code not in request.cookies.get("STORMS", "").split('```'):
        resp = make_response(render_template("storm_interface.html", storm=storm, ideas=ideas))
        now_cookies = request.cookies.get("STORMS", "").split('```')
        now_cookies.append(code)
        value = "```".join(now_cookies)
        resp.set_cookie("STORMS", value)
        return resp
    else:
        return render_template("storm_interface.html", storm=storm, ideas=ideas)


@app.route("/mystorms")
def my_storms():
    my_storms = request.cookies.get("STORMS", "")
    my_storms = my_storms.split("```")
    storms = []
    for my_storm in my_storms:
        if my_storm:
            storms.append(Storm.query.filter(Storm.code == my_storm).first())

    # if not storms:
    #     return render_template('404.html'), 404
    return render_template('your_storms.html', storms=storms[::-1])


@app.route("/storm/download/<code>")
def download_file(code):
    try:
        filelist = [f for f in os.listdir(app.config["CLIENT_TXT"])]
        for file in filelist:
            os.remove(os.path.join(app.config["CLIENT_TXT"], file))

        storm = Storm.query.filter(Storm.code == code).first()
        ideas = Idea.query.filter(Idea.storm_id == storm.id)
        path = app.config["CLIENT_TXT"]+"storm_"+code+".txt"
        text = generate_text(ideas)
        f = open(path, "w", encoding="utf-8")
        f.write(text)
        f.close()
        return send_file(path, as_attachment=True, cache_timeout=0)
    except FileNotFoundError:
        abort(404)



if __name__ == '__main__':
    log_to_stderr(app)
    app.run(port=8070)
