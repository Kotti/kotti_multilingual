# -*- coding: utf-8 -*-

"""
Created on 2013-05-06
:author: Andreas Kaiser (disko)
"""


def includeme(config):
    """
    Pyramid includme hook.  Don't use it directly but indirectly via the
    :func:`kotti_configure_template_overrides` hook.

    :param config: Pyramid config object
    :type config: :class:`pyramid.config.Configurator`
    """

    config.override_asset(
        to_override='kotti:templates/view/nav.pt',
        override_with='kotti_multilingual:templates/nav.pt')
