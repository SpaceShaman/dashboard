from fasthtml.common import *
from fasthtml_basecoat import (
    BasecoatInput,
    BasecoatJS,
    Button,
    ThemeSwitcher,
)
from fasthtml_tailwindcss import TailwindHead

ASSETS_ROOT = Path(__file__).parent.parent


def Base(*c, title: str, user=None, **kwargs) -> FT:
    return Html(
        Head(
            Title(title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.11/dist/htmx.js"),
            BasecoatJS(),
            TailwindHead(input=BasecoatInput("nova"), watch=True),
        ),
        Body(
            Div(
                id="alerts",
                cls="fixed top-4 inset-x-0 z-50 flex flex-col items-center gap-4",
            ),
            Div(
                Button(
                    "Logout",
                    variant="outline",
                    hx_post="/auth/logout",
                    hx_swap="none",
                )
                if user
                else None,
                ThemeSwitcher(),
                cls="fixed top-4 right-4 z-50 flex items-center gap-4",
            ),
            *c,
        ),
        **kwargs,
    )
