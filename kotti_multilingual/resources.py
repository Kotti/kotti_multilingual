# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from kotti.interfaces import IDefaultWorkflow
from kotti.interfaces import INavigationRoot
from kotti.resources import Document
from kotti.resources import TypeInfo
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from zope.interface import implements

from kotti_multilingual import _


class LanguageRootTypeInfo(TypeInfo):
    """ LanguageRoot specific TypeInfo. """

    def addable(self, context, request):
        """
        In addition to the restrictions of
        :func:`kotti.resources.TypeInfo.addable`, a LanguageRoot must not be
        added within a parent that already has a language set.
        """

        if hasattr(context, 'language') and context.language:
            return False

        return super(LanguageRootTypeInfo, self).addable(context, request)

type_info = LanguageRootTypeInfo(
    name=u'LanguageRoot',
    title=_(u'Language root'),
    add_view=u'add_language_root',
    addable_to=Document.type_info.addable_to,
    edit_links=Document.type_info.edit_links,
    selectable_default_views=Document.type_info.selectable_default_views
)


class LanguageRoot(Document):
    """ Root for a language specific subtree. """

    implements(IDefaultWorkflow, INavigationRoot)

    id = Column(
        Integer(),
        ForeignKey('documents.id'),
        primary_key=True
    )

    type_info = type_info
