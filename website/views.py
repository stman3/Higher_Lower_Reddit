from flask import Blueprint, render_template,request,session,redirect
import praw
from .handleReddit import get_posts, handle_choise
import random

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")



@views.route('/Contact')
def contact():
    return render_template("contact.html")

@views.route('/about')
def about():
    return render_template("about.html")

 
@views.route('/classic', methods=['GET', 'POST'])
def classic():
    posts_data = get_posts()
    current_index = session.get('current_index', 0)
    if request.method == 'POST':
      session['current_index'] = current_index
      should_redirect = handle_choise()
      if should_redirect:
            random.shuffle(posts_data)
            return redirect('/result')
      else:
            return redirect('/classic')
    return render_template("classic.html", posts=posts_data, current_index=current_index)


@views.route('/result')
def result():
    score = session.get('current_index', 0)
    session['current_index'] = 0
    return render_template("result.html",score=score)