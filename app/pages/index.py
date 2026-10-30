from core.types import User
from fasthtml.common import FT, H1, H2, Header, P, Section
from layouts.dashboard import DashboardLayout


def IndexPage(user: User) -> FT:
    return DashboardLayout(
        Header(
            H1("Overview", cls="text-3xl font-semibold tracking-tight md:text-4xl"),
            P(
                f"Welcome back, {user.username}.",
                cls="text-muted-foreground",
            ),
            cls="space-y-2",
        ),
        *(
            Section(
                H2(heading, cls="text-2xl font-semibold tracking-tight"),
                P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                    "Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                    "laboris nisi ut aliquip ex ea commodo consequat."
                ),
                P(
                    "Duis aute irure dolor in reprehenderit in voluptate velit esse "
                    "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
                    "cupidatat non proident, sunt in culpa qui officia deserunt "
                    "mollit anim id est laborum."
                ),
                cls="space-y-4 leading-7",
            )
            for heading in (
                "Lorem ipsum dolor sit amet",
                "Consectetur adipiscing elit",
                "Sed do eiusmod tempor",
                "Ut enim ad minim veniam",
                "Duis aute irure dolor",
            )
        ),
        title="Dashboard",
        user=user,
    )
