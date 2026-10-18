import asyncio
from typing import Annotated

from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse
from fasthx.htmy import HTMY
from htmy import Component, Renderer, html

app = FastAPI()
htmy = HTMY()
renderer = Renderer()

messages = []


@app.get("/")
@htmy.page()
async def index() -> Component:
    return (
        html.DOCTYPE.html,
        html.html(
            html.head(
                html.title("My HTMY App"),
                html.Meta.charset(),
                html.Meta.viewport(),
                html.script(src="https://unpkg.com/htmx.org@2.0.2"),
                html.script(src="https://unpkg.com/htmx-ext-sse@2.2.4/sse.js"),
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
            html.div(
                hx_ext="sse",
                sse_connect="/messages",
                sse_swap="message",
            ),
        ),
    )


@app.post("/submit", response_model=None)
@htmy.hx()
async def submit(message: Annotated[str, Form()]) -> Component:
    messages.append(message)
    return html.div(f"Message submitted: {message}", id="submit-response")


async def sse_messages():
    while True:
        content = await renderer.render(html.ul(*[html.li(msg) for msg in messages]))
        yield "data: " + content.replace("\n", "\ndata: ") + "\n\n"
        await asyncio.sleep(1)


@app.get("/messages")
async def get_messages() -> StreamingResponse:
    return StreamingResponse(sse_messages(), media_type="text/event-stream")
