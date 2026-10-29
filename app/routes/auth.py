from components.alert import Alert
from components.auth.register import SuccessfulRegisterCard
from core.harbor import harbor
from core.types import HTMLResult
from fasthtml.common import FT, HttpHeader, Response, fast_app
from pages.auth import AuthPage
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
