
import grokcore.view
from grokcore.view.meta.views import default_view_name
import grokcore.component
import martian

import zope.component
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zeam.form.composed.interfaces import ISubForm
from zeam.form.composed.form import SubFormBase


def set_form_prefix(subform, form, name):
    """Recursively set the form prefix (to be compatible with groups)
    """
    # We use __dict__.get not to look if prefix was set in a parent class.
    if not subform.__dict__.get('prefix'):
        if not form.prefix:
            set_form_prefix(
                form,
                grokcore.view.view.bind().get(form),
                grokcore.view.name.bind(
                    get_default=default_view_name).get(form))
        subform.prefix = '%s.%s' % (form.prefix, name)


class SubFormGrokker(martian.ClassGrokker):
    """Grokker to register sub forms.
    """
    martian.component(SubFormBase)
    martian.directive(grokcore.component.context)
    martian.directive(grokcore.view.layer, default=IDefaultBrowserLayer)
    martian.directive(grokcore.view.view)
    martian.directive(grokcore.view.name, get_default=default_view_name)

    def grok(self, name, factory, module_info, **kw):
        factory.module_info = module_info
        return super(SubFormGrokker, self).grok(
            name, factory, module_info, **kw)

    def execute(self, factory, config, context, layer, view, name, **kw):
        set_form_prefix(factory, view, name)

        adapts = (context, view, layer)
        config.action(
            discriminator=('adapter', adapts, ISubForm, name),
            callable=zope.component.provideAdapter,
            args=(factory, adapts, ISubForm, name),
            )
        return True
