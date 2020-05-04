from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import NewsPost
from django.urls import reverse

class NewsPostFeed(Feed):
    title = "News Bourse Post"
    link = ""
    description = "News posts of smartbourse."

    def items(self):
        return NewsPost.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_link(self, item):
        return reverse('news:post', args=[item.slug])