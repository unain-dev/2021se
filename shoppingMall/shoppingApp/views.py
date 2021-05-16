from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserAccounts
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm#, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreateForm
import re
from productApp.models import product
from noticeApp.models import Notice_Event as notice
from django.core.paginator import Paginator

# Create your views here.
def login_view(request) :
    products_recent = product.objects.filter(published=True).order_by('pubDate')[:3]
    products_popular = product.objects.filter(published=True).order_by('-salesamount')[:3]
    #noti_info=notice.objects.filter(on_off=True)

    noti_info_all=notice.objects.all()
    paginator=Paginator(noti_info_all, 1)
    page=request.GET.get('page')
    noti_info=paginator.get_page(page)

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                if request.user.is_superuser :
                    return redirect('/admin')

        return redirect("userMain", {'products_recent':products_recent, 'products_popular':products_popular, 'noti_info':noti_info})
    else :
        form = AuthenticationForm()
        return render(request, "userMain.html", {'form': form, 'products_recent':products_recent, 'products_popular':products_popular, 'noti_info':noti_info})

def logout_view(request) :
    logout(request)
    return redirect("userMain")

def register_view(request):
    new_userAccounts=UserAccounts()
    if request.method == 'POST' :

        if request.POST['new_user_id']=="" or request.POST['new_user_pw'] =="" or request.POST['new_user_name']=="" or request.POST['new_user_address']=="" or request.POST['new_user_email']=="" or request.POST['new_user_phone']=="":
            errorMsg = "빈 항목이 있습니다. 다시 회원가입해주세요"
            return render(request, "error.html", {'errorMsg' : errorMsg})

        #아이디 중복체크
        if UserAccounts.objects.filter(user_id=request.POST['new_user_id']).exists() :
            errorMsg = "같은 아이디가 존재합니다. 다른 아이디로 가입해주세요"
            return render(request, "error.html", {'errorMsg' : errorMsg})

        #이메일 중복체크
        if UserAccounts.objects.filter(user_email=request.POST['new_user_email']).exists():
            errorMsg = "동일한 이메일로 가입한 또 다른 가입자가 존재합니다. 다른 이메일로 가입해주세요"
            return render(request, "error.html", {'errorMsg' : errorMsg})

        #비밀번호 조건 검사
        if len(request.POST['new_user_pw'])<8 or not re.findall('[`~!@#$%^&*(),<.>/?]+', request.POST['new_user_pw']):
            errorMsg = "비밀번호 생성조건에 맞지 않습니다."
            return render(request, "error.html", {'errorMsg' : errorMsg})

        else: 
            try :
                new_userAccounts.user_id = request.POST['new_user_id']
                new_userAccounts.user_pw = request.POST['new_user_pw']
                new_userAccounts.user_name = request.POST['new_user_name']
                new_userAccounts.user_address = request.POST['new_user_address']
                new_userAccounts.user_email = request.POST['new_user_email']
                new_userAccounts.user_phone = request.POST['new_user_phone']
                new_userAccounts.save()

                username=request.POST['new_user_id']
                email = request.POST['new_user_email']
                password = request.POST['new_user_pw']
                new_user = User.objects.create_user(username, email, password)

                return redirect("userMain")
            except:
                errorMsg = "오류가 발생했습니다. 다시 가입해주세요"
                return render(request, "error.html", {'errorMsg' : errorMsg})
    else :
        #form = UserCreateForm()
        return render(request, 'join.html')



def socks(request) :
    return render(request, 'socks.html')

def rings(request) :
    return render(request, 'rings.html')

def hats(request) :
    return render(request, 'hats.html')

def bags(request) :
    return render(request, 'bags.html')

def necklace(request) :
    return render(request, 'necklace.html')

def glasses(request) :
    return render(request, 'glasses.html')

#productlist view

"""
def product_listview(request):
   products=get_object_or_404(product,id=product_id)
   return render(request,'glasses.html',{'products':products})
"""