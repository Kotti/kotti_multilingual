# -*- coding: utf-8 -*-

"""
Created on 2013-05-06
:author: Andreas Kaiser (disko)
"""

from logging import getLogger

from babel import Locale
from kotti.views.util import TemplateAPI as KottiTemplateAPI

from kotti_multilingual.resources import LanguageSection


log = getLogger(__name__)


class TemplateAPI(KottiTemplateAPI):

    @property
    def language_root(self):

        if not (hasattr(self.context, 'language') and self.context.language):
            return self.root

        return LanguageSection.query \
            .filter(LanguageSection.language == self.context.language) \
            .one()

    @property
    def language_sections(self):

        selected_language = getattr(self.context, 'language', None)

        languages = []

        for l in LanguageSection.query.all():
            if self.has_permission('view', l):
                languages.append({
                    'id': l.language,
                    'selected': l.language == selected_language,
                    'title': Locale(l.language).get_display_name(l.language),
                    'url': self.url(l),
                })

        languages.sort(key=lambda l: l['title'])

        return languages
