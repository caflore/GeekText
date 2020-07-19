from django.contrib import admin

from cart.models import ShoppingCart, ShoppingCartItems

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItems)
