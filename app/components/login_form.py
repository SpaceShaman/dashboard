from .ui import (
    FT,
    A,
    Button,
    Div,
    Form,
    Input,
    Label,
)


def LoginForm() -> FT:
    return Form(
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
        Button("Login", cls="w-full"),
        cls="grid gap-6",
        hx_post="/login",
        hx_swap="none",
    )
