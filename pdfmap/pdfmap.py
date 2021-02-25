import pdfminer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

class pdfWordMap:

    def __init__(self):
        self.word_map = [] # list of (x1,x2,y1,y2,'textString') tuples

    def parse_obj(self, lt_objs):

        # loop over the object list
        for obj in lt_objs:

            if isinstance(obj, pdfminer.layout.LTTextLine):
                block = ([obj.bbox[0], obj.bbox[1]], [obj.bbox[2], obj.bbox[3]], obj.get_text().replace('\n', ''))
                block[0][0] = round(block[0][0], 2)
                block[0][1] = round(block[0][1], 2)
                block[1][0] = round(block[1][0], 2)
                block[1][1] = round(block[1][1], 2)
                self.word_map.append(block)

            # if it's a textbox, also recurse
            if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
                self.parse_obj(obj._objs)

            # if it's a container, recurse
            elif isinstance(obj, pdfminer.layout.LTFigure):
                self.parse_obj(obj._objs)

    def parse_pdf(self, filename):

        self.word_map = []

        # Open a PDF file.
        fp = open(filename, 'rb')

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

        # loop over all pages in the document
        for page in PDFPage.get_pages(fp):
            # read the page into a layout object
            interpreter.process_page(page)
            layout = device.get_result()

            # extract text from this object
            self.parse_obj(layout._objs)
        
        return self.word_map