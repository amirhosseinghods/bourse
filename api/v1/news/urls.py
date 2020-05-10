from rest_framework import routers
from django.urls import re_path

from . import views as view

router = routers.SimpleRouter()

router.register(r'news/category', view.NewsCategoryViewSet)
router.register(r'news', view.NewsPostViewSet)
# router.register(r'analysis', view.AnalyzePostViewSet)

urlpatterns = router.urls
