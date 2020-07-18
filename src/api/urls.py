from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'creditcards', views.CreditCardViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'rating', views.RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]