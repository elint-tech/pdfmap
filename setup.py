# PyPi publish flow
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*

from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).resolve().parent

VERSION = (here / 'VERSION').read_text().strip()

setup(
    name='pdfmap',
    version=VERSION,

    description="Turning PDFs into WordMaps and WordMazes",
    long_description=(here / 'README.md').read_text(),
    long_description_content_type="text/markdown",

    license='proprietary',
    author='elint-tech',
    author_email='contato@elint.com.br',

    url='https://github.com/elint-tech/pdfmap/',
    download_url=f'https://github.com/elint-tech/pdfmap/dist/pdfmap-{VERSION}.tar.gz',

    install_requires=Path(here, 'requirements.txt').read_text().splitlines(),
    packages=find_packages(),

    keywords=['pdfmap', 'pdf', 'wordmap'],
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
)
