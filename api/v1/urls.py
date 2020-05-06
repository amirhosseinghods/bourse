from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Smart Bourse API Documentation')

urlpatterns = [
    re_path(r'^api-documentation/', schema_view),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^api/v1/', include('api.v1.analysis.urls')),
]