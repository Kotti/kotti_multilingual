# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import Document, get_root
from kotti.testing import DummyRequest

from kotti_multilingual.resources import LanguageRoot
from kotti_multilingual.resources import Translation


def test_LanguageRoot(db_session, config):
    config.include('kotti_multilingual')

    root = get_root()
    content = LanguageRoot()
    addable = content.type_info.addable(root, DummyRequest())
    if isinstance(addable, bool):
        assert content.type_info.addable(root, DummyRequest()) is True
    else:
        # Kotti 1.0.0-alpha.4
        assert bool(
            content.type_info.addable(root, DummyRequest()).boolval
            ) is True
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


def test_type_info_isolation():
    language_root_ti = LanguageRoot.type_info
    document_ti = Document.type_info
    for attr in LanguageRoot.type_info.__dict__:
        assert getattr(language_root_ti, attr) is not \
            getattr(document_ti, attr)
