
from megrok import pagetemplate as pt
from grokcore.component.util import sort_components
from grokcore import component as grok
from zope import component

from zeam.form.base import form
from zeam.form.composed import interfaces
from zope.interface import implementer

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

    def htmlId(self):
        return self.prefix.replace('.', '-')

    def getComposedForm(self):
        return self.parent.getComposedForm()


@implementer(interfaces.ISubFormGroup)
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
        self.subforms = []

    def getSubForm(self, identifier):
        for form in self.subforms:
            if form.htmlId() == identifier:
                return form
        return None

    def getComposedForm(self):
        return self

    def htmlId(self):
        return self.prefix.replace('.', '-')

    def update(self):
        # Call update for all forms
        for subform in self.allSubforms:
            subform.update()

    def updateActions(self):
        # Set/run actions for all forms
        form, action, status = self, None, None
        for subform in self._getAvailableSubForms():
            form, action, status = subform.updateActions()
            if action is not None:
                break
        return form, action, status

    def updateWidgets(self):
        # Set the subforms to render
        self.subforms = self._getAvailableSubForms()
        # Set widgets for all forms
        for subform in self.subforms:
            subform.updateWidgets()

    def _getAvailableSubForms(self):
        # filter out unavailables ones
        return filter(lambda f: f.available(), self.allSubforms)


@implementer(interfaces.ISimpleSubForm)
class SubForm(SubFormBase, form.FormCanvas):
    """Form designed to be included in an another form (a
    ComposedForm).
    """
    grok.baseclass()


class SubFormTemplate(pt.PageTemplate):
    """Default template for a SubForm
    """
    pt.view(SubForm)


@implementer(interfaces.ISubFormGroup)
class SubFormGroup(SubFormBase, SubFormGroupBase, form.GrokViewSupport):
    """A group of subforms.
    """
    grok.baseclass()

    def available(self):
        return len(self._getAvailableSubForms()) != 0


class SubFormGroupTemplate(pt.PageTemplate):
    """Default template for a SubFormGroup.
    """
    pt.view(SubFormGroup)


@implementer(interfaces.IComposedForm)
class ComposedForm(SubFormGroupBase, form.Form):
    """A form which is composed of other forms (SubForm).
    """
    grok.baseclass()

    def updateForm(self):
        executed_form, action, status = SubFormGroupBase.updateActions(self)
        if action is None:
            form.Form.updateActions(self)
        SubFormGroupBase.updateWidgets(self)
        form.Form.updateWidgets(self)


class ComposedFormTemplate(pt.PageTemplate):
    """Default template for a ComposedForm.
    """
    pt.view(ComposedForm)
