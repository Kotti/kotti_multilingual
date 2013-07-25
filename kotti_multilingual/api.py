from babel import Locale
from kotti.resources import Content
from kotti.resources import DBSession
from kotti_multilingual.resources import LanguageRoot
from kotti_multilingual.resources import Translation
from kotti.security import has_permission


def get_source(content):
    translation = DBSession.query(Translation).filter_by(
        target_id=content.id).first()
    if translation is not None:
        return translation.source


def get_translations(content):
    query = DBSession.query(Translation, Content).filter(
        Translation.source_id == content.id,
        Content.id == Translation.target_id,
        )
    return dict((content.language, content) for translation, content in query)


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
            'title': Locale(l.language).get_display_name(l.language),
        }
        if request != None:
            lang_root['url'] = request.resource_url(l)
        languages.append(lang_root)
    return languages
