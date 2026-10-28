from fasthtml.common import FT, fast_app
from pages.dashboard import DashboardPage

dashboard_app, rt = fast_app()


@rt
def index() -> FT:
    return DashboardPage()
