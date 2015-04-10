# -*- coding: utf-8 -*-

"""
Created on 2013-05-06
:author: Andreas Kaiser (disko)
"""

from kotti.events import ObjectInsert
from kotti.events import ObjectUpdate
from kotti.events import subscribe
from kotti.resources import DBSession
from pyramid.events import ContextFound
from pyramid.events import subscriber
from pyramid.httpexceptions import HTTPForbidden

from kotti_multilingual import api
from kotti_multilingual.resources import LanguageRoot


@subscriber(ContextFound)
def set_context_locale(event):
    """ Set the request's locale from the context's language (if that exists).

    :param event: ``ContextFound`` event
    :type event: :class:`pyramid.events.ContextFound`
    """

    request = event.request
    context = request.context

    # If the context has a non empty language attribute: use it.
    if hasattr(context, 'language') and context.language:
        request._LOCALE_ = context.language


def _set_language_to_same_as_parent(context, recurse=True):
    """
    Set context's language to that of context's parent.  No checks are
    performed at all.

    :param context: Node of which the language is to be changed.
    :type context: :class:`kotti.resources.Content`

    :param recurse: If ``True`` also set the language of all children.  This is
                    required e.g. for cut and paste operations.
    :type recurse: bool
    """

    if context.type == 'language_root':
        # LanguageRoot instances must not be within another LanguageRoot
        if context.parent.language is not None:
            raise HTTPForbidden
    else:
        # LanguageRoot instances' language must not be set to None.
        context.language = context.parent.language

    if recurse:
        for c in context.children:
            _set_language_to_same_as_parent(c)


@subscribe(ObjectInsert)
@subscribe(ObjectUpdate)
def update_language(event):
    """ Update the language (if necessary).

    :param event: Event that needs attention w.r.t. the related object's
                  language.
    :type event: :class:`kotti.events.ObjectEvent`
    """

    context = event.object
    if hasattr(context, 'language') and hasattr(context, 'parent') and \
            hasattr(context.parent, 'language') and hasattr(context, 'type') \
            and (context.type != 'language_root') and \
            (context.language != context.parent.language):

        _set_language_to_same_as_parent(context)


@subscribe(ObjectInsert, LanguageRoot)
def autolink_language_root(event):
    context = event.object

    lr = DBSession.query(LanguageRoot).first()
    if lr is None:
        return

    source = api.get_source(lr)
    if source is None:
        source = lr

    api.link_translation(source, context)
