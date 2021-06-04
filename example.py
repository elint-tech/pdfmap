from pprint import pprint
from pathlib import Path

from wordmaze.wordmaze import Origin
from pdfmap.pdfmaze import PDFMaze
from pdfmap import PDFWordMap


def print_header(s: str) -> None:
    print(f' {s} '.center(80, '+'))


N_ENTRIES = 5
filepath = Path('examples', 'bitcoin.pdf')


print_header(f'First {N_ENTRIES} entries from {filepath}')
pdfwm = PDFWordMap()
wordmap = pdfwm.parse_pdf(filepath)
pprint(wordmap[:N_ENTRIES])

print_header(f'First {N_ENTRIES} entries from {filepath} with confidence')
pdfwm = PDFWordMap()
wordmap = pdfwm.parse_pdf(filepath, confidence=100)
pprint(wordmap[:N_ENTRIES])

print_header(f'First {N_ENTRIES} entries from {filepath} split to words')
pdfwm = PDFWordMap()
wordmap = pdfwm.parse_pdf(filepath, split_words=True, key_split_chars=[' ', ':', '-'])
pprint(wordmap[:N_ENTRIES])

print_header(f'First {N_ENTRIES} entries from {filepath} bytes')
with filepath.open('rb') as fp:
    data = fp.read()
pdfwm = PDFWordMap()
wordmap = pdfwm.parse_pdf(data)
pprint(wordmap[:N_ENTRIES])


print_header(f'Calculate pages size from {filepath}')
pdfwm = PDFWordMap()
sizes = pdfwm.pages_size(filepath)
pprint(sizes)


print_header(f'Use {Origin.TOP_LEFT} to read {filepath}')
pdfwm = PDFWordMap()
wordmap = pdfwm.parse_pdf(data, origin=Origin.TOP_LEFT)
pprint(wordmap[:N_ENTRIES])

print_header(f'Use {Origin.BOTTOM_LEFT} to read {filepath}')
pdfwm = PDFWordMap()
wordmap = pdfwm.parse_pdf(data, origin=Origin.BOTTOM_LEFT)
pprint(wordmap[:N_ENTRIES])


print("\n\n")
print_header("The same functionalities made only with PDFMaze")
print()

print_header(f'First {N_ENTRIES} entries from {filepath} (made only by PDFMaze)')
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(filepath)
pprint(wordmap[0][:N_ENTRIES])
print()

print_header(f'First {N_ENTRIES} entries of every page from {filepath} (made only by PDFMaze)')
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(filepath)
for index, page in enumerate(wordmap):
    print_header(f'First {N_ENTRIES} entries from page {index + 1}')
    pprint(page[:N_ENTRIES])
print()

print_header(f'First {N_ENTRIES} entries from {filepath} with confidence (made only by PDFMaze)')
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(filepath, confidence=100)
pprint(wordmap[0][:N_ENTRIES])
print()

print_header(f'First {N_ENTRIES} entries from {filepath} split to words (made only by PDFMaze)')
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(filepath, split_words=True, key_split_chars=[' ', ':', '-'])
pprint(wordmap[0][:N_ENTRIES])
print()

print_header(f'First {N_ENTRIES} entries from {filepath} bytes (made only by PDFMaze)')
with filepath.open('rb') as fp:
    data = fp.read()
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(data)
pprint(wordmap[0][:N_ENTRIES])
print()


print_header(f'Calculate pages size from {filepath} (made only by PDFMaze)')
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(filepath)
pages_size = [page.shape for page in wordmap]
pprint(pages_size)
print()


print_header(f'Use {Origin.TOP_LEFT} to read {filepath} (made only by PDFMaze)')
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(data, origin=Origin.TOP_LEFT)
pprint(wordmap[0][:N_ENTRIES])
print()

print_header(f'Use {Origin.BOTTOM_LEFT} to read {filepath} (made only by PDFMaze)')
pdfwm = PDFMaze()
wordmap = pdfwm.parse_pdf(data, origin=Origin.BOTTOM_LEFT)
pprint(wordmap[0][:N_ENTRIES])
print()
