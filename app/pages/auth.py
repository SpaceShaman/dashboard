from components.login_form import LoginForm
from fasthtml.common import FT, H2, Div, Header, P, Section
from fasthtml_basecoat import Button, Card, CardAction
from layouts.base import Base


def AuthPage() -> FT:
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
