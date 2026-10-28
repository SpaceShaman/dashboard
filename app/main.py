from core.harbor import harbor
from fasthtml.common import (
    FastHTML,
    StaticImmutable,
)
from routes.auth import auth_app
from routes.dashboard import dashboard_app
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from starlette.routing import Mount


async def check_session(request, call_next):
    path = request.url.path

    if path.startswith(("/auth", "/static")):
        return await call_next(request)

    token = request.cookies.get("session_token")

    if not token or not harbor.verify_session(token):
        return RedirectResponse("/auth/", status_code=303)

    return await call_next(request)


app = FastHTML(
    middleware=[
        Middleware(BaseHTTPMiddleware, dispatch=check_session),
    ],
    routes=[
        Mount("/static", StaticImmutable(directory="static"), name="static"),
        Mount("/auth", auth_app, name="auth"),
        Mount("/", dashboard_app, name="dashboard"),
    ],
)
