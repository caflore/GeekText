from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse


from users.models import User, CreditCard
from django.db.models import Sum, Count
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
    
    @action(detail=False)
    def top_rated(self, request):
        rating = int(request.GET["rating"])
        book_rating = Rating.objects.values('book').annotate(average = Sum('rating')/Count('rating')).filter(average__gte = rating)
        final_result = Book.objects.all().filter(id__in=book_rating.values_list('book'))
        page = self.paginate_queryset(final_result)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(final_result, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def avg_book_rating(self, request):
        isbn = request.GET["ISBN"]
        book_rating = list(Rating.objects.values('book__title').annotate(average=Sum('rating') / Count('rating')).filter(book__book_ISBN = isbn))
        return JsonResponse(book_rating, safe=False)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer

    @action(detail=False)
    def top_ratings(self, request):
        top_ratings = Rating.objects.all().order_by('-rating')

        page = self.paginate_queryset(top_ratings)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(top_ratings, many=True)
        return Response(serializer.data)

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = serializers.ShoppingCartSerializer

class ShoppingCartItemsViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItems.objects.all()
    serializer_class = serializers.ShoppingCartItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['cart__user__username']
