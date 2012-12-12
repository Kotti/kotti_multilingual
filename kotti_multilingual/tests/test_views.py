from kotti.resources import get_root

from kotti_multilingual.resources import Language
from kotti_multilingual.views import LanguageView


def test_views(db_session, dummy_request):

    root = get_root()
    content = Language()
    root['content'] = content

    view = LanguageView(root['content'], dummy_request)

    assert view.view() == {}
    assert view.alternative_view() == {}
