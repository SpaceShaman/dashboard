from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from userharbor import UserHarbor
from userharbor_smtp import SMTPEmailSender
from userharbor_sqlalchemy import SQLAlchemyUserStore

from .settings import (
    APP_URL,
    SECRET_KEY,
    SMTP_FROM_EMAIL,
    SMTP_HOST,
    SMTP_PASSWORD,
    SMTP_PORT,
    SMTP_USERNAME,
)

engine = create_engine("sqlite:///users.db")
SessionLocal = sessionmaker(bind=engine)

store = SQLAlchemyUserStore(SessionLocal)
store.metadata.create_all(engine)

email_sender = SMTPEmailSender(
    host=SMTP_HOST,
    port=SMTP_PORT,
    username=SMTP_USERNAME,
    password=SMTP_PASSWORD,
    from_email=SMTP_FROM_EMAIL,
    template_dir=Path(__file__).parent.parent / "email_templates",
    template_context={
        "app_url": APP_URL,
    },
)

harbor = UserHarbor(
    secret_key=SECRET_KEY,
    store=store,
    email_sender=email_sender,
)
