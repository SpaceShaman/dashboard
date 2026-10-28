from components.alert import Alert
from fasthtml.common import FT, FastHTML
from pages.login import LoginPage

login_app = FastHTML()
rt = login_app.route


@rt("/")
def get() -> FT:
    return LoginPage()


@rt("/")
def post(username: str, password: str) -> FT:
    return Alert("Login Failed", "Invalid username or password.")
