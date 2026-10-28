import os

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

SMTP_HOST = os.getenv("HOST", "")
SMTP_PORT = int(os.getenv("PORT", "587"))
SMTP_USERNAME = os.getenv("USERNAME")
SMTP_PASSWORD = os.getenv("PASSWORD")
SMTP_FROM_EMAIL = os.getenv("USERNAME", "")
