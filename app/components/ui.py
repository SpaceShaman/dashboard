from functools import wraps

from fasthtml.common import *


def with_classes(component, default_cls):
    @wraps(component)
    def wrapped(*args, cls="", **kwargs):
        classes = f"{default_cls} {cls}".strip()
        return component(*args, cls=classes, **kwargs)

    return wrapped


Input = with_classes(Input, "input")
Button = with_classes(Button, "btn")

Card = with_classes(Div, "card")
CardAction = with_classes(Div, "card-action")


def Icon(name: str, **kwargs) -> FT:
    return Span(
        data_lucide=name,
        **kwargs,
    )
