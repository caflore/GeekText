from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User, CreditCard

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'first_name', 'last_name', 'address', 'zip_code', 'city', 'country',)
    validate_password = make_password

class CreditCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('url', 'user', 'creditcard_number',)