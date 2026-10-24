from components.alert import Alert
from components.login_form import LoginForm
from components.ui import (
    H2,
    Button,
    Card,
    CardAction,
    Div,
    Header,
    P,
    Section,
)
from fasthtml.common import FastHTML
from layouts.base import Base

login_app = FastHTML()
rt = login_app.route


@rt("/")
def get():
    return Base(
        Div(
            Card(
                Header(
                    H2("Login to your account"),
                    P("Enter your credentials to access your account."),
                    CardAction(
                        Button("Sign Up", data_variant="link"),
                    ),
                ),
                Section(
                    LoginForm(),
                ),
                cls="w-full max-w-sm",
            ),
            cls="min-h-dvh flex items-center justify-center p-4",
        ),
        title="Login Page",
    )


@rt("/")
def post(username: str, password: str):
    return Alert("Login Failed", "Invalid username or password.")
