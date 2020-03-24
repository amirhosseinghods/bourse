from django.urls import path, re_path, include
from . import views

app_name = 'analyze'
urlpatterns = [
    re_path(r'^$', views.AnalyzeView.as_view(), name='posts'),
    re_path(r'^single/$', views.SingleAnalyzeView.as_view(), name='post'),
]
