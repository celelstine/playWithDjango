from rest_framework import viewsets

from rss.serializers import BlogSerializer

from rss.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
