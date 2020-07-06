from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'address', 'zip_code', 'city', 'country',)
    validate_password = make_password