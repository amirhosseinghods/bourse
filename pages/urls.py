from django.urls import path, re_path, include
from . import views


app_name = 'pages'
urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
    re_path(r'^contact/$', views.ContactView.as_view(), name='contact'),
]
