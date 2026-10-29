from fasthtml.common import FT, H2, A, Div, Header, P, Section
from fasthtml_basecoat import Card
from layouts.base import Base


def VerifyEmailPage(error: str | None = None) -> FT:
    title = "Verification Failed" if error is not None else "Account Activated"
    message = (
        error
        if error is not None
        else "Your account has been activated.\nYou can now log in."
    )
    return Base(
        Div(
            Card(
                Header(H2(title), P(message)),
                Section(
                    A(
                        "Back to login",
                        href="/auth/",
                        cls="text-sm underline underline-offset-4",
                    ),
                ),
                cls="w-full max-w-sm text-center",
            ),
            cls="min-h-dvh flex items-center justify-center p-4",
        ),
        title=title,
    )
