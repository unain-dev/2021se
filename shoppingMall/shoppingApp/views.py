from django.shortcuts import render, redirect, get_object_or_404
from .models import UserAccounts,Notice,Event
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request) :
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect("userMain")
    else :
        form = AuthenticationForm()
        return render(request, "userMain.html", {'form': form})

def logout_view(request) :
    logout(request)
    return redirect("userMain")

def register_view(request) :
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("userMain") 

    else:
        form = UserCreationForm()
    return render(request, 'join.html', {'form':form})