from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, username, password = None):
        if not username:
            raise ValueError("Users must have a username.")

        user = self.model(
            username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    
    username    = models.CharField(max_length = 30, unique = True)
    email       = models.EmailField(verbose_name = 'email', max_length = 60, unique = True, blank = True)
    first_name  = models.CharField(max_length = 30)
    last_name   = models.CharField(max_length = 30)
    address     = models.CharField("Address line 1", max_length = 1024)
    zip_code    = models.CharField("Zip/Postal Code", max_length = 5)
    city        = models.CharField("City", max_length = 1024)
    country     = models.CharField("Country", max_length = 100)
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login  = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    is_admin    = models.BooleanField(default = False)
    is_active   = models.BooleanField(default = True)
    is_staff    = models.BooleanField(default = False)
    is_superuser= models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class CreditCard(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    creditcard_number = models.CharField(max_length = 16)