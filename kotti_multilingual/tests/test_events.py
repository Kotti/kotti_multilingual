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

    request = DummyRequest(context=DummyResource(language='en'))
    set_context_locale(DummyEvent(request))
    assert request._LOCALE_ == 'en'
