from setuptools import setup, find_packages
import os

version = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Products', 'huckPersonExtender', 'version.txt')).read().strip()
if version.endswith('dev'):
    version = version[:-3]

setup(name='Products.huckPersonExtender',
      version=version,
      description="A extender for FSD person objects",
      long_description=open("README.txt").read() + "\n" +
                       open("HISTORY.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Paul Rentschler',
      author_email='par117@psu.edu',
      url='http://huck.psu.edu/people/par117',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.FacultyStaffDirectory>=3.0',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )


