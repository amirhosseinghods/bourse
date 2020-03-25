from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from analysis.models import AnalyzePost

class HomeView(TemplateView):
    template_name = 'pages/index.html'
    page_name = _('خانه')
    is_rtl = False

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_posts'] = AnalyzePost.objects.all()[:3]
        return context

class ContactView(TemplateView):
    template_name = 'pages/contact.html'
    page_name = _('Contact Us')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        return context
