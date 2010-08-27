
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
    label = u''
    description = u''
    prefix = None

    def __init__(self, context, parent, request):
        super(SubFormBase, self).__init__(context, request)
        self.parent = parent

    def available(self):
        return True


class SubFormGroupBase(object):
    """A group of subforms: they can be grouped inside a composed form.
    """

    def __init__(self, context, request):
        super(SubFormGroupBase, self).__init__(context, request)
        # retrieve subforms by adaptation
        subforms = map(lambda f: f[1], component.getAdapters(
                (self.context, self,  self.request), interfaces.ISubForm))
        # sort them
        self.allSubforms = sort_components(subforms)
        # filter out unavailables ones
        self.subforms = filter(lambda f: f.available(), self.allSubforms)

    def update(self):
        # Call update for all forms
        for subform in self.allSubforms:
            subform.update()

    def updateActions(self):
        # Set/run actions for all forms
        for subform in self.subforms:
            action, status = subform.updateActions()
            if action is not None:
                break
        # The result of the actions might have changed the available subforms
        self.subforms = filter(lambda f: f.available(), self.allSubforms)
        return action, status

    def updateWidgets(self):
        # Set widgets for all forms
        for subform in self.subforms:
            subform.updateWidgets()


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


class SubFormGroup(SubFormBase, SubFormGroupBase, form.GrokViewSupport):
    """A group of subforms.
    """
    grok.baseclass()

    def available(self):
        return len(self.subforms) != 0


class SubFormGroupTemplate(pt.PageTemplate):
    """Default template for a SubFormGroup.
    """
    pt.view(SubFormGroup)


class ComposedForm(SubFormGroupBase, form.Form):
    """A form which is composed of other forms (SubForm).
    """
    grok.baseclass()
    grok.implements(interfaces.IComposedForm)

    def updateForm(self):
        action, status = SubFormGroupBase.updateActions(self)
        if action is None:
            form.Form.updateActions(self)
        SubFormGroupBase.updateWidgets(self)
        form.Form.updateWidgets(self)


class ComposedFormTemplate(pt.PageTemplate):
    """Default template for a ComposedForm.
    """
    pt.view(ComposedForm)
