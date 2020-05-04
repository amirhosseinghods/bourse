from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import AnalyzePost
from django.urls import reverse

class AnalyzePostFeed(Feed):
    title = "Analyse Bourse Post"
    link = ""
    description = "New posts of smartbourse Analysis."

    def items(self):
        return AnalyzePost.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_link(self, item):
        return reverse('analyze:post', args=[item.slug])