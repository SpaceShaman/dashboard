import re
from collections.abc import Callable
from functools import cache, wraps
from pathlib import Path
from typing import Any, cast
from xml.etree import ElementTree as ET

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


ICONS_DIR = Path(__file__).resolve().parents[1] / "icons"
ET.register_namespace("", "http://www.w3.org/2000/svg")


@cache
def _icon_source(name: str) -> str:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError(f"Invalid icon name: {name}")
    return (ICONS_DIR / f"{name}.svg").read_text(encoding="utf-8")


def Icon(name: str, *, cls: str = "", size: int | str = 24) -> NotStr:
    svg = ET.fromstring(_icon_source(name))
    svg.set("width", str(size))
    svg.set("height", str(size))
    svg.set("class", f"{svg.get('class', '')} {cls}".strip())
    svg.set("aria-hidden", "true")
    return NotStr(ET.tostring(svg, encoding="unicode"))
