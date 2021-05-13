from django.db import models

# Create your models here.
class Notice(models.Model):
    noticeId = models.IntegerField()
    title = models.CharField(max_length=50)
    cdate = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    contents = models.TextField()

class Event(models.Model):
    eventId = models.IntegerField()
    title = models.CharField(max_length=50)
    cdate = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    contents = models.TextField()
    on_off = models.BooleanField()
    activation = models.CharField(choices=on_off.choices, max_length=10)
    dueDate = models.DateTimeField()
    