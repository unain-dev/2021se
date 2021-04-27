from django.shortcuts import render, redirect, get_object_or_404
from .models import UserAccounts

# Create your views here.
def signUp(request):
    return render(request, "signUp.html")

def hello(request, id):
    useraccounts=get_object_or_404(UserAccounts, pk=id)
    return render(request, "hello.html", {'useraccounts':useraccounts})

def test(request):
    useraccounts=UserAccounts.objects.all()
    return render(request, "test.html", {'useraccounts' : useraccounts})

def createUser(request):
    new_userAccounts=UserAccounts()
    new_userAccounts.user_id = request.POST['new_user_id']
    new_userAccounts.user_pw = request.POST['new_user_pw']
    new_userAccounts.user_address = request.POST['new_user_address']
    new_userAccounts.user_email = request.POST['new_user_email']
    new_userAccounts.user_phone = request.POST['new_user_phone']
    new_userAccounts.save()
    return redirect('hello', new_userAccounts.id)