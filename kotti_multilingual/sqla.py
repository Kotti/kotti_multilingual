# -*- coding: utf-8 -*-

from kotti.resources import Content
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.ext.associationproxy import AssociationProxy

from kotti_multilingual.api import get_source


class SharedInstrumentedAttribute(InstrumentedAttribute):
    """Attached to attributes that are shared between translations.
    """

    def __set__(self, instance, value):
        """Refuse to set the attribute if we're a translation target.
        """
        if get_source(instance):
            # just don't save the field, experienced a random
            # type error on edit with data fields like files
            return
            # raise TypeError(
            #     "Can't set %r attribute on translation." % self.key)

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


class SharedAssociationProxy(AssociationProxy):

    def __get__(self, obj, class_):
        source = get_source(obj)
        if source is not None:
            if not self.scalar:
                return [getattr(item, self.value_attr) for item in
                        getattr(source, self.target_collection)]
            else:
                return getattr(
                    getattr(source, self.target_collection),
                    self.value_attr
                    )
        return super(SharedAssociationProxy, self).__get__(obj, class_)

    def __set__(self, obj, values):
        if get_source(obj):
            return
        return super(SharedAssociationProxy, self).__set__(obj, values)


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
        if isinstance(ia, AssociationProxy):
            ia.__class__ = SharedAssociationProxy
        elif isinstance(ia, InstrumentedAttribute):
            ia.__class__ = SharedInstrumentedAttribute
