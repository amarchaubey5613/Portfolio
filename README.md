# Portfolio

[![CI](https://github.com/amarchaubey5613/Portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/amarchaubey5613/Portfolio/actions/workflows/ci.yml)

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

## Deploy to PythonAnywhere (quick guide)

This project can be hosted on PythonAnywhere under the account name `amarportfolio` (or any account you create).

Manual steps (recommended for first deploy):

1. Create an account at https://www.pythonanywhere.com/ (free tier available).
2. Create a new Web App on PythonAnywhere and select "Manual configuration" -> "Django".
3. On your PythonAnywhere console, create a virtualenv and install dependencies:

```bash
python3 -m venv ~/venv
source ~/venv/bin/activate
pip install -r requirements.txt
```

4. Clone your GitHub repo into PythonAnywhere (or use the `Git` option):

```bash
git clone https://github.com/amarchaubey5613/Portfolio.git mysite
cd mysite
```

5. Point your PythonAnywhere web app to the project's WSGI file (edit the "WSGI configuration file" path in the Web tab), ensure `STATIC_ROOT`/`MEDIA_ROOT` are configured, and run migrations:

```bash
python manage.py migrate
```

6. Reload the web app from the PythonAnywhere Web tab and visit the site at `https://amarportfolio.pythonanywhere.com/` (replace with your actual PythonAnywhere webapp domain).

Automated deploy (optional):

You can add a GitHub Actions workflow that triggers a reload of your PythonAnywhere web app whenever you push to `main`. To use it:

- Create a PythonAnywhere API token: on PythonAnywhere go to your account -> "Account" -> "API token" and generate one.
- In your GitHub repository, add repository Secrets:
	- `PYTHONANYWHERE_API_TOKEN` — the token value
	- `PYTHONANYWHERE_USERNAME` — your PythonAnywhere username (e.g. `amarportfolio`)
	- `PYTHONANYWHERE_WEBAPP` — the webapp domain (e.g. `amarportfolio.pythonanywhere.com`)

Then enable the provided GitHub Actions workflow `deploy-pythonanywhere.yml` (already added to this repo) which will call the PythonAnywhere API to reload the app after a push.

