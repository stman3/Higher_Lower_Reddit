from flask import Blueprint, render_template,request,session

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

    current_index = session.get('current_index', 0)
    if request.method == 'POST':
        current_index = session['current_index']
        choice = request.form.get('choice')
        if choice == 'higher':
            print('here',current_index)
            print(posts_data[0]['ups'])
            if int(posts_data[current_index]['ups']) < int(posts_data[current_index+1]['ups']):
                print(current_index)
                current_index += 1
                session['current_index'] = current_index
            else:
                pass

        elif choice == 'lower':
            print(len(posts_data))
            print(current_index)
            if int(posts_data[current_index]['ups']) > int(posts_data[current_index+1]['ups']):
                current_index += 1
                session['current_index'] = current_index
                print(current_index)
            else:
                pass
    session['current_index'] = current_index
    return render_template("classic.html", posts=posts_data, current_index=current_index)