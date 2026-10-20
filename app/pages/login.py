from fasthtml.common import H1, Form, fast_app
from layouts.base import Base
from ui import Button, Input

login_app, rt = fast_app()


@rt("/")
def get():
    return Base(
        H1("Login"),
        Form(
            Input(type="text", name="username", placeholder="Username", cls="input"),
            Input(type="password", name="password", placeholder="Password"),
            Button("Login", type="submit"),
        ),
        title="Login page",
    )
