from django.contrib import admin
from .models import UserAccounts

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_email', 'user_phone']

# Register your models here.
admin.site.register(UserAccounts, AccountsAdmin)