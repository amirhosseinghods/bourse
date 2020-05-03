from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic import DetailView
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product

class CartAddView(View):
    def post(self, request, pk, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id = pk)
        form = CartAddProductForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, product_count=cd['product_count'], update_count=cd['update'])
        
        return redirect('cart:cart_detail')

class CartRemoveView(View):
    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id = product_id)
        cart.remove(product)

        return redirect('cart:cart_detail')

class CartDetailView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)

        for item in cart:
            item['update_product_count_form'] = CartAddProductForm(initial={'product_count': item['product_count'], 'update': True})
        return render(request, 'pages/cart/detail.html', {'cart': cart})
