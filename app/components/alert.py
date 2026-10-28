from fasthtml.common import H2, Div, Footer, Section
from fasthtml_basecoat import Alert, Button
from fasthtml_lucide import Icon


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
