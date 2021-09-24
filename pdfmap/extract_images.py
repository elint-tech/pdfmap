import fitz

def get_all_pdf_images(file_location: str):
    # create list of all images objects
    all_images_objects = []

    # open the file
    pdf_file = fitz.open(file_location)
    
    # iterate over PDF pages
    for page_index in range(len(pdf_file)):
        
        # get the page itself
        page = pdf_file[page_index]

        # get the list of all images on the page
        image_list = page.getImageList(full=True)

        # get the page dimensions
        page_height = page.rect.height
        page_width = page.rect.width
        
        # iterate through all the images on the page
        for image_index, img in enumerate(image_list, start=1):
            
            # get the XREF of the image
            xref = img[0]
            
            # extract the image bytes
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]

            # configure the bbox of the image to the pdfminer standard
            rect = page.getImageBbox(img)
            if rect.x0 == 1 and rect.x1 == -1 and rect.y0 == 1 and rect.y1 == -1:
                x1 = 0
                x2 = page_width
                y1 = page_height
                y2 = 0
            else:
                x1 = rect.x0
                x2 = rect.x1
                y1 = page_height - rect.y0
                y2 = page_height - rect.y1

            # get the image extension
            image_ext = base_image["ext"]

            # append the new image object to the list
            all_images_objects.append((x1, x2, y1, y2, image_bytes, image_ext))
    
    # return the list of all images objects on the pdf
    return all_images_objects
