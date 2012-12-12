from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_multilingual')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_multilingual'

    settings['kotti.available_types'] += ' kotti_multilingual.resources.Language'



def includeme(config):

    config.add_translation_dirs('kotti_multilingual:locale')
    config.scan(__name__)
