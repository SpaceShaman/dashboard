from components.ui import FT, Button, Div, Icon, Script


def ToggleThemeButton() -> FT:
    return Div(
        Script("""
            const mode = localStorage.getItem("themeMode") || "dark";
            document.documentElement.classList.toggle(
                "dark",
                mode === "dark"
            );
        """),
        Button(
            Icon(
                name="sun",
                cls="hidden dark:block",
            ),
            Icon(
                name="moon",
                cls="block dark:hidden",
            ),
            type="button",
            aria_label="Toggle dark mode",
            data_tooltip="Toggle dark mode",
            data_side="bottom",
            onclick="window.basecoat.theme.toggle()",
            cls="btn size-8",
            data_variant="outline",
            data_size="icon",
        ),
    )
