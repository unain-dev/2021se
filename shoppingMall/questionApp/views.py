from django.shortcuts import render,redirect, get_object_or_404
from questionApp.models import question
from cartApp import context_processors

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
     new_question=question()
     new_question.CATEGORY_CHOICES=request.POST.get("q_category")
     new_question.title=request.POST['title']
     new_question.content=request.POST['content']
     new_question.save()
    return render(request,"question_list.html", {'count':count})

def question_list_view(request):
    cart_count=context_processors.counter(request)
    cart_count=int(cart_count)
    count={'cart_count':cart_count}

    get_questions=question.objects.all()

    return render(request,"question_list.html",{'get_questions':get_questions, 'count':count})