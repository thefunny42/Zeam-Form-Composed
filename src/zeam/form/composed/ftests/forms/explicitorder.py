"""
We will define a composed form with some ordered subforms.

Let's grok our example:

  >>> from zeam.form.composed.testing import grok
  >>> grok('zeam.form.composed.ftests.forms.explicitorder')

We can now lookup our form by the name of its class:

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()

  >>> from zeam.form.composed.ftests.forms.explicitorder import Content
  >>> context = Content()

  >>> from zope import component
  >>> form = component.getMultiAdapter(
  ...     (context, request), name='form')
  >>> form
  <zeam.form.composed.ftests.forms.explicitorder.Form object at ...>

Our form have subforms, which are in order D, C, B, and A, because we
used the order directive:

  >>> form.subforms
  [<zeam.form.composed.ftests.forms.explicitorder.DSubForm object at ...>,
   <zeam.form.composed.ftests.forms.explicitorder.CSubForm object at ...>,
   <zeam.form.composed.ftests.forms.explicitorder.BSubForm object at ...>,
   <zeam.form.composed.ftests.forms.explicitorder.ASubForm object at ...>]

"""

from zeam.form import composed, base

from grokcore import component as grok


class Content(grok.Context):
    pass


class Form(composed.ComposedForm):
    label = u"Main form"


class ASubForm(composed.SubForm):
    composed.view(Form)
    composed.order(20)

    label = u"Sub Form A"


class CSubForm(composed.SubForm):
    composed.view(Form)
    composed.order(10)

    label = u"Sub Form C"


class DSubForm(composed.SubForm):
    composed.view(Form)
    composed.order(0)

    label = u"Sub Form D"


class BSubForm(composed.SubForm):
    composed.view(Form)
    composed.order(15)

    label = u"Sub Form B"

