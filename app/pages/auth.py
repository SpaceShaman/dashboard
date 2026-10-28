from components.auth.forgot_password import ForgotPasswordCard
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
                        aria_controls="auth-login-card",
                        aria_selected="true",
                        tabindex="0",
                    ),
                    Button(
                        "Sign Up",
                        role="tab",
                        id="auth-register-tab",
                        aria_controls="auth-register-card",
                        aria_selected="false",
                        tabindex="-1",
                    ),
                    Button(
                        "Reset password",
                        role="tab",
                        id="auth-forgot-password-tab",
                        aria_controls="auth-forgot-password-card",
                        aria_selected="false",
                        tabindex="-1",
                        hidden=True,
                    ),
                    role="tablist",
                    aria_label="Account access",
                    cls="w-full",
                ),
                LoginCard(
                    role="tabpanel",
                    id="auth-login-card",
                    aria_labelledby="auth-login-tab",
                ),
                RegisterCard(
                    role="tabpanel",
                    id="auth-register-card",
                    aria_labelledby="auth-register-tab",
                    hidden=True,
                ),
                ForgotPasswordCard(
                    role="tabpanel",
                    id="auth-forgot-password-card",
                    aria_labelledby="auth-forgot-password-tab",
                    hidden=True,
                ),
                id="auth-tabs",
                cls="w-full max-w-sm",
            ),
            cls="min-h-dvh flex items-center justify-center p-4",
        ),
        title="Account access",
    )
