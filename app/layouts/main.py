from typing import override

from ludic.attrs import NoAttrs
from ludic.components import Component
from ludic.html import (
    body,
    head,
    html,
    link,
    meta,
    script,
)
from ludic.types import AnyChildren


class Page(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> html:
        return html(
            head(
                meta(charset="UTF-8"),
                meta(name="viewport", content="width=device-width, initial-scale=1"),
                link(rel="stylesheet", href="/static/app.css"),
                script(src="/static/app.js", defer=True),
            ),
            body(
                *self.children,
            ),
        )
