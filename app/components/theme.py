from components.ui import FT, Button, Div, Icon, Script


def ToggleThemeButton() -> FT:
    return Div(
        Button(
            Icon(
                "sun",
                cls="hidden dark:block",
            ),
            Icon(
                "moon",
                cls="block dark:hidden",
            ),
            aria_label="Toggle dark mode",
            data_tooltip="Toggle dark mode",
            data_side="bottom",
            data_align="end",
            onclick="window.basecoat.theme.toggle()",
            data_variant="ghost",
        ),
    )


def LoadThemeScript() -> FT:
    return Script(
        """
        const mode = localStorage.getItem("themeMode") || "dark";
        document.documentElement.classList.toggle(
            "dark",
            mode === "dark"
        );
        """,
    )
