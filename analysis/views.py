from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.utils.translation import ugettext_lazy as _
from .models import AnalyzePost
from .models import AnalyzeCategory
from .models import AnalyzeTag

class AnalyzeView(TemplateView):
    template_name = 'pages/analyze/posts.html'
    page_name = _('تحلیل بورس')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(AnalyzeView, self).get_context_data(**kwargs)
        context['posts'] = AnalyzePost.objects.all()
        context['tags'] = AnalyzeTag.objects.all()
        context['categories'] = AnalyzeCategory.objects.all()
        return context

class SingleAnalyzeView(DetailView):
    model = AnalyzePost
    template_name = 'pages/analyze/post.html'
    page_name = _('پست تحلیل بورس')
    slug_field = 'slug'
    context_object_name  = 'post'
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(SingleAnalyzeView, self).get_context_data(**kwargs)

        return context
