from django.contrib import admin


from .models import question
# Register your models here.
class questionAdmin(admin.ModelAdmin):
    list_display = ['q_user_id', 'title', 'content', 'is_checked'] 
    
   
   


admin.site.register(question, questionAdmin)