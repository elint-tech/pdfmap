# pdfmap


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
