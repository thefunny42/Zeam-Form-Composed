==================
zeam.form.composed
==================

This package let you defines forms containing other forms in
`zeam.form.base`_.

.. contents::

Example
=======

Here a simple example. Let's define a setting form::

  from zeam.form import composed, base
  from zope.interface import Interface


  class Setting(composed.ComposedForm):
      composed.context(Interface)

      label = u"Settings"


After, a module can add some mail settings on that screen::

  class MailSetting(composed.SubForm):
      composed.context(MyApplication)
      composed.view(Setting)
      composed.order(99)

      label = u"Mail delivery settings"
      ...

And publications of that application could add some publication
settings::

  class PublicationSetting(composed.SubForm):
      composed.context(MyPublications)
      composed.view(Setting)
      composed.order(10)

      label = u"Publication settings"
      ...


Some default templates are included as well, but you can replace like
you will do in `zeam.form.base`_.

API
===

Classes
-------

``ComposedForm``
    This class define a form which able to contain other forms. It
    behave like a ``zeam.form.base`` Form, but does use its fields.

``SubForm``
    This class represent a form which is contained inside a
    ``ComposedForm``. This form behave exactly like a
    ``zeam.form.base`` Form to which you add:

    - a method ``available()`` which is called before anything else to
      know if the form shoud still be included in the ``ComposedForm``.

Directives
----------

All those directives comes from Grokcore component. Please refer to
the `Grok documentation <http://grok.zope.org>`_ for more information.

``context``
    Define for which object the form/sub form is available.

``layer``
    Define the skin for which the form/sub form is aviable.

``require``
    Define a permission need to access the form.

``template``
    Define a Grok-like template for the form. After you done that, the
    Grok template will be look up and used. You can't use anymore a
    ``megrok.pagetemplate`` template, unless you set ``template=None``
    again on your form class.

``view``
    On a sub form, define for which form the sub form is available.

``order``
    Let you specify a number to sort your sub form afterwards using
    that setting.

.. _zeam.form.base: http://pypi.python.org/pypi/zeam.form.base
