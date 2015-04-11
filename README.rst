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

The package contains a single content type ``LanguageRoot`` which is
supposed to be the container of all content in a specific language.  All
content that is created in (or moved into) such a subtree will be automatically
tagged with the language of the root.  This is done by subscribing to
Kotti's ``ObjectInsert`` and ``ObjectUpdate`` events.

You can place ``LanguageRoot`` instances wherever you want in your content
tree, but it is considered best practice to have a tree structure like this::

 - /            Document        language neutral
    - /en       LanguageRoot    English
    - /de       LanguageRoot    German
    - /nl       LanguageRoot    Dutch
    - /images   Document        language neutral

Setup
=====

To activate the ``kotti_multilingual`` add-on in your Kotti site, you need to
add an entry to the ``kotti.configurators`` setting in your Paste Deploy config.
If you don't have a ``kotti.configurators`` option, add one.  The added entry
should look like this::

    kotti.configurators = kotti_multilingual.kotti_configure

You can register an optional ``kotti_multilingual.blacklist`` with the list of the
type names not handled by kotti_multilingual. 

.. _Kotti: http://pypi.python.org/pypi/Kotti

Tests
=====

The test setup requires additional steps::

    $ virtualenv --no-site-packages .
    $ source bin/activate
    $ pip install -r requirements.txt
    $ python setup.py develop
    $ python setup.py dev

How to launch tests::

    $ py.test

