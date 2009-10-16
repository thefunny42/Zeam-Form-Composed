
import grokcore.viewlet
import grokcore.view
from grokcore.view.meta.views import default_view_name
import grokcore.component
import martian

import zope.component
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zeam.form.composed.interfaces import ISubForm
from zeam.form.composed.form import SubFormBase


class SubFormGrokker(martian.ClassGrokker):
    """Grokker to register sub forms.
    """
    martian.component(SubFormBase)
    martian.directive(grokcore.component.context)
    martian.directive(grokcore.view.layer, default=IDefaultBrowserLayer)
    martian.directive(grokcore.viewlet.view)
    martian.directive(grokcore.view.name, get_default=default_view_name)

    def grok(self, name, factory, module_info, **kw):
        factory.module_info = module_info
        return super(SubFormGrokker, self).grok(
            name, factory, module_info, **kw)

    def execute(self, factory, config, context, layer, view, name, **kw):
        if not factory.prefix:
            factory.prefix = '%s.%s' % (view.prefix, name)

        adapts = (context, view, layer)
        config.action(
            discriminator=('adapter', adapts, ISubForm, name),
            callable=zope.component.provideAdapter,
            args=(factory, adapts, ISubForm, name),
            )
        return True
