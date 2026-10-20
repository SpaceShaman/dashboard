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
        Card(
            Header(
                H2("Login to your account"),
                P("Enter your email below to login to your account"),
                CardAction(
                    Button("Sign Up", type="button", data_variant="link"),
                ),
            ),
            Section(
                Form(
                    Div(
                        Label("Email", fr="demo-card-email", cls="label"),
                        Input(
                            type="email",
                            id="demo-card-email",
                            name="email",
                            placeholder="m@example.com",
                            required=True,
                        ),
                        cls="grid gap-2",
                    ),
                    Div(
                        Div(
                            Label("Password", fr="demo-card-password", cls="label"),
                            A(
                                "Forgot your password?",
                                href="#",
                                cls="ms-auto inline-block text-sm underline-offset-4 hover:underline",
                            ),
                            cls="flex items-center",
                        ),
                        Input(
                            type="password",
                            id="demo-card-password",
                            name="password",
                            required=True,
                        ),
                        cls="grid gap-2",
                    ),
                    cls="grid gap-6",
                ),
            ),
            Footer(
                Button("Login", type="button", cls="btn w-full"),
                Button(
                    "Login with Google",
                    type="button",
                    cls="btn w-full",
                    data_variant="outline",
                ),
                cls="flex-col gap-2",
            ),
        ),
        title="Login Page",
    )
