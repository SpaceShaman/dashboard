from components.theme import LoadThemeScript, ToggleThemeButton
from fasthtml.common import *


def Base(*c, title: str, **kwargs):
    return Html(
        Head(
            Title(title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="/static/app.css"),
            Script(src="/static/app.js", defer=True),
        ),
        Body(
            Div(
                ToggleThemeButton(),
                cls="fixed top-4 right-4 z-50",
            ),
            *c,
            LoadThemeScript(),
        ),
        **kwargs,
    )
