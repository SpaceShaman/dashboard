from pathlib import Path

from fasthtml.common import FastHTML, serve
from pages.login import login_app
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

app = FastHTML(
    routes=(
        Mount("/static", StaticFiles(directory=Path(__file__).parent / "static")),
        Mount("/login", login_app, name="login"),
    ),
)
rt = app.route


serve()
