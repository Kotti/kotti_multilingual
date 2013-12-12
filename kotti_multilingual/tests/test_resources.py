# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import get_root
from kotti.testing import DummyRequest

from kotti_multilingual.resources import LanguageRoot
from kotti_multilingual.resources import Translation


def test_LanguageRoot(db_session, config):
    config.include('kotti_multilingual')

    root = get_root()
    content = LanguageRoot()
    assert content.type_info.addable(root, DummyRequest()) is True
    root['content'] = content


def test_translation_deleted_by_trigger(db_session):
    lang1 = LanguageRoot(title='fr', name='name')
    lang2 = LanguageRoot(title='en', name='name')
    db_session.add_all([lang1, lang2])
    db_session.flush()
    trans = Translation(source_id=lang1.id, target_id=lang2.id)
    db_session.add(trans)
    db_session.flush()
    db_session.delete(lang1)
    db_session.flush()
    assert db_session.query(Translation).count() == 0
