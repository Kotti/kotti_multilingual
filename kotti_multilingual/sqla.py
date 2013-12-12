from kotti.resources import Content
from kotti.resources import DBSession
from sqlalchemy.orm.attributes import InstrumentedAttribute

from .api import get_source
from .resources import Translation


class SharedInstrumentedAttribute(InstrumentedAttribute):
    """Attached to attributes that are shared between translations.
    """

    def __set__(self, instance, value):
        """Refuse to set the attribute if we're a translation target.
        """
        if get_source(instance):
            raise TypeError(
                "Can't set %r attribute on translation." % self.key)

        return super(SharedInstrumentedAttribute, self).__set__(
            instance, value)

    def __get__(self, instance, owner):
        """If we're a translation target, look up the attribute in the
        translation source instead of here.
        """
        if instance is None:
            return self

        source = get_source(instance)
        if source is not None:
            return getattr(source, self.key)

        return super(SharedInstrumentedAttribute, self).__get__(
            instance, owner)


def attach_language_independent_fields(mapper, class_):
    """Put in place our :class:`TranslatedInstrumentedAttribute`.

    Controlled by class' `type_info.language_independent_fields` tuple.
    """
    if not issubclass(class_, Content):
        return
    language_independent_fields = getattr(
        class_.type_info, 'language_independent_fields', ())
    for attr in language_independent_fields:
        ia = getattr(class_, attr)
        ia.__class__ = SharedInstrumentedAttribute
