from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from config import Config
from flask_script import Manager
from flask import render_template, redirect, url_for, request
import random
import logging
import sys
from logging import Formatter


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
            return redirect(url_for('index'))

    storm = Storm.query.filter(Storm.code == code).first_or_404()
    ideas = storm.ideas.order_by(Idea.created.desc())
    return render_template("storm_interface.html", storm=storm, ideas=ideas)


if __name__ == '__main__':
    log_to_stderr(app)
    app.run(port=8070)