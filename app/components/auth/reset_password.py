from core.types import HTMLResult
from fasthtml.common import FT, H2, A, Div, Form, Header, HttpHeader, P, Section
from fasthtml_basecoat import Button, Card, Input, Label


def ResetPasswordCard(token: str, **attrs) -> FT:
    return Card(
        Header(
            H2("Reset your password"),
            P("Enter and confirm your new password."),
        ),
        Section(_ResetPasswordForm(token)),
        **attrs,
    )


def SuccessfulResetPasswordCard() -> HTMLResult:
    return (
        Card(
            Header(
                H2("Password Updated"),
                P("Your password has been updated. You can now log in."),
            ),
            Section(
                A(
                    "Back to login",
                    href="/auth/",
                    cls="text-sm underline underline-offset-4",
                ),
            ),
            cls="w-full max-w-sm text-center",
            id="reset-password-card",
        ),
        HttpHeader("HX-Retarget", "#reset-password-card"),
        HttpHeader("HX-Reswap", "outerHTML"),
    )


def _ResetPasswordForm(token: str) -> FT:
    return Form(
        Input(type="hidden", name="token", value=token),
        Div(
            Label("New password", fr="new-password"),
            Input(
                type="password",
                id="new-password",
                name="new_password",
                autocomplete="new-password",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Div(
            Label("Confirm password", fr="confirm-password"),
            Input(
                type="password",
                id="confirm-password",
                name="confirm_password",
                autocomplete="new-password",
                required=True,
            ),
            cls="grid gap-2",
        ),
        Button("Reset password", cls="w-full"),
        cls="grid gap-6",
        hx_post="/auth/update_password",
        hx_swap="none",
    )
