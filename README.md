# Monen Schilderwerken Website

A production-ready, professional website for Monen Schilderwerken, built with Flask and Jinja2.

## Features
- Clean, mobile-first design
- Black & white color palette
- Dynamic project gallery (auto-loads images)
- Professional hero section with action photos
- WhatsApp floating button and Instagram link
- Responsive, accessible, and semantic HTML

## Project Structure
```
app/
  __init__.py
  routes.py
  templates/
    index.html
  static/
    css/
      style.css
    js/
      main.js
    pictures/
      hero/      # Professional action shots
      gallery/   # Project photos (auto-loaded)
      logos/     # Wide and square logos
config.py
run.py
requirements.txt
README.md
```

## Setup (Development)
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   python -m venv venv
   venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   python run.py
   ```
   The site will be available at [http://localhost:5000](http://localhost:5000)

## Deployment (Production)
1. **Set environment variables** (optional but recommended)
   - `SECRET_KEY`: Set a strong secret key for Flask sessions.
2. **Use a production WSGI server** (e.g., Gunicorn or Waitress)
   - Example with Gunicorn (Linux/macOS):
     ```bash
     gunicorn -w 4 -b 0.0.0.0:8000 run:app
     ```
   - Example with Waitress (Windows):
     ```bash
     pip install waitress
     waitress-serve --port=8000 run:app
     ```
3. **Serve static files**
   - For best performance, serve `/app/static` via a web server (e.g., Nginx, Apache) in production.

## Customization
- **Gallery**: Add/remove images in `app/static/pictures/gallery/` (subfolders = projects)
- **Hero images**: Place action shots in `app/static/pictures/hero/`
- **Logos**: Place wide and square logos in `app/static/pictures/logos/`
- **Colors/Style**: Edit `app/static/css/style.css`

## Contact
- Email: info@monenschilderwerken.nl
- WhatsApp: +31 6 47323264
- Instagram: [@monenschilderwerken](https://www.instagram.com/monenschilderwerken)

---
© Monen Schilderwerken. All rights reserved. 