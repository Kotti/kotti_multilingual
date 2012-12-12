# -*- coding: utf-8 -*-

from colander import SchemaNode
from colander import String
from kotti.views.edit.content import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_multilingual import _
from kotti_multilingual.resources import Language
from kotti_multilingual.fanstatic import kotti_multilingual


class LanguageSchema(ContentSchema):
    """Schema for add / edit forms of Language"""

    example_attribute = SchemaNode(
        String(),
        title=_(u'Example Attribute'),
        missing=u"",
    )


@view_config(name=Language.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class LanguageAddForm(AddFormView):

    schema_factory = LanguageSchema
    add = Language
    item_type = _(u"Language")


@view_config(name='edit',
             context=Language,
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class LanguageEditForm(EditFormView):

    schema_factory = LanguageSchema


@view_defaults(context=Language, permission='view')
class LanguageView(object):
    """View(s) for Language"""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name='view',
                 renderer='kotti_multilingual:templates/language.pt')
    def view(self):

        kotti_multilingual.need()

        return {}

    @view_config(name='alternative-view',
                 renderer='kotti_multilingual:templates/language-alternative.pt')
    def alternative_view(self):

        return {}
