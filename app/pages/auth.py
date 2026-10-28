from components.auth.login import LoginCard
from components.auth.register import RegisterCard
from fasthtml.common import FT, Button, Div, Nav
from fasthtml_basecoat import Tabs
from layouts.base import Base


def AuthPage() -> FT:
    return Base(
        Div(
            Tabs(
                Nav(
                    Button(
                        "Login",
                        role="tab",
                        id="auth-login-tab",
                        aria_controls="auth-login-panel",
                        aria_selected="true",
                        tabindex="0",
                    ),
                    Button(
                        "Sign Up",
                        role="tab",
                        id="auth-register-tab",
                        aria_controls="auth-register-panel",
                        aria_selected="false",
                        tabindex="-1",
                    ),
                    role="tablist",
                    aria_orientation="horizontal",
                    aria_label="Account access",
                    cls="w-full",
                ),
                LoginCard(
                    role="tabpanel",
                    id="auth-login-panel",
                    aria_labelledby="auth-login-tab",
                    aria_selected="true",
                    tabindex="-1",
                ),
                RegisterCard(
                    role="tabpanel",
                    id="auth-register-panel",
                    aria_labelledby="auth-register-tab",
                    aria_selected="false",
                    tabindex="-1",
                    hidden=True,
                ),
                id="auth-tabs",
                cls="w-full max-w-sm",
            ),
            cls="min-h-dvh flex items-center justify-center p-4",
        ),
        title="Login or Sign Up",
    )
