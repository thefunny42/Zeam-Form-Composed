"""
We will define a composed form with two subforms.

Let's grok our example:

  >>> from zeam.form.composed.testing import grok
  >>> grok('zeam.form.composed.ftests.forms.composed')

We can now lookup our form by the name of its class:

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()

  >>> from zeam.form.composed.ftests.forms.composed import Content
  >>> context = Content()

  >>> from zope import component
  >>> form = component.getMultiAdapter(
  ...     (context, request), name='complexform')
  >>> form
  <zeam.form.composed.ftests.forms.composed.ComplexForm object at ...>

Our form have subforms:

  >>> form.subforms
  [<zeam.form.composed.ftests.forms.composed.Hello object at ...>,
   <zeam.form.composed.ftests.forms.composed.ByeBye object at ...>]

Each sub form is prefixed differently with the name of the form:

  >>> [s.prefix for s in form.subforms]
  ['form.hello', 'form.byebye']

And we can render the form:

  >>> print form()
  <html>
    <head>
    </head>
    <body>
        <h1>Complex form</h1>
        <div class="subforms">
          <div class="subform"><form action="http://127.0.0.1" method="post"
                                     enctype="multipart/form-data">
            <h2>Hello Form</h2>
            <div class="actions">
              <div class="action">
                <input type="submit" id="form-hello-action-hello"
                       name="form.hello.action.hello" value="Hello" />
              </div>
            </div>
           </form>
          </div>
          <div class="subform"><form action="http://127.0.0.1" method="post"
                                     enctype="multipart/form-data">
          <h2>Bye Bye Form</h2>
          <div class="actions">
            <div class="action">
               <input type="submit" id="form-byebye-action-bye-bye"
                      name="form.byebye.action.bye-bye" value="Bye Bye" />
           </div>
          </div>
        </form>
       </div>
      </div>
    </body>
  </html>

"""

from zeam.form import composed, base

from grokcore import component as grok


class Content(grok.Context):
    pass


class ComplexForm(composed.ComposedForm):
    label = u"Complex form"


class Hello(composed.SubForm):
    composed.view(ComplexForm)
    composed.order(10)

    label = u"Hello Form"
    actions = base.Actions(base.Action("Hello"))


class ByeBye(composed.SubForm):
    composed.view(ComplexForm)
    composed.order(20)

    label = u"Bye Bye Form"
    actions = base.Actions(base.Action("Bye Bye"))
