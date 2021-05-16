from django.db import models

class Notice_Event(models.Model):
    noti_event_id = models.IntegerField()
    title = models.CharField(max_length=50)
    pubdate = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()
    images = models.ImageField(blank=True, upload_to="notice/", null=True)
    on_off = models.BooleanField()
    activation = models.CharField(choices=on_off.choices, max_length=10)
    dueDate = models.DateTimeField()
    