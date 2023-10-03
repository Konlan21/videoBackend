from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import *



# class UserCreateSerializer(BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
#         fields = ['id', 'email', 'password']


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_file']


class VideoChunkSerializer(ModelSerializer):
    class Meta:
        model = VideoChunk
        fields = ['id', 'session_id', 'chunk_number', 'total_chunks', 'video_chunk']
