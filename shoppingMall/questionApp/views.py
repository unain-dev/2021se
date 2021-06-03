from django.shortcuts import render,redirect, get_object_or_404
from .models import question
from cartApp import context_processors
from shoppingApp.models import UserAccounts
from django.contrib.auth.models import User
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
     new_question.q_category=request.POST.get("q_category")
     new_question.title=request.POST['title']
     new_question.content=request.POST['content']
     new_question.q_user_id=uid
     new_question.save()
    return render(request,"question_list.html", {'count':count})

def question_list_view(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    uid=request.session.get('user_id')
    get_questions = question.objects.get(q_user_id=uid)
    

    return render(request,"question_list.html",{'get_questions':get_questions, 'count':count})