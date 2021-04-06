from pathlib import Path
from pprint import pprint

from pdfmap import pdfWordMap


def print_header(s: str) -> None:
    print(f' {s} '.center(80, '+'))


N_ENTRIES = 5
filepath = Path('examples', 'bitcoin.pdf')


print_header(f'First {N_ENTRIES} entries from {filepath}')
pdfwm = pdfWordMap()
wordmap = pdfwm.parse_pdf(filepath)
pprint(wordmap[:N_ENTRIES])


print_header(f'First {N_ENTRIES} entries from {filepath} with confidence')
pdfwm = pdfWordMap()
wordmap = pdfwm.parse_pdf(filepath, confidence=100)
pprint(wordmap[:N_ENTRIES])


print_header(f'First {N_ENTRIES} entries from {filepath} bytes')
with filepath.open('rb') as fp:
    data = fp.read()
pdfwm = pdfWordMap()
wordmap = pdfwm.parse_pdf(data)
pprint(wordmap[:N_ENTRIES])


print_header(f'Calculate pages size from {filepath}')
pdfwm = pdfWordMap()
sizes = pdfwm.pages_size(filepath)
print(sizes)
