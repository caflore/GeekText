from rest_framework import viewsets
from rest_framework.filters import SearchFilter
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
    filter_backends = [SearchFilter]
    search_fields = ['user__username']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book_ISBN', 'author', 'title', 'genre']

    @action(detail=False)
    def top_sellers(self, request):
        top_ten_books = Book.objects.all().order_by('-copiesSold')[:10]

        page = self.paginate_queryset(top_ten_books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(top_ten_books, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def top_x(self, request):
        x = int(request.GET["count"])
        top_x_books = Book.objects.all().order_by('-copiesSold')[:x]

        page = self.paginate_queryset(top_x_books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(top_x_books, many=True)
        return Response(serializer.data)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer

    @action(detail=False)
    def top_rated(self, request):
        pass

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = serializers.ShoppingCartSerializer

class ShoppingCartItemsViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItems.objects.all()
    serializer_class = serializers.ShoppingCartItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['cart__user__username']
