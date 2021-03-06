from django.db import models

class Notice_Event(models.Model):
    noti_event_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    pubdate = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()
    images = models.ImageField(blank=True, upload_to="notice/", null=True)
    on_off = models.BooleanField()
    dueDate = models.DateTimeField()
    