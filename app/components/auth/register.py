from core.types import HTMLResult
from fasthtml import HttpHeader
from fasthtml.common import FT, H2, Div, Form, Header, P, Section
from fasthtml_basecoat import Button, Card, Input, Label


def RegisterCard(**attrs) -> FT:
    return Card(
        Header(
            H2("Create an account"),
            P("Enter your details to create your account."),
        ),
        Section(_RegisterForm()),
        **attrs,
    )


def SuccessfulRegisterCard() -> HTMLResult:
    return (
        Card(
            Header(
                H2("Registration Successful"),
                P("Please check your email to verify your account."),
            ),
            cls="w-full max-w-sm text-center",
            id="auth-register-card",
            role="tabpanel",
            aria_labelledby="auth-register-tab",
        ),
        HttpHeader("HX-Retarget", "#auth-register-card"),
        HttpHeader("HX-Reswap", "outerHTML"),
    )


def _RegisterForm() -> FT:
    return Form(
        Div(
            Label("Username", fr="register-username"),
            Input(
                type="text",
                id="register-username",
                name="username",
                autocomplete="username",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Div(
            Label("Email", fr="register-email"),
            Input(
                type="email",
                id="register-email",
                name="email",
                autocomplete="email",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Div(
            Label("Password", fr="register-password"),
            Input(
                type="password",
                id="register-password",
                name="password",
                autocomplete="new-password",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Button("Create account", cls="w-full"),
        cls="grid gap-6",
        hx_post="register",
        hx_swap="none",
    )
