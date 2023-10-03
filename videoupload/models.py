from django.db import models
from django.contrib.auth.models import User



class Video(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')


class VideoChunk(models.Model):
    session_id = models.CharField(max_length=255)
    chunk_number = models.PositiveIntegerField()   
    total_chunks = models.PositiveIntegerField()   
    video_chunk = models.FileField(upload_to='video_chunks/')
