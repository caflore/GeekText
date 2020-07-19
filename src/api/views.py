from rest_framework import viewsets, filters

from users.models import User, CreditCard
from . import serializers
from books.models import Book, Author
from ratings.models import Rating
from cart.models import ShoppingCart, ShoppingCartItems


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = serializers.CreditCardSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer

class RatingViewSet(viewsets.ModelViewSet):
        queryset = Rating.objects.all()
        serializer_class = serializers.RatingSerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = serializers.ShoppingCartSerializer

class ShoppingCartItemsViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItems.objects.all()
    serializer_class = serializers.ShoppingCartItemSerializer