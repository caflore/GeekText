from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, first_name, last_name, address, zip_code, city, country, password = None):
        if not username:
            raise ValueError("Users must have a username.")
        if not email:
            email = None

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            address = address,
            zip_code = zip_code,
            city = city,
            country = country,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, first_name, last_name, address, zip_code, city, country, password):
        user = self.create_user(
            username = username,
            password = password,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            address = address,
            zip_code = zip_code,
            city = city,
            country = country,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    
    username    = models.CharField(max_length = 30, unique = True)
    email       = models.EmailField(verbose_name = 'email', max_length = 60, unique = True, blank = True, null=True)
    first_name  = models.CharField(max_length = 30, blank = True, null=True)
    last_name   = models.CharField(max_length = 30, blank = True, null=True)
    address     = models.CharField("Address line 1", max_length = 1024, blank = True, null=True)
    zip_code    = models.CharField("Zip/Postal Code", max_length = 5, blank = True, null=True)
    city        = models.CharField("City", max_length = 1024, blank = True, null=True)
    country     = models.CharField("Country", max_length = 100, blank = True, null=True)
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login  = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    is_admin    = models.BooleanField(default = False)
    is_active   = models.BooleanField(default = True)
    is_staff    = models.BooleanField(default = False)
    is_superuser= models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'address', 'zip_code', 'city', 'country']

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

    def __str__(self):
        return self.user + ', ' + self.creditcard_number