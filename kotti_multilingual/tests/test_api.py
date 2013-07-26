from kotti.resources import Document


def test_get_source(translated_docs, db_session):
    from kotti_multilingual.api import get_source

    source, target = translated_docs
    assert get_source(target) is source


def test_get_source_none(root, db_session):
    from kotti_multilingual.api import get_source

    assert get_source(root) is None


def test_get_translations(translated_docs, db_session):
    from kotti_multilingual.api import get_translations

    source, target = translated_docs
    assert get_translations(source) == {'sl': target}
    assert get_translations(target) == {'en': source}


def test_get_translations_alotta(translated_docs, root, db_session):
    from kotti_multilingual.api import get_translations
    from kotti_multilingual.api import link_translation
    from kotti_multilingual.resources import LanguageRoot

    source, target = translated_docs
    fr = root['fr'] = LanguageRoot(language=u'fr', title=u'Le root')
    fr['doc'] = Document(title=u'English doc')

    link_translation(source, fr['doc'])
    assert get_translations(fr['doc']) == {'en': source, 'sl': target}


def test_get_translations_none(root, db_session):
    from kotti_multilingual.api import get_translations

    assert get_translations(root) == {}


def test_link_translation(multilingual_doc, root, db_session):
    from kotti_multilingual.api import link_translation
    from kotti_multilingual.api import get_translations

    doc2 = root['sl']['doc2'] = Document(language=u'sl')
    link_translation(multilingual_doc, doc2)

    assert get_translations(multilingual_doc) == {'sl': doc2}


def test_unlink_translation(translated_docs, db_session):
    from kotti_multilingual.api import unlink_translation
    from kotti_multilingual.api import get_translations

    source, target = translated_docs
    unlink_translation(target)

    assert get_translations(source) == {}


def test_get_languages_no_language_root(root):
    from kotti_multilingual.api import get_languages

    assert get_languages() == []


def test_get_languages_no_request(root):
    from kotti_multilingual.api import get_languages
    from kotti_multilingual.resources import LanguageRoot

    root['de'] = LanguageRoot(language=u'de')

    assert get_languages() == [{'id': u'de', 'title': u'Deutsch'}]


def test_get_languages_request(root, dummy_request):
    from kotti_multilingual.api import get_languages
    from kotti_multilingual.resources import LanguageRoot

    root['de'] = LanguageRoot(language=u'de')

    assert get_languages(dummy_request) == [
        {'id': u'de', 'title': u'Deutsch', 'url': u'http://example.com/de/'}]


def test_get_languages_no_permissions(config, root, dummy_request):
    from kotti_multilingual.api import get_languages
    from kotti_multilingual.resources import LanguageRoot

    root['de'] = LanguageRoot(language=u'de')
    assert get_languages(dummy_request) == [
        {'id': u'de', 'title': u'Deutsch', 'url': u'http://example.com/de/'}]
    config.testing_securitypolicy(permissive=False)
    assert get_languages(dummy_request) == []


def test_get_languages_order(root, dummy_request):
    from kotti_multilingual.api import get_languages
    from kotti_multilingual.resources import LanguageRoot

    root['de'] = LanguageRoot(language=u'de')
    root['sl'] = LanguageRoot(language=u'sl')
    root['hu'] = LanguageRoot(language=u'hu')

    assert get_languages() == [
        {'id': u'de', 'title': u'Deutsch'},
        {'id': u'sl', 'title': u'sloven\u0161\u010dina'},
        {'id': u'hu', 'title': u'magyar'}
    ]

    de, sl, hu = root.values()
    root.children[:] = [sl, hu, de]

    assert get_languages() == [
        {'id': u'sl', 'title': u'sloven\u0161\u010dina'},
        {'id': u'hu', 'title': u'magyar'},
        {'id': u'de', 'title': u'Deutsch'}
    ]


def test_get_language_title(root):
    from kotti_multilingual.api import get_language_title

    assert get_language_title(u'en') == u'English'
