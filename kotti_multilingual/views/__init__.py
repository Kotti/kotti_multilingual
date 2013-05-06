# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""


class BaseView(object):
    """Base for view classes."""

    def __init__(self, context, request):
        """ Constructor

        :param context: Context on which the view is called.
        :type context: arbitrary, but usually :class:`kotti.resources.Content`

        :param request: Current request.
        :type request: :class:`pyramid.request.Request`
        """

        self.context = context
        self.request = request
