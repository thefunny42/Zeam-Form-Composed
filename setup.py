from setuptools import setup, find_packages
import os

version = '1.3.2'

tests_require = [
    'zope.app.wsgi',
    'zope.configuration',
    'zope.testing',
    'zeam.form.base [test]',
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
        'grokcore.chameleon',
        'grokcore.component >= 2.5',
        'grokcore.view',
        'martian',
        'megrok.pagetemplate',
        'setuptools',
        'zeam.form.base >= 1.2',
        'zope.component',
        'zope.interface',
        'zope.publisher',
        ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
