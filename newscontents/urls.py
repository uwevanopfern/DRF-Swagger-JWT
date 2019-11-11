from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import NewsContentViewSet

router = SimpleRouter()
router.register('news-content', NewsContentViewSet, base_name="news_content")
urlpatterns = router.urls
