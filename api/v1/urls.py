from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views

schema_view = get_swagger_view(title='Smart Bourse API Documentation')

urlpatterns = [
    re_path(r'^api-documentation/', schema_view),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^v1/', include('api.v1.analysis.urls')),
    re_path(r'^v1/', include('api.v1.news.urls')),
]