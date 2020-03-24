from django.urls import path, re_path, include
from . import views


app_name = 'tutorial'
urlpatterns = [
    re_path(r'^$', views.TutorialView.as_view(), name='posts'),
    re_path(r'^single/$', views.SingleTutorialView.as_view(), name='post'),
]
