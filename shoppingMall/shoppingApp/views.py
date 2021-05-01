from django.shortcuts import render, redirect, get_object_or_404
from .models import UserAccounts
from django.contrib import messages

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
            return render(request, "error.html")
        else : 
            new_userAccounts.user_id = request.POST['new_user_id']
            new_userAccounts.user_pw = request.POST['new_user_pw']
            new_userAccounts.user_name = request.POST['new_user_name']
            new_userAccounts.user_address = request.POST['new_user_address']
            new_userAccounts.user_email = request.POST['new_user_email']
            new_userAccounts.user_phone = request.POST['new_user_phone']
            new_userAccounts.save()
            return redirect('login', new_userAccounts.id)

