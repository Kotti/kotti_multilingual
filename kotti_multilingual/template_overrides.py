# -*- coding: utf-8 -*-

"""
Created on 2013-05-06
:author: Andreas Kaiser (disko)
"""


def includeme(config):

    config.override_asset(
        to_override='kotti:templates/view/nav.pt',
        override_with='kotti_multilingual:templates/nav.pt')
