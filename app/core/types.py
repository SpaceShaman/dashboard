from fasthtml.common import FT, HttpHeader, Response
from userharbor.interfaces import UserLike

type HTMLResult = FT | Response | tuple[FT | HttpHeader, ...]


class User(UserLike): ...
