"""
We will define a composed form with some un-ordered subforms.

Let's grok our example:

  >>> from zeam.form.composed.testing import grok
  >>> grok('zeam.form.composed.ftests.forms.implicitorder')

We can now lookup our form by the name of its class:

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()

  >>> from zeam.form.composed.ftests.forms.implicitorder import Content
  >>> context = Content()

  >>> from zope import component
  >>> form = component.getMultiAdapter(
  ...     (context, request), name='form')
  >>> form
  <zeam.form.composed.ftests.forms.implicitorder.Form object at ...>

Our form have subforms, which are in order D, C, B, and A:

  >>> form.subforms
  [<zeam.form.composed.ftests.forms.implicitorder.ASubForm object at ...>,
   <zeam.form.composed.ftests.forms.implicitorder.BSubForm object at ...>,
   <zeam.form.composed.ftests.forms.implicitorder.CSubForm object at ...>,
   <zeam.form.composed.ftests.forms.implicitorder.DSubForm object at ...>]

"""

from zeam.form import composed, base

from grokcore import component as grok


class Content(grok.Context):
    pass


class Form(composed.ComposedForm):
    label = u"Main form"


class ASubForm(composed.SubForm):
    composed.view(Form)

    label = u"Sub Form A"


class BSubForm(composed.SubForm):
    composed.view(Form)

    label = u"Sub Form B"


class CSubForm(composed.SubForm):
    composed.view(Form)

    label = u"Sub Form C"

class DSubForm(composed.SubForm):
    composed.view(Form)

    label = u"Sub Form D"
