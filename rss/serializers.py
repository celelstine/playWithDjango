from rest_framework import serializers

from rss.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'pub_date')
