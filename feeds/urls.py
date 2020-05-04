from django.urls import path, re_path, include
from .views import AnalyzePostFeed
from .views import NewsPostFeed

urlpatterns = [
    re_path('rss/analysis/', AnalyzePostFeed()),
    re_path('rss/news/', NewsPostFeed()),
]
