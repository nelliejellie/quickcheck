from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Latest_news, Comments
from .tasks import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json
from .serializers import NewsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.generic import TemplateView, ListView


# Create your views here.

# index view
def index(request):
    # call the task function
    try:
        save_latest_news()
    except:
        print("connection error")
    # import models
    news_list = Latest_news.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'news':news
    }
    return render(request, "index.html", context)

# the detail page view
def news_details(request, hacker_id, hackers_id):
    news_details = get_object_or_404(Latest_news, pk=hacker_id)
    # get the comments
    news_id = news_details.hacker_id
    url_endpoint = f'https://hacker-news.firebaseio.com/v0/item/{news_id}.json?print=pretty'
    try:
        response = requests.get(url=url_endpoint, timeout=3,)
        my_dict = json.loads(response.text)
        new_array = []
        for child in my_dict['kids']:
            try:
                new_response  = requests.get(url=f'https://hacker-news.firebaseio.com/v0/item/{int(child)}.json?print=pretty')
                my_new_dict = json.loads(new_response.text)
                new_array.append(my_new_dict)
            except:
                print('connection error')
        for data in new_array:
            by = data['by']
            comment_id = data['id']
            parent = data['parent']
            text = data['text']
            time = data['time']
            types = data['type']

            detail_comments = Comments(by=by, comment_id=comment_id, parent=parent, Text=text, time=time, type=types)
            detail_comments.save()
    except:
        print('connection error')
    comment = Comments.objects.filter(parent = news_details.hacker_id)
    context = {'news_details': news_details, 'comments': comment}
    return render(request, "details.html", context)

# the api view
class NewsViewset(viewsets.ModelViewSet):
    queryset = Latest_news.objects.all()
    serializer_class = NewsSerializer
    filter_fields = ('by', 'title', 'type', 'hacker_id')
    permission_classes = (AllowAny,)


# search view
class SearchResultView(ListView):
    model = Comments
    template_name = 'search_results.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Comments.objects.filter(
            by__icontains=query
        )
        return object_list