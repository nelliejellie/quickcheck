import requests
from requests.api import request
import json

url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty&orderBy=%22$key%22&limitToFirst=10"
url_two = "https://hacker-news.firebaseio.com/v0/item/27893678.json?print=pretty"


response = requests.get(url="https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty&orderBy=%22$key%22&limitToFirst=10", timeout=3,)
word = response.text
new_list = word.split(',')
filtered_list = new_list[1:8]

new_array = []
for child in filtered_list:
    new_response  = requests.get(url=f'https://hacker-news.firebaseio.com/v0/item/{int(child)}.json?print=pretty')
    my_dict = json.loads(new_response.text)
    print(type(my_dict))
    print(my_dict['by'])
    new_array.append(my_dict)
for data in new_array:
    print(data['url'])

