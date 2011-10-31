"""
We will define a composed form with two `groups` subforms. A group of
subforms is a logical ensemble of subforms, behaving like a single
subform. It is registered the same way as a SubForm.

Let's grok our example:

    >>> from zeam.form.composed.testing import grok
    >>> grok('zeam.form.composed.ftests.forms.group')

We can now lookup our form by the name of its class:

    >>> from zope.publisher.browser import TestRequest
    >>> request = TestRequest()

    >>> animals = Animals()

    >>> from zope import component
    >>> form = component.getMultiAdapter(
    ...     (animals, request), name='zooform')
    >>> form
    <zeam.form.composed.ftests.forms.group.ZooForm object at ...>
    >>> form.updateForm()

The form should have the two groups as subforms::

    >>> form.subforms
    [<zeam.form.composed.ftests.forms.group.Birds object at ...>,
     <zeam.form.composed.ftests.forms.group.Bears object at ...>]

Each group is prefixed differently with the name of the form:

    >>> [s.prefix for s in form.subforms]
    ['form.birds', 'form.bears']

Each subform inside a group is prefixed with the name of the form and
the group::

    >>> for group in form.subforms:
    ...    [s.prefix for s in group.subforms]
    ['form.birds.blackbird', 'form.birds.eagle', 'form.birds.vulture']
    ['form.bears.firefox', 'form.bears.grizzly',
     'form.bears.scandinavianbears']

There a group embbedded in a group here, as we can mix groups and
subforms transparently. Let's verify that our subgroup subforms are
there ::

    >>> bears = form.getSubForm('form-bears')
    >>> subbears = bears.getSubForm('form-bears-scandinavianbears')
    >>> print subbears.subforms
    [<zeam.form.composed.ftests.forms.group.BrownBear object at ...>,
     <zeam.form.composed.ftests.forms.group.PolarBear object at ...>]

We can render the whole form:

    >>> # print form()


Integration tests
-----------------

  >>> root = getRootFolder()
  >>> root['animals'] = animals

  >>> from zope.app.wsgi.testlayer import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False


Empty submission
~~~~~~~~~~~~~~~~

We are going just to submit the form without giving any required
information, and we should get an error:

  >>> browser.open('http://localhost/animals/zooform')
  >>> action = browser.getControl('Growl')
  >>> action
  <SubmitControl name='form.bears.grizzly.action.growl' type='submit'>

  >>> action.click()
  >>> 'The Grizzly growled !' in browser.contents
  True

"""


from zeam.form import composed, base
from grokcore import component as grok


class Animals(grok.Context):
    pass


class ZooForm(composed.ComposedForm):
    label = u"A zoo form"


## Groups

class Birds(composed.SubFormGroup):
    composed.view(ZooForm)
    composed.order(10)
    label = u"Birds Form"


class Bears(composed.SubFormGroup):
    composed.view(ZooForm)
    composed.order(20)
    label = u"Bears form"


class ScandinavianBears(composed.SubFormGroup):
    composed.view(Bears)
    composed.order(20)
    label = u"Scandinavian bears form"


## Sub forms

class Eagle(composed.SubForm):
    composed.view(Birds)
    composed.order(20)
    actions = base.Actions(base.Action("Catch rabbit"))


class Blackbird(composed.SubForm):
    composed.view(Birds)
    composed.order(10)
    actions = base.Actions(base.Action("Chirp"))


class Vulture(composed.SubForm):
    composed.view(Birds)
    composed.order(30)
    fields = base.Fields(base.Field("Size"), base.Field("Weight"))
    actions = base.Actions(base.Action("Eat carcass"))


class Firefox(composed.SubForm):
    composed.view(Bears)
    composed.order(10)
    actions = base.Actions(base.Action("Eat bamboo"))


class Grizzly(composed.SubForm):
    composed.view(Bears)
    composed.order(12)

    fields = base.Fields(base.Field("Name"), base.Field("Gender"))

    @base.action(u"Growl")
    def register(self):
        data, errors = self.extractData()
        if errors:
            return
        # In case of success we don't keep request value in the form
        self.ignoreRequest = True
        self.status = u"The Grizzly growled !"


class BrownBear(composed.SubForm):
    composed.view(ScandinavianBears)
    composed.order(0)
    fields = base.Fields(base.Field("Name"), base.Field("Age"))
    actions = base.Actions(base.Action("Play in pool"))


class PolarBear(composed.SubForm):
    composed.view(ScandinavianBears)
    composed.order(1)
    actions = base.Actions(base.Action("Eat seal"))
