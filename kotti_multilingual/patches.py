from kotti.resources import Node
from pyramid.threadlocal import get_current_request
from sqlalchemy.orm import object_mapper

TRANSLATE_BLACKLIST = ['translation_targets', 'translation_source']


def copy(self, **kwargs):
    """ Fix problem with multilingual and copy&paste.

        If you paste objects after a copy action, the
        translation_targets and translation_source properties
        should be omitted from copy.
    """
    request = get_current_request()
    action = request.session.get('kotti.paste', (None, None))[1]
    if not action or action == 'copy':
        children = list(self.children)
        copy = self.__class__()
        for prop in object_mapper(self).iterate_properties:
            black_list = tuple(
                list(self.copy_properties_blacklist) +
                TRANSLATE_BLACKLIST
                )
            if prop.key not in black_list:
                setattr(copy, prop.key, getattr(self, prop.key))
        for key, value in kwargs.items():
            setattr(copy, key, value)
        for child in children:
            copy.children.append(child.copy())

        return copy
    else:
        return self.__original_copy(**kwargs)


Node.__original_copy = Node.copy
Node.copy = copy
