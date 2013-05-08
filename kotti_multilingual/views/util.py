# -*- coding: utf-8 -*-

"""
Created on 2013-05-06
:author: Andreas Kaiser (disko)
"""

from logging import getLogger

from babel import Locale
from kotti.security import has_permission
from pyramid.events import BeforeRender
from pyramid.events import subscriber

from kotti_multilingual.resources import LanguageRoot


log = getLogger(__name__)


def language_roots(context, request):
    """
    Language roots that are visible for the user.

    :result: A sequence of dictionaries representing the language roots.
    :rtype: list of dict
    """

    selected_language = getattr(context, 'language', None)

    languages = []

    for l in LanguageRoot.query.all():
        if has_permission('view', l, request):
            languages.append({
                'id': l.language,
                'selected': l.language == selected_language,
                'title': Locale(l.language).get_display_name(l.language),
                'url': request.resource_url(l),
            })

    languages.sort(key=lambda l: l['title'])

    return languages


@subscriber(BeforeRender)
def add_renderer_globals(event):
    if event['renderer_name'] != 'json':
        request = event['request']
        roots = getattr(request, 'language_roots', None)
        if roots is None and request is not None:
            roots = language_roots(event['context'], event['request'])
        event['language_roots'] = roots
