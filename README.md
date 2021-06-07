# PDFMap [![PyPI version fury.io](https://img.shields.io/pypi/v/pdfmap?color=green)](https://github.com/elint-tech/pdfmap) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/pdfmap)](https://github.com/elint-tech/pdfmap)

## Installation

We recommend using the most up-to-date version of `pip` and `wheel` packages, so first run:

```bash
pip install -U pip wheel
```

Then install PDFMap with:

```bash
pip install pdfmap
```

## Usage

Simple usage can be achieved with:

```python
from pdfmap import PDFWordMap

pdfwm = PDFWordMap()
print(pdfwm.parse_pdf('folder/pdfname.pdf'))
```

You can also extract [`wordmaze.WordMaze`](https://github.com/elint-tech/wordmaze) instances by using `PDFMaze`:

```python
from pdfmap import PDFMaze

pdfmaze = PDFMaze()
print(pdfmaze.parse_pdf('folder/pdfname.pdf'))
```

For other examples, check out [our example script](example.py)
