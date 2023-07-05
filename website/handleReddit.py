import praw
from flask import Blueprint, render_template,request,session,redirect




posts_data = []
def get_posts():
    if not posts_data:
        print('Fetching data...')
        reddit = praw.Reddit(client_id='EDCRTsHPuqwB3ONd0ejxHw', client_secret='6lHbT3yJ8FrkYmtTiu-favjMmkJ_Jw', user_agent='Higher_Lower/1.0 stman')
        subreddit = reddit.subreddit('memes')
        hot_posts = subreddit.hot(limit=100)
        for post in hot_posts:
            posts_data.append({'url': post.url, 'ups': post.ups})
    return posts_data



def handle_choise():
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
            session['current_index'] = 0

    elif choice == 'lower':
        print(len(posts_data))
        print(current_index)
        if int(posts_data[current_index]['ups']) > int(posts_data[current_index+1]['ups']):
            current_index += 1
            session['current_index'] = current_index
            print(current_index)
        else:
            pass
