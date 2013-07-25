# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import Content
from kotti.resources import Document
from kotti.resources import File
from kotti.resources import Image
from kotti.util import LinkRenderer
from pyramid.i18n import TranslationStringFactory
from sqlalchemy import event
from sqlalchemy.orm import mapper

_ = TranslationStringFactory('kotti_multilingual')


def kotti_configure(settings):
    """ Basic Kotti configurator.  Enables content types and locales.

    :param settings: Kotti settings dictionary
    :type settings: dict
    """
    from .sqla import attach_language_independent_fields

    settings['pyramid.includes'] += ' kotti_multilingual'

    settings['kotti.available_types'] += \
        ' kotti_multilingual.resources.LanguageRoot'

    Content.type_info.edit_links.append(
        LinkRenderer(
            name='translation-dropdown',
            predicate=lambda context, request: context.language is not None
        )
    )
    Document.type_info.addable_to.append('LanguageRoot')
    File.type_info.addable_to.append('LanguageRoot')
    Image.type_info.addable_to.append('LanguageRoot')

    File.type_info.language_independent_fields = ('data',)
    Image.type_info.language_independent_fields = ('data',)

    event.listen(
        mapper, 'mapper_configured', attach_language_independent_fields)


def includeme(config):
    """
    Pyramid includme hook.  Don't use it directly but indirectly via the
    :func:`kotti_configure` hook.

    :param config: Pyramid config object
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_multilingual:locale')
    config.scan(__name__)
