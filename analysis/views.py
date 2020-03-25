from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

class AnalyzeView(TemplateView):
    template_name = 'pages/analyze/posts.html'
    page_name = _('تحلیل بورس')

    def get_context_data(self, **kwargs):
        context = super(AnalyzeView, self).get_context_data(**kwargs)

        return context

class SingleAnalyzeView(TemplateView):
    template_name = 'pages/analyze/post.html'
    page_name = _('پست تحلیل بورس')

    def get_context_data(self, **kwargs):
        context = super(SingleAnalyzeView, self).get_context_data(**kwargs)

        return context
