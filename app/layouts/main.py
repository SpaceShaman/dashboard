from fastapi import FastAPI
from ludic.contrib.fastapi import LudicRoute

app = FastAPI()
app.router.route_class = LudicRoute

from typing import override

from fastapi import FastAPI
from ludic.attrs import NoAttrs
from ludic.components import Component
from ludic.contrib.fastapi import LudicRoute
from ludic.html import (
    body,
    html,
    script,
)
from ludic.types import AnyChildren

app = FastAPI()
app.router.route_class = LudicRoute


class Page(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> html:
        return html(
            *body(
                *self.children,
                script(
                    src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.11/dist/htmx.min.js"
                ),
            )
        )
