from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include
from django.views.generic import RedirectView



news_api_router = routers.SimpleRouter()
news_api_router.register("", views.NewsViewset, basename='newsapi')



urlpatterns = [
    path('',views.index, name='index'),
    path('news/<int:hacker_id>/<int:hackers_id>/',views.news_details, name='news_detail'),
    path('search/', views.SearchResultView.as_view(),name='search_results'),
    path("", RedirectView.as_view(url="/news/api/")),
    path("news/api/", include(news_api_router.urls)),
]


# http://localhost:8000/news/api/

# http://localhost:8000/news/api/1