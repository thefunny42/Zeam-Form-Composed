
from zope import interface
from zope.publisher.interfaces.browser import IBrowserView

from zeam.form.base.interfaces import IForm, IFormCanvas, ISimpleFormCanvas
from zeam.form.base.interfaces import IZeamFormBaseAPI


class ISubForm(IFormCanvas, IBrowserView):
    """A form designed to be included in an another form.
    """
    parent = interface.Attribute("Parent form")

    def available():
        """Return true if the form is available and should be
        rendered.
        """

    def getComposedForm():
        """Return the associated composed form.
        """


class ISimpleSubForm(ISubForm, ISimpleFormCanvas):
    """A simple sub form.
    """


class ISubFormGroup(interface.Interface):
    """A group of subforms.
    """
    subforms = interface.Attribute("List of available subforms")
    allSubforms = interface.Attribute("List of all subforms")

    def getSubForm(identifier):
        """Return a subform based on its HTML identifier.
        """


class IComposedForm(ISubFormGroup, IForm):
    """A form which is composed of other forms.
    """


class IZeamFormComposedAPI(IZeamFormBaseAPI):
    """API exported by zeamf.form.composed.
    """
    ComposedForm = interface.Attribute(
        u"A form which can be compose of other forms")
    SubForm = interface.Attribute(
        u"A form included in a ComposedForm")
    SubFormGroup = interface.Attribute(
        u"A group of subforms that behave like one subform")

    view = interface.Attribute(
        u"Directive to select which ComposedForm a SubForm belongs to")
    order = interface.Attribute(
        u"Directive used to order SubForms between themselves")
