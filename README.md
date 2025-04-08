# 📝 Blogtopia — A Simple Django Blog App

Blogtopia is a personal blogging platform built with Django. It supports user authentication, post creation with optional images, comments, likes, and a responsive frontend using Tailwind CSS. This project is perfect for learning Django fundamentals, AJAX, and real-time UI interactions.

## 🚀 Features

- 🔐 User registration & login/logout
- 📝 Create and list blog posts
- 📷 Image upload for blog posts
- ❤️ Like/unlike posts using AJAX (real-time without page reload)
- 💬 Comment on posts with Django forms
- 🖼️ Tailwind CSS styled UI
- 🛡️ CSRF protection for all forms and AJAX calls

---


## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/blogtopia.git
cd blogtopia
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not generated yet, manually install:

```bash
pip install django pillow
```

Then save:

```bash
pip freeze > requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000/

---

## ✏️ Usage

- Sign up or login
- Create new blog posts with optional images
- Like or unlike any post via AJAX
- Leave comments on posts
- Only authenticated users can comment or create posts

---

## 📦 Technologies Used

- Django (Python 3)
- Tailwind CSS (via CDN)
- JavaScript (AJAX for likes)
- SQLite (default database)
- Pillow (for image uploads)

---

## 📂 Media & Static Files

- Images uploaded are stored in the /media/ directory.
- Make sure your settings.py includes:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Also, in your main urls.py:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 💡 Tips

- Use Django's admin panel at /admin to manage users and posts.
- Update `ALLOWED_HOSTS` in settings.py for production use.
- Protect your `SECRET_KEY` if deploying.
- Consider pagination if you add many posts.

---

## 📸 Screenshots (optional)

Add screenshots here showing:
- Home page with posts
- Create post form
- Likes and comments in action

---

## 🧑‍💻 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

MIT License. Do whatever you want. Just don't forget to give credit 😉

---

## 🙌 Acknowledgments

Thanks to the Django docs, Tailwind CSS, and open source communities for making learning so fun and easy!
