from fasthtml.common import (
    FT,
    Div,
)
from fasthtml_basecoat import (
    ThemeSwitcher,
)

from .base import BaseLayout


def AuthLayout(*c, title: str, **kwargs) -> FT:
    return BaseLayout(
        Div(
            ThemeSwitcher(),
            cls="fixed top-4 right-4 z-50 flex items-center gap-4",
        ),
        *c,
        title=title,
        **kwargs,
    )
