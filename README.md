# Django Polls Application

This is a basic polling application built following the official Django documentation tutorial. It allows users to view open polls, vote on choices, and see real-time results. It also includes a fully functional administrative interface for managing questions and choices.

---

## 🚀 Features

* Public Interface: Users can browse a list of recent polls, view details for a specific question, and cast votes.
* Results View: Dynamic updates of vote counts for each choice after a vote is cast.
* Admin Dashboard: A pre-configured administrative site to create, update, and delete questions and choices.
* Automated Testing: Includes basic tests for model logic (e.g., checking if questions were published recently).
* Custom Styling: Integrated static files for a clean, documentation-inspired UI.

---

## 🛠️ Technology Stack

* Framework: Django
* Language: Python 3.x
* Database: SQLite (Default)
* Frontend: Django Template Language (HTML/CSS)

---

## ⚙️ Installation & Setup

Follow these steps to get the project running locally:

### 1. Clone the Repository
git clone <repository-url>
cd django-polls

### 2. Create a Virtual Environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

### 3. Install Dependencies
pip install django

### 4. Database Migrations
Apply the initial schema to your SQLite database:
python manage.py migrate

### 5. Create an Admin User
To access the /admin panel, create a superuser:
python manage.py createsuperuser

### 6. Run the Server
python manage.py runserver
Visit http://127.0.0.1:8000/polls/ to view the app or http://127.0.0.1:8000/admin/ to manage it.

---

## 📂 Project Structure

A quick overview of the key files:

* polls/models.py: Defines Question and Choice schemas.
* polls/views.py: Contains the logic for the index, detail, and results pages.
* polls/urls.py: Maps URL patterns to the specific views.
* polls/templates/: Contains the HTML files using Django Template Language.
* mysite/settings.py: The main configuration file for the Django project.

---

## 🧪 Running Tests

To ensure the logic is working correctly (especially the was_published_recently() method), run:
python manage.py test polls

---

> Note: This project was developed as part of Phase 1 (Foundations) of a Django learning roadmap to understand the core MVT (Model-View-Template) architecture, including URL routing, database relationships, and form handling.
