from .ui import H2, Div, Section


def Alert(heading: str, message: str, variant: str = "destructive"):
    return Div(
        Div(
            H2(heading),
            Section(message),
            cls="alert w-full max-w-md",
            data_variant=variant,
        ),
        hx_swap_oob="beforeend:#alerts",
    )
