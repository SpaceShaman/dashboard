from collections.abc import Callable
from functools import wraps
from typing import Any, cast

from fasthtml.common import *


def with_classes[C: Callable[..., Any]](
    component: C,
    default_cls: str,
) -> C:
    @wraps(component)
    def wrapped(*args: Any, cls: str = "", **kwargs: Any) -> Any:
        classes = f"{default_cls} {cls}".strip()
        return component(*args, cls=classes, **kwargs)

    return cast(C, wrapped)


Label = with_classes(Label, "label")
Input = with_classes(Input, "input")
Button = with_classes(Button, "btn")

Card = with_classes(Div, "card")
CardAction = with_classes(Div, "card-action")


def Icon(name: str, **kwargs) -> FT:
    return Span(
        data_lucide=name,
        **kwargs,
    )
