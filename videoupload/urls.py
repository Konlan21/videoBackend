from django.urls import path
from . import views

urlpatterns = [
    # API endpoint to combine and save video chunks
    path('combine_and_save_video/', views.combine_and_save_video, name='combine-and-save-video'),

    # List and create videos
    path('videos/', views.ListCreateVideoView.as_view(), name='list-create-video'),

    # Retrieve, update, and delete a specific video by ID
    path('videos/<int:pk>/', views.RetrieveUpdateDestroyVideoView.as_view(), name='retrieve-update-destroy-video'),

    # API endpoint to get a list of all videos
    path('get_all_videos/', views.get_all_videos, name='get-all-videos'),

    # API endpoint to get a complete video by session ID
    path('get_complete_video/<str:session_id>/', views.get_complete_video, name='get-complete-video'),
]
