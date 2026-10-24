from components.theme import LoadThemeScript, ToggleThemeButton
from components.ui import Icon
from fasthtml.common import *
from fasthtml.core import vurl

ASSETS_ROOT = Path(__file__).parent.parent


def Base(*c, title: str, **kwargs):
    return Html(
        Head(
            Title(title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href=vurl("/static/app.css", root=ASSETS_ROOT)),
            Script(src=vurl("/static/app.js", root=ASSETS_ROOT), defer=True),
        ),
        Body(
            Div(
                id="alerts",
                cls="fixed top-4 inset-x-0 z-50 flex flex-col items-center gap-4 px-4",
            ),
            Icon("info"),
            Div(
                ToggleThemeButton(),
                cls="fixed top-4 right-4 z-50",
            ),
            *c,
            LoadThemeScript(),
        ),
        **kwargs,
    )
