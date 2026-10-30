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

    token = request.cookies.get("session_token")
    is_authenticated = token is not None and harbor.verify_session(token)

    if is_authenticated:
        request.scope["user"] = harbor.get_current_user(token)

    if path.startswith("/auth") and path != "/auth/logout" and is_authenticated:
        return RedirectResponse("/", status_code=303)

    if not path.startswith(("/auth", "/static")) and not is_authenticated:
        response = RedirectResponse("/auth/", status_code=303)
        response.delete_cookie("session_token", path="/")
        return response

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
