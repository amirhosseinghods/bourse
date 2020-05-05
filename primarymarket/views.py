from django.shortcuts import render
from django.views.generic import ListView
from .models import PrimaryMarket
from django.utils.translation import ugettext_lazy as _

class PrimaryMarketListView(ListView):
    model = PrimaryMarket
    template_name = "pages/primarymarkets.html"
    context_object_name = 'primarymarkets'
    page_name = _('عرضه اولیه')



