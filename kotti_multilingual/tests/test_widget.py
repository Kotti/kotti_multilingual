import pytest
import mock


@pytest.mark.parametrize("source, addform, readonly",
                         [(None, False, False),
                          (mock.Mock(), False, True),
                          (None, True, False),
                          (mock.Mock(), True, False),
                          ])
def test_edit_i10n_widget_factory(source, addform, readonly):
    from kotti_multilingual.widget import i10n_widget_factory
    from deform.widget import SelectWidget

    deferred = i10n_widget_factory(SelectWidget, values=[])
    kw = mock.MagicMock()
    diz = dict(request=mock.Mock(), addform=addform)

    def side_effect(key, default=None):
        return diz.get(key, default)
    kw.__getitem__.side_effect = lambda x: diz[x]
    kw.get.side_effect = side_effect
    with mock.patch('kotti_multilingual.widget.get_source') as get_source:
        get_source.return_value = source
        assert deferred(mock.Mock(), kw).readonly is readonly
