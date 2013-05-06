# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import get_root

from kotti_multilingual.resources import LanguageSection
from kotti_multilingual.views import LanguageSectionView


def test_views(db_session, dummy_request):

    root = get_root()
    content = LanguageSection()
    root['content'] = content

    view = LanguageSectionView(root['content'], dummy_request)

    assert view.view() == {}
    assert view.alternative_view() == {}
