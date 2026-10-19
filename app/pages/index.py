from layouts.main import Page
from ludic.html import (
    b,
    button,
    div,
    form,
    h1,
    input,
    p,
    span,
)


def index_page() -> Page:
    return Page(
        div(
            h1("My Homepage"),
            p("Hello ", b("World!")),
            id="container",
        ),
        div(
            form(
                input(type="text", name="message", placeholder="Enter a message"),
                button("Send", type="submit", class_="btn"),
                hx_post="/message",
                hx_target="#container",
            ),
            span(
                "This is a simple example of a Ludic page with HTMX integration.",
                class_="font-medium text-sky-300",
            ),
        ),
    )
