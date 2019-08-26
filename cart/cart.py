from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(Object):

    def __init__(self):
        """Initialize cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self,product,quantity=1,update_quantity=False):
        """Add a product to the cart"""