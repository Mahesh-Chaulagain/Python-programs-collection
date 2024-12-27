# pip install pdf2docx

from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, doc_path):
    # initialize the converter
    cv = Converter(pdf_path)

    # convert PDF to DOCX
    cv.convert(doc_path)
    cv.close()

convert_pdf_to_docx('document.pdf', 'document.docx')