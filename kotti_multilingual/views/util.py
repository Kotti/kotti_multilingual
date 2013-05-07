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

from kotti_multilingual.resources import LanguageSection


log = getLogger(__name__)


def language_sections(context, request):
    """
    Language sections that are visible for the user.

    :result: A sequence of dictionaries representing the language sections.
    :rtype: list of dict
    """

    selected_language = getattr(context, 'language', None)

    languages = []

    for l in LanguageSection.query.all():
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
        sections = getattr(request, 'language_sections', None)
        if sections is None and request is not None:
            sections = language_sections(event['context'], event['request'])
        event['language_sections'] = sections
