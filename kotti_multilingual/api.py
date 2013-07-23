from kotti.resources import Content
from kotti.resources import DBSession
from .resources import Translation


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
