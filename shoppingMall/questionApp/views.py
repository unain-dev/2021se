from django.shortcuts import render,redirect, get_object_or_404
from .models import question
from cartApp import context_processors
from shoppingApp.models import UserAccounts
from django.contrib.auth.models import User
from django.core.paginator  import Paginator
# Create your views here.
def postquestion_view(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}
    return render(request,"postquestion.html", {'count':count})

def postquestion_save(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}


    if request.method == 'POST' :
     uid=request.session.get('user_id')
     
     new_question=question()
     new_question.product_name=request.POST.get("product_name")
     new_question.q_category=request.POST.get("q_category")
     new_question.title=request.POST['title']
     new_question.content=request.POST['content']
     new_question.q_user_id=uid
     new_question.save()
    uid=request.session.get('user_id')
    
    my_questions=question.objects
    get_questions = question.objects.all().filter(q_user_id=uid)
    
    paginator=Paginator(get_questions,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,"question_list.html", {'posts':posts,'my_questions':my_questions,'get_questions':get_questions,'count':count})

def question_list_view(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    uid=request.session.get('user_id')
    my_questions=question.objects
    get_questions = question.objects.all().filter(q_user_id=uid)
    
    paginator=Paginator(get_questions,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
   
    return render(request,"question_list.html",{'posts':posts,'my_questions':my_questions, 'count':count})

def question_detail_view(request,pk):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}


    
    d_question_get=question.objects.filter(pk=pk)
    return render(request,"question_detail.html",{'count':count,'d_question_get': d_question_get})