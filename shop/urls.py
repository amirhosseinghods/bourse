from django.urls import path, re_path, include
from . import views

app_name = 'shop'
urlpatterns = [
    re_path(r'^$', views.ProductsView.as_view(), name='posts'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.ProductView.as_view(), name='post'),
]
