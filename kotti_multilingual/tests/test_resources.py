from kotti.resources import get_root
from kotti.testing import DummyRequest

from kotti_multilingual.resources import Language


def test_language(db_session):

    root = get_root()
    content = Language()
    assert content.type_info.addable(root, DummyRequest()) is True
    root['content'] = content
