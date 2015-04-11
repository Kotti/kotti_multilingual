from sqlalchemy import or_
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.security import has_permission
from pyramid.exceptions import Forbidden

from kotti.resources import Node
from kotti.views.edit.actions import NodeActions as OriginalNodeActions
from kotti.util import title_to_name
from kotti.util import _
from kotti import DBSession

from kotti_multilingual.resources import Translation


@view_defaults(permission='edit')
class NodeActions(OriginalNodeActions):

    @view_config(name='paste')
    def paste_nodes(self):
        """
        Paste nodes view. Paste formerly copied or cutted nodes into the
        current context. Note that a cutted node can not be pasted into itself.

        :result: Redirect response to the referrer of the request.
        :rtype: pyramid.httpexceptions.HTTPFound

        kotti_multilingual override:
        If you paste objects after a cut action we want to
        clear all translations (prevent edge case problems)

        """

        def unlink_translation(content):
            content_id = content.id
            DBSession.query(Translation).filter(
                or_(
                    Translation.target_id == content_id,
                    Translation.source_id == content_id
                    )
                ).delete()

        ids, action = self.request.session['kotti.paste']
        for count, id in enumerate(ids):
            item = DBSession.query(Node).get(id)
            if item is not None:
                if action == 'cut':
                    if not has_permission('edit', item, self.request):
                        raise Forbidden()

                    # unlink translations for each child
                    children = self._all_children(item, permission='edit')
                    unlink_translation(item)
                    for child in children:
                        unlink_translation(child)

                    item.__parent__.children.remove(item)
                    item.name = title_to_name(item.name,
                                              blacklist=self.context.keys())
                    self.context.children.append(item)
                    if count is len(ids) - 1:
                        del self.request.session['kotti.paste']
                elif action == 'copy':
                    copy = item.copy()
                    name = copy.name
                    if not name:  # for root
                        name = copy.title
                    name = title_to_name(name, blacklist=self.context.keys())
                    copy.name = name
                    self.context.children.append(copy)
                self.flash(_(u'${title} was pasted.',
                             mapping=dict(title=item.title)), 'success')
            else:
                self.flash(_(u'Could not paste node. It no longer exists.'),
                           'error')
        if not self.request.is_xhr:
            return self.back()
