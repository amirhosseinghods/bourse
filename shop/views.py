from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.utils.translation import ugettext_lazy as _

from shop.models import Product
from cart.forms import CartAddProductForm

class ProductsView(TemplateView):
    template_name = "pages/tutorial/posts.html"
    page_name = _('آموزشگاه')

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context['cart_add_product_form'] = CartAddProductForm()
        return context

class ProductView(DetailView):
    template_name = 'pages/tutorial/post.html'
    page_name = _('آموزش')
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)

        return context
