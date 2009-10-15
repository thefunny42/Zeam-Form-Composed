
from zope import interface

from zeam.form.base.interfaces import IForm, IFormCanvas, ISimpleFormCanvas
from zeam.form.base.interfaces import IZeamFormBaseAPI


class ISubForm(IFormCanvas):
    """A form designed to be included in an another form.
    """

    parent = interface.Attribute("Parent form")

    def available():
        """Return true if the form is available and should be
        rendered.
        """


class ISimpleSubForm(ISubForm, ISimpleFormCanvas):
    """A simple sub form.
    """


class IComposedForm(IForm):
    """A form which is composed of other forms.
    """

    subforms = interface.Attribute("List of subforms")


class IZeamFormComposedAPI(IZeamFormBaseAPI):
    """API exported by zeamf.form.composed.
    """

    ComposedForm = interface.Attribute(
        u"A form which can be compose of other forms")
    SubForm = interface.Attribute(
        u"A form included in a ComposedForm")

    view = interface.Attribute(
        u"Directive to select which ComposedForm a SubForm belongs to")
    order = interface.Attribute(
        u"Directive used to order SubForms between themselves")

