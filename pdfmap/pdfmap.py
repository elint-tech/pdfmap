import io
from numbers import Number
from os import PathLike
from typing import List, Optional, Tuple, Union

import pdfminer
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser

from pdfmap.utils import Origin, Shape

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


class pdfWordMap:
    def __init__(self):
        self.word_map = [] # list of (page,x1,x2,y1,y2,'textString') tuples

    def parse_obj(
            self,
            lt_objs,
            page_number: int,
            page_size: Shape,
            origin: Origin = Origin.TOP_LEFT,
            confidence: Optional[Number] = None
    ) -> None:
        # loop over the object list
        for obj in lt_objs:
            if isinstance(obj, pdfminer.layout.LTTextLine):
                x1, y1, x2, y2 = (
                    round(vertex, 2)
                    for vertex in obj.bbox
                )

                if origin is Origin.TOP_LEFT:
                    y1, y2 = (page_size.height - y2, page_size.height - y1)
                elif origin is not Origin.BOTTOM_LEFT:
                    raise ValueError(
                        f'there is no support for {origin} yet.'
                        ' please use either'
                        f' {Origin.BOTTOM_LEFT} or {Origin.TOP_LEFT}'
                    )

                block = (
                    page_number,
                    (x1, y1),
                    (x2, y2),
                    obj.get_text().replace('\n', '')
                )

                if confidence is not None:
                    block += (confidence,)

                self.word_map.append(block)

            # if it's a textbox, also recurse
            if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
                self.parse_obj(
                    obj._objs,
                    page_number=page_number,
                    page_size=page_size,
                    origin=origin,
                    confidence=confidence
                )

            # if it's a container, recurse
            elif isinstance(obj, pdfminer.layout.LTFigure):
                self.parse_obj(
                    obj._objs,
                    page_number=page_number,
                    page_size=page_size,
                    origin=origin,
                    confidence=confidence
                )

    def parse_pdf(
            self,
            source: Union[str, PathLike, bytes],
            origin: Origin = Origin.TOP_LEFT,
            confidence: Optional[Number] = None
    ) -> Union[WordMap, ConfidentWordMap]:
        self.word_map = []

        if isinstance(source, bytes):
            # Use PDF bytes.
            fp = io.BytesIO(source)
        else:
            # Open a PDF file.
            fp = open(source, 'rb')

        # Create a PDF parser object associated with the file object.
        parser = PDFParser(fp)

        # Create a PDF document object that stores the document structure.
        # Password for initialization as 2nd parameter
        document = PDFDocument(parser)

        # Check if the document allows text extraction. If not, abort.
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed

        # Create a PDF resource manager object that stores shared resources.
        rsrcmgr = PDFResourceManager()

        # Create a PDF device object.
        device = PDFDevice(rsrcmgr)

        # BEGIN LAYOUT ANALYSIS
        # Set parameters for analysis.
        laparams = LAParams()

        # Create a PDF page aggregator object.
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)

        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # loop over all pages in the document and get the page index number
        for page_number, page in enumerate(PDFPage.get_pages(fp)):
            # read the page into a layout object
            interpreter.process_page(page)
            layout = device.get_result()

            # extract text from this object
            self.parse_obj(
                layout._objs,
                page_number=page_number+1,
                page_size=self.page_size(page),
                origin=origin,
                confidence=confidence
            )

        return self.word_map

    def page_size(self, page: PDFPage) -> Shape:
        _, _, width, height = page.mediabox
        return Shape(width=width, height=height)

    def pages_size(
            self,
            source: Union[str, PathLike, bytes]
    ) -> List[Shape]:
        # source: https://stackoverflow.com/a/48886525/5811400

        if isinstance(source, bytes):
            # Use PDF bytes.
            fp = io.BytesIO(source)
        else:
            # Open a PDF file.
            fp = open(source, 'rb')

        # Create a PDF parser object associated with the file object.
        parser = PDFParser(fp)

        # Create a PDF document object that stores the document structure.
        # Password for initialization as 2nd parameter
        document = PDFDocument(parser)

        pages_size = []
        for page in PDFPage.create_pages(document):
            shape = self.page_size(page)
            pages_size.append(shape)

        return pages_size
