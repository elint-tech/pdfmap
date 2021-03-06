from pathlib import Path
from pprint import pprint

from pdfmap import pdfWordMap


N_ENTRIES = 5
filepath = Path('examples', 'bitcoin.pdf')

pdfwm = pdfWordMap()
wordmap = pdfwm.parse_pdf(filepath)
print(f'First {N_ENTRIES} entries from {filepath}'.center(80, '+'))
pprint(wordmap[:N_ENTRIES])
