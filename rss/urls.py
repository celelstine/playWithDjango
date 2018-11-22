from django.urls import path

from rest_framework.routers import DefaultRouter

from rss.feeds import LatestBlogsFeed
from rss.views import BlogViewSet

router = DefaultRouter()
router.register('blogs', BlogViewSet, base_name='blog')

urlpatterns = router.urls

print(urlpatterns)
urlpatterns += [
    path('blog/', LatestBlogsFeed()),
]
