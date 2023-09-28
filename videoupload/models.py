from django.db import models
from django.contrib.auth.models import User



class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
