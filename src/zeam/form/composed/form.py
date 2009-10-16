
from megrok import pagetemplate as pt
from grokcore.viewlet.util import sort_components
from grokcore import component as grok
from zope import component

from zeam.form.base import form
from zeam.form.composed import interfaces

pt.templatedir('default_templates')


class SubFormBase(object):
    """Base class to be applied on a FormCanvas to get a subform.
    """
    grok.baseclass()

    # Set prefix to None, so it's changed by the grokker
    prefix = None

    def __init__(self, context, parent, request):
        super(SubFormBase, self).__init__(context, request)
        self.parent = parent

    def available(self):
        return True


class SubForm(SubFormBase, form.FormCanvas):
    """Form designed to be included in an another form (a
    ComposedForm).
    """
    grok.baseclass()
    grok.implements(interfaces.ISimpleSubForm)


class SubFormTemplate(pt.PageTemplate):
    """Default template for a SubForm
    """
    pt.view(SubForm)


class ComposedForm(form.Form):
    """A form which is composed of other forms (SubForm).
    """
    grok.baseclass()
    grok.implements(interfaces.IComposedForm)

    def __init__(self, context, request):
        super(ComposedForm, self).__init__(context, request)
        # retrieve subforms by adaptation
        subforms = map(lambda x: x[1], component.getAdapters(
                (self.context, self,  self.request), interfaces.ISubForm))
        # filter out unavailables ones
        subforms = filter(lambda x: x.available(), subforms)
        # sort them
        self.subforms = sort_components(subforms)

    def updateForm(self):
        # Set/run actions for all forms
        for subform in self.subforms:
            subform.updateActions()
        # Run our actions
        self.updateActions()
        # Set widgets for all forms
        for subform in self.subforms:
            subform.updateWidgets()


class ComposedFormTemplate(pt.PageTemplate):
    """Default template for a ComposedForm.
    """
    pt.view(ComposedForm)
