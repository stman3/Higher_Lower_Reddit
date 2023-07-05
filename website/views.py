from flask import Blueprint, render_template,request
import praw
import requests


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")




posts_data = []
@views.route('/classic', methods=['GET', 'POST'])
def classic():
    if not posts_data:
        print('Fetching data...')
        reddit = praw.Reddit(client_id='EDCRTsHPuqwB3ONd0ejxHw', client_secret='6lHbT3yJ8FrkYmtTiu-favjMmkJ_Jw', user_agent='Higher_Lower/1.0 stman')
        subreddit = reddit.subreddit('memes')
        hot_posts = subreddit.hot(limit=100)
        for post in hot_posts:
            posts_data.append({'url': post.url, 'ups': post.ups})

    current_index = 0
    if request.method == 'POST':
        current_index = int(request.form.get('current_index', 0))
        if current_index < len(posts_data) - 1:
            current_index += 1

    return render_template("classic.html", posts=posts_data, current_index=current_index)