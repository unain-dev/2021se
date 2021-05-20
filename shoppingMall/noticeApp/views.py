from noticeApp.models import Notice_Event
from django.shortcuts import render

# Create your views here.
def show_notice(request, noti_event_id):
    id=noti_event_id
    noti_info=Notice_Event.objects.get(noti_event_id=id)
    return render(request, 'notice.html', {'noti_info':noti_info})