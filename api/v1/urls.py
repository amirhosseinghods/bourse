from rest_framework import routers
from django.urls import re_path
from django.urls import path
from django.urls import include
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views

from . import views as view


router = routers.SimpleRouter()

router.register('posts', view.PostViewSet)
router.register('tags', view.TagViewSet)
router.register('categories', view.CategoryViewSet)

urlpatterns = router.urls
urlpatterns += [
    re_path(r'^jwt/token/$', jwt_views.TokenObtainPairView.as_view(), name='jwt_token'),
    re_path(r'^jwt/token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='jwt_token_refresh'),
    re_path(r'^device/token/$', view.GenerateAuthToken.as_view(), name='token'),
]
