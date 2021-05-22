from django.urls import path
from noticeApp import views

app_name='notice'
urlpatterns = [
    path('notice/<int:noti_event_id>', views.show_notice, name='show_notice'),
]