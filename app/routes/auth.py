from components.alert import Alert
from core.harbor import harbor
from fasthtml.common import FT, fast_app
from pages.auth import AuthPage
from starlette.responses import RedirectResponse
from userharbor.exceptions import UserHarborError

auth_app, rt = fast_app()


@rt
def index() -> FT:
    return AuthPage()


@rt
def login(username: str, password: str) -> FT | RedirectResponse:
    try:
        session_token = harbor.login(username, password)
    except UserHarborError as e:
        return Alert("Login Failed", str(e), variant="error")
    response = RedirectResponse("/", status_code=303)
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
def register(username: str, email: str, password: str) -> FT:
    try:
        harbor.register(username, email, password)
    except UserHarborError as e:
        return Alert("Registration Failed", str(e), variant="error")
    return Alert(
        "Registration Successful",
        "Check your email for a verification link.",
        variant="info",
    )
