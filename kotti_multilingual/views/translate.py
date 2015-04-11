# -*- coding: utf-8 -*-

from kotti.interfaces import IContent
from kotti.resources import Content
from kotti.resources import DBSession
from pyramid.httpexceptions import HTTPFound
from pyramid.location import lineage
from pyramid.security import has_permission
from pyramid.view import view_config

from kotti_multilingual import api


@view_config(
    context=IContent,
    name='translation-dropdown',
    permission='edit',
    renderer='kotti_multilingual:templates/translation-dropdown.pt')
def translation_dropdown(context, request):
    languages = api.get_languages(request)
    translations = api.get_translations(context)
    translatable_into = []

    for lang in languages:
        if lang['id'] in translations or lang['id'] == context.language:
            continue
        translated_parent = find_parent(
            context.__parent__,
            lambda item: lang['id'] in api.get_translations(item))
        if translated_parent is None:
            continue
        container = api.get_translations(translated_parent).get(lang['id'])
        url = request.resource_url(
            container,
            'add-translation',
            query={'id': context.id}
        )

        if has_permission('add', container, request):
            translatable_into.append({
                'language': lang['id'],
                'title': lang['title'],
                'url': url
            })
    translations = [
        {
            'language': tr.language,
            'title': api.get_language_title(tr.language),
            'url': request.resource_url(tr),
        } for tr in translations.values()
    ]
    return {
        'translations': translations,
        'translatable_into': translatable_into
    }


@view_config(
    context=IContent,
    name='add-translation',
    permission='add')
def add_translation(context, request):
    """XXX: Check that we dont leak anything"""
    source_id = request.params['id']
    source = DBSession.query(Content).get(int(source_id))

    translation = context[source.__name__] = source.copy()
    api.link_translation(source, translation)
    return HTTPFound(location=request.resource_url(translation, 'edit'))


def find_parent(item, predicate):
    """XXX: move to kotti.utils"""
    for item in lineage(item):
        if predicate(item):
            return item
