from django.contrib import admin
from .models import Notice_Event

class notice_event_Admin(admin.ModelAdmin):
    list_display = ['noti_event_id', 'title', 'pubdate', 'dueDate', 'on_off']
    search_fields=['noti_event_id', 'title', 'pubdate']

# Register your models here.
admin.site.register(Notice_Event, notice_event_Admin)
