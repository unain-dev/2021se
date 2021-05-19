from django.contrib import admin
from .models import UserAccounts,address

class addressInline(admin.TabularInline):
    model = address


class AccountsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_email', 'user_phone']
    inlines = [addressInline, ]




# Register your models here.
admin.site.register(UserAccounts, AccountsAdmin)