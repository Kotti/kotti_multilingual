# -*- coding: utf-8 -*-

"""
Created on 2015-03-12
:author: Davide Moro (davidemoro)
"""
from pytest import fixture


@fixture
def mock_context():
    import mock
    context = mock.Mock()
    context.language = 'en'
    context.type_info = mock.Mock()
    return context


@fixture
def mock_request():
    import mock
    request = mock.Mock()
    request.registry = mock.Mock()
    request.registry.settings = {'kotti_multilingual.blacklist': 'Document'}
    return request


def test_predicate_action_true(mock_context, mock_request):
    from kotti_multilingual import translation_predicate
    mock_context.type_info.name = 'MyType'
    assert translation_predicate(mock_context, mock_request) is True


def test_predicate_action_false(mock_context, mock_request):
    from kotti_multilingual import translation_predicate
    mock_context.type_info.name = 'Document'
    assert translation_predicate(mock_context, mock_request) is False


def test_predicate_action_no_blacklist(mock_context, mock_request):
    from kotti_multilingual import translation_predicate
    mock_context.type_info.name = 'Document'
    del mock_request.registry.settings['kotti_multilingual.blacklist']
    assert translation_predicate(mock_context, mock_request) is True
