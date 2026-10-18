from typing import Annotated

from fastapi import FastAPI, Form
from fasthx.htmy import HTMY
from htmy import Component, html

app = FastAPI()
htmy = HTMY()

messages = []


@app.get("/")
@htmy.page()
def index() -> Component:
    return (
        html.DOCTYPE.html,
        html.html(
            html.head(
                html.title("My HTMY App"),
                html.Meta.charset(),
                html.Meta.viewport(),
                html.script(src="https://unpkg.com/htmx.org@2.0.2"),
            )
        ),
        html.body(
            html.h1("Message Board"),
            html.form(
                html.input_(
                    type="text", name="message", placeholder="Enter your message"
                ),
                html.button("Submit", type="submit"),
                hx_post="/submit",
                hx_target="#submit-response",
            ),
            html.div(id="submit-response"),
            html.h2("Messages"),
            html.div(hx_get="/messages", hx_trigger="every 1s"),
        ),
    )


@app.post("/submit", response_model=None)
@htmy.hx()
def submit(message: Annotated[str, Form()]) -> Component:
    messages.append(message)
    return html.div(f"Message submitted: {message}", id="submit-response")


@app.get("/messages", response_model=None)
@htmy.hx()
def get_messages() -> Component:
    return html.ul(*[html.li(msg) for msg in messages])
