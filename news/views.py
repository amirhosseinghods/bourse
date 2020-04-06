from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.utils.translation import ugettext_lazy as _

from .models import NewsCategory
from .models import NewsPost
from .models import NewsTag


class NewsListView(ListView):
    model = NewsPost
    context_object_name = 'posts'
    template_name = 'pages/news/posts.html'
    is_rtl = True
    page_name = _('اخبار')

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)

        return context


class SinglePostNewsDetail(DetailView):
    model = NewsPost
    template_name = 'pages/news/post.html'
    context_object_name = 'post'
    page_name = _('خبر')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(SinglePostNewsDetail, self).get_context_data(**kwargs)

        return context

class MorePostsView(TemplateView):
    template_name = 'pages/news/more-posts.html'
    page_name = _('خبر')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(MorePostsView, self).get_context_data(**kwargs)

        return context