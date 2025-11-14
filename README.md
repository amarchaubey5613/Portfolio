# Portfolio

This is Amar Chaubey's portfolio website built with Django.

## Quick Start (development)

1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations and create a superuser (if you haven't):

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```powershell
python manage.py runserver
```

5. Open the site at `http://127.0.0.1:8000/` and the admin at `http://127.0.0.1:8000/admin/`.

## Admin

- Username example: `amar` (your account)
- To set/reset password locally:

```powershell
python manage.py changepassword amar
```

## Add Projects

Use the admin panel to add `Project` entries. Fields:
- Title
- Description
- Technologies (comma-separated)
- Image (upload file)
- Link (optional)

Uploaded images are stored under `media/projects/`.

## Notes

- This project uses Django (5.2.8) and Pillow for image support.
- For production deployment, configure `DEBUG=False`, set `ALLOWED_HOSTS`, and use a proper static/media serving setup.
