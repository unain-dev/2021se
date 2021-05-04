from django.shortcuts import render, redirect, get_object_or_404
from .models import UserAccounts,Notice,Event
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def join(request):
    return render(request, "join.html")

def login(request, id):
    useraccounts=get_object_or_404(UserAccounts, pk=id)
    return render(request, "login.html", {'useraccounts':useraccounts})

def userMain(request):
    useraccounts=UserAccounts.objects.all()
    return render(request, "userMain.html", {'useraccounts' : useraccounts})

def createUser(request):
    new_userAccounts=UserAccounts()
    if request.method =='POST' :
        if UserAccounts.objects.filter(user_id=request.POST['new_user_id']).exists() :
            #messages.warning(request, "권한이 없습니다.")
            errorMsg = "같은 아이디가 존재합니다. 다른 아이디로 가입해주세요"
            return render(request, "error.html", {'errorMsg' : errorMsg})
        if UserAccounts.objects.filter(user_email=request.POST['new_user_email']).exists() :
            errorMsg = "동일한 이메일로 가입한 또 다른 가입자가 존재합니다. 다른 이메일로 가입해주세요"
            return render(request, "error.html", {'errorMsg' : errorMsg})
        else : 
            new_userAccounts.user_id = request.POST['new_user_id']
            new_userAccounts.user_pw = request.POST['new_user_pw']
            new_userAccounts.user_name = request.POST['new_user_name']
            new_userAccounts.user_address = request.POST['new_user_address']
            new_userAccounts.user_email = request.POST['new_user_email']
            new_userAccounts.user_phone = request.POST['new_user_phone']
            new_userAccounts.save()
            return redirect('login', new_userAccounts.id)

"""
def createNotice(request):
    new_notice=Notice()
    if request.method =='POST' :
        new_notice.title = request.POST['new_notice_title']
        new_notice.cdate = request.POST['new_notice_cdate']
        new_notice.name = request.POST['new_notice_name']
        new_notice.contents = request.POST['new_notice_contents']
        new_notice.uniqueNumber = request.POST['new_notice_uniqueNumber']
        new_notice.save()
        return redirect('userMain', new_notice.uniqueNumber)

def createEvent(request):
    new_event=Event()
    if request.method =='POST' :
        new_event.title = request.POST['new_event_title']
        new_event.cdate = request.POST['new_event_cdate']
        new_event.name = request.POST['new_event_name']
        new_event.contents = request.POST['new_event_contents']
        new_event.activation = request.POST['new_event_activation']
        new_event.dueDate = request.POST['new_event_dueDate']
        new_event.uniqueNumber = request.POST['new_event_uniqueNumber']
        new_event.save()
        return redirect('userMain', new_notice.uniqueNumber) #redirect userMain이 맞나?
        """