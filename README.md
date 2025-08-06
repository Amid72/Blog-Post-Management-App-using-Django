
# 📝 Django Blog App

A simple blog and post management web application built with Django. This project demonstrates user authentication, admin panel usage, and basic CRUD operations.

## 🚀 Features

- 🏠 Homepage displaying all posts
- 🛠 Admin panel for managing posts
- 🧾 User authentication with Django (login/logout/signup)
- 🔄 REST API endpoint for accessing posts (via Django REST Framework)

## 🛠 Tech Stack

- Python
- Django
- SQLite
- HTML/CSS (Django templating)
- Django Admin
- Django REST Framework

## 📁 Project Structure

```
django_project_starter/
├── myproject/
│   ├── settings.py
│   ├── urls.py
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── home.html
│       └── registration/
│           ├── login.html
│           └── signup.html
├── db.sqlite3
├── manage.py
```

## ✅ How to Run

1. **Clone this project:**
   ```bash
   git clone https://github.com/your-username/django-blog-app.git
   cd django-blog-app
   ```

2. **Create virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations & create superuser:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run server:**
   ```bash
   python manage.py runserver
   ```

6. **Visit the app:**
   - http://127.0.0.1:8000/ → Home
   - http://127.0.0.1:8000/admin/ → Admin panel
   - http://127.0.0.1:8000/signup/ → User signup
   - http://127.0.0.1:8000/api/posts/ → API endpoint

---

## 📌 Author

Amid Basha  
Email: your-email@example.com  
GitHub: [your-username](https://github.com/your-username)

