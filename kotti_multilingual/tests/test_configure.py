# -*- coding: utf-8 -*-

"""
Created on 2013-05-05
:author: Andreas Kaiser (disko)
"""

from pyramid.interfaces import ITranslationDirectories

from kotti_multilingual import includeme
from kotti_multilingual import kotti_configure


def test_kotti_configure():

    settings = {
        'kotti.available_types': '',
        'pyramid.includes': '',
    }

    kotti_configure(settings)

    assert settings['pyramid.includes'] == ' kotti_multilingual'
    assert settings['kotti.available_types'] == \
        ' kotti_multilingual.resources.LanguageRoot'


def test_includeme(config):

    includeme(config)

    utils = config.registry.__dict__['_utility_registrations']
    k = (ITranslationDirectories, u'')

    # test if the translation dir is registered
    assert k in utils
    assert utils[k][0][0].find('kotti_multilingual/locale') > 0
