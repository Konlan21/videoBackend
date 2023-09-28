from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import Video



# class UserCreateSerializer(BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
#         fields = ['id', 'email', 'password']


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'