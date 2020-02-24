"""
Used and modified example from https://github-flask.readthedocs.io/en/latest/
"""
import os
from flask import Flask, request, g, session, redirect, url_for, render_template
from flask import jsonify
from flask_github import GitHub
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

# setup variables
DEBUG = False

SECRET_KEY = os.environ['DB_SECRET_KEY']
REPO_INFO = os.environ['REPO_INFO']
REPO_URL = 'https://github.com/{}'.format(REPO_INFO)
GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']

# setup flask
app = Flask(__name__)
app.config.from_object(__name__)

# setup github-flask
github = GitHub(app)

# setup sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/cloner.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    github_access_token = Column(String(255))
    github_id = Column(Integer)
    github_login = Column(String(255))

    def __init__(self, github_access_token):
        self.github_access_token = github_access_token


db.create_all()
db.session.commit()


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@app.after_request
def after_request(response):
    db.session.remove()
    return response


@app.route('/')
def index():
    return render_template('main.html', repo=REPO_URL, user=g.user)


@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.github_access_token


@app.route('/github-callback')
@github.authorized_handler
def authorized(access_token):
    next_url = request.args.get('next') or url_for('index')
    if access_token is None:
        return redirect(next_url)

    user = User.query.filter_by(github_access_token=access_token).first()
    if user is None:
        user = User(access_token)
        db.session.add(user)

    user.github_access_token = access_token

    # Not necessary to get these details here
    # but it helps humans to identify users easily.
    g.user = user
    github_user = github.get('/user')
    user.github_id = github_user['id']
    user.github_login = github_user['login']

    db.session.commit()

    session['user_id'] = user.id
    return redirect(next_url)


@app.route('/login', methods=['POST'])
def login():
    if session.get('user_id', None) is None:
        return github.authorize(scope="public_repo")
    else:
        return 'Already logged in'


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/user')
def user():
    return jsonify(github.get('/user'))


@app.route('/clone_repo', methods=['GET', 'POST'])
def clone_repo():
    res = github.post('/repos/{}/forks'.format(REPO_INFO))
    if res.get('html_url'):
        return redirect(res.get('html_url'))
    return "Something went wrong, clear session and try again"