from django.contrib.syndication.views import Feed
from django.urls import reverse
from rss.models import Blog

class LatestBlogsFeed(Feed):
    title = "Cele Blogs"
    link = "/blogs/"
    description = "Share my thought."

    def items(self):
        return Blog.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog-detail', args=[item.pk])
