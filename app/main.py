from fasthtml.common import fast_app, serve
from pages.login import login_app
from starlette.routing import Mount

app, rt = fast_app(routes=(Mount("/login", login_app, name="login"),))


serve()
