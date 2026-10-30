from core.types import User
from fasthtml.common import (
    FT,
    Div,
    P,
)
from fasthtml_basecoat import (
    Button,
    ThemeSwitcher,
)

from .base import BaseLayout


def DashboardLayout(*c, title: str, user: User, **kwargs) -> FT:
    return BaseLayout(
        Div(
            P(f"Welcome, {user.username}!", cls="text-lg font-semibold"),
            Button(
                "Logout",
                variant="outline",
                hx_post="/auth/logout",
                hx_swap="none",
            ),
            ThemeSwitcher(),
            cls="fixed top-4 right-4 z-50 flex items-center gap-4",
        ),
        *c,
        title=title,
        **kwargs,
    )
