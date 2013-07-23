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


def test_get_translations_none(root, db_session):
    from kotti_multilingual.api import get_translations

    assert get_translations(root) == {}
