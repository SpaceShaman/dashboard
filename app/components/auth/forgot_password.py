from core.types import HTMLResult
from fasthtml.common import FT, H2, Div, Form, Header, HttpHeader, P, Section
from fasthtml_basecoat import Button, Card, Input, Label


def ForgotPasswordCard(**attrs) -> FT:
    return Card(
        Header(
            H2("Forgot your password?"),
            P("Enter your email address to receive password reset instructions."),
        ),
        Section(_ForgotPasswordForm()),
        **attrs,
    )


def SuccessfulForgotPasswordCard() -> HTMLResult:
    return (
        Card(
            Header(
                H2("Check your email"),
                P(
                    "If an account exists for this email, you will receive password reset instructions."
                ),
            ),
            cls="text-center",
            id="auth-forgot-password-card",
            role="tabpanel",
            aria_labelledby="auth-forgot-password-tab",
        ),
        HttpHeader("HX-Retarget", "#auth-forgot-password-card"),
        HttpHeader("HX-Reswap", "outerHTML"),
    )


def _ForgotPasswordForm() -> FT:
    return Form(
        Div(
            Label("Email", fr="forgot-password-email"),
            Input(
                type="email",
                id="forgot-password-email",
                name="email",
                autocomplete="email",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Button("Send reset instructions", cls="w-full"),
        cls="grid gap-6",
        hx_post="forgot_password",
        hx_swap="none",
    )
