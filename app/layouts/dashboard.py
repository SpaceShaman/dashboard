from components.dashboard.navbar import DashboardNavbar
from components.dashboard.sidebar import DashboardSidebar
from core.types import User
from fasthtml.common import (
    FT,
    Div,
    Main,
)

from .base import BaseLayout


def DashboardLayout(*c, title: str, user: User, active_path: str = "/", **kwargs) -> FT:
    return BaseLayout(
        DashboardSidebar(active_path=active_path),
        Div(
            DashboardNavbar(title=title, user=user),
            Main(
                Div(
                    *c,
                    cls="mx-auto w-full max-w-6xl space-y-6 px-4 py-8 md:px-8 md:py-10",
                ),
                id="dashboard-content",
                tabindex="-1",
                cls="min-w-0 flex-1",
            ),
            cls="flex min-h-dvh min-w-0 flex-col",
        ),
        title=title,
        **kwargs,
    )
