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
