# AWPL Django Project

AWPL is a Django web application that combines a simple public website, a blog, and a product/shop area. It uses SQLite for local development, Django templates for rendering pages, media uploads for blog and product images, and includes authentication for registering, logging in, and managing blog posts.

## What The Project Includes

- A homepage, about page, and contact page
- A blog where users can browse posts, view details, and create or manage posts when logged in
- User registration and standard Django authentication pages
- A shop area with product listing and product detail pages
- Image uploads for blog posts and products
- Static assets and Tailwind-based styling support
- Django browser reload for a smoother development experience

## Technology Stack

- Python 3
- Django 6.0.4
- SQLite
- Django templates
- django-tailwind
- django-browser-reload
- Pillow for image uploads

## Project Structure

- `awpl/manage.py` is the Django command entry point
- `awpl/awpl/` contains the project settings, root URLs, and shared views
- `awpl/blog/` contains the blog app, including posts, registration, forms, and templates
- `awpl/shop/` contains the shop app, including product models, views, and templates
- `awpl/theme/` contains the Tailwind app and frontend source files
- `awpl/templates/` contains shared templates, including the base layout
- `awpl/static/` contains static CSS and JavaScript assets
- `awpl/media/` stores uploaded blog and product images during development

## Local Setup

The repository includes a dependency file named `requirments.txt`.

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirments.txt
```

3. Apply database migrations:

```bash
python awpl/manage.py migrate
```

4. Create an admin user if you want to use the Django admin:

```bash
python awpl/manage.py createsuperuser
```

## Run The Project

Start the development server from the repository root:

```bash
python awpl/manage.py runserver
```

Then open the site in your browser at:

```text
http://127.0.0.1:8000/
```

## Main Pages And Routes

- `/` - homepage
- `/about/` - about page
- `/contact/` - contact page
- `/shop/` - product listing page
- `/shop/product/<id>/` - product detail page
- `/blog/` - blog post list
- `/blog/<id>/` - blog post detail page
- `/blog/create/` - create a blog post
- `/blog/<id>/edit/` - edit a blog post
- `/blog/<id>/delete/` - delete a blog post
- `/blog/register/` - user registration
- `/accounts/login/` - login page
- `/accounts/logout/` - logout page
- `/admin/` - Django admin panel

## Notes

- Blog post creation, editing, and deletion require a logged-in user.
- Uploaded images are saved under the `media/` directory.
- The app is configured for development with `DEBUG = True`.
- If you add new dependencies, update `requirments.txt` so the setup steps stay accurate.

## Useful Commands

```bash
python awpl/manage.py makemigrations
python awpl/manage.py migrate
python awpl/manage.py runserver
python awpl/manage.py createsuperuser
```
