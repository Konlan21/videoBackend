from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from . models import Video
from . serializers import VideoSerializer


class ListCreateVideoView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer