from fasthtml.common import (
    FastHTML,
    StaticImmutable,
)
from routes.login import login_app
from starlette.routing import Mount

app = FastHTML(
    routes=[
        Mount("/static", StaticImmutable(directory="static"), name="static"),
        Mount("/login", login_app, name="login"),
    ],
)
