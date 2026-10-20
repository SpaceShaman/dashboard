from components.ui import FT, Button, Div, Script


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
            "Toggle theme",
            onclick="window.basecoat.theme.toggle()",
        ),
    )
