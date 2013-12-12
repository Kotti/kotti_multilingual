def test_set_attribute_no_translation(multilingual_doc):
    multilingual_doc.title = u"Bar"
    assert multilingual_doc.title == u"Bar"


def test_set_attribute(translated_docs):
    source, target = translated_docs

    source.title = u"My title"
    source.body = u"My body"

    assert source.title == u"My title"
    assert source.body == u"My body"
    assert target.title != u"My title"
    assert target.body == u"My body"
