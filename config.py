import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this-secret-key')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    # Add more production settings as needed 