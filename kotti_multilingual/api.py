# -*- coding: utf-8 -*-

from babel import Locale
from kotti.resources import Content
from kotti.resources import DBSession
from kotti.security import has_permission

from kotti_multilingual.resources import LanguageRoot
from kotti_multilingual.resources import Translation


def get_source(content):
    """Given a translation target, this returns the translation source
    or None.

    If ``content`` is the source, this returns ``None``.
    """
    with DBSession.no_autoflush:
        translation = DBSession.query(Translation).filter_by(
            target_id=content.id).first()
    if translation is not None:
        return translation.source


def get_translations(content):
    source = get_source(content)
    if source is None:
        source = content

    query = DBSession.query(Translation, Content).filter(
        Translation.source_id == source.id,
        Content.id == Translation.target_id,
        )
    res = dict((content.language, content) for translation, content in query)
    res.pop(content.language, None)
    if source is not content:
        res[source.language] = source

    return res


def link_translation(source, target):
    DBSession.add(Translation(source=source, target=target))


def unlink_translation(content):
    DBSession.query(Translation).filter_by(target_id=content.id).delete()


def get_languages(request=None):
    """
    Get a list of available languages.

    :param request: request object. If present, return also the url to the
        language root.

    :result: A sequence of dictionaries representing the languages.
    :rtype: list of dict
    """
    languages = []

    for l in LanguageRoot.query.order_by(LanguageRoot.position):
        if (request != None and not has_permission('view', l, request)):
            continue
        lang_root = {
            'id': l.language,
            'title': get_language_title(l.language),
        }
        if request != None:
            lang_root['url'] = request.resource_url(l)
        languages.append(lang_root)
    return languages


def get_language_title(language_code):
    return Locale(language_code).get_display_name(language_code)
