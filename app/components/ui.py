from functools import partial

from fasthtml.common import *

Input = partial(Input, cls="input")
Button = partial(Button, cls="btn")

Card = partial(Div, cls="card")
CardAction = partial(Div, cls="card-action")


def Icon(name: str, **kwargs) -> FT:
    return Span(
        data_lucide=name,
        **kwargs,
    )
