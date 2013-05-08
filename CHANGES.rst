Changelog
=========

0.1a3 - 2013-05-08
------------------

-   Rename ``LanguageSection`` to ``LanguageRoot`` to better fit Kotti's
    ``INavigationRoot``.  This implies a change in the DB schema for which no
    automatic schema migration is available; you'll have to rename the table
    ``language_sections`` to ``language_roots`` yourself.

-   Add some tests.

0.1a2 - 2013-05-07
------------------

-   Removed a lot of code that's now replaced by Kotti's ``INavigationRoot`` /
    ``TemplateAPI.navigation_root``.  This greatly simplifies the setup of
    ``kotti_multilingua``.

-   Depend on Kotti>=0.9a3dev (needed for the above).

0.1a1 - 2013-05-06
------------------

-   Initial release.
