from django.urls import re_path
from . import views

app_name = 'cart'
urlpatterns = [
    re_path(r'^$', views.CartDetailView.as_view(), name = 'cart_detail'),
    re_path(r'^add/(?P<pk>\d+)/$', views.CartAddView.as_view(), name = 'cart_add'),
    re_path(r'^remove/(?P<pk>\d+)/$', views.CartRemoveView.as_view(), name = 'cart_remove'),
]