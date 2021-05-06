from pathlib import Path
from pprint import pprint

from pdfmap import pdfWordMap
from pdfmap.utils import Origin


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

print_header(f'First {N_ENTRIES} entries from {filepath} split to words')
pdfwm = pdfWordMap()
wordmap = pdfwm.parse_pdf(filepath, split_words=True, key_split_chars=[' ', ':', '-'])
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
pprint(sizes)


print_header(f'Use {Origin.TOP_LEFT} to read {filepath}')
pdfwm = pdfWordMap()
wordmap = pdfwm.parse_pdf(data, origin=Origin.TOP_LEFT)
pprint(wordmap[:N_ENTRIES])

print_header(f'Use {Origin.BOTTOM_LEFT} to read {filepath}')
pdfwm = pdfWordMap()
wordmap = pdfwm.parse_pdf(data, origin=Origin.BOTTOM_LEFT)
pprint(wordmap[:N_ENTRIES])
