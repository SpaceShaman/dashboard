from contextlib import suppress

from core.harbor import harbor
from fasthtml.common import (
    FastHTML,
    StaticImmutable,
)
from routes.auth import auth_app
from routes.index import index_app
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from starlette.routing import Mount
from userharbor.exceptions import UserHarborError


async def check_session(request, call_next):
    path = request.url.path
    user = None

    if token := request.cookies.get("session_token"):
        with suppress(UserHarborError):
            user = harbor.get_current_user(token)

    request.scope["user"] = user

    if user and path.startswith("/auth") and path != "/auth/logout":
        return RedirectResponse("/", status_code=303)

    if not user and not path.startswith(("/auth", "/static")):
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
        Mount("/", index_app, name="index"),
    ],
)
