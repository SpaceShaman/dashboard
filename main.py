from typing import Any

from fastapi import FastAPI
from fasthx.htmy import HTMY
from htmy import Component, html

app = FastAPI()
htmy = HTMY()


def index_page(_: Any) -> Component:
    return (
        html.DOCTYPE.html,
        html.html(
            html.head(
                html.title("My HTMY App"),
                html.Meta.charset(),
                html.Meta.viewport(),
            )
        ),
        html.body(
            html.h1("Welcome to My HTMY App"),
            html.p("This is a simple HTMY application."),
        ),
    )


@app.get("/")
@htmy.page(index_page)
def index() -> None: ...
