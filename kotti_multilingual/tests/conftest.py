# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import Document
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


@fixture
def multilingual_doc(request, config, root):
    from kotti_multilingual.sqla import attach_language_independent_fields

    config.include('kotti_multilingual')
    Document.type_info.language_independent_fields = ('body',)
    attach_language_independent_fields(None, Document)

    def fin():
        detach_language_independent_fields(Document)
        del Document.type_info.language_independent_fields

    request.addfinalizer(fin)
    return root


@fixture
def translated_docs(multilingual_doc, db_session):
    from kotti_multilingual.resources import Translation

    translation = multilingual_doc['translation'] = Document(language=u'sl')
    db_session.add(Translation(source=multilingual_doc, target=translation))

    db_session.flush()  # o_O
    return multilingual_doc, translation
