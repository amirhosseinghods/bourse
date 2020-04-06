from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Contact

from django.utils.translation import ugettext_lazy as _
from analysis.models import AnalyzePost

class HomeView(CreateView):
    template_name = 'pages/index.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('pages:success')
    page_name = _('خانه')
    is_rtl = False

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            'Smart Bourse Contact: {}'.format(form.data['subject']),
            '{}'.format(form.data['message']),
            'animatedidea@gmail.com',
            ['sa.goldeneagle@gmail.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_posts'] = AnalyzePost.objects.all()[:3]
        return context

class ContactView(CreateView):
    template_name = 'pages/contact.html'
    page_name = _('Contact Us')
    is_rtl = True

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        return context

class SuccessView(TemplateView):
    template_name = "pages/success.html"