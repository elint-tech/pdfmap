import io
import itertools
from numbers import Real
from os import PathLike
from typing import Iterable, List, Optional, Union

import pdfminer
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser
from wordmaze.wordmaze import Origin
from wordmaze.wordmaze import Page as WMPage
from wordmaze.wordmaze import Shape, TextBox, WordMaze


class PDFMaze:
    def _parse_objs(
        self,
        lt_objs,
        confidence: Optional[Real] = None
    ) -> Iterable[TextBox]:
        return itertools.chain.from_iterable(
            self._parse_obj(obj, confidence=confidence)
            for obj in lt_objs
        )

    def _parse_obj(
            self,
            obj,
            confidence: Optional[Real] = None
    ) -> List[TextBox]:
        textboxes = []

        # loop over the object list
        if isinstance(obj, pdfminer.layout.LTTextLine):
            x1, y1, x2, y2 = obj.bbox

            textbox = TextBox(
                x1=x1,
                x2=x2,
                y1=y1,
                y2=y2,
                text=obj.get_text().strip(),
                confidence=confidence
            )

            textboxes.append(textbox)

        # if it's a textbox or a container, also recurse
        if isinstance(
            obj,
            (pdfminer.layout.LTTextBoxHorizontal, pdfminer.layout.LTFigure)
        ):
            other_textboxes = self._parse_objs(obj._objs, confidence=confidence)
            textboxes.extend(other_textboxes)

        return textboxes

    def parse_pdf(
            self,
            source: Union[str, PathLike, bytes],
            origin: Origin = Origin.TOP_LEFT,
            confidence: Optional[Real] = None
    ) -> WordMaze:
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

        wm = WordMaze()
        # loop over all pages in the document and get the page index number
        for page in PDFPage.get_pages(fp):
            # read the page into a layout object
            interpreter.process_page(page)
            layout = device.get_result()

            # extract text from this object
            textboxes = self._parse_objs(
                layout._objs,
                confidence=confidence
            )

            print(textboxes)

            wm_page = WMPage(
                shape=self.page_shape(page),
                origin=Origin.BOTTOM_LEFT, # default origin from pdfminer
                entries=textboxes
            ).rebased(origin=origin)

            wm.append(wm_page)

        return wm

    @staticmethod
    def page_shape(page: PDFPage) -> Shape:
        _, _, width, height = page.mediabox
        return Shape(width=width, height=height)
