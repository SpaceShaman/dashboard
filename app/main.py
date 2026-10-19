from typing import Annotated

from fastapi import FastAPI, Form
from ludic.contrib.fastapi import LudicRoute

app = FastAPI()
app.router.route_class = LudicRoute


from fastapi import FastAPI
from layouts.main import Page
from ludic.contrib.fastapi import LudicRoute
from ludic.html import (
    body,
    div,
    h1,
    head,
    html,
    p,
    title,
)
from pages.index import index_page

app = FastAPI()
app.router.route_class = LudicRoute


@app.get("/")
def index() -> Page:
    return index_page()


@app.post("/message")
def add_message(message: Annotated[str, Form()]) -> html:
    return html(
        head(title("Message Received")),
        body(
            div(
                h1("Message Received"),
                p(f"You sent: {message}"),
                id="container",
            )
        ),
    )
