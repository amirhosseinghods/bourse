from django.shortcuts import render
from django.views.generic import ListView
from .models import PrimaryMarket


class PrimaryMarketListView(ListView):
    model = PrimaryMarket
    template_name = "pages/primarymarkets.html"
    context_object_name = 'primarymarkets'



