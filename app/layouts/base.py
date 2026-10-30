from pathlib import Path

from fasthtml.common import (
    FT,
    Body,
    Div,
    Head,
    Html,
    Meta,
    Script,
    Title,
)
from fasthtml_basecoat import (
    BasecoatInput,
    BasecoatJS,
)
from fasthtml_tailwindcss import TailwindHead

ASSETS_ROOT = Path(__file__).parent.parent


def BaseLayout(*c, title: str, **kwargs) -> FT:
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
            *c,
        ),
        **kwargs,
    )
