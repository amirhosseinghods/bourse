from django.conf import settings
from tutorial.models import TutorialPost

class Cart():
    def __init__(self, request):
        """Initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart