import os

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM_EMAIL = os.getenv("SMTP_FROM_EMAIL", "")
APP_URL = os.getenv("APP_URL", "http://localhost:8000")
