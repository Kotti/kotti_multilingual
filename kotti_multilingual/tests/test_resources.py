# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import get_root
from kotti.testing import DummyRequest

from kotti_multilingual.resources import LanguageSection


def test_languagesection(db_session, config):
    config.include('kotti_multilingual')

    root = get_root()
    content = LanguageSection()
    assert content.type_info.addable(root, DummyRequest()) is True
    root['content'] = content
