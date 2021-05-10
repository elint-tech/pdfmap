import io
from numbers import Number
from os import PathLike
from typing import List, Optional, Tuple, Union, Iterable

from pdfmap.pdfmaze import PDFMaze
from wordmaze.wordmaze import Origin, Shape

WordMap = List[
    Tuple[
        Number, # page
        Number, # x1
        Number, # x2
        Number, # y1
        Number, # y2
        str # text
    ]
]
ConfidentWordMap = List[
    Tuple[
        Number, # page
        Number, # x1
        Number, # x2
        Number, # y1
        Number, # y2
        str, # text
        Number # confidence
    ]
]
pdfmaze = PDFMaze()

class PDFWordMap:
    def parse_pdf(
            self,
            source: Union[str, PathLike, bytes],
            origin: Origin = Origin.TOP_LEFT,
            confidence: Optional[Number] = None,
            split_words: bool = False,
            key_split_chars: Iterable[str] = (' ',)
    ) -> Union[WordMap, ConfidentWordMap]:
        self.word_map = []

        word_maze = pdfmaze.parse_pdf(
            source=source,
            origin=origin,
            confidence=confidence,
            split_words=split_words,
            key_split_chars = tuple(key_split_chars)
        )

        for index, page in enumerate(word_maze):
            page_number = index + 1
            for textbox in page:
                block = (
                    page_number,
                    (textbox.x1, textbox.y1),
                    (textbox.x2, textbox.y2),
                    textbox.text,
                )

                if textbox.confidence is not None:
                    block += (textbox.confidence,)
                
                self.word_map.append(block)
        
        return self.word_map

    def pages_size(
            self,
            source: Union[str, PathLike, bytes]
    ) -> List[Shape]:
        pages_size = []
        word_maze = pdfmaze.parse_pdf(source=source)
        for page in word_maze:
            shape = page.shape
            pages_size.append(shape)

        return pages_size
