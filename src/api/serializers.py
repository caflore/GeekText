from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User, CreditCard
from books.models import Book, Author
from ratings.models import Rating
from cart.models import ShoppingCart, ShoppingCartItems


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    validate_password = make_password


class CreditCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields='__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields='__all__'

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields='__all__'

class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

class ShoppingCartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingCartItems
        fields = '__all__'