from typing import Text
from django.db import models

# Create your models here.
class Latest_news(models.Model):
    by = models.CharField(max_length=14)
    descendants = models.IntegerField()
    hacker_id = models.IntegerField()
    score = models.IntegerField()
    time = models.IntegerField()
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.by

class Comments(models.Model):
    by = models.CharField(max_length=14)
    comment_id =  models.IntegerField()
    parent = models.IntegerField()
    Text = models.TextField()
    time = models.IntegerField()
    type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.by