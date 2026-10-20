from functools import partial

from fasthtml.common import *

Input = partial(Input, cls="input")
Button = partial(Button, cls="btn")

Card = partial(Div, cls="card")
CardAction = partial(Div, cls="card-action")


def Icon(name: str, cls: str = "", **kwargs) -> FT:
    # return Img(src=f"/static/icons/{name}.svg", **kwargs)
    return Span(
        cls=f"icon {cls}",
        style=f"--icon-url: url('/static/icons/{name}.svg')",
        aria_hidden="true",
        **kwargs,
    )
