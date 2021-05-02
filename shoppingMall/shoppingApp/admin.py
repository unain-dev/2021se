from django.contrib import admin
from .models import UserAccounts, Notice, Event

# Register your models here.
admin.site.register(UserAccounts)
admin.site.register(Notice)
admin.site.register(Event)
