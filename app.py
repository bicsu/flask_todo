from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *

app = Flask(__name__)

# db설정
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///todo'
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') #Heroku할 때
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app,db)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/posts/new')
def new():
    return render_template('new.html')

@app.route('/posts/create', methods=["POST"])
def create():
    todo = request.form.get('todo')
    date = request.form.get('date')
    post = Post(todo = todo, date = date)
    db.session.add(post)
    db.session.commit()
    return redirect('/posts/{}'.format(post.id))