
from zope.interface import implements
from zope import component

from zeam.form.base import form
from zeam.form.composed import interfaces


class SubForm(form.FormCanvas):
    implements(interfaces.ISubForm)

    # Set prefix to None, so it's changed by the grokker
    prefix = None

    def __init__(self, context, parent, request):
        super(SubForm, self).__init__(context, request)
        self.parent = parent

    def available(self):
        return True


class ComposedForm(form.Form):
    implements(interfaces.IComposedForm)

    def __init__(self, context, request):
        super(ComposedForm, self).__init__(context, request)

        subforms = map(lambda x: x[1], component.getAdapters(
                (self.context, self,  self.request), interfaces.ISubForm))
        # TODO sort forms
        self.subforms = []
        for subform in subforms:
            if subform.available():
                self.subforms.append(subform)

    def updateForm(self):
        # Set/run actions for all forms
        for subform in self.subforms:
            subform.updateActions()
        # Run our actions
        self.updateActions()
        # Set widgets for all forms
        for subform in self.subforms:
            subfrom.updateWidgets()
