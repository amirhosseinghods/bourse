from django.urls import path, re_path, include
from . import views

app_name = 'news'
urlpatterns = [
    re_path(r'^$', views.NewsListView.as_view(), name='posts'),
    re_path(r'^(?P<slug>[\w\-]+)/$', views.SinglePostNewsDetail.as_view(), name='post'),
    re_path(r'^more-posts/$', views.MorePostsView.as_view(), name='more-posts'),
]
