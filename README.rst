==================
kotti_multilingual
==================

Multilingual Sites with Kotti_.

Kotti's data model includes a ``language`` attribute on the ``Content`` class,
from which all content types inherit.  However, this attribute is neither
exposed by Kotti's UI, nor used in any other way.  ``kotti_multilingual``
provides a generic approach to build multilingual sites.

Work in Progress
================

``kotti_multilingual`` is still in an early stage of development.  It is
neither feature complete nor can be considered API stable.  Things will change!

Features
========

The package contains a single content type ``LanguageSection`` which is
supposed to be the container of all content in a specific language.  All
content that is created in (or moved into) such a subtree will be automatically
tagged with the language of the section.  This is done by subscribing to
Kotti's ``ObjectInsert``and ``ObjectUpdate`` events.

The package also extends Kotti's ``TemplateAPI`` with an additional
``language_root`` attribute that can be used as the navigation root for the
currently selected language.  The included ``language_nav.pt`` template makes
use of that attribute.

You can place ``LanguageSection`` instances wherever you want in your content
tree, but it is considered best practice to have a tree structure like this::

 - /            Document            language neutral
    - /en       LanguageSection     English
    - /de       LanguageSection     German
    - /nl       LanguageSection     Dutch
    - /images   Document            language neutral

Setup
=====

To activate the ``kotti_multilingual`` add-on in your Kotti site, you need to
add **one or more** entries to the ``kotti.configurators`` setting in your
Paste Deploy config.  If you don't have a ``kotti.configurators`` option,
add one.

You must always add (enables content type(s) and event subscribers)::

    kotti.configurators = kotti_multilingual.kotti_configure

You most likely will want to also enable the TemplateAPI extensions for
``kotti_multilingual``::

    kotti.configurators = kotti_multilingual.kotti_configure_template_api

The one exception when you don't want this is if you already have a custom
TemplateAPI in your project.  In this case your class should inherit from
``kotti_multilingual.views.util.TemplateAPI``.

To use the template overrides (most notably the language aware navigation bar
with included language switcher) also add::

    kotti.configurators = kotti_multilingual.kotti_configure_template_overrides

If unsure (or you just want to test drive ``kotti_multilingual``) add all of
the above.

.. _Kotti: http://pypi.python.org/pypi/Kotti
