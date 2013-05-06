# -*- coding: utf-8 -*-

"""
Created on 2013-05-06
:author: Andreas Kaiser (disko)
"""

from kotti.events import ObjectInsert
from kotti.events import ObjectUpdate
from kotti.events import subscribe
from pyramid.events import ContextFound
from pyramid.events import subscriber


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


@subscribe(ObjectInsert)
@subscribe(ObjectUpdate)
def set_language_of_parent(event):

    context = event.object

    if hasattr(context, 'language') and hasattr(context, 'parent') and \
            hasattr(context.parent, 'language') and hasattr(context, 'type') \
            and context.type != 'language_section':

        context.language = context.parent.language
