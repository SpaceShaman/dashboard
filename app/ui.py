from functools import partial

from fasthtml.common import Button, Input

Input = partial(Input, cls="input")
Button = partial(Button, cls="btn")
