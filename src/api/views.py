from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, CreditCard
from . import serializers
from books.models import Book, Author
from ratings.models import Rating
from cart.models import ShoppingCart, ShoppingCartItems

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = serializers.CreditCardSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    @action(detail=False)
    def top_sellers(self, request):

        top_ten_books = Book.objects.all()

        page = self.paginate_queryset(top_ten_books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(top_ten_books, many=True)
        return Response(serializer.data)

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