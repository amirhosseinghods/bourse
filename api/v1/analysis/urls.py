from rest_framework import routers
from django.urls import re_path

from . import views as view

router = routers.SimpleRouter()

router.register(r'analysis/category', view.AnalyzeCategoryViewSet)
router.register(r'analysis', view.AnalyzePostViewSet)
# router.register(r'analysis', view.AnalyzePostViewSet)

urlpatterns = router.urls
