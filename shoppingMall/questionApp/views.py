from django.shortcuts import render,redirect, get_object_or_404
from questionApp.models import question
# Create your views here.
def postquestion_view(request):

    return render(request,"postquestion.html")

def postquestion_save(request):
    if request.method == 'POST' :
     new_question=question()
     new_question.CATEGORY_CHOICES=request.POST.get("q_category")
     new_question.title=request.POST['title']
     new_question.content=request.POST['content']
     new_question.save()
    return render(request,"question_list.html")

def question_list_view(request):
    get_questions=question.objects.all()

    return render(request,"question_list.html",{'get_questions':get_questions})