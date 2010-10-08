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
    ['form.bears.firefox', 'form.bears.polarbear', 'form.bears.grizzly',
     'form.bears.brownbear']

We can render the whole form:

    >>> print form()
    <html>
      <head>
      </head>
      <body>
          <h1>A zoo form</h1>
          <div class="subforms">
            <div class="subform"><div class="subform-group">
      <h2>Birds Form</h2>
      <div class="subform"><form action="http://127.0.0.1" method="post" enctype="multipart/form-data">
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-birds-blackbird-action-chirp" name="form.birds.blackbird.action.chirp" value="Chirp" class="action" />
        </div>
      </div>
    </form></div> <div class="subform"><form action="http://127.0.0.1" method="post" enctype="multipart/form-data">
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-birds-eagle-action-catch-rabbit" name="form.birds.eagle.action.catch-rabbit" value="Catch rabbit" class="action" />
        </div>
      </div>
    </form></div> <div class="subform"><form action="http://127.0.0.1" method="post" enctype="multipart/form-data">
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-birds-vulture-action-eat-carcass" name="form.birds.vulture.action.eat-carcass" value="Eat carcass" class="action" />
        </div>
      </div>
    </form></div>
    </div></div> <div class="subform"><div class="subform-group">
      <h2>Bears form</h2>
      <div class="subform"><form action="http://127.0.0.1" method="post" enctype="multipart/form-data">
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-bears-firefox-action-eat-bamboo" name="form.bears.firefox.action.eat-bamboo" value="Eat bamboo" class="action" />
        </div>
      </div>
    </form></div> <div class="subform"><form action="http://127.0.0.1" method="post" enctype="multipart/form-data">
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-bears-polarbear-action-eat-seal" name="form.bears.polarbear.action.eat-seal" value="Eat seal" class="action" />
        </div>
      </div>
    </form></div> <div class="subform"><form action="http://127.0.0.1" method="post" enctype="multipart/form-data">
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-bears-grizzly-action-growl" name="form.bears.grizzly.action.growl" value="Growl" class="action" />
        </div>
      </div>
    </form></div> <div class="subform"><form action="http://127.0.0.1" method="post" enctype="multipart/form-data">
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-bears-brownbear-action-play-in-pool" name="form.bears.brownbear.action.play-in-pool" value="Play in pool" class="action" />
        </div>
      </div>
    </form></div>
    </div></div>
          </div>
      </body>
    </html>

  
"""


from zeam.form import composed, base
from grokcore import component as grok


class Animals(grok.Context):
    pass


class ZooForm(composed.ComposedForm):
    label = u"A zoo form"


class Birds(composed.SubFormGroup):
    composed.view(ZooForm)
    composed.order(10)
    label = u"Birds Form"


class Bears(composed.SubFormGroup):
    composed.view(ZooForm)
    composed.order(20)
    label = u"Bears form"


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
    actions = base.Actions(base.Action("Eat carcass"))


class Firefox(composed.SubForm):
    composed.view(Bears)
    composed.order(10)
    actions = base.Actions(base.Action("Eat bamboo"))


class Grizzly(composed.SubForm):
    composed.view(Bears)
    composed.order(12)
    actions = base.Actions(base.Action("Growl"))


class BrownBear(composed.SubForm):
    composed.view(Bears)
    composed.order(13)
    actions = base.Actions(base.Action("Play in pool"))


class PolarBear(composed.SubForm):
    composed.view(Bears)
    composed.order(11)
    actions = base.Actions(base.Action("Eat seal"))
