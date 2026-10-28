from typing import Literal

from fasthtml.common import FT, H2, Div, Footer, Section
from fasthtml_basecoat import Button
from fasthtml_lucide import Icon


def Alert(heading: str, message: str, variant: Literal["info", "error"]) -> FT:
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
            data_variant="destructive" if variant == "error" else None,
            hx_on__load="setTimeout(() => { this.remove() }, 10000)",
        ),
        hx_swap_oob="beforeend:#alerts",
    )
