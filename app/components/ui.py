from functools import partial

from fasthtml.common import *

Input = partial(Input, cls="input")
Button = partial(Button, cls="btn")
Card = partial(Div, cls="card")
CardAction = partial(Div, cls="card-action")
