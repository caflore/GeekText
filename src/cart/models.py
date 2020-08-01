from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save

from functools import partial

from books.models import Book

shopping_cart_id = partial(get_random_string, 10)

class ShoppingCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "Cart: " + self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="create_shopping_cart_for_user")
def create_shopping_cart_for_user(sender, instance=None, created=False, **kwargs):
    if created:
        ShoppingCart.objects.create(user=instance)

class ShoppingCartItems(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.cart.user.username + ": " + self.item_id.title
