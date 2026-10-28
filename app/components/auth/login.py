from fasthtml.common import FT, H2, A, Div, Form, Header, P, Section
from fasthtml_basecoat import (
    Button,
    Card,
    Input,
    Label,
)


def LoginCard(**attrs) -> FT:
    return Card(
        Header(
            H2("Login to your account"),
            P("Enter your credentials to access your account."),
        ),
        Section(_LoginForm()),
        **attrs,
    )


def _LoginForm() -> FT:
    return Form(
        Div(
            Label("Username", fr="username"),
            Input(
                type="text",
                id="username",
                name="username",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Div(
            Div(
                Label("Password", fr="password"),
                A(
                    "Forgot your password?",
                    onclick="event.preventDefault(); this.closest('.tabs').select(document.getElementById('auth-forgot-password-tab'));",
                    cls="ms-auto inline-block text-sm underline-offset-4 hover:underline",
                ),
                cls="flex items-center",
            ),
            Input(
                type="password",
                id="password",
                name="password",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Button("Login", cls="w-full"),
        cls="grid gap-6",
        hx_post="login",
        hx_swap="none",
    )
