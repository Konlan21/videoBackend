from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from . models import Video
from . serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated

class ListCreateVideoView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter videos by the currently authenticated user
        return Video.objects.all()
    
    def perform_create(self, serializer):
        # Automatically set the user field to the currently authenticated user
        serializer.save()