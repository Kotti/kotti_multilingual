# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from babel import UnknownLocaleError

from colander import Invalid
from colander import SchemaNode
from colander import String

from kotti.views.edit.content import DocumentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_multilingual import _
from kotti_multilingual.api import get_language_title
from kotti_multilingual.resources import LanguageRoot
from kotti_multilingual.views import BaseView


def available_language(node, value):
    """Checks that given language is available
    """
    try:
        get_language_title(value)
    except UnknownLocaleError:
        raise Invalid(node,
                      _(u"${lang} is not a valid language",
                        mapping={'lang': value}))


class LanguageRootSchema(DocumentSchema):
    """Schema for add / edit forms of LanguageRoot"""

    language = SchemaNode(
        String(),
        title=_(u'Language'),
        validator=available_language,
    )


@view_config(name=LanguageRoot.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class LanguageRootAddForm(AddFormView):

    schema_factory = LanguageRootSchema
    add = LanguageRoot
    item_type = _(u"Language Root")


@view_config(name='edit',
             context=LanguageRoot,
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class LanguageRootEditForm(EditFormView):

    schema_factory = LanguageRootSchema


@view_defaults(context=LanguageRoot, permission='view')
class LanguageRootView(BaseView):
    """View(s) for LanguageRoot"""

    @view_config(name='view',
                 renderer='kotti:templates/view/document.pt')
    def view(self):

        return {}
