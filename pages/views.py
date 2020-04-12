from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ContactForm
from .forms import OpenAccountForm
from django.core.mail import send_mail
from .models import Contact
from .models import OpenAccount

from django.utils.translation import ugettext_lazy as _
from analysis.models import AnalyzePost
from news.models import NewsPost
from news.models import NewsCategory

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
        context['news_posts'] = NewsPost.objects.all()
        context['news_categories'] = NewsCategory.objects.all()
        return context

class ContactView(CreateView):
    template_name = 'pages/contact.html'
    model = Contact
    form_class = ContactForm
    page_name = _('تماس با ما')
    success_url = reverse_lazy('pages:success')
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
        context = super(ContactView, self).get_context_data(**kwargs)

        return context


class OpenAccountView(CreateView):
    template_name = 'pages/open-account.html'
    model = OpenAccount
    form_class = OpenAccountForm
    page_name = _('افتتاح حساب')
    success_url = reverse_lazy('pages:success')
    is_rtl = False

    def form_valid(self, form):
        # import pdb; pdb.set_trace();
        self.object = form.save()
        send_mail(
            'Smart Bourse Contact: {}'.format(form.data['full_name']),
            '{}'.format(form.data['phone']),
            'animatedidea@gmail.com',
            ['sa.goldeneagle@gmail.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(OpenAccountView, self).get_context_data(**kwargs)

        return context



class SuccessView(TemplateView):
    template_name = "pages/success.html"