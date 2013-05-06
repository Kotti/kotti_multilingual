# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.interfaces import IContent
from kotti.views.util import is_root
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_multilingual.views import BaseView


@view_defaults(context=IContent, permission='view',
               custom_predicates=(is_root, ))
class LanguageSelectionViews(BaseView):
    """View(s) for LanguageSection"""

    @view_config(name='view',
                 renderer='kotti_multilingual:templates/language-selection.pt')
    def view(self):

        return {}
