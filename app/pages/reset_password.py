from components.auth.reset_password import ResetPasswordCard
from fasthtml.common import FT, Div
from layouts.base import Base


def ResetPasswordPage(token: str) -> FT:
    return Base(
        Div(
            ResetPasswordCard(
                token,
                id="reset-password-card",
                cls="w-full max-w-sm",
            ),
            cls="min-h-dvh flex items-center justify-center p-4",
        ),
        title="Reset your password",
    )
