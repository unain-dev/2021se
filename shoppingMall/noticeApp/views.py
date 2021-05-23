from noticeApp.models import Notice_Event
from django.shortcuts import render
from cartApp import context_processors

# Create your views here.
def show_notice(request, noti_event_id):
    id=noti_event_id
    noti_info=Notice_Event.objects.get(noti_event_id=id)
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}
    return render(request, 'notice.html', {'noti_info':noti_info, 'count':count})