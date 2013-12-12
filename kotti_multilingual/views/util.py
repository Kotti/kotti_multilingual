# -*- coding: utf-8 -*-

"""
Created on 2013-05-06
:author: Andreas Kaiser (disko)
"""

from logging import getLogger
from pyramid.events import BeforeRender
from pyramid.events import subscriber

from kotti_multilingual.api import get_languages


log = getLogger(__name__)


@subscriber(BeforeRender)
def add_renderer_globals(event):
    if event['renderer_name'] != 'json':
        request = event['request']
        event['languages'] = get_languages(request=request)
