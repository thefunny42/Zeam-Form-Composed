from setuptools import setup, find_packages
import os

version = '1.2.1'

tests_require = [
    'zope.configuration',
    'zope.app.authentication',
    'zope.app.testing',
    'zope.app.zcmlfiles',
    'zope.securitypolicy',
    'zope.testbrowser',
    'zope.testing',
    ]

setup(name='zeam.form.composed',
      version=version,
      description="Composed form support for zeam.form",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zeam form composed',
      author='Sylvain Viollon',
      author_email='thefunny@gmail.com',
      url='http://pypi.python.org/pypi/zeam.form.composed',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zeam', 'zeam.form'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'zeam.form.base >= 1.0',
        'martian',
        'grokcore.component',
        'grokcore.view',
        'grokcore.viewlet',
        'megrok.pagetemplate',
        'megrok.chameleon',
        'zope.component',
        'zope.interface',
        'zope.publisher',
        ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
