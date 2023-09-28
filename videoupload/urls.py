from django.urls import path
from . import views



urlpatterns = [
    path('', views.ListCreateVideoView.as_view(), name='list-create-video')
]