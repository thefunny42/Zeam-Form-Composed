from setuptools import setup, find_packages
import os

version = '1.0'

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
        'zeam.form.base',
        'martian',
        'grokcore.component',
        'grokcore.view',
        'grokcore.viewlet',
        'megrok.pagetemplate',
        'zope.component',
        'zope.interface',
        'zope.publisher',
        # Test
        'zope.securitypolicy',
        'zope.app.authentication',
        'zope.app.testing',
        'zope.app.zcmlfiles',
        'zope.testing',
        'zope.testbrowser',
        ],
      )
