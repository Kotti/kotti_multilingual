# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import Document
from kotti_multilingual import api
from pytest import fixture
from sqlalchemy.orm.attributes import InstrumentedAttribute

# See http://kotti.readthedocs.org/en/latest/developing/testing.html

pytest_plugins = "kotti"


def detach_language_independent_fields(class_):
    language_independent_fields = getattr(
        class_.type_info, 'language_independent_fields', ())
    for attr in language_independent_fields:
        ia = getattr(class_, attr)
        ia.__class__ = InstrumentedAttribute


@fixture(scope='function')
def ml_events(config, events):
    config.include('kotti_multilingual')


@fixture
def multilingual_doc(request, config, root, db_session, ml_events):
    from kotti_multilingual.resources import LanguageRoot
    from kotti_multilingual.resources import Translation
    from kotti_multilingual.sqla import attach_language_independent_fields

    Document.type_info.language_independent_fields = ('body',)
    attach_language_independent_fields(None, Document)
    en = root['en'] = LanguageRoot(language=u'en', title=u'English root')
    sl = root['sl'] = LanguageRoot(language=u'sl', title=u'Slovenian root')
    db_session.add(Translation(source=en, target=sl))
    en['doc'] = Document(title=u'English doc')

    def fin():
        detach_language_independent_fields(Document)
        del Document.type_info.language_independent_fields

    request.addfinalizer(fin)
    return en['doc']


@fixture
def translated_docs(multilingual_doc, db_session, root, events):
    from kotti_multilingual.resources import Translation

    sl = root['sl']
    doc = sl['translation'] = Document(title=u'Slovenian translation')
    db_session.add(Translation(source=multilingual_doc, target=doc))

    db_session.flush()  # o_O
    return multilingual_doc, doc
