from django.urls import path
from questionApp import views
from django.conf import settings

app_name='question'

urlpatterns = [
    path('postquestion_view/',views.postquestion_view, name='postquestion_view'),
    path('postquestion_view/postquestion_save',views.postquestion_save, name='postquestion_save'),
    path('question_list/',views.question_list_view, name='question_list')
  
   
]
