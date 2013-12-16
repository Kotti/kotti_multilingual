# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""
from copy import copy

from kotti.interfaces import IDefaultWorkflow
from kotti.interfaces import INavigationRoot
from kotti.resources import Base
from kotti.resources import Document
from kotti.resources import TypeInfo
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from zope.interface import implements

from kotti_multilingual import _


class Translation(Base):
    """The translation table maps between translation sources and
    translation targets.
    """
    __table_args__ = (
        UniqueConstraint('source_id', 'target_id'),
        )
    id = Column(Integer(), primary_key=True)
    source_id = Column(ForeignKey('contents.id'))
    target_id = Column(ForeignKey('contents.id'))

    source = relationship(
        'Content',
        primaryjoin='Translation.source_id == Content.id',
        backref=backref(
            'translation_targets', cascade="all, delete, delete-orphan")
        )
    target = relationship(
        'Content',
        primaryjoin='Translation.target_id == Content.id',
        backref=backref(
            'translation_source', cascade="all, delete, delete-orphan")
        )

    def __repr__(self):
        return "<{0} from {1} to {2}".format(
            self.__class__.__name__, self.source, self.target)


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
    addable_to=copy(Document.type_info.addable_to),
    edit_links=copy(Document.type_info.edit_links),
    selectable_default_views=copy(Document.type_info.selectable_default_views)
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
