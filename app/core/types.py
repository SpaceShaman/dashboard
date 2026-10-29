from fasthtml.common import FT, HttpHeader, Response

type HTMLResult = FT | Response | tuple[FT | HttpHeader, ...]
