# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from babel import Locale
from kotti.interfaces import IContent
from kotti.views.util import is_root
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_multilingual.views import BaseView
from kotti_multilingual.resources import LanguageSection


@view_defaults(context=IContent, permission='view',
               custom_predicates=(is_root, ))
class LanguageSelectionViews(BaseView):
    """View(s) for LanguageSection"""

    @view_config(name='view',
                 renderer='kotti_multilingual:templates/language-selection.pt')
    def view(self):

        languages = []
        for l in LanguageSection.query.all():
            languages.append({
                'id': l.language,
                'title': Locale(l.language).get_display_name(l.language),
                'url': self.request.resource_url(l),
            })

        languages.sort(key=lambda l: l['title'])

        return {
            'languages': languages,
        }
