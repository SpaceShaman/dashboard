from core.types import HTMLResult
from fasthtml.common import fast_app
from pages.dashboard import DashboardPage

dashboard_app, rt = fast_app()


@rt
def index() -> HTMLResult:
    return DashboardPage()
