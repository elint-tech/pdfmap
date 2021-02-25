# pdfmap


#### Dependencies
* pdfminer

### Setup

```bash
pip3 install pdfmap
```

### Usage

```python
from pdfmap import pdfWordMap

pdfwm = pdfWordMap()
print(pdfwm.parse_pdf('folder/pdfname.pdf'))
```
