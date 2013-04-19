.. contents::

Introduction
============

This package is WORK IN PROGRESS. It is based on the concepts of
collective/slc.linguatools,
but this package works with *plone.app.multilingual* and both with both *dexterity* and *archetypes*.

Purpose
-------

It aims to offer a handfull of utilities for performing the same action on all
translations of an item at the same time, such as

* change workflow status
* rename (change id)
* reindex
* delete
* cut and paste (move)
* set title / description from msgid
* propagate or block portlets
* set or remove properties (such as layout)
* set or remove marker interface

Also, there's an option to make a copy of any item to all available languages (or
a subset), optionally copying individual attributes (title, description, tags, etc).

As I said, WORK IN PROGRESS. Basic functionality is becoming stable, but documentation
and good tests are not there yet.

Interface
---------

The interface can use more love for sure. Basically some information about the current
object and its translations is dislpayed; below it a list of various possible actions.

.. image:: https://raw.github.com/collective/collective.multilingualtools/master/docs/editor.png

After every action, feedback is displayed about the status, in this example after making a copy of
a News item into 3 languages:

.. image:: https://raw.github.com/collective/collective.multilingualtools/master/docs/make_translations.png


Dependencies
============

* Plone >= 4.2
* plone.app.multilingual





To do
=====

* Proper testing
* travis integration
* Refactor from formlib to z3c.form
* Interface makeover
* Integrate more useful functions from other LinguaPlone-based add-ons, such as valentine.linguaflow
