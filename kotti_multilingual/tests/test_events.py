# -*- coding: utf-8 -*-

"""
Created on 2013-05-07
:author: Andreas Kaiser (disko)
"""

from pyramid.testing import DummyRequest
from pyramid.testing import DummyResource
from pytest import raises


class DummyEvent(object):
    def __init__(self, request):
        self.request = request


def test_set_context_locale():

    from kotti_multilingual.events import set_context_locale

    request = DummyRequest(context=DummyResource())
    set_context_locale(DummyEvent(request))
    with raises(AttributeError):
        request._LOCALE_

    request = DummyRequest(context=DummyResource(language=None))
    with raises(AttributeError):
        set_context_locale(DummyEvent(request))
        request._LOCALE_

    request = DummyRequest(context=DummyResource(language=u'en'))
    set_context_locale(DummyEvent(request))
    assert request._LOCALE_ == 'en'


# broken test, see comment
# def test_language_root_autolink(root, ml_events, config, db_session):
#     from kotti_multilingual.resources import LanguageRoot
#     from kotti_multilingual.api import get_source
#     from kotti_multilingual.api import get_translations
#
#     root['sl'] = LanguageRoot(language=u'sl')
#     db_session.flush()
#     root['en'] = LanguageRoot(language=u'en')
#     db_session.flush()   # integrity error here (probaly the event is
#                          # fired two times and I wasn't able to
#                          # prevent the integrity error.
#
#     assert get_translations(root['sl']) == {'en': root['en']}
#     assert get_source(root['en']) == root['sl']
#
#     # Add another language root.  This one should also connect to 'sl'
#     # automatically.
#     root['de'] = LanguageRoot(language=u'de')
#
#     assert get_source(root['de']) == root['sl']
#     assert get_translations(root['de']) == {'en': root['en'], 'sl': root['sl']}
