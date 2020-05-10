from django.conf import settings
from shop.models import Product
from decimal import Decimal

class Cart(object):
    def __init__(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            self.session[settings.CART_SESSION_ID] = {}
            cart = self.session[settings.CART_SESSION_ID]
        
        self.cart = cart

    def add(self, product, quantity = 1, update_count = False):
        product_id = str(product.id)
        if product.id not in self.cart:
            self.cart[product_id] = {
                'quantity':0, 
                'price': str(product.price)
                }

        if update_count:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
    
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['product_count']
            yield item

    def __len__(self):
        return sum(item['product_count'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Int(item['price']) * item['product_count'] for item in self.cart.values())
    
    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True