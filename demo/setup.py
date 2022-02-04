# -*- coding: utf-8 -*-
"""Python packaging."""
import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.dirname(here)


NAME = 'django-anysign-demo'
DESCRIPTION = 'Demo for django-anysign.'
README = open(os.path.join(here, 'README.rst')).read()
VERSION = open(os.path.join(project_root, 'VERSION')).read().strip()
AUTHOR = u'Benoît Bryon'
EMAIL = u'novafloss@people-doc.com'
URL = 'https://django-anysign.readthedocs.io/'
CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'License :: OSI Approved :: BSD License',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.7',
               'Programming Language :: Python :: 3.8',
               'Framework :: Django']
KEYWORDS = []
PACKAGES = ['django_anysign_demo']
REQUIREMENTS = [
    'django-anysign',
    'django-nose',
    'setuptools',
]
ENTRY_POINTS = {
    'console_scripts': [
        'django-anysign-demo = django_anysign_demo.manage:main',
    ]
}


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(name=NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=README,
          classifiers=CLASSIFIERS,
          keywords=' '.join(KEYWORDS),
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license='BSD',
          packages=PACKAGES,
          include_package_data=True,
          zip_safe=False,
          install_requires=REQUIREMENTS,
          entry_points=ENTRY_POINTS)
