# Django Video API for Chrome Extension

This Django-based API allows you to post and retrieve a list of videos for use in a Chrome extension. It allows you to upload videos in smaller chunks and then concat them to post to this backend.

## Requirements
- Python 3.8 or greater
- Django
- RestFramework

## Endpoints
- /videoupload/   - POST and GET videos
- /auth/users/    - POST and GET (Signup and Getting List of Users)
- /auth/jwt/create - Login(Generate a json web token for login)
  

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
