from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

class TutorialView(TemplateView):
    template_name = 'pages/tutorial/posts.html'
    page_name = _('آموزشگاه')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(TutorialView, self).get_context_data(**kwargs)

        return context

class SingleTutorialView(TemplateView):
    template_name = 'pages/tutorial/post.html'
    page_name = _('آموزش')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(SingleTutorialView, self).get_context_data(**kwargs)

        return context
