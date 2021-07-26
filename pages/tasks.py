from celery import group, shared_task
from celery.schedules import crontab
from django.db import connection
from django.utils import timezone
from .models import Latest_news, Comments
import requests
from requests.api import request
import json


#tasks to save latest news
@shared_task(run_every=crontab(minute=('*/5')))
def save_latest_news():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty&orderBy=%22$key%22&limitToFirst=100"
    try:
        response = requests.get(url="https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty&orderBy=%22$key%22&limitToFirst=100", timeout=3,)
    except:
        print("connection error")

    word = response.text
    new_list = word.split(',')
    filtered_list = new_list[2:97]
    new_array = []
    for child in filtered_list:
        try:
            new_response  = requests.get(url=f'https://hacker-news.firebaseio.com/v0/item/{int(child)}.json?print=pretty')
        except:
            print('connection error')
        my_dict = json.loads(new_response.text)
        new_array.append(my_dict)
    for data in new_array:
        by = data['by']
        descendants = data['descendants']
        hacker_id = data['id']
        score = data['score']
        time = data['time']
        title = data['title']
        type = data['type']
        if not data['url']:
            url = "google.com"
        url = data['url']

        news =  Latest_news(by=by, descendants=descendants, hacker_id=hacker_id, score=score, time=time, title=title, type=type,url=url)
        news.save()


