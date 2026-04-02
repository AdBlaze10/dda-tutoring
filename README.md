# DDA Tutoring Website (Django)

Production-ready, premium, conversion-focused website for **DDA Tutoring**.

## 1) Local Development Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## 2) Google Forms Integration

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

## 3) Static Files

Static files are served with WhiteNoise.

```bash
python manage.py collectstatic
```

## 4) Deployment (Render / Railway)

### Environment variables
- `DJANGO_SECRET_KEY` = secure random value
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = your deployed domain(s), comma-separated

### Render
1. Create a new web service from this repo.
2. Build command:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```
3. Start command:
   ```bash
   gunicorn dda_tutoring.wsgi:application
   ```
4. Add environment variables above.

### Railway
1. Create new project from this repo.
2. Set start command:
   ```bash
   gunicorn dda_tutoring.wsgi:application
   ```
3. Configure the same environment variables.
4. Add optional deploy step for static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

## 5) Project Structure

```text
.
├── dda_tutoring/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
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
