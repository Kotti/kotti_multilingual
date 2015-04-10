import colander
from kotti_multilingual.api import get_source


def i10n_widget_factory(widget_class, *args, **kwargs):
    """ Deferred widget. Turns field into readonly mode
        if the context is a translation.
    """
    @colander.deferred
    def deferred_widget(node, kw):
        widget = widget_class(*args, **kwargs)
        # We assume by default that we are on an edit form. So
        # if the context is a translation, it will be returned
        # in readonly mode.
        # If we are on an addform, the widget will be returned
        # as usual.
        addform = kw.get('addform', False)
        if not addform:
            # Edit form
            request = kw['request']
            context = request.context
            if get_source(context) is not None:
                # This is a translation, so let's switch to
                # readonly mode
                widget.readonly = True
        return widget
    return deferred_widget
