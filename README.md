# Django Slider Test Task

Test task implementation using:

- Python 3.12
- Django 5.2
- MySQL
- django-filer
- django-admin-sortable2
- Bootstrap 5
- Slick Slider (Slider Syncing)
- Fancybox (fullscreen gallery)

---

## Features

- Images uploaded via Django Admin (django-filer)
- Drag & drop sorting of slides (django-admin-sortable2)
- Bootstrap 5 layout
- Slick synced slider (main + thumbnails)
- Fullscreen gallery on click
- MySQL database

---

## Installation

### 1. Clone repository

git clone https://github.com/iampsih/slider.git
cd slider
2. Create virtual environment
python3.12 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r req.pip
4. Configure MySQL

Create database:

CREATE DATABASE slider CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

Update database credentials in:

config/settings.py
5. Apply migrations
python manage.py migrate
6. Create superuser
python manage.py createsuperuser
7. Run server
python manage.py runserver

Open:

http://127.0.0.1:8000/

Admin:

http://127.0.0.1:8000/admin/