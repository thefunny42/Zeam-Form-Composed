
import zeam.form.composed

from zope.app.wsgi.testlayer import BrowserLayer
from zope.configuration.config import ConfigurationMachine
from grokcore.component import zcml
import zope.testbrowser.wsgi


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        BrowserLayer):
    pass


FunctionalLayer = Layer(zeam.form.composed, allowTearDown=True)


def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok(module_name, config)
    config.execute_actions()
