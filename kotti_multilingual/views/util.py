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
    """ TemplateAPI extensions for sites with multilingual content. """

    @property
    def language_root(self):
        """
        Root object for the current language's content subtree.  If used in a
        language neutral context, the site root will be returned.

        :result:
        :rtype: :class:`kotti_multilingual.resources.LanguageSection` or
                :class:`kotti.resources.Content` or descendant.
        """

        if not (hasattr(self.context, 'language') and self.context.language):
            return self.root

        return LanguageSection.query \
            .filter(LanguageSection.language == self.context.language) \
            .one()

    @property
    def language_sections(self):
        """
        Language sections that are visible for the user.

        :result: A sequence of dictionaries representing the language sections.
        :rtype: list of dict
        """

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
