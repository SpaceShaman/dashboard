from components.alert import Alert
from core.harbor import harbor
from fasthtml.common import FT, fast_app
from pages.login import LoginPage
from starlette.responses import RedirectResponse
from userharbor.exceptions import UserHarborError

auth_app, rt = fast_app()


@rt
def index() -> FT:
    return LoginPage()


@rt
def login(username: str, password: str) -> FT | RedirectResponse:
    try:
        session_token = harbor.login(username, password)
    except UserHarborError:
        return Alert("Login Failed", "Invalid username or password.")
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
