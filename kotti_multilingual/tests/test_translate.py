def test_translation_dropdown_no_translations(root, dummy_request):
    from kotti_multilingual.views.translate import translation_dropdown

    assert translation_dropdown(root, dummy_request) == {
        'translations': [],
        'translatable_into': []
    }


def test_translation_dropdown_translations_exist(
        translated_docs, dummy_request):
    from kotti_multilingual.views.translate import translation_dropdown

    source, target = translated_docs

    assert translation_dropdown(source, dummy_request) == {
        'translations': [{
            'language': u'sl',
            'title': u'sloven\u0161\u010dina',
            'url': u'http://example.com/sl/translation/'
        }],
        'translatable_into': []
    }

    assert translation_dropdown(target, dummy_request) == {
        'translations': [{
            'language': u'en',
            'title': u'English',
            'url': u'http://example.com/en/doc/'
        }],
        'translatable_into': []
    }


def test_translation_dropdown_translatable_into(
        multilingual_doc, dummy_request):
    from kotti_multilingual.views.translate import translation_dropdown

    assert translation_dropdown(multilingual_doc, dummy_request) == {
        'translations': [],
        'translatable_into': [{
            'language': u'sl',
            'title': u'sloven\u0161\u010dina',
            'url': u'http://example.com/sl/add-translation?id=%s'
            % multilingual_doc.id,
        }]
    }
