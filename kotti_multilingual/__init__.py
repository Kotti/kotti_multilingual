# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.resources import Document
from kotti.resources import File
from kotti.resources import Image
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_multilingual')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_multilingual'

    settings['kotti.available_types'] += \
        ' kotti_multilingual.resources.LanguageSection'

    Document.type_info.addable_to.append('LanguageSection')
    File.type_info.addable_to.append('LanguageSection')
    Image.type_info.addable_to.append('LanguageSection')


def includeme(config):

    config.add_translation_dirs('kotti_multilingual:locale')
    config.scan(__name__)
