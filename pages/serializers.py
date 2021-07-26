from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Latest_news
from rest_framework.authtoken.models import Token



class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Latest_news
        fields = ('by','descendants','hacker_id', 'score', 'time','title','type','url')
        URL_FIELD_NAME = 'newsapi'