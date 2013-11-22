# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import get_root

from kotti_multilingual.resources import LanguageRoot
from kotti_multilingual.views.content import LanguageRootView


def test_views(db_session, dummy_request):

    root = get_root()
    content = LanguageRoot()
    root['content'] = content

    view = LanguageRootView(root['content'], dummy_request)

    assert view.view() == {}


def test_forbid_unkown_language():
    import pytest
    from kotti_multilingual.views.content import LanguageRootSchema
    from colander import Invalid
    schema = LanguageRootSchema()
    with pytest.raises(Invalid):
        schema.deserialize(dict(language='dummy_lang', title='dummy_title'))
