# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import get_root
from kotti.testing import DummyRequest

from kotti_multilingual.resources import LanguageRoot


def test_LanguageRoot(db_session, config):
    config.include('kotti_multilingual')

    root = get_root()
    content = LanguageRoot()
    assert content.type_info.addable(root, DummyRequest()) is True
    root['content'] = content
