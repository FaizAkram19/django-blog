
# Django Blog Application (Ongoing)
## Overview

A full-stack blogging platform built using Django, focused on content management, user authentication, and role-based access control.

This project is being developed to understand how real-world content-driven web applications are designed and maintained, similar to professional CMS platforms.

## Objectives

- Understand content management system (CMS) architecture

- Implement user authentication and authorization

- Design relational database models for posts and comments

- Learn Django’s ORM, views, templates, and admin customization

- Practice clean backend code and scalable project structure

## Project Status

Status: 🛠️ Ongoing
Actively being developed and improved.

## Planned Features
### User Features

- User registration and login

- Create, edit, and delete blog posts

- Comment on posts

- User-specific dashboards

### Content Management

- Rich text / Markdown support

- Draft and publish workflow

- Post categorization and tags

- Search functionality

### Permissions & Roles

- Role-based access (Admin / Author / Reader)

- Only authors can edit their own posts

- Admin moderation for comments

### Admin Panel

- Manage posts, users, and comments

- Content moderation using Django Admin

## Tech Stack
### Backend

- Python

- Django

### Frontend

- HTML

- CSS

- JavaScript (basic)

### Database

- SQLite (development)

- PostgreSQL (planned)

### Tools

- Git & GitHub

- VS Code

## Project Structure (Planned)
django-blog/
│
├── blog/             # Blog app (posts, comments)
├── accounts/         # User authentication & profiles
├── templates/        # HTML templates
├── static/           # CSS & JS files
├── db.sqlite3
└── manage.py

## Installation & Setup (Local)
1️⃣ Clone the Repository
git clone https://github.com/FaizAkram19/django-blog.git
cd django-blog

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install django

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start Development Server
python manage.py runserver


Open browser and visit:

http://127.0.0.1:8000/

## Learning Outcomes

- Building content-driven web applications

- Implementing authentication & authorization

- Designing scalable Django project architecture

- Using Django ORM for relational data

- Managing user roles and permissions

## Future Enhancements

- Django REST Framework API

- Rich text editor integration

- Like / bookmark system

- Deployment on cloud platforms

- Docker support

## Contributing

This is a personal learning project.
Suggestions and feedback are welcome.

## Author

Faiz Akram
B.Tech Computer Science Student
GitHub: https://github.com/FaizAkram19