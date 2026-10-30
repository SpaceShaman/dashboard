from core.types import User
from fasthtml.common import FT, Div, Header, Span
from fasthtml_basecoat import Button, ThemeSwitcher
from fasthtml_lucide import Icon


def DashboardNavbar(*, title: str, user: User) -> FT:
    return Header(
        Div(
            Button(
                Icon("panel-left"),
                type="button",
                variant="ghost",
                size="icon",
                aria_label="Toggle sidebar",
                aria_controls="dashboard-sidebar",
                onclick="document.getElementById('dashboard-sidebar').toggle()",
            ),
            Span(title, cls="truncate text-sm font-medium"),
            cls="flex min-w-0 items-center gap-3",
        ),
        Div(
            Span(
                user.username,
                cls="hidden max-w-48 truncate text-sm text-muted-foreground sm:block",
            ),
            Button(
                Icon("log-out"),
                Span("Logout", cls="hidden sm:inline"),
                type="button",
                variant="ghost",
                aria_label="Logout",
                hx_post="/auth/logout",
                hx_swap="none",
            ),
            ThemeSwitcher(variant="ghost"),
            cls="flex shrink-0 items-center gap-2 sm:gap-4",
        ),
        cls="sticky top-0 z-30 flex h-16 items-center justify-between gap-4 border-b bg-background px-4 md:px-6",
    )
