# Django Video API for Chrome Extension

This Django-based API allows you to post and retrieve a list of videos for use in a Chrome extension. It allows you to upload videos in smaller chunks and then concat them to post to this backend.

## Requirements
- Python 3.8 or greater
- Django
- RestFramework

## How it Works

### Video Upload in Smaller Chunks

- The API allows you to upload videos in smaller chunks. The frontend application should record or split the video into these smaller chunks on the client side.

- Each video chunk should include metadata such as `session_id`, `chunk_number`, and `total_chunks` to help the server combine the chunks into a complete video.

- The server receives and stores these chunks in the `VideoChunk` model, associating them with the same `session_id`.

- Once all chunks for a session are received, the server combines them into a complete video and saves it as a `Video` object associated with the `session_id`.

## Endpoints## Endpoints
- `/combine_and_save_video/` - API endpoint to combine and save video chunks.
- `/videos/` - List and create videos.
- `/videos/<int:pk>/` - Retrieve, update, and delete a specific video by ID.
- `/get_all_videos/` - API endpoint to get a list of all videos.
- `/get_complete_video/<str:session_id>/` - API endpoint to get a complete video by session ID.
- `/auth/users/` - POST and GET (Signup and Getting List of Users).
- `/auth/jwt/create` - Login (Generate a JSON web token for login).

  

## Features
- Create, Read operations for videos in smaller chunks.
- Secure authentication to protect your data.
- Easy integration with your Chrome extension.

## Installation

1. Clone the repository:
   git clone https://github.com/Konlan21/videoBackend.git
2. Create a virtual environment for the project
   - python pm venv yourvritualenv name
3. Navigate to your venv and install requirements.txt
   - pip install requirements.txt
4. Configure database settings to one of your choice and migrate
    - python manage.py makemigrations
    - python manage.py migrate
5. Start application
    python manage.py runserver
