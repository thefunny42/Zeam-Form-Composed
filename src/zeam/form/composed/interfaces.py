
from zope import interface

from zeam.form.base.interfaces import IForm, IFormCanvas


class ISubForm(IFormCanvas):
    """A form designed to be included in an another form.
    """

    parent = interface.Attribute("Parent form")

    def available():
        """Return true if the form is available and should be
        rendered.
        """


class IComposedForm(IForm):
    """A form which is composed of other forms.
    """

    subforms = interface.Attribute("List of subforms")
