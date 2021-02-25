#!/usr/bin/env python

# PyPi publish flow
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*

from setuptools import setup, find_packages
from os.path import join, dirname

here = dirname(__file__)

_VERSION = '0.0.7'

setup(name='pdfmap',
      version=_VERSION,
      description="Turning PDF into WordMap algorithm",
      long_description=open(join(here, 'README.md')).read(),
      license='proprietary',
      author='elint-tech',
      author_email='contato@elint.com.br',
      url='https://github.com/elint-tech/pdfmap/',
      download_url = 'https://github.com/elint-tech/pdfmap/dist/pdfmap-' + _VERSION + 'tar.gz',
      install_requires=list(map(
        lambda string: string.strip("\n"),
        open("requirements.txt", "r")
      )),
      packages=find_packages(),
      keywords = ['pdfmap'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
      ],
      )