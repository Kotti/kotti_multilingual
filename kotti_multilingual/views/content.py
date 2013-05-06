# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from colander import SchemaNode
from colander import String
from kotti.views.edit.content import DocumentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_multilingual import _
from kotti_multilingual.resources import LanguageSection
from kotti_multilingual.views import BaseView


class LanguageSectionSchema(DocumentSchema):
    """Schema for add / edit forms of LanguageSection"""

    language = SchemaNode(
        String(),
        title=_(u'Language'),
    )


@view_config(name=LanguageSection.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class LanguageSectionAddForm(AddFormView):

    schema_factory = LanguageSectionSchema
    add = LanguageSection
    item_type = _(u"LanguageSection")


@view_config(name='edit',
             context=LanguageSection,
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class LanguageSectionEditForm(EditFormView):

    schema_factory = LanguageSectionSchema


@view_defaults(context=LanguageSection, permission='view')
class LanguageSectionView(BaseView):
    """View(s) for LanguageSection"""

    @view_config(name='view',
                 renderer='kotti:templates/view/document.pt')
    def view(self):

        return {}
