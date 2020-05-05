from django.urls import re_path
from . import views

app_name = 'market'
urlpatterns = [
    re_path(r'^$', views.PrimaryMarketListView.as_view(), name = "primary-market"),
]