# pdfmap [![PyPI version fury.io](https://img.shields.io/pypi/v/pdfmap?color=green)](https://github.com/elint-tech/pdfmap) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/pdfmap)](https://github.com/elint-tech/pdfmap)


## Dependencies
* pdfminer

## Setup

```bash
pip3 install pdfmap
```

## Usage

Simple usage can be achieved with:

```python
from pdfmap import pdfWordMap

pdfwm = pdfWordMap()
print(pdfwm.parse_pdf('folder/pdfname.pdf'))
```

For other examples, check out [our example script](example.py)

You can also extract [`wordmaze`](https://github.com/elint-tech/wordmaze/blob/main/README.md) `WordMaze` instances by using `PDFMaze`:

```python
from pdfmap import PDFMaze

pdfmaze = PDFMaze()
print(pdfmaze.parse_pdf('folder/pdfname.pdf'))
```

