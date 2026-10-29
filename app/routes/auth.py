from components.alert import Alert
from components.auth.forgot_password import SuccessfulForgotPasswordCard
from components.auth.register import SuccessfulRegisterCard
from components.auth.reset_password import SuccessfulResetPasswordCard
from core.harbor import harbor
from core.types import HTMLResult
from fasthtml.common import FT, HttpHeader, Response, fast_app
from pages.auth import AuthPage
from pages.reset_password import ResetPasswordPage
from pages.verify_email import VerifyEmailPage
from userharbor.exceptions import UserHarborError

auth_app, rt = fast_app()


@rt
def index() -> FT:
    return AuthPage()


@rt
def login(username: str, password: str) -> HTMLResult:
    try:
        session_token = harbor.login(username, password)
    except UserHarborError as e:
        return Alert("Login Failed", str(e), variant="error")
    response = Response(headers={"HX-Redirect": "/"})
    response.set_cookie(
        "session_token",
        session_token,
        path="/",
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax",
    )
    return response


@rt
def register(username: str, email: str, password: str) -> HTMLResult:
    try:
        harbor.register(username, email, password)
    except UserHarborError as e:
        return Alert("Registration Failed", str(e), variant="error")
    return SuccessfulRegisterCard()


@rt(methods=["GET"])
def verify_email(token: str) -> HTMLResult:
    try:
        harbor.verify_email(token)
    except UserHarborError as e:
        page = VerifyEmailPage(error=str(e))
    else:
        page = VerifyEmailPage()
    return page, HttpHeader("Referrer-Policy", "no-referrer")


@rt(methods=["POST"])
def forgot_password(email: str) -> HTMLResult:
    try:
        harbor.send_password_reset(email)
    except UserHarborError as e:
        return Alert("Password Reset Failed", str(e), variant="error")
    return SuccessfulForgotPasswordCard()


@rt(methods=["GET"])
def reset_password(token: str) -> HTMLResult:
    return (
        ResetPasswordPage(token),
        HttpHeader("Referrer-Policy", "no-referrer"),
        HttpHeader("Cache-Control", "no-store"),
    )


@rt(methods=["POST"])
def update_password(token: str, new_password: str, confirm_password: str) -> HTMLResult:
    if new_password != confirm_password:
        return Alert(
            "Password Reset Failed", "Passwords do not match.", variant="error"
        )
    try:
        harbor.reset_password(new_password=new_password, reset_token=token)
    except UserHarborError as e:
        return Alert("Password Reset Failed", str(e), variant="error")
    return SuccessfulResetPasswordCard()
