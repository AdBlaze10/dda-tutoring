# DDA Tutoring Website (Django)

Production-ready, premium, conversion-focused website for **DDA Tutoring**.

## Render Deployment (dashboard.render.com)

This project is now set up to work directly from the Render dashboard at:
`https://dashboard.render.com/`

You can deploy **either way**:

### Option A — Fastest (Blueprint)
1. Push this repo to GitHub.
2. In Render dashboard, click **New +** → **Blueprint**.
3. Select your repo.
4. Render uses `render.yaml` automatically.
5. Deploy.

### Option B — Manual Web Service (from dashboard)
1. In Render dashboard, click **New +** → **Web Service**.
2. Connect your repo.
3. Fill these settings:
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn dda_tutoring.wsgi:application --log-file -`
4. Add environment variables:
   - `DJANGO_SECRET_KEY` = click **Generate**
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = your Render hostname (for example `dda-tutoring.onrender.com`)
   - Optional: `CSRF_TRUSTED_ORIGINS` = `https://your-service-name.onrender.com`
5. Click **Create Web Service**.

> Render also provides `RENDER_EXTERNAL_HOSTNAME`; this project auto-adds it to Django `ALLOWED_HOSTS` and CSRF trusted origins.

---

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Google Forms Integration

The site intentionally uses Google Forms (no backend form handling required).

### Required form fields
- Parent Name
- Student Name
- Grade
- Email
- Phone
- Goals/Concerns
- Current resources
- Why DDA Tutoring?

### Steps
1. Create a new form at https://forms.google.com.
2. Add all required fields above.
3. Click **Send**:
   - Copy form URL for external opening.
   - Copy embed URL from the `<>` tab.
4. Update these variables in `tutoring_site/views.py`:
   - `google_form_url`
   - `google_embed_url`
5. In Google Forms, open **Responses** → **Link to Sheets** to automatically send responses to Google Sheets.

## Static Files

```bash
python manage.py collectstatic
```

## Project Structure

```text
.
├── Procfile
├── build.sh
├── dda_tutoring/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── render.yaml
├── tutoring_site/
│   ├── static/tutoring_site/
│   │   ├── scripts.js
│   │   └── styles.css
│   ├── templates/tutoring_site/
│   │   └── home.html
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```
