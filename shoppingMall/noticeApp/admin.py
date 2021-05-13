from django.contrib import admin
from .models import Notice, Event

class noticeAdmin(admin.ModelAdmin):
    list_display = ['noticeId', 'title', 'cdate']
    search_fields=['noticeId', 'title', 'cdate']

class eventAdmin(admin.ModelAdmin):
    list_display = ['eventId', 'title', 'cdate', 'dueDate', 'on_off']
    search_fields=['eventId', 'title', 'cdate']

# Register your models here.
admin.site.register(Notice, noticeAdmin)
admin.site.register(Event, eventAdmin)