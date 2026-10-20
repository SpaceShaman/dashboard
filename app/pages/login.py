from components.ui import (
    H2,
    A,
    Button,
    Card,
    CardAction,
    Div,
    Footer,
    Form,
    Header,
    Input,
    Label,
    P,
    Section,
)
from fasthtml.common import fast_app
from layouts.base import Base

login_app, rt = fast_app()


@rt("/")
def get():
    return Base(
        Div(
            Card(
                Header(
                    H2("Login to your account"),
                    P("Enter your credentials to access your account."),
                    CardAction(
                        Button("Sign Up", data_variant="link"),
                    ),
                ),
                Section(
                    Form(
                        Div(
                            Label("Username", fr="username"),
                            Input(
                                id="username",
                                name="username",
                                required=True,
                            ),
                            cls="grid gap-2",
                        ),
                        Div(
                            Div(
                                Label("Password", fr="password"),
                                A(
                                    "Forgot your password?",
                                    href="#",
                                    cls="ms-auto inline-block text-sm underline-offset-4 hover:underline",
                                ),
                                cls="flex items-center",
                            ),
                            Input(
                                type="password",
                                id="password",
                                name="password",
                                required=True,
                            ),
                            cls="grid gap-2",
                        ),
                        cls="grid gap-6",
                    ),
                ),
                Footer(
                    Button("Login", cls="w-full"),
                ),
                cls="w-full max-w-sm",
            ),
            cls="min-h-dvh flex items-center justify-center p-4",
        ),
        title="Login Page",
    )
