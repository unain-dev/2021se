from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserAccounts,address
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm#, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreateForm
import re
from productApp.models import product
from noticeApp.models import Notice_Event as notice
from django.core.paginator import Paginator
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils import timezone
from cartApp import context_processors
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

from cartApp.models import Cart, CartItem



# Create your views here.
@csrf_exempt
def login_view(request) :
    products_recent = product.objects.filter(published=True).order_by('-pubDate')[:3]
    products_popular = product.objects.filter(published=True).order_by('-salesamount')[:3]
    #noti_info=notice.objects.filter(on_off=True)
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    noti_info_all=notice.objects.filter(on_off=True)
    for noti in noti_info_all:
        now=DateFormat(datetime.now()).format('Ymd')
        dueDate=DateFormat(noti.dueDate).format('Ymd')
        if int(dueDate)-int(now)>0:
            pass
        else:
            noti.on_off=False
            noti.save()

    noti_info_all=notice.objects.filter(on_off=True)
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
                request.session['user_id']=form.cleaned_data.get("username")
           
                if request.user.is_superuser :
                    return redirect('/admin')
        else:
            errorMsg = "아이디/비밀번호가 틀렸습니다."
            return render(request, "error.html", {'errorMsg' : errorMsg})

        cart_count=context_processors.counter(request)
        cart_count=int(cart_count)
        count={'cart_count':cart_count}
        return render(request, "userMain.html", { 'products_recent':products_recent, 'products_popular':products_popular, 'noti_info':noti_info, 'count':count})
    
    else :
        form = AuthenticationForm()
        return render(request, "userMain.html", {'form': form, 'products_recent':products_recent, 'products_popular':products_popular, 'noti_info':noti_info, 'count':count})
        #return render(request, "userMain.html", {'form': form, 'products_recent':products_recent, 'products_popular':products_popular, 'noti_info':noti_info})

def logout_view(request) :
    logout(request)
    return redirect("userMain")

def register_view(request):
    new_userAccounts=UserAccounts()
    if request.method == 'POST' :

        if request.POST['new_user_id']=="" or request.POST['new_user_pw'] =="" or request.POST['new_user_name']=="" or request.POST['new_user_email']=="" or request.POST['new_user_phone']=="":
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
            #try :
            new_userAccounts.user_id = request.POST['new_user_id']
            new_userAccounts.user_pw = request.POST['new_user_pw']
            new_userAccounts.user_name = request.POST['new_user_name']
            new_userAccounts.user_email = request.POST['new_user_email']
            new_userAccounts.user_phone = request.POST['new_user_phone']
            new_userAccounts.save()

            username=request.POST['new_user_id']
            email = request.POST['new_user_email']
            password = request.POST['new_user_pw']
            new_user = User.objects.create_user(username, email, password)

            user = authenticate(request=request, username=username, password=password)
            login(request, user)
            request.session['user_id']=request.POST.get('new_user_id', '')

            return redirect("userMain")
            #except:
            #    errorMsg = "오류가 발생했습니다. 다시 가입해주세요"
            #    return render(request, "error.html", {'errorMsg' : errorMsg})
    else :
        #form = UserCreateForm()
        return render(request, 'join.html')



def create_view(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    uid=request.session.get('user_id')
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    shippings = address.objects.filter(accounts__in=get_user)
    if shippings is None:
        return render(request, 'create.html')

    return render(request, 'create.html', {'shippings':  shippings, 'count':count})
    
def create_default_save(request):
    
    if request.method == 'POST' :
        uid=request.session.get('user_id')
        get_all=UserAccounts.objects.all()
        get_user=get_all.filter(user_id=uid)
        shippings = address.objects.filter(accounts__in=get_user)

        old_address=shippings.get(is_default='True')
     
        if old_address is not None:
            old_address.is_default='False'
            old_address.save()

        n_pk = request.POST.get('is_default') 
        n_address=shippings.get(pk=n_pk)
        n_address.is_default='True'
        n_address.save()

        product_id=request.session.get('product_id')
        return redirect('products:address_after_detail')
        #return render(request,'create.html',{'shippings':  shippings})

def create_default(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}
    
    uid=request.session.get('user_id')
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    shippings = address.objects.filter(accounts__in=get_user)

    return render(request,'create_default.html',{'shippings':  shippings, 'count':count} )
    
 

def postaddress(request):
    uid=request.session.get('user_id')
  
    new_address=address()
    new_address.accounts=UserAccounts.objects.get(user_id=uid)
    new_address.title= request.POST['title']
    new_address.post_num=request.POST['post_num']
    new_address.road_address=request.POST['road_address']
    new_address.detail_address=request.POST['detail_address']
    new_address.post_name=request.POST['post_name']
    new_address.post_phonenum=request.POST['post_phonenum']
    new_address.save()
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    shippings = address.objects.filter(accounts__in=get_user)
    ad_num=shippings.count()
    if(ad_num==1):
        new_address.is_default='True'
    new_address.save()
    
    return render(request,'create.html',{'shippings':  shippings,})
    

def delete(request,pk):
    if request.method == 'POST':
     new_address = address.objects.get(pk=pk)
     new_address.delete()
    return redirect('create')


def editsave(request):
    
    if request.method == 'POST' :
        pk=request.session.get('edit_ad')

        uid=request.session.get('user_id')
        get_all=UserAccounts.objects.all()
        get_user=get_all.filter(user_id=uid)
        u_address = address.objects.get(accounts__in=get_user, pk=pk)

        u_title= request.POST['title']
        u_post_num=request.POST['post_num']
        u_road_address=request.POST['road_address']
        u_detail_address=request.POST['detail_address']
        u_post_name=request.POST['post_name']
        u_post_phonenum=request.POST['post_phonenum']
        u_address.title= u_title
        u_address.post_num=u_post_num
        u_address.road_address= u_road_address
        u_address.detail_address= u_detail_address
        u_address.post_name= u_post_name
        u_address.post_phonenum= u_post_phonenum

        u_address.save()
    return redirect("create")



def newpost(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    return render(request,'newpost.html', {'count':count})

def edit(request,pk):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    uid=request.session.get('user_id')
    get_all=UserAccounts.objects.all()
    get_user=get_all.filter(user_id=uid)
    u_address = address.objects.get(accounts__in=get_user, pk=pk)

    request.session['edit_ad']=pk

    return render(request,'edit.html' ,{'u_address':u_address, 'count':count})

def view_myPage(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    return render(request, 'myPage.html', {'count':count})