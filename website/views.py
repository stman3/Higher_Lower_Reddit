from flask import Blueprint, render_template,request,session,redirect

import praw
from .handleReddit import get_posts, handle_choise


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")




 
@views.route('/classic', methods=['GET', 'POST'])
def classic():
    posts_data = get_posts()
    current_index = session.get('current_index', 0)
    if request.method == 'POST':
      handle_choise()
    return render_template("classic.html", posts=posts_data, current_index=current_index)


@views.route('/result')
def result():
    return render_template("result.html")