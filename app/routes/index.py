from core.types import HTMLResult
from fasthtml.common import fast_app
from pages.index import IndexPage

index_app, rt = fast_app()


@rt
def index(request) -> HTMLResult:
    return IndexPage(user=request.scope.get("user"))
