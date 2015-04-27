Changelog
=========

0.2a3 (2015-04-27)
------------------

- Fixed 0.2a2 version (still wrong MANIFEST.in)

0.2a2 (2015-04-27)
------------------

- Fixed MANIFEST.in file

0.2a1 (2015-04-27)
------------------

- Maintain translation links between content items, with translation source
  and targets.

- Add a translation dropdown UI for adding a translation of an item.

- Added ``widget.i10n_widget_factory`` deferred widget.
  Turns field into readonly mode if the context is a translation.

  This deferred widget is also compatible with add forms, you should bind an ``addform``
  property to ``True`` and the widget will be rendered as usual in edit mode.
  You can do that adding a ``get_bind_data`` method on your add form.

- Added a ``kotti_multilingual.blacklist`` setting with a list of type names
  not translatable

- Changed policy for translate action. Now the translated document is automatically
  filled with the parent translation (enhanced usability since we don't have the screen
  splitted in two parts like LinguaPlone). This is possible thanks to a change in 
  sqla.py since we don't set language independent attributes on translated documents

- Fixed translation of objects with not nullable fields

- Added support for sqlalchemy's association_proxy

- Fixed intermittent problem with get_source (integrity error)

0.1a3 - 2013-05-08
------------------

- Rename ``LanguageSection`` to ``LanguageRoot`` to better fit Kotti's
  ``INavigationRoot``.  This implies a change in the DB schema for which no
  automatic schema migration is available; you'll have to rename the table
  ``language_sections`` to ``language_roots`` yourself.

- Add some tests.

0.1a2 - 2013-05-07
------------------

- Removed a lot of code that's now replaced by Kotti's ``INavigationRoot`` /
  ``TemplateAPI.navigation_root``.  This greatly simplifies the setup of
  ``kotti_multilingua``.

- Depend on Kotti>=0.9a3dev (needed for the above).

0.1a1 - 2013-05-06
------------------

- Initial release.
