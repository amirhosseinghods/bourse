from django.urls import path, re_path, include
from . import views


app_name = 'dashboard'
urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
]
