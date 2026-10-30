from fasthtml.common import FT, H2, Header, P, Section
from fasthtml_basecoat import Card, CardAction
from layouts.base import Base


def DashboardPage(user) -> FT:
    return Base(
        Card(
            Header(
                H2("Dashboard"),
                P("Welcome to the dashboard!"),
                CardAction(
                    # Add any actions you want here
                ),
            ),
            Section(
                P("This is the main content of the dashboard."),
            ),
            cls="w-full max-w-sm",
        ),
        cls="min-h-dvh flex items-center justify-center p-4",
        title="Dashboard Page",
        user=user,
    )
