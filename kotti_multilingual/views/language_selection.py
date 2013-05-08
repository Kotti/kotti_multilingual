# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.interfaces import IContent
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_multilingual.views import BaseView


@view_defaults(context=IContent, permission='view', )
class LanguageSelectionViews(BaseView):
    """View(s) for LanguageRoot"""

    @view_config(name='language-selection',
                 renderer='kotti_multilingual:templates/language-selection.pt')
    def view(self):

        return {}
