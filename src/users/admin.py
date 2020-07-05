from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, CreditCard

# class UsersAdmin(UserAdmin):
#     list_display = ('username', 'date_joined', 'last_login', 'is_superuser')
#     search_fields = ('username', 'first_name', 'last_name')
#     readonly_fields = ('date_joined', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

admin.site.register(User)
admin.site.register(CreditCard)