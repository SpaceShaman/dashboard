from .ui import H2, Button, Div, Footer, Icon, Section


def Alert(heading: str, message: str, variant: str = "destructive"):
    return Div(
        Div(
            Icon("info"),
            H2(heading),
            Section(message),
            Footer(
                Button(
                    Icon("circle-x"),
                    aria_label="Close",
                    data_tooltip="Close",
                    data_side="bottom",
                    data_variant="ghost",
                    onclick="this.closest('.alert').remove()",
                ),
            ),
            cls="alert w-full max-w-md",
            data_variant=variant,
            hx_on__load="setTimeout(() => { this.remove() }, 5000)",
        ),
        hx_swap_oob="beforeend:#alerts",
    )
