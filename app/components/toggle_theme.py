from components.ui import FT, Button, Div, Script, Span
from fasthtml.svg import Circle, Svg, ft_svg


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
            Span(
                Svg(
                    Circle(r=4, cx=12, cy=12),
                    *(
                        ft_svg("path", d=d)
                        for d in (
                            "M12 2v2",
                            "M12 20v2",
                            "m4.93 4.93 1.41 1.41",
                            "m17.66 17.66 1.41 1.41",
                            "M2 12h2",
                            "M20 12h2",
                            "m6.34 17.66-1.41 1.41",
                            "m19.07 4.93-1.41 1.41",
                        )
                    ),
                    cls="lucide lucide-sun",
                    width=24,
                    height=24,
                    viewBox="0 0 24 24",
                    fill="none",
                    stroke="currentColor",
                    stroke_width=2,
                    stroke_linecap="round",
                    stroke_linejoin="round",
                ),
                cls="hidden dark:block",
            ),
            Span(
                Svg(
                    ft_svg(
                        "path",
                        d="M20.985 12.486a9 9 0 1 1-9.473-9.472c.405-.022.617.46.402.803a6 6 0 0 0 8.268 8.268c.344-.215.825-.004.803.401",
                    ),
                    cls="lucide lucide-moon",
                    width=24,
                    height=24,
                    viewBox="0 0 24 24",
                    fill="none",
                    stroke="currentColor",
                    stroke_width=2,
                    stroke_linecap="round",
                    stroke_linejoin="round",
                ),
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
