from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

class HomeView(TemplateView):
    template_name = 'pages/index.html'
    page_name = _('خانه')
    is_rtl = False

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context

class ContactView(TemplateView):
    template_name = 'pages/contact.html'
    page_name = _('Contact Us')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        return context
