from fasthtml.common import (
    H1,
    H2,
    Div,
    FastHTML,
    Footer,
    Form,
    Header,
    Main,
    P,
    Section,
    Span,
    StaticImmutable,
)
from fasthtml_basecoat import *
from fasthtml_tailwindcss import TailwindHead

app = FastHTML(
    hdrs=[
        TailwindHead(input=BasecoatInput("lyra"), watch=True),
        BasecoatJS(),
    ]
)
app.mount("/static", StaticImmutable(directory="static"), name="static")


@app.route("/")
def get():
    return Main(
        Header(
            Div(
                H1("Account settings", cls="text-3xl font-semibold tracking-tight"),
                P(
                    "Manage your profile, notifications, and subscription.",
                    cls="mt-2 text-muted-foreground",
                ),
            ),
            Badge(
                "Active account",
                variant="secondary",
                data_tooltip="Your account is active",
            ),
            cls="flex flex-wrap items-center justify-between gap-4",
        ),
        Div(
            Card(
                Header(
                    H2("Profile"),
                    P("Your public profile and contact details."),
                ),
                Section(
                    Form(
                        Field(
                            Label("Display name", fr="display-name"),
                            Input(
                                id="display-name",
                                name="display_name",
                                type="text",
                                value="John Doe",
                                autocomplete="nickname",
                                required=True,
                            ),
                        ),
                        Field(
                            Label("Email address", fr="email"),
                            Input(
                                id="email",
                                name="email",
                                type="email",
                                value="test@gmail.com",
                                autocomplete="email",
                                required=True,
                            ),
                        ),
                        Div(
                            Button("Save changes", type="submit"),
                            Button("Reset", type="reset", variant="outline"),
                            cls="flex flex-wrap gap-2",
                        ),
                        action="/",
                        method="get",
                        cls="space-y-5",
                    ),
                ),
            ),
            Card(
                Header(
                    H2("Notifications"),
                    P("Choose which updates you want to receive."),
                ),
                Section(
                    Field(
                        Div(
                            Label("Product updates", fr="product-updates"),
                            P(
                                "New features and improvements.",
                                cls="text-sm text-muted-foreground",
                            ),
                            cls="flex-1",
                        ),
                        Switch(id="product-updates", checked=True),
                        orientation="horizontal",
                    ),
                    Field(
                        Div(
                            Label("Security alerts", fr="security-alerts"),
                            P(
                                "Important changes to your account.",
                                cls="text-sm text-muted-foreground",
                            ),
                            cls="flex-1",
                        ),
                        Switch(id="security-alerts", checked=True),
                        orientation="horizontal",
                    ),
                    Field(
                        Div(
                            Label("Newsletter", fr="newsletter"),
                            P(
                                "Occasional tips and inspiration.",
                                cls="text-sm text-muted-foreground",
                            ),
                            cls="flex-1",
                        ),
                        Switch(id="newsletter"),
                        orientation="horizontal",
                    ),
                    cls="space-y-6",
                ),
                Footer(
                    P(
                        "Switches are interactive demo controls.",
                        cls="text-sm text-muted-foreground",
                    ),
                ),
            ),
            Card(
                Header(
                    H2("Your workspace"),
                    P("Storage usage and subscription details."),
                ),
                Section(
                    Div(
                        Span("Pro plan", cls="font-medium"),
                        Badge("Monthly", variant="outline"),
                        cls="flex items-center justify-between",
                    ),
                    Div(
                        P(
                            "68 GB of 100 GB used",
                            cls="mb-3 text-sm text-muted-foreground",
                        ),
                        Progress(
                            Span(style="width: 68%"),
                            aria_label="Storage usage",
                            aria_valuenow=68,
                            aria_valuemin=0,
                            aria_valuemax=100,
                        ),
                    ),
                    P(
                        "Your workspace has room for more projects.",
                        cls="text-sm text-muted-foreground",
                    ),
                    cls="space-y-6",
                ),
                Footer(
                    Button(
                        "Explore Basecoat",
                        tag="a",
                        href="https://basecoatui.com/",
                        target="_blank",
                        rel="noopener noreferrer",
                        variant="outline",
                        cls="w-full",
                        data_tooltip="Your account is active",
                    ),
                ),
            ),
            cls="grid items-start gap-6 lg:grid-cols-3",
        ),
        cls="mx-auto max-w-7xl space-y-8 px-6 py-12",
    )
